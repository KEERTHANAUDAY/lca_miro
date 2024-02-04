from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

from compas.datastructures import Mesh
import json


class Panel(Mesh):
    def __init__(self):
        super(Panel, self).__init__()
        self.json_object = None
        self.name = None
        self.material_type = None

    # @property
    # def data(self):
    #     if self.name is None: self.update_name()
    #     return self.name

    # json stuff
    def load_data_json(self, file_path):
        with open(file_path, "r") as json_file:
            self.json_object = json.load(json_file)
            self.name = self.json_object["name"]
            self.material_type = self.json_object["material_type"]

            # self.json_file = data

    def save_file(self, file_path):
        with open(file_path, "w") as json_file:
            json.dump(self.json_file, json_file)

    # load rhino as panel mesh
    def from_rhinomesh(cls, obj):
        """Class method for constructing a panel from a Rhino mesh."""
        from compas_rhino.conversions import mesh_to_compas

        mesh = mesh_to_compas(obj)
        return mesh

    # embodied carbon
    # get the material quantity of the assembly
    # multiply with mesh surface area
    # update face centroid with the attribute


if __name__ == "__main__":
    import os

    panel = Panel()
    panel.load_data_json("C:/Users/ukeer/GitHub/lca_miro/data/jsontest00.json")
    print(panel.name)
    print(panel.json_object)
    print(panel.material_type)
