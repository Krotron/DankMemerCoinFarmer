import discord, time, os
client = discord.Client()

@client.event
async def on_ready():
    print("Logged on as {0}!".format(client.user.name))

@client.event
async def on_connect():
    channel = client.get_channel(926436487757701160)
    while True:
        await channel.send("pls hunt")
        time.sleep(5)
        await channel.send("pls search")
        time.sleep(5)
        await channel.send("pls fish")
        time.sleep(9)
        await channel.send("pls beg")
        time.sleep(20)
        await channel.send("pls pm")
        time.sleep(5)
        await channel.send("pls beg")
        time.sleep(5)
        await channel.send("pls dep all")
        time.sleep(15)
            
token = os.getenv('OTIxNjI1MjY5ODQyODk4OTQ1.YcnHuQ.DGffyFiZS9ojhc0-Wg4RahN6pX4')
client.run(token, bot = False)
