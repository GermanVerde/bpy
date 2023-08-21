import bpy
import random

def clear_scene_except_camera_and_light():
    bpy.ops.object.select_all(action='DESELECT')

    for obj in bpy.context.scene.objects:
        if obj.type not in {'CAMERA', 'LIGHT'}:
            obj.select_set(True)
            bpy.ops.object.delete()

def add_sphere(location, radius=1):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=32, ring_count=16, radius=radius, location=location)

def generate_random_positions(num_positions, min_range, max_range):
    positions = []

    for _ in range(num_positions):
        x = random.uniform(min_range, max_range)
        y = random.uniform(min_range, max_range)
        z = random.uniform(min_range, max_range)
        positions.append((x, y, z))

    return positions

def animate_sphere(sphere, start_location, end_location, start_frame, end_frame):
    sphere.location = start_location
    sphere.keyframe_insert(data_path="location", frame=start_frame)

    sphere.location = end_location
    sphere.keyframe_insert(data_path="location", frame=end_frame)

def create_material(name, color):
    material = bpy.data.materials.new(name)
    material.use_nodes = True
    bsdf = material.node_tree.nodes["Principled BSDF"]
    bsdf.inputs['Base Color'].default_value = color
    return material

def reposition_camera():
    camera = None
    for obj in bpy.context.scene.objects:
        if obj.type == 'CAMERA':
            camera = obj
            break

    if camera:
        camera.location = (0, -30, 15)
        camera.rotation_euler = (1.0472, 0, 0)

# Limpia la escena y deja solo la cámara y la luz
clear_scene_except_camera_and_light()

# Número de esferas a generar
num_spheres = 10
num_small_spheres = 20

# Rango de posiciones aleatorias
min_range = -10
max_range = 10

# Genera posiciones aleatorias y agrega esferas en esas posiciones
random_positions = generate_random_positions(num_spheres + num_small_spheres, min_range, max_range)

# Duración de la animación en segundos
animation_duration = 20

# Velocidad máxima y mínima de las esferas
min_speed = 0.5
max_speed = 3.0


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

for i, position in enumerate(random_positions):
    radius = 0.5 if i >= num_spheres else 1
    add_sphere(position, radius)
    sphere = bpy.context.active_object

    # Genera una posición final aleatoria
    end_position = generate_random_positions(1, min_range, max_range)[0]

    # Genera una velocidad aleatoria
    speed = random.uniform(min_speed, max_speed)

    # Calcula los frames de inicio y final para la animación
    start_frame = bpy.context.scene.frame_start
    end_frame = start_frame + int(animation_duration / speed * bpy.context.scene.render.fps)

    # Anima la esfera para que se mueva a la posición final aleatoria
    animate_sphere(sphere, position, end_position, start_frame, end_frame)

    # Asigna un color aleatorio a la esfera
    color = (random.random(), random.random(), random.random(), 1)
    material = create_material("Sphere Material", color)
    sphere.data.materials.append(material)

# Reposiciona la cámara para
