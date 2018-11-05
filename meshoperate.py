
from openmesh import *


mesh=read_trimesh("cat.obj")
# modify mesh ..
mesh.request_halfedge_normals()
mesh.request_vertex_normals()


write_mesh("cat_test.off", mesh, vertex_normal=True)

