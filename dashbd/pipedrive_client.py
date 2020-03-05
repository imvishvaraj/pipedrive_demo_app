from .models import Pipedrive as pc
import requests

PIPEDRIVE_API_KEY = "API KEY"

# client = Client(domain="https://spectacular-jail.pipedrive.com/")
# client.set_api_token(PIPEDRIVE_API_KEY)
# create singleton


def get_data(url, headers):
    try:
        return requests.get(url, headers=headers).json()
    except:
        return None


class Person:
    """Implementing operations reagrding person/contact on pipedrive."""

    def __init__(self, key):
        self.key = key
        self.headers = {"Accept": "application/json"}

    def get_all(self):
        url = "https://api.pipedrive.com/v1/persons?start=0&api_token={}".format(self.key)
        # url = "/".join([self.domain, 'persons'])
        data = get_data(url, self.headers)
        return data

    def get_details(self, id):
        url = "https://api.pipedrive.com/v1/persons/{}?api_token={}".format(id, self.key)
        data = get_data(url, self.headers)
        return data


class Deals:
    """Implementing function regarding"""

    def __init__(self, key):
        self.key = key
        self.headers = {"Accept": "application/json"}

    def get_all(self):
        url = "https://api.pipedrive.com/v1/deals?status=all_not_deleted&start=0&api_token={}".format(self.key)
        data = get_data(url, self.headers)
        return data
