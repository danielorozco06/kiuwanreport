import json
import os

def filter_as400_applications(applications):
    """
    Filter applications to include only those with quality_model "AS400"
    """
    return [app for app in applications if app.get('quality_model') == 'AS400']

def export_app_info_to_json(app_name, app_info):
    """
    Export application info to a JSON file in the output/ directory.
    """
    output_dir = 'output'
    os.makedirs(output_dir, exist_ok=True)
    filename = os.path.join(output_dir, f"{app_name.replace(' ', '_')}_info.json")
    with open(filename, 'w') as f:
        json.dump(app_info, f, indent=4)
    print(f"Exported {filename}")
