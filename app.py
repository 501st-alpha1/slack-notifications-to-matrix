import os
from slack_bolt import App

app = App(
  token=os.environ.get("SLACK_BOT_TOKEN"),
  signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

@app.event("message")
def handle_dm(client, event, logger):
  print('got an event')

if __name__ == "__main__":
  app.start(port=int(os.environ.get("PORT", 3000)))
