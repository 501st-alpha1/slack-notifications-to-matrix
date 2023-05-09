# slack-notifications-to-matrix
A web service + Matrix bot that sends you your Slack notifications over Matrix.

## Motivation

I wanted a way to receive Slack notifications on my Graphene OS device, without Google Play Services running, which the Slack app doesn't support.  The Matrix client Element allows a background service to be enabled, so that would provide a solution if I can get notifications from Slack into Matrix.  It seemed like overkill to add a [Matrix/Slack bridge](https://github.com/matrix-org/matrix-appservice-slack) when all I need are notifications (since the rest of the Slack app works fine), thus this project.
