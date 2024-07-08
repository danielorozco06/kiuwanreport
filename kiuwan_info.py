from kiuwan_endpoints import get_kiuwan_info, get_kiuwan_applications

if __name__ == "__main__":
    print("Fetching Kiuwan info:")
    info = get_kiuwan_info()
    print(info)

    print("\nFetching Kiuwan applications:")
    applications = get_kiuwan_applications()
    print(applications)
