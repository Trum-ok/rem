from datetime import datetime

import discord
from discord.ext import commands

bot = commands.Bot("!")
channel_id = 767482755897360394


@bot.command(aliases=['ping'])
async def test(ctx):
    await ctx.send('pong')


def validate_time(alarm_time):
    return "ok"


while True:
    alarm_time = "17:53:00"

    validate = validate_time(alarm_time)
    if validate != "ok":
        print(validate)
    else:
        print(f"Будильник установлен на время {alarm_time}")
        break

alarm_hour = int(alarm_time[0:2])
alarm_min = int(alarm_time[3:5])
alarm_sec = int(alarm_time[6:8])

while True:
    now = datetime.now()

    current_hour = now.hour
    current_min = now.minute
    current_sec = now.second

    if alarm_hour == current_hour:
        if alarm_min == current_min:
            if alarm_sec == current_sec:
                async def daily_task():
                    message_channel = bot.get_channel(channel_id)
                    print(f"Got channel {message_channel}")
                    c = bot.get_channel(channel_id)
                    file = discord.File("img/EiReminder.png", filename="EiReminder.png")
                    embed = discord.Embed(color=0xffffff)
                    embed.set_image(url="attachment://EiReminder.png")
                    embed.description = "⊱⋅ ─<:Electro:898961646188363837>**[ Отметиться во славу Сёгуна ](" \
                                        "https://webstatic-sea.mihoyo.com/ys/event/signin-sea/index.html?act_id=e202102251931481&lang" \
                                        "=ru-ru)**<:Electro:898961646188363837>─ ⋅⊰ "
                    embed.set_footer(text="⊱⋅ ──────────── ❴ • Y • ❵ ──────────── ⋅⊰")
                    await c.send(file=file, embed=embed)
                break


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="на сладости..."))


bot.run('ODkxNzUzNjIyNDk5NjU1NzEw.YVC8Rw.131Ptd1vyXu1usO4zy82RIGA-98')


'''async def daily_task():
    message_channel = bot.get_channel(channel_id)
    print(f"Got channel {message_channel}")
    c = bot.get_channel(channel_id)
    file = discord.File("img/EiReminder.png", filename="EiReminder.png")
    embed = discord.Embed(color=0xffffff)
    embed.set_image(url="attachment://EiReminder.png")
    embed.description = "⊱⋅ ─<:Electro:898961646188363837>**[ Отметиться во славу Сёгуна ](" \
                        "https://webstatic-sea.mihoyo.com/ys/event/signin-sea/index.html?act_id=e202102251931481&lang" \
                        "=ru-ru)**<:Electro:898961646188363837>─ ⋅⊰ "
    embed.set_footer(text="⊱⋅ ──────────── ❴ • Y • ❵ ──────────── ⋅⊰")
    await c.send(file=file, embed=embed)'''



