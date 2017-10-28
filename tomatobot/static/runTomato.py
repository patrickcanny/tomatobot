import os
import time
from slackclient import SlackClient

BOT_ID = os.environ.get('BOT_ID')
AT_BOT = "<@" + BOT_ID + ">"
COMMAND = "tomato"
STOPCOMMAND = "tomatostop"

slack_client = SlackClient(os.environ.get('SLACK_API_TOKEN'))

def handle_command(command, channel):
    tomatostop = False;
    response = "Not sure what you mean. Use the *" + COMMAND + \
               "* command with numbers, delimited by spaces."
    if command.startswith(COMMAND):

        while tomatostop == False:
            if command.startswith(STOPCOMMAND):
                response = "Thanks for stopping the timer!"
                slack_client.api_call("chat.postMessage", channel=channel,
                                  text=response, as_user=True)
                tomatostop = True;
                break
            else:
                response = "Starting Timer!!!"
                slack_client.api_call("chat.postMessage", channel=channel,
                                      text=response, as_user=True)
                time.sleep(10)
                response = "Ran that Timer!!!"
                slack_client.api_call("chat.postMessage", channel=channel,
                                  text=response, as_user=True)
                time.sleep(5)

def parse_slack_output(slack_rtm_output):
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in  output and AT_BOT in output['text']:
                return output['text'].split(AT_BOT)[1].strip().lower(), \
                       output['channel']
    return None, None


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
