import os
import time
from slackclient import SlackClient

BOT_ID = os.environ.get('BOT_ID')
AT_BOT = "<@" + BOT_ID + ">"
COMMAND = "tomato"

slack_client = SlackClient(os.environ.get('SLACK_API_TOKEN'))

if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1 # 1s Delay between readings
    if slack_client.rtm_connect():
        print("Tomatotimer is Running!!!")
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
        else:
            print("Failed Connection!")

            
