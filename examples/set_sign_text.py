from replcraftpy import ReplCraft
import os

token = os.environ['token']
client = ReplCraft(token)

client.login()

client.set_sign_text(0, 0, 0, ["first line", "second", "third", "fourth"])

client.disconnect()