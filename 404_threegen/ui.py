import bpy
from bpy_extras.io_utils import ImportHelper
from bpy.types import Context, Operator, Panel
from bpy.props import StringProperty, BoolProperty, EnumProperty
import os
import re

from .client import request_model
from .gaussian_splatting import import_gs


class GenerateOperator(Operator):
    """Generate 3DGS model"""

    bl_idname = "threegen.generate"
    bl_label = "Generate"

    def execute(self, context: Context):
        threegen = context.window_manager.threegen
        model_filepath, winner_hotkey = request_model(threegen.prompt)

        if not model_filepath:
            return {"CANCELLED"}

        name = re.sub(r"\s+", "_", threegen.prompt)
        import_gs(model_filepath, name, winner_hotkey)

        return {"FINISHED"}


class ImportOperator(Operator, ImportHelper):
    """Import 3DGS model from file"""

    bl_idname = "threegen.import"
    bl_label = "Import"
    filename_ext = ".ply"

    filter_glob: StringProperty(
        default="*.ply",
        options={"HIDDEN"},
        maxlen=255,  # Max internal buffer length, longer would be clamped.
    )
    use_setting: BoolProperty(
        name="Example Boolean",
        description="Example Tooltip",
        default=True,
    )

    type: EnumProperty(
        name="Example Enum",
        description="Choose between two items",
        items=(
            ("OPT_A", "First Option", "Description one"),
            ("OPT_B", "Second Option", "Description two"),
        ),
        default="OPT_A",
    )

    def execute(self, context):
        base_name = os.path.basename(self.filepath)
        name, _ = os.path.splitext(base_name)
        name = re.sub(r"\s+", "_", name)
        import_gs(self.filepath, name, "")

        return {"FINISHED"}
        # return read_some_data(context, self.filepath, self.use_setting)


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
        row = layout.row()
        row.operator(ImportOperator.bl_idname)


class DisplaySettingsPanel(Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "404"
    bl_idname = "Threegen_PT_settings"
    bl_label = "Splat Display Settings"

    @classmethod
    def poll(cls, context):
        obj = context.object
        return obj is not None and "Gaussian Splatting" in obj.modifiers

    def draw(self, context: Context):
        layout = self.layout
        obj = context.active_object

        row = layout.row()
        row.prop(obj.modifiers["Gaussian Splatting"], '["Socket_4"]', text="Render as point cloud (Cycles only)")

        row = layout.row()
        row.prop(obj.modifiers["Gaussian Splatting"], '["Socket_2"]', text="Opacity Threshold")

        row = layout.row()
        row.prop(obj.modifiers["Gaussian Splatting"], '["Socket_3"]', text="Display Percentage")


class ConversionPanel(Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "404"
    bl_idname = "Threegen_PT_conversion"
    bl_label = "Mesh Conversion"

    @classmethod
    def poll(cls, context):
        obj = context.object
        return obj is not None and "Gaussian Splatting" in obj.modifiers

    def draw(self, context: Context):
        layout = self.layout
        obj = context.active_object

        row = layout.row()
        row.prop(obj.modifiers["Gaussian Splatting"], '["Socket_5"]', text="Convert")

        row = layout.row()
        row.prop(obj.modifiers["Gaussian Splatting"], '["Socket_6"]', text="Voxel Size")

        row = layout.row()
        row.prop(obj.modifiers["Gaussian Splatting"], '["Socket_7"]', text="Adaptivity")


classes = (
    GenerateOperator,
    ImportOperator,
    MainPanel,
    DisplaySettingsPanel,
    ConversionPanel,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
