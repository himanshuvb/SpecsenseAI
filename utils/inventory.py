import os
import pandas as pd


def load_inventory():
    json_file_path = os.path.join(
        "..",
        "inventory",
        "inventory.json"
    )

    inventory = pd.read_json(json_file_path)

    specs = pd.json_normalize(inventory["specs"])

    inventory = pd.concat(
        [inventory.drop(columns=["specs"]), specs],
        axis=1
    )

    return inventory