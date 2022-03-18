import math
import os
import pandas as pd


class Country:
    def __init__(self, code, x, y):
        self.id = code
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Country {self.id}: ({self.x}, {self.y})"

    @property
    def hex_coordinates(self):
        r = 1 / math.sin(math.pi / 3)
        coordinates = list()
        n = 6
        base_angle = 360 // n
        for i in range(n):
            relative_angle = ((base_angle * i) + (base_angle // 2)) * (
                        math.pi / 180)
            # Note: -self.y - (r * math.sin(relative_angle))
            # to conform to the browser's coordinate system;
            # revert back to self.y + (r * math.sin(relative_angle)) for MPL
            coord_ = [self.x + (r * math.cos(relative_angle)),
                      -self.y - (r * math.sin(relative_angle))]
            coordinates.append(coord_)
        coordinates.append(coordinates[0])
        return coordinates

    @property
    def hexes_string(self):
        coordinates = self.hex_coordinates
        stringed = [",".join(map(lambda x: str(x), i)) for i in coordinates]
        return " ".join(stringed)


def get_hex_data():
    country_data = list()
    try:
        # base_path = os.environ["PYTHON_PROJECTS"]
        base_path = os.getcwd()
        file_path = os.path.join(base_path, "hive", "inputs", "hexcodes.json")
        hex_codes = pd.read_json(file_path)
        hex_codes['y_scaled'] = hex_codes['y'] - hex_codes['y'].min()
        for c, x, y in zip(hex_codes.id, hex_codes.x, hex_codes.y_scaled):
            country_data.append(Country(c, x, y))
    except KeyError:
        print("Couldn't locate country data")
    return country_data
