import json
import os


def validate_and_format_app_name(app_info):
    """
    Validate the quality_model and format the app name if necessary.
    """
    if app_info.get("quality_model") == "AS400":
        app_info["name"] = f"IS{app_info['name']}0001"
    return app_info


def export_app_info_to_json(app_info):
    """
    Export application info to a JSON file in the output/ directory.
    """
    app_info = validate_and_format_app_name(app_info)
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    filename = os.path.join(output_dir, f"{app_info['name']}.json")
    with open(filename, "w") as f:
        json.dump(app_info, f, indent=4)
    print(f"Exported {filename}")
