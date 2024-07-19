import bpy
import bmesh
import mathutils
import numpy as np
import time
import os

from .plyfile import PlyData, PlyElement

RECOMMENDED_MAX_GAUSSIANS = 200_000


def import_gs(filepath: str, name):
    
    
    if "GaussianSplatting.003" not in bpy.data.node_groups:
        script_file = os.path.realpath(__file__)
        path = os.path.dirname(script_file)
        blendfile = os.path.join(path, "gs_nodetree.blend")
        section   = "/NodeTree/"
        object    = "GaussianSplatting"

        directory = blendfile + section
        filename  = object

        bpy.ops.wm.append(
            filename=filename,
            directory=directory)

    start_time_0 = time.time()
    start_time = time.time()

    plydata = PlyData.read(filepath)

    print(f"PLY loaded in {time.time() - start_time} seconds")

    start_time = time.time()

    xyz = np.stack(
        (
            np.asarray(plydata.elements[0]["x"]),
            np.asarray(plydata.elements[0]["y"]),
            np.asarray(plydata.elements[0]["z"]),
        ),
        axis=1,
    )

    N = len(xyz)
    print(f"ply data: {plydata.elements[0]}")
    
    if "opacity" in plydata.elements[0]:
        log_opacities = np.asarray(plydata.elements[0]["opacity"])[..., np.newaxis]
        opacities = 1 / (1 + np.exp(-log_opacities))
    else:
        log_opacities = np.asarray(1)[..., np.newaxis]
        opacities = 1 / (1 + np.exp(-log_opacities))

    features_dc = np.zeros((N, 3, 1))
    features_dc[:, 0, 0] = np.asarray(plydata.elements[0]["f_dc_0"])
    features_dc[:, 1, 0] = np.asarray(plydata.elements[0]["f_dc_1"])
    features_dc[:, 2, 0] = np.asarray(plydata.elements[0]["f_dc_2"])

    extra_f_names = [p.name for p in plydata.elements[0].properties if p.name.startswith("f_rest_")]
    extra_f_names = sorted(extra_f_names, key=lambda x: int(x.split("_")[-1]))

    if len(extra_f_names) > 0:
        features_extra = np.zeros((N, len(extra_f_names)))
        for idx, attr_name in enumerate(extra_f_names):
            features_extra[:, idx] = np.asarray(plydata.elements[0][attr_name])
        features_extra = features_extra.reshape((N, 3, 15))

    log_scales = np.stack(
        (
            np.asarray(plydata.elements[0]["scale_0"]),
            np.asarray(plydata.elements[0]["scale_1"]),
            np.asarray(plydata.elements[0]["scale_2"]),
        ),
        axis=1,
    )

    scales = np.exp(log_scales)

    quats = np.stack(
        (
            np.asarray(plydata.elements[0]["rot_0"]),
            np.asarray(plydata.elements[0]["rot_1"]),
            np.asarray(plydata.elements[0]["rot_2"]),
            np.asarray(plydata.elements[0]["rot_3"]),
        ),
        axis=1,
    )

    rots_euler = np.zeros((N, 3))

    for i in range(N):
        quat = mathutils.Quaternion(quats[i].tolist())
        euler = quat.to_euler()
        rots_euler[i] = (euler.x, euler.y, euler.z)

    print("Data loaded in", time.time() - start_time, "seconds")

    start_time = time.time()

    mesh = bpy.data.meshes.new(name="Mesh")
    mesh.from_pydata(xyz.tolist(), [], [])
    mesh.update()

    print("Mesh loaded in", time.time() - start_time, "seconds")

    start_time = time.time()

    log_opacity_attr = mesh.attributes.new(name="log_opacity", type="FLOAT", domain="POINT")
    log_opacity_attr.data.foreach_set("value", log_opacities.flatten())

    opacity_attr = mesh.attributes.new(name="opacity", type="FLOAT", domain="POINT")
    opacity_attr.data.foreach_set("value", opacities.flatten())

    scale_attr = mesh.attributes.new(name="scale", type="FLOAT_VECTOR", domain="POINT")
    scale_attr.data.foreach_set("vector", scales.flatten())

    logscale_attr = mesh.attributes.new(name="logscale", type="FLOAT_VECTOR", domain="POINT")
    logscale_attr.data.foreach_set("vector", log_scales.flatten())

    sh0_attr = mesh.attributes.new(name="sh0", type="FLOAT_VECTOR", domain="POINT")
    sh0_attr.data.foreach_set("vector", features_dc.flatten())

    rot_quatxyz_attr = mesh.attributes.new(name="quatxyz", type="FLOAT_VECTOR", domain="POINT")
    rot_quatxyz_attr.data.foreach_set("vector", quats[:, :3].flatten())

    rot_quatw_attr = mesh.attributes.new(name="quatw", type="FLOAT", domain="POINT")
    rot_quatw_attr.data.foreach_set("value", quats[:, 3].flatten())

    rot_euler_attr = mesh.attributes.new(name="rot_euler", type="FLOAT_VECTOR", domain="POINT")
    rot_euler_attr.data.foreach_set("vector", rots_euler.flatten())

    obj = bpy.data.objects.new(name, mesh)
    bpy.context.collection.objects.link(obj)
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)

    obj.rotation_mode = "XYZ"
    obj.rotation_euler = (-np.pi / 2, 0, 0)
    obj.rotation_euler[0] = 1.5708

    obj["gaussian_splatting"] = True

    print("Mesh attributes added in", time.time() - start_time, "seconds")

    setup_nodes(obj)

    print("Total Processing time: ", time.time() - start_time_0)

def setup_nodes(obj):
    start_time = time.time()
    node_tree = bpy.data.node_groups["GaussianSplatting"]
    m = obj.modifiers.new(name="Gaussian Splatting", type="NODES")
    m.node_group = node_tree
    print("Geometry nodes created in", time.time() - start_time, "seconds")

