"""
Final step for Pipeline, check if the web services is running. 
"""

import requests
import json
import  logging
import threading
import urllib.request
import os

logger = logging.getLogger(__name__)

SLACK_NOTIFY_CHANNELS = ['alerts', 'general']
URL = "https://django.walii.es"

# Add other supported channels.

def notify_slack(slack_channel: str, status: str, msg: str) -> None:
    if slack_channel not in SLACK_NOTIFY_CHANNELS:
        logger.error(
            'the requested Slack notification channel, %s, is not supported',
            slack_channel)
        return

    slack_channel = slack_channel.replace('-', '').replace('_', '').upper()
    url = os.environ['slack_webhook']

    json_data = json.dumps({
        'text': '--- {} ---\n{}'.format(status, msg)
        }).encode('ascii')
    req = urllib.request.Request(
        url, data=json_data, headers={'Content-type': 'application/json'})
    thr = threading.Thread(target=urllib.request.urlopen, args=(req, ))
    try:
        thr.start()
    except Exception as e:
        logger.error('failed to send alert to Slack:\n%s', str(e))

def check_site(URL):
    try:
        response = requests.head(URL)
    except Exception as e:
        print(f"NOT OK: {str(e)}")
        return False
    else:
        if response.status_code != 200:
            print(f"NOT OK: HTTP response code {response.status_code}")
            return False
    return True
        
        


def main():
    slack_webhook = os.getenv('slack_webhook')
    if check_site(URL): 
        print("Testing work correctly. Service App Online")
        notify_slack("general", "good", "Deploy OK")
    else:
        notify_slack("alerts", "#ff00ff", "Deploy FAIL")

if __name__ == "__main__":
    main()