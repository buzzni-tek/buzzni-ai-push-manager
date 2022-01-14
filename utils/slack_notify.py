import slack as sc


TOKEN = "xoxb-405348602032-2976878263024-TWr8WVdIO3Y68B6Uo37CsAq7"
_SLACK_CHAANEL = "푸쉬매니저"

def clean_channel(channel):
    if channel.startswith('#'):
        return channel
    return '#' + channel


def notify(channel=_SLACK_CHAANEL, msg:str = None):
    cleaned_channel = clean_channel(channel)
    client = sc.WebClient(token=TOKEN)
    return client.chat_postMessage(
        channel=cleaned_channel,
        text=msg)
