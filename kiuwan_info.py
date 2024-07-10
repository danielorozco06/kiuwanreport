from kiuwan_endpoints import get_application_info, get_kiuwan_applications
from utils import export_app_info_to_json

if __name__ == "__main__":
    print("\nFetching Kiuwan applications:")
    all_applications = get_kiuwan_applications()

    print("\nFetching info for iSeries applications and exporting to JSON:")
    for app in all_applications:
        app_info = get_application_info(app["name"])
        print(f"\nInfo for {app['name']}:")
        export_app_info_to_json(app_info)
