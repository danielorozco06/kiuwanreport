from kiuwan_endpoints import get_application_info, get_kiuwan_applications
from utils import export_app_info_to_json, filter_applications

if __name__ == "__main__":
    print("\nFetching Kiuwan applications:")
    all_applications = get_kiuwan_applications()

    quality_model = input("Enter quality model to filter (AS400, ALL): ").upper()
    filtered_applications = filter_applications(all_applications, quality_model)

    print("\nFetching info for applications and exporting to JSON:")
    for app in filtered_applications:
        app_info = get_application_info(app["name"])
        export_app_info_to_json(app_info)
