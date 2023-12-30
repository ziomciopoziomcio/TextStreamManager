import json

# Function to write version from data file
def version_writer(path, to_save):
    try:
        with open(path, "r") as json_file:
            data = json.load(json_file)
        data["version"] = to_save
        with open(path, "w") as json_file:
            json.dump(data, json_file, indent=2)
        return 0

    except :
        return 1

def lines_amount_writer(path, to_save):
    try:
        with open(path, "r") as json_file:
            data = json.load(json_file)
        data["version"] = to_save
        with open(path, "w") as json_file:
            json.dump(data, json_file, indent=2)
        return 0
    except:
        return 1

# Function to read amount of text lines from
# Test function
# if __name__ == '__main__':
#     print(lines_amount(variable_path()))
