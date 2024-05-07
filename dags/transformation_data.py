import pandas as pd
from read_data import read_data


def extract_columns():
    data = read_data()
    return data.columns


def transformation_columns():
    # data normalization
    columns = extract_columns()
    data = read_data()
    transform_data = data.rename(
        columns={
            columns[0]: "pos",
            columns[1]: "driver_code",
            columns[2]: "driver_name",
            columns[3]: "constructor",
            columns[4]: "points",
            columns[5]: "pole_positions",
            columns[6]: "fastest_laps",
            columns[7]: "wins",
            columns[8]: "podiums",
            columns[9]: "dnfs",
        }
    )
    return transform_data