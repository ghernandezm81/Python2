from pprint import pprint

from belvo.client import Client
from belvo.enums import AccessMode

# Login to Belvo API
client = Client("ab1add96-6c2b-469f-9cff-0dc1c27caaba", "POFb09x7xLlaKySBQg#9W4hKgnLfMqwF7BrPc5N-nDD15UWSFto94fK0lvvqFkFQ", "https://sandbox.belvo.com")

# Register a link 
link = client.Links.create(
    institution="erebor_mx_retail",
    username="bnk100",
    password="full",
    #access_mode=AccessMode.SINGLE
)

# Get all accounts
client.Accounts.create(link=link["id"])

# Pretty print all checking accounts
for account in client.Accounts.list(type="checking"):
    print(account)