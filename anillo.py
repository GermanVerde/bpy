import bpy

# Eliminar todos los objetos existentes
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# Crear un anillo básico (toro)
bpy.ops.mesh.primitive_torus_add(
    align='WORLD', 
    location=(0, 0, 1), 
    rotation=(0, 0, 0), 
    major_radius=1, 
    minor_radius=0.2
)

# Asignar el objeto recién creado a una variable
ring = bpy.context.active_object

# Cambiar el nombre del objeto
ring.name = "Ring"

# Crear un material
material = bpy.data.materials.new(name="Gold_Material")
material.diffuse_color = (0.8, 0.6, 0.2, 1)

# Asignar el material al objeto
ring.data.materials.append(material)
