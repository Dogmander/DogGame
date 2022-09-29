from panda3d.core import *
from direct.showbase.ShowBase import ShowBase


base = ShowBase()

# set up a light source
p_light = PointLight("point_light")
p_light.set_color((1., 1., 1., 1.))
base.light = base.camera.attach_new_node(p_light)
base.light.set_pos(5., -100., 7.)
base.render.set_light(base.light)

# load model(s)
path_to_model = "smiley"
model_root = base.loader.load_model(path_to_model)
model_root.reparent_to(base.render)

# create a temporary copy to generate the collision meshes from
model_copy = model_root.copy_to(base.render)
model_copy.detach_node()
# "bake" the transformations into the vertices
model_copy.flatten_light()

# create root node to attach collision nodes to
collision_root = NodePath("collision_root")
collision_root.reparent_to(model_root)
# offset the collision meshes from the model so they're easier to see
collision_root.set_x(1.)

# Please note that the code below will not copy the hierarchy structure of the
# loaded `model_root` and that the resulting collision meshes will all have
# their origins at (0., 0., 0.), an orientation of (0., 0., 0.) and a scale of 1
# (as a result of the call to `flatten_light`).
# If a different relationship between loaded models and their corresponding
# collision meshes is required, feel free to alter the code as needed, but keep
# in mind that any (especially non-uniform) scale affecting a collision mesh
# (whether set on the mesh itself or inherited from a node at a higher level)
# can cause problems for the built-in collision system.

# create a collision mesh for each of the loaded models
for model in model_copy.find_all_matches("**/+GeomNode"):

    model_node = model.node()
    collision_node = CollisionNode(model_node.name)
    collision_mesh = collision_root.attach_new_node(collision_node)
    # collision nodes are hidden by default
    collision_mesh.show()

    for geom in model_node.modify_geoms():

        geom.decompose_in_place()
        vertex_data = geom.modify_vertex_data()
        vertex_data.format = GeomVertexFormat.get_v3()
        view = memoryview(vertex_data.arrays[0]).cast("B").cast("f")
        index_list = geom.primitives[0].get_vertex_list()
        index_count = len(index_list)

        for indices in (index_list[i:i+3] for i in range(0, index_count, 3)):
            points = [Point3(*view[index*3:index*3+3]) for index in indices]
            coll_poly = CollisionPolygon(*points)
            collision_node.add_solid(coll_poly)


base.run()