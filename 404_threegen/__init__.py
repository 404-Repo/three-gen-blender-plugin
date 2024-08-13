import bpy
from . import dependencies
from . import preferences


bl_info = {
    "name": "404 Three Gen",
    "description": "AI generated 3d Gaussian splatting",
    "location": "View3D > Toolshelf > GScatter",
    "author": "404",
    "version": (0, 4, 0),
    "blender": (4, 0, 0),
    "support": "COMMUNITY",
    "category": "Object",
}

modules = []


def register():
    preferences.register()
    modules.append(preferences)
    if dependencies.installed():
        from . import props, ui

        ui.register()
        props.register()
        modules.append(ui)
        modules.append(props)


def unregister():
    for m in modules:
        m.unregister()
