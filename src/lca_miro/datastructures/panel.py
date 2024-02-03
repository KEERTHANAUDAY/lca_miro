from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

from compas.datastructures import Mesh
import json


class Panel(Mesh):
    def __init__(self):
        super(Panel, self).__init__()
        self.json_file = None

    def load_json(self, file_path):
        with open(file_path, "r") as json_file:
            data = json.load(json_file)
            self.json_file = data

    def save_file(self, file_path):
        with open(file_path, "w") as json_file:
            json.dump(self.json_file, json_file)

    def from_rhinomesh(cls, obj):
        """Class method for constructing a panel from a Rhino mesh.
        Parameters
        ----------
        guid : str
            The GUID of the mesh.
        Returns
        -------
        Panel
            The block corresponding to the Rhino mesh.
        """
        from compas_rhino.conversions import mesh_to_compas

        mesh = mesh_to_compas(obj)
        return mesh.to_compas(cls)


if __name__ == "__main__":
    panel = Panel()
    panel.load_json("lca_miro/data/jsontest00.json")
    json_data = panel.json_file
    print(json_data)
