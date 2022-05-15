from replcraftpy import ReplCraft, ItemIndex, Recipe
import os

token = os.environ['token']
client = ReplCraft(token)

client.login()

cobblestone = ItemIndex(0, 0, 0, 1)
stick = ItemIndex(0, 0, 0, 2)

sword_recipe = Recipe(cobblestone.item(), None, None, cobblestone.item(), None, None, stick.item())

client.craft(0, 0, 0, sword_recipe.table())

client.disconnect()