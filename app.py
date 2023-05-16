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

def get_message(event):
  username = 'FIXME'

  message = username + ' just sent you '

  if event['channel_type'] == 'im':
    message += 'a DM!'
  elif event['channel_type'] == 'mpim':
    # TODO: specify which mpim this was sent to.
    message += 'a multi-party DM!'
  else:
    channel_name = 'FIXME'
    message += 'a message in the {0} channel!'.format(channel_name)

@app.event("message")
def handle(client, event, logger):
  print('got an event')
  print(json.dumps(event))

  if 'channel' in event:
    if should_notify_channel(event['channel']):
      print('notify user here')
      message = get_message(event)
      print('Sending user this message: {0}'.format(message))
    else:
      print('nothing to see here')
  else:
    print('todo: handle other event types')
  print('-----end of handle------')

if __name__ == "__main__":
  app.start(port=int(os.environ.get("PORT", 3000)))
