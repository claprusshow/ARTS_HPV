from telethon import events
import asyncio
import os
import sys

@borg.on(events.NewMessage(pattern=r"\.sam", outgoing=True))
async def _(event):
    if event.fwd_from:
        return

    await event.edit("""
**⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⣿⣿⣿⡿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⣿⣿⡟⡴⠛⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⣿⡏⠴⠞⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⣿⣿⣿⣿⣿⣿⣿⡏⠩⣭⣭⢹⣿⣿⣿⣿⡇
⣿⣿⣿⣿⣿⣿⠟⣵⣾⠟⠟⣼⣿⣿⣿⣿⡇
⣿⣿⣿⣿⣿⠿⠀⢛⣵⡆⣶⣿⣿⣿⣿⣿⡇
⣿⣿⣿⣿⡏⢸⣶⡿⢋⣴⣿⣿⣿⣿⣿⣿⡇
⣿⣿⣿⣿⣇⣈⣉⣉⣼⣿⣿⣿⣿⣿⣿⣿⡇
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢣⠞⢺⣿⡇
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢡⡴⣣⣿⣿⡇
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣿⣿⣿⡇
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇**""")

@borg.on(events.NewMessage(pattern=r"\.gg", outgoing=True))
async def _(event):
    if event.fwd_from:
        return

    await event.edit("""
**⠟⠛⠉⠉⠉⠉⠉⠉⠙⠛⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠉⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⠻⣿⣿⣿⣿⣿⣿
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⢻⣿⣿⣿⣿
⠄⠄⠄⠄⠄⢀⣀⣀⣀⣀⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⢻⣿⣿⣿
⠄⠄⠄⠉⠉⠉⠄⣀⣀⣀⡈⠉⠛⠛⠛⠉⠉⠲⠄⠄⠄⣿⣿⣿
⠠⠤⠤⠔⠒⠋⠉⠄⠄⠄⠈⠉⠒⠒⠒⠒⠒⠂⠄⠄⠄⢻⣿⣿
⠄⠄⢀⠤⠐⠒⠒⠒⠒⠂⠄⠄⠄⠄⠄⠐⠒⠒⠒⢄⠄⠄⢿⣿
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠆⠄⠄⠄⠄⢰⠄⠄⠄⠄⠄⠄⢸⣿
⠄⠄⠄⢠⡖⢲⣶⣶⣤⡀⠄⠄⠄⠄⠄⠈⢀⣤⣤⣤⡀⠄⢸⣿
⠄⠄⠄⠈⠙⠚⠛⠛⠓⠃⠄⠄⠄⠄⠄⠄⠧⠤⢿⣿⡇⠄⢸⣿
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢰⡆⠄⠄⠄⠄⠄⠄⠄⣿
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠳⡀⠄⠄⠄⠄⠄⠄⢸
⠄⠄⠄⠄⠄⠄⠄⠄⠄⡤⠤⠄⠄⠄⠄⠄⢘⡆⠄⠄⠄⠄⢠⣿
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠻⣤⠄⠴⠆⠠⣄⡞⠄⠄⠄⠄⢀⣾⣿
⣆⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣾⣿⣿
⠈⠳⣄⠄⠄⠄⠄⠄⠖⠒⠶⠤⠤⠤⠤⠤⢤⠄⠄⢀⣿⣿⣿⣿
⠄⠄⠈⠑⢦⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣼⣿⣿⣿⣿
⠄⠄⠄⠄⠄⠙⢦⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⣠⣿⣿⣿⣿⣿⣿
⠄⠄⠄⠄⠄⠄⠄⠈⠓⠲⠤⠤⠤⣤⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠣⡀⠄⠄⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠉⠉⠉⠉⠉⠉⠛⠛
⠄⠄⠈⠉⠑⢆⣀⡔⠈⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄**""")

@borg.on(events.NewMessage(pattern=r"\.putin", outgoing=True))
async def _(event):
    if event.fwd_from:
        return

    await event.edit("""
**⣿⣿⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣵⣿⣿⣿⠿⡟⣛⣧⣿⣯⣿⣝⡻⢿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠋⠁⣴⣶⣿⣿⣿⣿⣿⣿⣿⣦⣍⢿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⢷⠄⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⢼⣿⣿⣿⣿
⢹⣿⣿⢻⠎⠔⣛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⣿⣿⣿⣿
⢸⣿⣿⠇⡶⠄⣿⣿⠿⠟⡛⠛⠻⣿⡿⠿⠿⣿⣗⢣⣿⣿⣿⣿
⠐⣿⣿⡿⣷⣾⣿⣿⣿⣾⣶⣶⣶⣿⣁⣔⣤⣀⣼⢲⣿⣿⣿⣿
⠄⣿⣿⣿⣿⣾⣟⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⢟⣾⣿⣿⣿⣿
⠄⣟⣿⣿⣿⡷⣿⣿⣿⣿⣿⣮⣽⠛⢻⣽⣿⡇⣾⣿⣿⣿⣿⣿
⠄⢻⣿⣿⣿⡷⠻⢻⡻⣯⣝⢿⣟⣛⣛⣛⠝⢻⣿⣿⣿⣿⣿⣿
⠄⠸⣿⣿⡟⣹⣦⠄⠋⠻⢿⣶⣶⣶⡾⠃⡂⢾⣿⣿⣿⣿⣿⣿
⠄⠄⠟⠋⠄⢻⣿⣧⣲⡀⡀⠄⠉⠱⣠⣾⡇⠄⠉⠛⢿⣿⣿⣿
⠄⠄⠄⠄⠄⠈⣿⣿⣿⣷⣿⣿⢾⣾⣿⣿⣇⠄⠄⠄⠄⠄⠉⠉
⠄⠄⠄⠄⠄⠄⠸⣿⣿⠟⠃⠄⠄⢈⣻⣿⣿⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⢿⣿⣾⣷⡄⠄⢾⣿⣿⣿⡄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠸⣿⣿⣿⠃⠄⠈⢿⣿⣿⠄⠄⠄⠄⠄⠄⠄
    ПРИШЛО ВРЕМЯ НАЛОГОВОЙ**""")

@borg.on(events.NewMessage(pattern=r"\.stalin", outgoing=True))
async def _(event):
    if event.fwd_from:
        return

    await event.edit("""
**⠄⠄⠄⠄⠄⠄⢀⣠⣤⣴⣶⣶⣶⣶⣦⣤⣀⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⠄⠄⠄⠄
⠄⠄⠄⣿⣿⣟⣡⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣭⡿⣿⣷⡄⠄⠄
⠄⠄⢸⣿⡿⠋⠄⠉⠛⠻⠿⠿⠿⠿⠟⠋⠛⠿⣿⡏⣿⣿⡄⠄
⠄⠄⣾⣿⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣾⣿⣾⣿⣧⠄
⠄⠄⣿⡇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠘⣿⣿⣿⣿⠄
⠄⠄⣿⠣⠞⡛⢶⣦⡄⠄⠠⣤⣶⡿⠿⢷⣆⠄⠄⢨⣿⣿⣿⠄
⠄⠄⡿⠄⠼⠿⠿⣿⠟⠄⠁⢿⣾⣷⡟⢷⡅⠄⠄⠈⣿⣿⡏⠄
⠄⠘⡇⠄⠄⠄⠄⠉⠄⠄⠄⠈⠓⠄⠄⠄⠄⠄⠄⠄⠿⠛⣗⡀
⠄⡗⠇⠄⠄⠄⢠⢀⡇⠄⠄⡀⢲⠄⠄⠄⠄⠄⠄⠄⠄⣄⠸⠁
⠄⢱⡀⠄⠄⠔⢃⣤⡤⣦⣜⣽⣉⠱⡀⠄⠄⠄⠄⠄⠄⠛⢠⠂
⠄⠸⢷⠄⠄⣴⣯⣿⣿⣿⣿⣾⣿⣿⣆⠄⠄⠄⠄⢀⣄⣰⠃⠄
⠄⠄⢸⡈⠛⠿⠟⠋⢉⣭⣭⡉⠻⢿⣿⡧⠄⠄⠄⡞⠈⠁⠄⠄
⠄⠄⠄⠃⠄⠄⠄⠄⠈⠉⠉⠁⠄⠄⠄⠄⠄⢀⠆⡇⠄⠄⠄⠄
⠄⠄⢀⡾⣮⠂⠄⠄⠄⢀⣀⡀⠄⠄⠄⠄⠄⠄⢰⡇⠄⠄⠄⠄
⢀⡴⠋⠄⠘⢷⡀⠘⠛⠛⠛⠿⠋⠉⠁⠄⠄⢠⡾⠻⡄⠄⠄⠄
⣿⠄⠄⠄⠄⠄⠙⣦⡰⣄⣀⣀⠄⠄⠄⠄⢰⡿⠁⠄⠈⢢⠄⣀
⠈⡄⠄⠄⢠⢦⡀⠄⠉⠊⠝⡿⣧⣠⢄⣠⠾⠁⢠⡀⠄⠈⢷⢄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
                   РАССТРЕЛЯТЬ**""")

@borg.on(events.NewMessage(pattern=r"\.spasu", outgoing=True))
async def _(event):
    if event.fwd_from:
        return

    await event.edit("""
**⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢠⣴⠶⣤⡀
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣿⣿⣤⣿⣿
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⡿⠬⠛⠤⢿
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢡⠄⠤⠄⣸
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣀⣤⣾⣿⣶⣾⣿⣿⣿⣷⣶⣄⡀
⠄⠄⠄⠄⠄⠄⠄⠄⣀⣼⣿⣿⣿⣿⡟⢿⡿⣿⣿⣿⣿⣿⣿⣷⣄
⠄⠄⠄⠄⠄⠄⢀⣾⣿⣿⣿⣿⣿⣥⠄⠄⢾⣿⣿⣿⣿⣿⣿⣿⣿⡄
⠄⠄⠄⠄⠄⠄⣾⣿⣿⣿⣿⣿⣿⣿⣾⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀
⠄⠄⢀⣤⣶⣦⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠛⠛⣿⣿⠙⣿⢻⣿⣿⣿⡇
⠄⢠⠞⠋⠛⢿⣿⣿⣿⣿⢻⢻⣿⡄⠄⠄⠄⠄⣿⣿⢸⡇⠄⠻⣿⣿⣿⡄
⠄⡞⢀⣀⡀⠄⠹⣿⣿⡇⠈⢣⢿⣷⠄⠄⠄⠄⣿⡿⢸⠄⠄⠄⢿⣿⣿⣿⡄
⢰⢧⣿⣿⣿⣆⠄⠹⣿⣧⢰⣾⣾⣿⡇⠄⠄⢀⣿⣇⣸⣦⠄⠄⠸⣿⣿⣿⡇
⢸⣾⡿⢻⣿⣿⡄⠄⢿⣿⣾⣿⣿⣿⣿⣶⣶⣾⣿⣿⣿⡿⠄⠄⠄⠹⣿⣿⣿
⢸⣿⠃⠄⢰⣿⣷⠄⢸⣿⣏⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠄⠄⠄⠄⢹⣿⣿
⠄⣿⣧⠄⠹⣿⣿⠄⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠄⠄⣰⢿⣿⣿
⠄⢿⣿⣸⣶⣿⡿⠄⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠄⠄⠁⠸⣿⣿⡇
⠄⠸⣏⢿⣿⣿⠇⠄⣸⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⠄⠄⠄⠄⢿⠋
⠄⠄⢻⣆⠉⠁⠄⢀⣿⣿⢿⣿⣿⣿⣿⣿⠁⢻⣿⣿⣿⣿⣿⡆
⠄⠄⠄⠙⢷⣦⣴⣿⣿⠏⠸⣿⣿⣿⣿⣿⠄⠘⣿⣿⣿⣿⣿⠃
⠄⠄⠄⠄⠄⠉⠛⠛⠁⠄⠄⣿⣿⣿⣿⣿⠄⠄⣻⣿⣿⣿⣿
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣹⣿⣿⣿⣿⠄⣰⣿⣿⣿⣿⣿
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣿⣿⣿⣿⣧⠄⢹⣿⣿⣿⣿⡏
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢠⣿⣿⣿⣿⣿⠄⢸⣿⣿⣿⡿⠁
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠸⣿⣿⣿⣿⣿⠄⣾⣿⣿⠟⠁
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢿⣿⣿⣿⣿⡄⣿⣿⣿
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠘⢿⣿⣿⣿⢠⣿⣿⣿
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⣿⣿⣿⡜⣿⣿⣿
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸⣿⣿⣿⠙⠛⠁
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣿⣿⣿⡿
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢰⣿⣿⣿⣷
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠘⠛⠻⠿⠟
ПРИШЕЛ СПАСАТЬ ТВОЮ ЖОПЫ**""")

@borg.on(events.NewMessage(pattern=r"\.xakep", outgoing=True))
async def _(event):
    if event.fwd_from:
        return

    await event.edit("""
**⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡿⠋⠉⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠉⠙⠿⣿⣿⣿
⣿⣿⡏⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢹⣿⣿
⣿⣿⠁⠄⣀⣤⣤⣄⣀⠄⠄⠄⠄⠄⠄⣀⣤⣤⣤⣄⠄⠄⢿⣿
⣿⡇⠄⠚⠉⠛⠿⢿⣿⣷⡄⠄⠄⢠⣾⣿⡿⠿⠛⠉⠓⠄⢸⣿
⣿⡇⠄⠄⠄⣀⣀⠄⠙⣿⡅⠄⠄⢨⡿⠋⠄⣀⣀⠄⠄⠄⢸⣿
⣿⡇⢀⣴⣿⣿⣿⣿⣶⣼⣷⠄⠄⠈⢠⣶⣿⣿⣿⣿⣦⣀⣸⣿
⣿⡇⠘⠋⠉⠉⠉⠁⠄⢸⣿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸⣿
⣿⣿⡄⠄⠄⠄⠄⠄⠄⣾⣿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣼⣿
⣿⣿⡽⣦⣤⠤⠤⠄⣾⢿⣿⠄⠄⠄⠳⡄⠠⠤⣤⣤⣴⢿⣿⣿
⣿⣿⣧⣻⣽⣦⣄⠄⠉⠸⡇⠄⠄⡀⠄⠁⠄⢀⣾⢏⡟⣼⣿⣿
⣿⣿⣿⣧⡹⣿⠿⢿⣷⣿⣿⠟⢿⣿⣶⣶⣾⠿⣿⡟⣼⣿⣿⣿
⣿⣿⣿⣿⣧⡘⢿⣦⡈⡉⠉⠛⠒⠋⠉⠉⠁⣠⢏⣼⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣷⡘⢿⠄⠁⠙⣿⣿⠂⠄⠄⡴⢃⣾⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣎⠄⠄⢰⣿⣿⠄⠄⠄⣠⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠸⣿⣿⠄⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
           ВЗЛОМ ЖОПЫ НАЧАЛСЯ**""")

@borg.on(events.NewMessage(pattern=r"\.udar", outgoing=True))
async def _(event):
    if event.fwd_from:
        return

    await event.edit("""
**⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣠⣄⡀
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣤⣾⣿⣿⠟⠋
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣤⣾⣿⡿⠛⠉
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣴⣾⣿⠿⠋⠁
⠄⠄⠄⠄⠄⠄⠄⢀⣴⣾⡿⠟⠋
⠄⠄⠄⡀⢾⣶⣾⡿⠛⠁
⠄⣴⣿⣷⡘⢿⡇⠄⣠⣤⣤⣦⡀
⠸⣿⣿⣿⠁⠄⢠⣾⣿⣿⣿⣿⣿⣧
⠄⣿⣿⣿⠄⠄⣿⣿⣿⣿⣿⣿⣿⡿
⢠⣿⣿⣿⡄⢰⣿⣿⣿⣧⣌⣉⣈⣡
⢈⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⠟⠄⠄⠄⠄⠄⠄⠄⣤⡀
⠄⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣦⣀⠄⣼⣿⡇
⠄⠄⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⡦
⠄⠄⠄⠄⠸⣿⣿⣿⣿⣿⣿⣿⣿⡿⡿⣿⡿⠿⠛⠛⠛⠛⠁
⠄⠄⣀⡀⢶⣦⣙⠛⣛⡛⠿⠛⣩⣴
⢠⣿⣿⣿⣦⣙⠻⢿⣿⣿⣿⠿⢋⣡⣾⣶⡄
⠘⣿⣿⣿⣿⣿⠇⣼⡏⢿⡆⢺⣿⣿⣿⣿⣧
⠄⠈⣿⣿⣿⡇⠈⠛⠄⠘⠋⠄⢿⣿⣿⣿⣿⣦⣀⡀
⠰⣾⣿⣿⣿⠇⠄⠄⠄⠄⠄⠄⠄⠄⠙⠿⣿⣿⣿⣿⡇
⠄⠈⠛⠉⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⠛⠛⠛⠁
УЕБУ, СУКА**""")

@borg.on(events.NewMessage(pattern=r"\.f", outgoing=True))
async def _(event):
    if event.fwd_from:
        return

    await event.edit("""
**┏━━━┓
┃┏━━┛
┃┗━━┓
┃┏━━┛
┃┃
┗┛**""")

@borg.on(events.NewMessage(pattern=r"\.us", outgoing=True))
async def _(event):
    if event.fwd_from:
        return

    await event.edit("""
**⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⢀⡴⠒⣙⠓⠲⢦⣀⠄⠄⠄⠄
⠄⠄⠄⠄⢀⣀⣀⣰⠋⣰⣿⠿⠿⢷⣦⡈⢻⡀⠄⠄
⠄⠄⠄⠄⡎⢠⣦⠄⣴⣿⠇⠄⣶⣤⣤⣁⠄⣇⠄⠄
⠄⠄⢀⡾⢀⣿⠃⢰⣿⣿⠄⠄⠙⠿⠿⣿⡧⢘⡇⠄
⠄⠄⢸⠄⣼⡏⢀⣿⣿⣿⣷⣤⣀⣀⡀⠄⢀⡼⠃⠄
⠄⠄⢿⠐⠿⠄⣼⣿⣿⣿⣿⣿⣿⣿⡿⠄⡾⠄⠄⠄
⠄⠄⢈⡷⠄⣴⣿⣿⠟⠿⣿⣿⣿⣿⠃⣸⠁⠄⠄⠄
⠄⠄⢸⡅⠸⢿⡿⢃⡄⢠⣤⣬⡿⢃⣼⠃⠄⠄⠄⠄
⠄⠄⠄⠉⠓⠤⠴⠿⣄⠻⠿⢋⣠⠋⠁⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠉⠳⠖⠋⠁⠄⠄⠄⠄⠄⠄⠄**""")

@borg.on(events.NewMessage(pattern=r"\.dargo", outgoing=True))
async def _(event):
    if event.fwd_from:
        return

    await event.edit("""
**⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣀⣤⠖⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⢀⣤⣤⣴⣾⣿⣷⣤⣤⣤⣤⣤⡦⠤⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⣠⣼⣿⣰⣿⣿⣿⣿⣿⣿⣿⣟⠛⠄⠄⠄⠄
⠄⠄⠄⠄⣤⣶⣿⣿⣿⣿⡿⠻⠃⣸⣿⣿⣿⣿⡟⠷⣄⠄⠄⠄
⠄⠄⠄⠄⠙⠋⠠⣤⣤⣤⣤⣤⣶⣿⣿⣿⣿⣿⣿⡄⠈⠄⠄⠄
⠄⠄⠄⢀⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠸⣿⠇⠄⠄⠄⠄
⠄⠄⣰⣿⣿⣿⣿⡿⠛⠉⠛⠛⠋⠉⢀⣀⠄⠄⠋⠄⠄⠄⠄⠄
⠄⠄⣿⣿⣿⣿⡿⠇⠄⠄⠄⠄⣀⠄⣀⣈⣻⣷⣦⣀⠄⠄⠄⠄
⠄⠄⢻⢿⣿⣿⣿⣷⣖⣀⣀⣴⣿⣿⣿⡿⠿⠿⣿⣿⣷⡄⠄⠄
⠄⠄⠄⠄⣿⠟⠻⣿⣿⣿⣿⣟⠻⣿⣿⣦⠄⠄⠄⠹⢿⣿⠄⠄
⠄⠄⠄⠸⠋⠄⠄⠄⠄⠈⠉⠻⢷⡄⠉⠉⠁⠄⠄⠄⢸⣿⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⠄⠄⠄⠄⠄⠄⠘⠁**""")

@borg.on(events.NewMessage(pattern=r"\.xyu", outgoing=True))
async def _(event):
    if event.fwd_from:
        return

    await event.edit("""
**／\￣ ＼
|      )
＼  _＿ ノ\
 ＼  _ノ\
  ＼ ノ \
   ＼ ノ \
    ＼ノ\／￣＼
   ／￣＼ ＼＿／
   ＼＿／**""")

@borg.on(events.NewMessage(pattern=r"\.csgo", outgoing=True))
async def _(event):
    if event.fwd_from:
        return

    await event.edit("""
**▒█▀▀█ ▒█▀▀▀█ ▄ ▒█▀▀█ ▒█▀▀▀█
▒█░░░ ░▀▀▀▄▄ ░ ▒█░▄▄ ▒█░░▒█
▒█▄▄█ ▒█▄▄▄█ ▀ ▒█▄▄█ ▒█▄▄▄█**""")

@borg.on(events.NewMessage(pattern=r"\.all", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
       
 
    await event.edit("""**⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⣿⣿⣿⡿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⣿⣿⡟⡴⠛⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⣿⡏⠴⠞⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⣿⣿⣿⣿⣿⣿⣿⡏⠩⣭⣭⢹⣿⣿⣿⣿⡇
⣿⣿⣿⣿⣿⣿⠟⣵⣾⠟⠟⣼⣿⣿⣿⣿⡇
⣿⣿⣿⣿⣿⠿⠀⢛⣵⡆⣶⣿⣿⣿⣿⣿⡇
⣿⣿⣿⣿⡏⢸⣶⡿⢋⣴⣿⣿⣿⣿⣿⣿⡇
⣿⣿⣿⣿⣇⣈⣉⣉⣼⣿⣿⣿⣿⣿⣿⣿⡇
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢣⠞⢺⣿⡇
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢡⡴⣣⣿⣿⡇
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣿⣿⣿⡇
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇**""")
    await asyncio.sleep(1.5)
    await event.edit("""**⠟⠛⠉⠉⠉⠉⠉⠉⠙⠛⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠉⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⠻⣿⣿⣿⣿⣿⣿
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⢻⣿⣿⣿⣿
⠄⠄⠄⠄⠄⢀⣀⣀⣀⣀⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⢻⣿⣿⣿
⠄⠄⠄⠉⠉⠉⠄⣀⣀⣀⡈⠉⠛⠛⠛⠉⠉⠲⠄⠄⠄⣿⣿⣿
⠠⠤⠤⠔⠒⠋⠉⠄⠄⠄⠈⠉⠒⠒⠒⠒⠒⠂⠄⠄⠄⢻⣿⣿
⠄⠄⢀⠤⠐⠒⠒⠒⠒⠂⠄⠄⠄⠄⠄⠐⠒⠒⠒⢄⠄⠄⢿⣿
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠆⠄⠄⠄⠄⢰⠄⠄⠄⠄⠄⠄⢸⣿
⠄⠄⠄⢠⡖⢲⣶⣶⣤⡀⠄⠄⠄⠄⠄⠈⢀⣤⣤⣤⡀⠄⢸⣿
⠄⠄⠄⠈⠙⠚⠛⠛⠓⠃⠄⠄⠄⠄⠄⠄⠧⠤⢿⣿⡇⠄⢸⣿
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢰⡆⠄⠄⠄⠄⠄⠄⠄⣿
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠳⡀⠄⠄⠄⠄⠄⠄⢸
⠄⠄⠄⠄⠄⠄⠄⠄⠄⡤⠤⠄⠄⠄⠄⠄⢘⡆⠄⠄⠄⠄⢠⣿
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠻⣤⠄⠴⠆⠠⣄⡞⠄⠄⠄⠄⢀⣾⣿
⣆⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣾⣿⣿
⠈⠳⣄⠄⠄⠄⠄⠄⠖⠒⠶⠤⠤⠤⠤⠤⢤⠄⠄⢀⣿⣿⣿⣿
⠄⠄⠈⠑⢦⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣼⣿⣿⣿⣿
⠄⠄⠄⠄⠄⠙⢦⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⣠⣿⣿⣿⣿⣿⣿
⠄⠄⠄⠄⠄⠄⠄⠈⠓⠲⠤⠤⠤⣤⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠣⡀⠄⠄⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠉⠉⠉⠉⠉⠉⠛⠛
⠄⠄⠈⠉⠑⢆⣀⡔⠈⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄**""")
    await asyncio.sleep(1.5)
    await event.edit("""**⣿⣿⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣵⣿⣿⣿⠿⡟⣛⣧⣿⣯⣿⣝⡻⢿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠋⠁⣴⣶⣿⣿⣿⣿⣿⣿⣿⣦⣍⢿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⢷⠄⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⢼⣿⣿⣿⣿
⢹⣿⣿⢻⠎⠔⣛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⣿⣿⣿⣿
⢸⣿⣿⠇⡶⠄⣿⣿⠿⠟⡛⠛⠻⣿⡿⠿⠿⣿⣗⢣⣿⣿⣿⣿
⠐⣿⣿⡿⣷⣾⣿⣿⣿⣾⣶⣶⣶⣿⣁⣔⣤⣀⣼⢲⣿⣿⣿⣿
⠄⣿⣿⣿⣿⣾⣟⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⢟⣾⣿⣿⣿⣿
⠄⣟⣿⣿⣿⡷⣿⣿⣿⣿⣿⣮⣽⠛⢻⣽⣿⡇⣾⣿⣿⣿⣿⣿
⠄⢻⣿⣿⣿⡷⠻⢻⡻⣯⣝⢿⣟⣛⣛⣛⠝⢻⣿⣿⣿⣿⣿⣿
⠄⠸⣿⣿⡟⣹⣦⠄⠋⠻⢿⣶⣶⣶⡾⠃⡂⢾⣿⣿⣿⣿⣿⣿
⠄⠄⠟⠋⠄⢻⣿⣧⣲⡀⡀⠄⠉⠱⣠⣾⡇⠄⠉⠛⢿⣿⣿⣿
⠄⠄⠄⠄⠄⠈⣿⣿⣿⣷⣿⣿⢾⣾⣿⣿⣇⠄⠄⠄⠄⠄⠉⠉
⠄⠄⠄⠄⠄⠄⠸⣿⣿⠟⠃⠄⠄⢈⣻⣿⣿⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⢿⣿⣾⣷⡄⠄⢾⣿⣿⣿⡄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠸⣿⣿⣿⠃⠄⠈⢿⣿⣿⠄⠄⠄⠄⠄⠄⠄
    ПРИШЛО ВРЕМЯ НАЛОГОВОЙ**""")
    await asyncio.sleep(1.5)
    await event.edit("""**⠄⠄⠄⠄⠄⠄⢀⣠⣤⣴⣶⣶⣶⣶⣦⣤⣀⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⠄⠄⠄⠄
⠄⠄⠄⣿⣿⣟⣡⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣭⡿⣿⣷⡄⠄⠄
⠄⠄⢸⣿⡿⠋⠄⠉⠛⠻⠿⠿⠿⠿⠟⠋⠛⠿⣿⡏⣿⣿⡄⠄
⠄⠄⣾⣿⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣾⣿⣾⣿⣧⠄
⠄⠄⣿⡇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠘⣿⣿⣿⣿⠄
⠄⠄⣿⠣⠞⡛⢶⣦⡄⠄⠠⣤⣶⡿⠿⢷⣆⠄⠄⢨⣿⣿⣿⠄
⠄⠄⡿⠄⠼⠿⠿⣿⠟⠄⠁⢿⣾⣷⡟⢷⡅⠄⠄⠈⣿⣿⡏⠄
⠄⠘⡇⠄⠄⠄⠄⠉⠄⠄⠄⠈⠓⠄⠄⠄⠄⠄⠄⠄⠿⠛⣗⡀
⠄⡗⠇⠄⠄⠄⢠⢀⡇⠄⠄⡀⢲⠄⠄⠄⠄⠄⠄⠄⠄⣄⠸⠁
⠄⢱⡀⠄⠄⠔⢃⣤⡤⣦⣜⣽⣉⠱⡀⠄⠄⠄⠄⠄⠄⠛⢠⠂
⠄⠸⢷⠄⠄⣴⣯⣿⣿⣿⣿⣾⣿⣿⣆⠄⠄⠄⠄⢀⣄⣰⠃⠄
⠄⠄⢸⡈⠛⠿⠟⠋⢉⣭⣭⡉⠻⢿⣿⡧⠄⠄⠄⡞⠈⠁⠄⠄
⠄⠄⠄⠃⠄⠄⠄⠄⠈⠉⠉⠁⠄⠄⠄⠄⠄⢀⠆⡇⠄⠄⠄⠄
⠄⠄⢀⡾⣮⠂⠄⠄⠄⢀⣀⡀⠄⠄⠄⠄⠄⠄⢰⡇⠄⠄⠄⠄
⢀⡴⠋⠄⠘⢷⡀⠘⠛⠛⠛⠿⠋⠉⠁⠄⠄⢠⡾⠻⡄⠄⠄⠄
⣿⠄⠄⠄⠄⠄⠙⣦⡰⣄⣀⣀⠄⠄⠄⠄⢰⡿⠁⠄⠈⢢⠄⣀
⠈⡄⠄⠄⢠⢦⡀⠄⠉⠊⠝⡿⣧⣠⢄⣠⠾⠁⢠⡀⠄⠈⢷⢄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
                   РАССТРЕЛЯТЬ**""")
    await asyncio.sleep(1.5)
    await event.edit("""**⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢠⣴⠶⣤⡀
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣿⣿⣤⣿⣿
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⡿⠬⠛⠤⢿
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢡⠄⠤⠄⣸
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣀⣤⣾⣿⣶⣾⣿⣿⣿⣷⣶⣄⡀
⠄⠄⠄⠄⠄⠄⠄⠄⣀⣼⣿⣿⣿⣿⡟⢿⡿⣿⣿⣿⣿⣿⣿⣷⣄
⠄⠄⠄⠄⠄⠄⢀⣾⣿⣿⣿⣿⣿⣥⠄⠄⢾⣿⣿⣿⣿⣿⣿⣿⣿⡄
⠄⠄⠄⠄⠄⠄⣾⣿⣿⣿⣿⣿⣿⣿⣾⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀
⠄⠄⢀⣤⣶⣦⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠛⠛⣿⣿⠙⣿⢻⣿⣿⣿⡇
⠄⢠⠞⠋⠛⢿⣿⣿⣿⣿⢻⢻⣿⡄⠄⠄⠄⠄⣿⣿⢸⡇⠄⠻⣿⣿⣿⡄
⠄⡞⢀⣀⡀⠄⠹⣿⣿⡇⠈⢣⢿⣷⠄⠄⠄⠄⣿⡿⢸⠄⠄⠄⢿⣿⣿⣿⡄
⢰⢧⣿⣿⣿⣆⠄⠹⣿⣧⢰⣾⣾⣿⡇⠄⠄⢀⣿⣇⣸⣦⠄⠄⠸⣿⣿⣿⡇
⢸⣾⡿⢻⣿⣿⡄⠄⢿⣿⣾⣿⣿⣿⣿⣶⣶⣾⣿⣿⣿⡿⠄⠄⠄⠹⣿⣿⣿
⢸⣿⠃⠄⢰⣿⣷⠄⢸⣿⣏⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠄⠄⠄⠄⢹⣿⣿
⠄⣿⣧⠄⠹⣿⣿⠄⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠄⠄⣰⢿⣿⣿
⠄⢿⣿⣸⣶⣿⡿⠄⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠄⠄⠁⠸⣿⣿⡇
⠄⠸⣏⢿⣿⣿⠇⠄⣸⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⠄⠄⠄⠄⢿⠋
⠄⠄⢻⣆⠉⠁⠄⢀⣿⣿⢿⣿⣿⣿⣿⣿⠁⢻⣿⣿⣿⣿⣿⡆
⠄⠄⠄⠙⢷⣦⣴⣿⣿⠏⠸⣿⣿⣿⣿⣿⠄⠘⣿⣿⣿⣿⣿⠃
⠄⠄⠄⠄⠄⠉⠛⠛⠁⠄⠄⣿⣿⣿⣿⣿⠄⠄⣻⣿⣿⣿⣿
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣹⣿⣿⣿⣿⠄⣰⣿⣿⣿⣿⣿
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣿⣿⣿⣿⣧⠄⢹⣿⣿⣿⣿⡏
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢠⣿⣿⣿⣿⣿⠄⢸⣿⣿⣿⡿⠁
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠸⣿⣿⣿⣿⣿⠄⣾⣿⣿⠟⠁
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢿⣿⣿⣿⣿⡄⣿⣿⣿
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠘⢿⣿⣿⣿⢠⣿⣿⣿
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⣿⣿⣿⡜⣿⣿⣿
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸⣿⣿⣿⠙⠛⠁
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣿⣿⣿⡿
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢰⣿⣿⣿⣷
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠘⠛⠻⠿⠟
ПРИШЕЛ СПАСАТЬ ТВОЮ ЖОПЫ**""")
    await asyncio.sleep(1.5)
    await event.edit("""**⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡿⠋⠉⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠉⠙⠿⣿⣿⣿
⣿⣿⡏⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢹⣿⣿
⣿⣿⠁⠄⣀⣤⣤⣄⣀⠄⠄⠄⠄⠄⠄⣀⣤⣤⣤⣄⠄⠄⢿⣿
⣿⡇⠄⠚⠉⠛⠿⢿⣿⣷⡄⠄⠄⢠⣾⣿⡿⠿⠛⠉⠓⠄⢸⣿
⣿⡇⠄⠄⠄⣀⣀⠄⠙⣿⡅⠄⠄⢨⡿⠋⠄⣀⣀⠄⠄⠄⢸⣿
⣿⡇⢀⣴⣿⣿⣿⣿⣶⣼⣷⠄⠄⠈⢠⣶⣿⣿⣿⣿⣦⣀⣸⣿
⣿⡇⠘⠋⠉⠉⠉⠁⠄⢸⣿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸⣿
⣿⣿⡄⠄⠄⠄⠄⠄⠄⣾⣿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣼⣿
⣿⣿⡽⣦⣤⠤⠤⠄⣾⢿⣿⠄⠄⠄⠳⡄⠠⠤⣤⣤⣴⢿⣿⣿
⣿⣿⣧⣻⣽⣦⣄⠄⠉⠸⡇⠄⠄⡀⠄⠁⠄⢀⣾⢏⡟⣼⣿⣿
⣿⣿⣿⣧⡹⣿⠿⢿⣷⣿⣿⠟⢿⣿⣶⣶⣾⠿⣿⡟⣼⣿⣿⣿
⣿⣿⣿⣿⣧⡘⢿⣦⡈⡉⠉⠛⠒⠋⠉⠉⠁⣠⢏⣼⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣷⡘⢿⠄⠁⠙⣿⣿⠂⠄⠄⡴⢃⣾⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣎⠄⠄⢰⣿⣿⠄⠄⠄⣠⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠸⣿⣿⠄⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
           ВЗЛОМ ЖОПЫ НАЧАЛСЯ**""")
    await asyncio.sleep(1.5)
    await event.edit("""**⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣠⣄⡀
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣤⣾⣿⣿⠟⠋
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣤⣾⣿⡿⠛⠉
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣴⣾⣿⠿⠋⠁
⠄⠄⠄⠄⠄⠄⠄⢀⣴⣾⡿⠟⠋
⠄⠄⠄⡀⢾⣶⣾⡿⠛⠁
⠄⣴⣿⣷⡘⢿⡇⠄⣠⣤⣤⣦⡀
⠸⣿⣿⣿⠁⠄⢠⣾⣿⣿⣿⣿⣿⣧
⠄⣿⣿⣿⠄⠄⣿⣿⣿⣿⣿⣿⣿⡿
⢠⣿⣿⣿⡄⢰⣿⣿⣿⣧⣌⣉⣈⣡
⢈⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⠟⠄⠄⠄⠄⠄⠄⠄⣤⡀
⠄⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣦⣀⠄⣼⣿⡇
⠄⠄⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⡦
⠄⠄⠄⠄⠸⣿⣿⣿⣿⣿⣿⣿⣿⡿⡿⣿⡿⠿⠛⠛⠛⠛⠁
⠄⠄⣀⡀⢶⣦⣙⠛⣛⡛⠿⠛⣩⣴
⢠⣿⣿⣿⣦⣙⠻⢿⣿⣿⣿⠿⢋⣡⣾⣶⡄
⠘⣿⣿⣿⣿⣿⠇⣼⡏⢿⡆⢺⣿⣿⣿⣿⣧
⠄⠈⣿⣿⣿⡇⠈⠛⠄⠘⠋⠄⢿⣿⣿⣿⣿⣦⣀⡀
⠰⣾⣿⣿⣿⠇⠄⠄⠄⠄⠄⠄⠄⠄⠙⠿⣿⣿⣿⣿⡇
⠄⠈⠛⠉⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⠛⠛⠛⠁
УЕБУ, СУКА**""")
    await asyncio.sleep(1.5)
    await event.edit("""**┏━━━┓
┃┏━━┛
┃┗━━┓
┃┏━━┛
┃┃
┗┛**""")
    await asyncio.sleep(1.5)
    await event.edit("""**⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⢀⡴⠒⣙⠓⠲⢦⣀⠄⠄⠄⠄
⠄⠄⠄⠄⢀⣀⣀⣰⠋⣰⣿⠿⠿⢷⣦⡈⢻⡀⠄⠄
⠄⠄⠄⠄⡎⢠⣦⠄⣴⣿⠇⠄⣶⣤⣤⣁⠄⣇⠄⠄
⠄⠄⢀⡾⢀⣿⠃⢰⣿⣿⠄⠄⠙⠿⠿⣿⡧⢘⡇⠄
⠄⠄⢸⠄⣼⡏⢀⣿⣿⣿⣷⣤⣀⣀⡀⠄⢀⡼⠃⠄
⠄⠄⢿⠐⠿⠄⣼⣿⣿⣿⣿⣿⣿⣿⡿⠄⡾⠄⠄⠄
⠄⠄⢈⡷⠄⣴⣿⣿⠟⠿⣿⣿⣿⣿⠃⣸⠁⠄⠄⠄
⠄⠄⢸⡅⠸⢿⡿⢃⡄⢠⣤⣬⡿⢃⣼⠃⠄⠄⠄⠄
⠄⠄⠄⠉⠓⠤⠴⠿⣄⠻⠿⢋⣠⠋⠁⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠉⠳⠖⠋⠁⠄⠄⠄⠄⠄⠄⠄**""")
    await asyncio.sleep(1.5)
    await event.edit("""**⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣀⣤⠖⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⢀⣤⣤⣴⣾⣿⣷⣤⣤⣤⣤⣤⡦⠤⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⣠⣼⣿⣰⣿⣿⣿⣿⣿⣿⣿⣟⠛⠄⠄⠄⠄
⠄⠄⠄⠄⣤⣶⣿⣿⣿⣿⡿⠻⠃⣸⣿⣿⣿⣿⡟⠷⣄⠄⠄⠄
⠄⠄⠄⠄⠙⠋⠠⣤⣤⣤⣤⣤⣶⣿⣿⣿⣿⣿⣿⡄⠈⠄⠄⠄
⠄⠄⠄⢀⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠸⣿⠇⠄⠄⠄⠄
⠄⠄⣰⣿⣿⣿⣿⡿⠛⠉⠛⠛⠋⠉⢀⣀⠄⠄⠋⠄⠄⠄⠄⠄
⠄⠄⣿⣿⣿⣿⡿⠇⠄⠄⠄⠄⣀⠄⣀⣈⣻⣷⣦⣀⠄⠄⠄⠄
⠄⠄⢻⢿⣿⣿⣿⣷⣖⣀⣀⣴⣿⣿⣿⡿⠿⠿⣿⣿⣷⡄⠄⠄
⠄⠄⠄⠄⣿⠟⠻⣿⣿⣿⣿⣟⠻⣿⣿⣦⠄⠄⠄⠹⢿⣿⠄⠄
⠄⠄⠄⠸⠋⠄⠄⠄⠄⠈⠉⠻⢷⡄⠉⠉⠁⠄⠄⠄⢸⣿⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⠄⠄⠄⠄⠄⠄⠘⠁**""")
    await asyncio.sleep(1.5)
    await event.edit("""**／\￣ ＼
|      )
＼  _＿ ノ\
 ＼  _ノ\
  ＼ ノ \
   ＼ ノ \
    ＼ノ\／￣＼
   ／￣＼ ＼＿／
   ＼＿／**""")
    await asyncio.sleep(1.5)
    await event.edit("""**▒█▀▀█ ▒█▀▀▀█ ▄ ▒█▀▀█ ▒█▀▀▀█
▒█░░░ ░▀▀▀▄▄ ░ ▒█░▄▄ ▒█░░▒█
▒█▄▄█ ▒█▄▄▄█ ▀ ▒█▄▄█ ▒█▄▄▄█**""")
    await asyncio.sleep(1.5)
    await event.edit("**@HACKER_PHONE_VIP**")