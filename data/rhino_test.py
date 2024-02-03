import compas
from lca_miro.datastructures import Panel
import json
import os

panel = Panel()


panel.load_json('C:\Users\ukeer\GitHub\lca_miro\data\jsontest00.json')
json_data = panel.json_file
print(json_data)


