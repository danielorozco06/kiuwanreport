from kiuwan_endpoints import get_kiuwan_applications, get_application_defects
from utils import filter_as400_applications

if __name__ == "__main__":
    print("\nFetching Kiuwan applications:")
    all_applications = get_kiuwan_applications()
    iseries_applications = filter_as400_applications(all_applications)
    print(iseries_applications)

    print("\nFetching defects for iSeries applications:")
    for app in iseries_applications:
        app_name = app['name']
        print(f"\nDefects for {app_name}:")
        defects = get_application_defects(app_name)
        print(defects)
