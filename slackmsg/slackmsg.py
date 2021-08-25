import time
import json
import requests

class Connect:
    def __init__(self, hookurl, channel, username, icon_emoji = ':slack:', proxy = ''):
        self.channel = channel
        self.username = username
        self.hook_url = hookurl
        self.icon_emoji = icon_emoji
        self.proxyDict = {
          "http": proxy,
          "https": proxy
        }

    def send(self, title, text, status):
        # Set our defaults for the slack message
        slack_message = {
          "mrkdwn": "true",
          "icon_emoji": ":wrench:",
          "username": 'slackmsg python'
        }
        text = str(text)
        title = str(title)
        status = str(status).lower()
        #If username is specified set it (otherwise we will default to hostname)
        if self.username:
          slack_message['username'] = self.username
        if self.channel != '':
          slack_message['channel'] = self.channel
        if self.icon_emoji != '':
          slack_message['icon_emoji'] = self.icon_emoji
        if text != '' and title == '' and status == '':
          slack_message['text'] = text.encode().decode('unicode-escape')
        if text != '' and ( title != '' or status != '' ):
          slack_message['attachments'] = json.loads('[{"mrkdwn":"true"}]')
          if title != '':
            slack_message['attachments'][0]['fallback'] = title.encode().decode('unicode-escape')
            slack_message['attachments'][0]['title'] = title.encode().decode('unicode-escape')
          slack_message['attachments'][0]['text'] = text.encode().decode('unicode-escape')
          slack_message['attachments'][0]['ts'] = int(time.time())
          if status == 'error':
            slack_message['attachments'][0]['color'] = "danger"
          elif status == 'warning':
            slack_message['attachments'][0]['color'] = "warning"
          elif status == 'info':
            slack_message['attachments'][0]['color'] = "#4444ff" #blue
          elif status == 'ok':
            slack_message['attachments'][0]['color'] = "good"
          else:
            slack_message['attachments'][0]['color'] = "#222222" #dark - almost black
        if self.channel != '':
          urldata = json.dumps(slack_message, sort_keys=True, indent=2, separators=(',', ': '), ensure_ascii=False).encode('utf8')
          response = requests.post(self.hook_url,data=urldata,timeout=10,proxies=self.proxyDict)
          if response.status_code != requests.codes.ok:
            return 'Error posting message HTTP ERROR:' + str(response.status_code)
          else:
            return False
        else:
          return 'Channel and/or text have not been specified'
