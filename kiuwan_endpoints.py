import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_kiuwan_applications():
    url = "https://api.kiuwan.com/applications"
    username = os.getenv("KIUWAN_USERNAME")
    password = os.getenv("KIUWAN_PASSWORD")
    corporate_domain_id = os.getenv("KIUWAN_CORPORATE_DOMAIN_ID")

    headers = {
        "X-KW-CORPORATE-DOMAIN-ID": corporate_domain_id
    }

    response = requests.get(url, auth=(username, password), headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code} - {response.text}"

def get_application_info(application_name):
    url = f"https://api.kiuwan.com/apps/{application_name}"
    username = os.getenv("KIUWAN_USERNAME")
    password = os.getenv("KIUWAN_PASSWORD")
    corporate_domain_id = os.getenv("KIUWAN_CORPORATE_DOMAIN_ID")

    headers = {
        "X-KW-CORPORATE-DOMAIN-ID": corporate_domain_id
    }

    response = requests.get(url, auth=(username, password), headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code} - {response.text}"
