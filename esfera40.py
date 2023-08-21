import bpy
import random

def add_high_resolution_sphere(location=(0, 0, 0)):
    bpy.ops.mesh.primitive_uv_sphere_add(
        segments=128,
        ring_count=64,
        radius=1,
        location=location
    )

def delete_random_faces(obj, percentage=0.4):
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='DESELECT')
    bpy.ops.object.mode_set(mode='OBJECT')

    num_faces = len(obj.data.polygons)
    num_faces_to_delete = int(num_faces * percentage)

    for _ in range(num_faces_to_delete):
        face_index = random.randint(0, num_faces - 1)
        obj.data.polygons[face_index].select = True

    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.delete(type='FACE')
    bpy.ops.object.mode_set(mode='OBJECT')

# Limpia la escena y deja solo la cámara y la luz
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()

# Agrega una esfera de alta resolución en la posición (0, 0, 0)
add_high_resolution_sphere((0, 0, 0))

# Obtiene la esfera creada
sphere = bpy.context.active_object

# Elimina el 40% de las caras de la esfera de manera aleatoria
delete_random_faces(sphere, percentage=0.4)
