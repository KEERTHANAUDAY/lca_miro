from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

from compas.datastructures import Mesh
import json


class Panel(Mesh):
    def __init__(self):
        super(Panel, self).__init__()
        self.json_file = None
        self.name = None

    def load_json(self, file_path):
        with open(file_path, "r") as json_file:
            data = json.load(json_file)
            self.json_file = data
            self.material.name = None

    def save_file(self, file_path):
        with open(file_path, "w") as json_file:
            json.dump(self.json_file, json_file)

    def from_rhinomesh(cls, obj):
        """Class method for constructing a panel from a Rhino mesh."""
        from compas_rhino.conversions import mesh_to_compas

        mesh = mesh_to_compas(obj)
        return mesh

    def set_material_name(self):
        if "name" in self.json_file:
            self.material_name = self.json_file["material_name"]


if __name__ == "__main__":
    import os

    HERE = os.path.dirname(__file__)
    FILE_I = os.path.join(HERE, "jsontest00.json")
    panel = Panel()
    panel.load_json(FILE_I)
    json_data = panel.json_file
    name = panel.name
    print(name)
