import bpy
import random
from collections import deque

def delete_existing_mesh_objects():
    bpy.ops.object.select_all(action='DESELECT')
    bpy.ops.object.select_by_type(type='MESH')
    bpy.ops.object.delete()

def generate_maze(width, height):
    maze = [[0] * width for _ in range(height)]
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def in_bounds(x, y):
        return 0 <= x < width and 0 <= y < height

    def carve(x, y):
        maze[y][x] = 1
        random.shuffle(dirs)

        for dx, dy in dirs:
            nx, ny = x + dx * 2, y + dy * 2
            if in_bounds(nx, ny) and maze[ny][nx] == 0:
                maze[y + dy][x + dx] = 1
                carve(nx, ny)

    carve(1, 1)
    maze[0][1] = 1  # Entrada
    maze[height - 1][width - 2] = 1  # Salida
    return maze

def create_wall(x, y, z, sx, sy, sz):
    bpy.ops.mesh.primitive_cube_add(location=(x, y, z))
    wall = bpy.context.active_object
    wall.scale.x = sx
    wall.scale.y = sy
    wall.scale.z = sz
    return wall

def create_maze_in_blender(maze, wall_height=2.0, wall_thickness=0.1):
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == 0:
                create_wall(x, y, wall_height / 2, 0.5, 0.5, wall_height / 2)
            else:
                if y < len(row) - 1 and maze[y + 1][x] == 0:
                    create_wall(x, y + 0.5, wall_height / 2, 0.5, wall_thickness / 2, wall_height / 2)
                if x < len(maze) - 1 and maze[y][x + 1] == 0:
                    create_wall(x + 0.5, y, wall_height / 2, wall_thickness / 2, 0.5, wall_height / 2)

delete_existing_mesh_objects()
width, height = 21, 21
maze = generate_maze(width, height)
create_maze_in_blender(maze)
