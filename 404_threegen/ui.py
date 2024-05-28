import bpy
from bpy.types import Context, Operator, Panel
import re

from .client import request_model
from .gaussian_splatting import import_gs


class GenerateOperator(Operator):
    """Generate 3DGS model"""

    bl_idname = "threegen.generate"
    bl_label = "Generate"

    def execute(self, context: Context):
        threegen = context.window_manager.threegen
        model_filepath = request_model(threegen.prompt)

        if not model_filepath:
            return {"CANCELED"}

        name = re.sub(r"\s+", "_", threegen.prompt)
        import_gs(model_filepath, name)

        return {"FINISHED"}


class MainPanel(Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "404"
    bl_idname = "Threegen_PT_main"
    bl_label = "3DGS Generation"

    def draw(self, context: Context):
        layout = self.layout
        threegen = context.window_manager.threegen
        row = layout.row()
        row.prop(threegen, "prompt", text="Prompt")
        row = layout.row()
        row.operator(GenerateOperator.bl_idname)


classes = (
    GenerateOperator,
    MainPanel,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
