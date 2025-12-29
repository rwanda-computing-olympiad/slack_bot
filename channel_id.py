from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from dotenv import load_dotenv
import os


load_dotenv()
token=os.environ['MONKEYS_TOKEN']

client = WebClient(token=token)

try:
    # response = client.conversations_list(types="private_channel")
    response = client.conversations_list(types="public_channel")
    for channel in response["channels"]:
        print(f"Name: {channel['name']}, ID: {channel['id']}")
except SlackApiError as e:
    print(f"Error fetching channels: {e.response['error']}")
