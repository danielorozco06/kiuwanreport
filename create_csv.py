import json
import os


def read_json_files(folder_path):
    """
    Read all JSON files in the specified folder and return a list of JSON objects.
    """
    json_objects = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "r") as file:
                json_data = json.load(file)
                json_objects.append(json_data)
    return json_objects


if __name__ == "__main__":
    output_folder = "output"
    json_data = read_json_files(output_folder)
