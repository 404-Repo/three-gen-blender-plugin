import bpy


class WindowManagerProps(bpy.types.PropertyGroup):
    prompt: bpy.props.StringProperty()
    n_generations: bpy.props.IntProperty(min=1, max=10, default=1)
    progress: bpy.props.FloatProperty(min=0.0, max=1.0, default=0.0)
    in_progress: bpy.props.BoolProperty(default=False)


classes = (WindowManagerProps,)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.WindowManager.threegen = bpy.props.PointerProperty(type=WindowManagerProps)


def unregister():
    del bpy.types.WindowManager.threegen

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
