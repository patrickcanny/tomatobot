import os
from slackclient import SlackClient

SLACK_CLIENT_ID = os.environ.get('CLIENT_ID')
SLACK_CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
VERIFICATION_TOKEN = os.environ.get('VERIFICATION_TOKEN')

slack_client = SlackClient(VERIFICATION_TOKEN)

def list_channels():
    channels_call = slack_client.api_call("channels.list")
    if channels_call.get('ok'):
        return channels_call['channels']
    return none

if __name__ == '__main__':
    channels = list_channels()
    if channels:
        print("Channels: ")
        for c in channels:
            print(c['name'] + " (" + c['id'] + ")")
    else:
        print("Unable to authenticate.")
