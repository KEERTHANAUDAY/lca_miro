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


if __name__ == "__main__":
    panel = Panel()
    panel.load_json("lca_miro/data/jsontest00.json")
    json_data = panel.json_file
    print(json_data)
