if input("輸入要選擇哪個Bot\n1.NK4 NK4#0753\n2.Next#7616\n") == "1":
    Token = "OTc2ODQ2MTc5MjU2MTIzMzky.Gg1tyt.aQ8K-aNJer8QXBt0GjPpwAZODtTpnxbtDsmMG8"
else:
    Token = "ODQ0OTU0ODg5OTIyNjc0NzM4.Gzc5DJ.U06ToI4OMYni2e_9jK2vafEgoOm1ZhTGmzQwDU"

import discord
from discord.ext import commands
import datetime
import os

client = discord.Client()

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


@client.event
async def on_ready():
    print('目前登入身份：', client.user)

@client.event
async def on_message(message):
    print(f"""
NAME：{message.author}
Message：{message.content}
guild：{message.guild}
channel：{message.channel}
time：{gettime()}
------------------------------\n""")
    log_file_path = os.path.join(os.getcwd(), "./Messages/All_message.txt")
    with open(f"./Messages/All_message.txt", "a", encoding='utf8') as log:
        log.write(f"""
NAME：{message.author}
Message：{message.content}
guild：{message.guild}
channel：{message.channel}
time：{gettime()}
------------------------------\n""")
        
    with open(f"./Messages/Author/{message.author}.txt", "a", encoding='utf8') as log:
        log.write(f"""
Message：{message.content}
guild：{message.guild}
channel：{message.channel}
time：{gettime()}
------------------------------\n""")
    with open(f"./Messages/Content/{message.content}.txt", "a", encoding='utf8') as log:
        log.write(f"""
NAME：{message.author}
guild：{message.guild}
channel：{message.channel}
time：{gettime()}
------------------------------\n""")
    with open(f"./Messages/Guild/{message.guild}.txt", "a", encoding='utf8') as log:
        log.write(f"""
NAME：{message.author}
Message：{message.content}
channel：{message.channel}
time：{gettime()}
------------------------------\n""")
    with open(f"./Messages/Channel/{message.channel}.txt", "a", encoding='utf8') as log:
        log.write(f"""
NAME：{message.author}
Message：{message.content}
guild：{message.guild}
time：{gettime()}
------------------------------\n""")





client.run(Token)