import bpy
import random
import math

def branch(depth, angle, scale, position, rotation):
    if depth == 0:
        return

    bpy.ops.mesh.primitive_cylinder_add(vertices=8, radius=0.1 * scale, depth=1, location=position, rotation=rotation)
    cylinder = bpy.context.active_object
    cylinder.scale.z = scale

    new_position = (position[0], position[1], position[2] + scale)
    new_scale = scale * 0.8

    new_angle = angle * random.uniform(0.5, 1.5)
    x_rot = rotation[0] + random.choice([-1, 1]) * math.radians(new_angle)
    y_rot = rotation[1] + random.choice([-1, 1]) * math.radians(new_angle)

    branch(depth - 1, angle, new_scale, new_position, (x_rot, y_rot, rotation[2]))
    branch(depth - 1, angle, new_scale, new_position, (x_rot, -y_rot, rotation[2]))

def create_tree(position=(0, 0, 0), depth=5, angle=30, scale=1):
    initial_rotation = (0, 0, 0)
    branch(depth, angle, scale, position, initial_rotation)

delete_existing_mesh_objects()
create_tree(position=(0, 0, 0), depth=5, angle=30, scale=1)
