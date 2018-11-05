#!D:/library/Miniconda/python
# -*- coding: utf-8 -*-

from openmesh import *


class MeshModel():
    def __init__(self):
        self.mesh_kernel = TriMesh()

    # todo(ShanWen): make open file code more flexible, add some estimate code
    def open(self, filename):
        self.mesh_kernel = read_trimesh(filename)
        print("n_vertices: %d" % self.mesh_kernel.n_vertices())

        if self.mesh_kernel.n_vertices() < 1:
            return False
        else:
            return True

    def save(self, filename):
        write_mesh(filename, self.mesh_kernel)

    def render(self):
        pass




