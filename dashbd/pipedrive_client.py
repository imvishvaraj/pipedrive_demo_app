from pipedrive.client import Client

PIPEDRIVE_API_KEY = "API KEY"

client = Client(domain="https://spectacular-jail.pipedrive.com/")
client.set_api_token(PIPEDRIVE_API_KEY)
# create singleton