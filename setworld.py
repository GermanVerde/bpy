import bpy
import random

def set_random_world_color():
    world = bpy.context.scene.world
    if world is None:
        world = bpy.data.worlds.new("World")
        bpy.context.scene.world = world
    
    world.use_nodes = True
    bg_node = world.node_tree.nodes["Background"]
    random_color = (random.random(), random.random(), random.random(), 1)
    bg_node.inputs["Color"].default_value = random_color

set_random_world_color()
