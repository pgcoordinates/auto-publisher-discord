import discord
import requests

client = discord.Client(intents=discord.Intents.all())

TOKEN = 
CHANNEL_ID = 
SERVER_ID =

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.channel.id == CHANNEL_ID:
        publish_message(message.id)

def publish_message(message_id):
    url = f"https://discord.com/api/v9/channels/{CHANNEL_ID}/messages/{message_id}/crosspost"
    headers = {
        "Authorization": f"Bot {TOKEN}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, headers=headers)
    
    if response.status_code == 200:
        print("Message published successfully.")
    else:
        print(f"Failed to publish message. Status code: {response.status_code}, Response: {response.text}")

client.run("TOKEN")
