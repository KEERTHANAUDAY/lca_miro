import compas
from lca_miro.datastructures import Panel
import json
import os
from compas_rhino.conversions import mesh_to_compas
import scriptcontext as sc
import rhinoscriptsyntax as rs

mesh_guid = rs.GetObject("Select mesh", rs.filter.mesh)

obj = sc.doc.Objects.Find(mesh_guid)
#mesh = mesh_to_compas(obj.Geometry)
panel = Panel()

##json load test
#panel.load_json('C:\Users\ukeer\GitHub\lca_miro\data\jsontest00.json')
#json_data = panel.json_file

panel.from_rhinomesh(obj.Geometry)
print(panel)


