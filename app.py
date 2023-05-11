import os
from slack_bolt import App
import json

app = App(
  token=os.environ.get("SLACK_BOT_TOKEN"),
  signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

my_channels = []

def should_notify_channel(channel):
  global my_channels
  if channel in my_channels:
    # Previously cached user belongs to this channel.
    return True

  response = app.client.conversations_info(channel=channel)

  if not response['ok']:
    print('got an error in should_notify_channel')
    print(response['error'])

    # Notify user just in case.
    return True

  if response['channel']['is_im']:
    my_channels.append(channel)
    # Always notify for IMs.
    return True
  elif response['channel']['is_mpim']:
    my_channels.append(channel)
    # Always notify for group IMs.
    return True
  elif response['channel']['is_member']:
    my_channels.append(channel)
    # Only joined channels otherwise.
    return True
  else:
    print('Skipping notification for unjoined channel ' + response['channel']['name'])
    return False

@app.event("message")
def handle(client, event, logger):
  print('got an event')
  print(json.dumps(event))

if __name__ == "__main__":
  app.start(port=int(os.environ.get("PORT", 3000)))
