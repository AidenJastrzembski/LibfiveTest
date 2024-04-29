import libfive
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def create_shape():
    tree = libfive.shapes.Sphere(0.5)
    return tree

def generate_mesh(tree, resolution=100):
    mesh = libfive.mesh.Mesh(tree.evalInterval(resolution))
    vertices = np.array(mesh.vertices)
    faces = np.array(mesh.faces)

    return vertices, faces

def plot_shape(vertices, faces):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_trisurf(vertices[:, 0], vertices[:, 1], vertices[:, 2], triangles=faces, cmap='viridis')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()

def main():
    shape_tree = create_shape()
    vertices, faces = generate_mesh(shape_tree)
    plot_shape(vertices, faces)

if __name__ == "__main__":
    main()
