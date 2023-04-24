# import something
import discord
from discord.ext import commands
import datetime
import os

# set variable
client = discord.Client()

# time set
def gettime():
    x = datetime.datetime.now()
    x += datetime.timedelta(hours=0)
    y = x.year
    m = ['1', '2', '3', '4', '5', '6', '7',
         '8', '9', '10', '11', '12'][x.month - 1]
    d = x.day
    h = x.hour
    mi = x.minute
    s = x.second
    w = ['Sun.', 'Mon.', 'Tues.', 'Web.', 'Thus.', 'Fri.', 'Sat.'][(x.weekday() + 1) % 7]
    res = f"{y}/{m}/{d} ({w}) {h}:{mi}:{s}"
    return res

# Print bot name when link to DisocrdAPI
@client.event
async def on_ready():
    print('Bot Name：', client.user)

# Main Code
@client.event
async def on_message(message):
    # Print Message
    print(f"""
NAME：{message.author}
Message：{message.content}
guild：{message.guild}
channel：{message.channel}
time：{gettime()}
------------------------------\n""")
    # save message in All_Message.txt
    log_file_path = os.path.join(os.getcwd(), "./Messages/All_message.txt")
    with open(f"./All_Message.txt", "a", encoding='utf8') as log:
        log.write(f"""
NAME：{message.author}
Message：{message.content}
guild：{message.guild}
channel：{message.channel}
time：{gettime()}
------------------------------\n""")

# Replace "Your_Token" with your Code
client.run("Your_Token")
