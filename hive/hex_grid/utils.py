import os
import pandas as pd


class Country:
    def __init__(self, code, x, y):
        self.id = code
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Country {self.id}: ({self.x}, {self.y})"


def get_hex_data():
    base_path = os.environ["PYTHON_PROJECTS"]
    file_path = os.path.join(base_path, "HexGridGenerator", "Inputs",
                             "hexcodes_expanded_2.csv")
    hex_codes = pd.read_csv(file_path)
    country_data = list()
    for c, x, y in zip(hex_codes.id, hex_codes.x, hex_codes.y):
        country_data.append(Country(c, x, y))
    return country_data
