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


def transform_json_objects(json_objects):
    """
    Transform JSON objects to include only specified properties.
    """
    transformed_objects = []
    for obj in json_objects:
        transformed_obj = {
            "name": obj.get("name"),
            "description": obj.get("description"),
            "auditName": obj.get("auditName"),
            "applicationBusinessValue": obj.get("applicationBusinessValue"),
            "label": obj.get("label"),
            "date": obj.get("date"),
            "modelId": obj.get("modelId"),
            "encoding": obj.get("encoding"),
            "analysisCode": obj.get("analysisCode"),
            "analysisURL": obj.get("analysisURL"),
            "analysisBusinessValue": obj.get("analysisBusinessValue"),
            "analysisStatus": obj.get("analysisStatus"),
            "quality_model": obj.get("quality_model"),
            "ordered_by": obj.get("ordered_by"),
            "risk_index": obj.get("Risk index", {}).get("value"),
            "quality_indicator": obj.get("Quality indicator", {}).get("value"),
            "effort_to_target": obj.get("Effort to target", {}).get("value"),
            "duplicated_code": next(
                (
                    metric["value"]
                    for metric in obj.get("Main metrics", [])
                    if metric["name"] == "Duplicated code"
                ),
                None,
            ),
            "total_defects": next(
                (
                    metric["value"]
                    for metric in obj.get("Main metrics", [])
                    if metric["name"] == "Total defects"
                ),
                None,
            ),
            "very_high_defects": next(
                (
                    metric["value"]
                    for metric in obj.get("Main metrics", [])
                    if metric["name"] == "Very high defects"
                ),
                None,
            ),
            "suppressed_defects": next(
                (
                    metric["value"]
                    for metric in obj.get("Main metrics", [])
                    if metric["name"] == "Supressed defects"
                ),
                None,
            ),
            "files": next(
                (
                    metric["value"]
                    for metric in obj.get("Main metrics", [])
                    if metric["name"] == "Files"
                ),
                None,
            ),
            "lines_of_code": next(
                (
                    metric["value"]
                    for metric in obj.get("Main metrics", [])
                    if metric["name"] == "Lines of code"
                ),
                None,
            ),
            "complexity": next(
                (
                    metric["value"]
                    for metric in obj.get("Main metrics", [])
                    if metric["name"] == "Complexity"
                ),
                None,
            ),
        }
        transformed_objects.append(transformed_obj)
    return sorted(transformed_objects, key=lambda x: x['name'])


if __name__ == "__main__":
    output_folder = "output"
    json_data = read_json_files(output_folder)
    transformed_data = transform_json_objects(json_data)
    print(f"Transformed {len(transformed_data)} JSON objects.")
