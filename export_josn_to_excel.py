import json

import pandas as pd


def read_json(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data


if __name__ == "__main__":
    # Load JSON data from a file or from a string (here I'm assuming it's loaded from a file)
    # println(f"-------------------read json-------------------")
    json_data = pd.read_json("json_data.json", encoding='utf-8')
    # Convert JSON data to pandas DataFrame
    df = pd.DataFrame(json_data)

    # Write DataFrame to Excel
    # println(f"-------------------export to excel-------------------")
    df.to_excel('output.xlsx', index=False)  # Set index=False if you don't want to include row numbers
