import discord

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("test")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("야"):
        await message.channel.send('뭐')

client.run("NTc4MjE4Njg0NTY1MTU5OTY2.XNwaTg.sN_OT3wt9o3ud1PiNQ_ztuLtxcg")