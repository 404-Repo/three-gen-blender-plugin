from bpy.types import AddonPreferences, Context, UILayout
from bpy.props import StringProperty
import bpy

from . import dependencies


class DependencyInstallationOperator(bpy.types.Operator):
    bl_idname = "threegen.installdeps"
    bl_label = "Install Dependencies"

    def execute(self, context: Context):
        dependencies.install()
        return {"FINISHED"}


class ThreegenPreferences(AddonPreferences):
    bl_idname = __name__.partition(".")[0]
    url: StringProperty(default="wss://0akbihcx8cbfk2-8888.proxy.runpod.net/ws/generate/")
    token: StringProperty()

    def draw(self, context: Context):
        layout: UILayout = self.layout
        col = layout.column()
        if dependencies.installed():
            col.prop(self, "url")
            col.prop(self, "token")
        else:
            col.operator(DependencyInstallationOperator.bl_idname)


classes = (
    DependencyInstallationOperator,
    ThreegenPreferences,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
