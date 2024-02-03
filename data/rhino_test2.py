import compas
from compas_rhino.conversions import mesh_to_compas
import scriptcontext as sc
import rhinoscriptsyntax as rs

mesh_guid = rs.GetObject("Select mesh", rs.filter.mesh)

obj = sc.doc.Objects.Find(mesh_guid)
mesh = mesh_to_compas(obj.Geometry)

print(type(mesh))



