from kiuwan_endpoints import get_kiuwan_info, get_kiuwan_applications
from utils import filter_as400_applications

if __name__ == "__main__":
    print("Fetching Kiuwan info:")
    info = get_kiuwan_info()
    print(info)

    print("\nFetching Kiuwan applications:")
    all_applications = get_kiuwan_applications()
    iseries_applications = filter_as400_applications(all_applications)
    print(iseries_applications)
