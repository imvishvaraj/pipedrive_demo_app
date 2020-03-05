from .models import Pipedrive

PIPEDRIVE_API_KEY = "API KEY"

# client = Client(domain="https://spectacular-jail.pipedrive.com/")
# client.set_api_token(PIPEDRIVE_API_KEY)
# create singleton

class Pipedrive:
    def __init__(self):
        self.key = Pipedrive()


class Person(Pipedrive):
    """Implementing operations reagrding person/contact on pipedrive."""
    pass


class Deals(Pipedrive):
    """Implementing function regarding"""