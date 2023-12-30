import json
import os

# Function to trace file with variables
def variable_path():
    try:
        current_directory = os.getcwd()
        assets_directory = os.path.join(current_directory, '../assets')
        filename_in_assets = 'variables.json'
        variable_location = os.path.join(assets_directory, filename_in_assets)
        if not os.path.exists(variable_location):
            raise FileNotFoundError(1)
        return variable_location
    except Exception:
        return 1


# Function to read version from data file
def version_reader(path):
    with open(path, "r") as json_file:
        data = json.load(json_file)
    if "version" in data:
        return data["version"]
    else:
        raise KeyError(1)

# Test function
# if __name__ == '__main__':
#     print(version_reader(variable_path()))