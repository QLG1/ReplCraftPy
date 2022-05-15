from replcraftpy import ReplCraft
import os

token = os.environ['token']
client = ReplCraft(token)

client.login()

client.set_block(0, 0, 0, 'minecraft:air')