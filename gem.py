import bpy
import bmesh
import math

# Eliminar todos los objetos existentes
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# Crear malla y objeto
mesh = bpy.data.meshes.new(name="Gem")
obj = bpy.data.objects.new("Gem", mesh)

# Añadir objeto a la escena
scene = bpy.context.scene
scene.collection.objects.link(obj)

# Hacer el objeto activo
bpy.context.view_layer.objects.active = obj
obj.select_set(True)

# Crear geometría de la gema con BMesh
bm = bmesh.new()

# Coordenadas básicas de la parte superior
coords_top = [
    (0, 0, 1),
]

# Coordenadas básicas de la parte inferior
coords_bottom = [
    (math.cos(math.radians(i * 72)) * 0.6, math.sin(math.radians(i * 72)) * 0.6, 0) for i in range(5)
]

# Crear vértices
verts_top = [bm.verts.new(coord) for coord in coords_top]
verts_bottom = [bm.verts.new(coord) for coord in coords_bottom]

# Crear caras
for i in range(5):
    bm.faces.new([verts_top[0], verts_bottom[i], verts_bottom[(i + 1) % 5]])

# Actualizar la malla
bm.to_mesh(mesh)
bm.free()

# Crear un material
material = bpy.data.materials.new(name="Gem_Material")
material.diffuse_color = (0.0, 0.0, 1.0, 1)

# Asignar el material al objeto
obj.data.materials.append(material)
