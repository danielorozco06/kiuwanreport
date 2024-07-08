from kiuwan_endpoints import get_kiuwan_applications, get_application_info
from utils import filter_as400_applications, export_app_info_to_json

if __name__ == "__main__":
    print("\nFetching Kiuwan applications:")
    all_applications = get_kiuwan_applications()
    iseries_applications = filter_as400_applications(all_applications)
    print(iseries_applications)

    print("\nFetching info for iSeries applications and exporting to JSON:")
    for app in iseries_applications:
        app_name = app['name']
        print(f"\nInfo for {app_name}:")
        app_info = get_application_info(app_name)
        print(app_info)
        export_app_info_to_json(app_name, app_info)
