
from os import system
import psutil
from pypresence import Presence
import time
import sys
import discord
import asyncio
import colorama
from colorama import Fore, init, Style
import platform
from serverclone import Clone

client = discord.Client()
os = platform.system()
if os == "Windows":
    system("cls")
else:
    system("clear")
    print(chr(27) + "[2J")
print(f"""{Fore.RED}         dP                                        dP                                              dP                                    .d888b. d88  888888P  a8888a  
         88                                        88                                              88                             dP dP  Y8' `88  88  88'     d8' ..8b 
.d8888b. 88 .d8888b. 88d888b. .d8888b. 88d888b.    88d888b. dP    dP    dP    dP 88d888b. .d8888b. 88 .d8888b. .d8888b. 88d888b. 8888888 `8bad88  88  88baaa. 88 .P 88 
88'  `"" 88 88'  `88 88'  `88 88ooood8 88'  `88    88'  `88 88    88    88    88 88'  `88 88'  `"" 88 88ooood8 88'  `88 88'  `88  88 88      `88  88      `88 88 d' 88 
88.  ... 88 88.  .88 88    88 88.  ... 88          88.  .88 88.  .88    88.  .88 88    88 88.  ... 88 88.  ... 88.  .88 88       8888888 d.  .88  88       88 Y8'' .8P 
`88888P' dP `88888P' dP    dP `88888P' dP          88Y8888' `8888P88    `88888P' dP    dP `88888P' dP `88888P' `88888P8 dP        dP dP  `8888P  d88P d88888P  Y8888P  
                                                                 .88                                                                                                   
                                                             d8888P                                                                                                    
{Style.RESET_ALL}
                                                            {Fore.MAGENTA}{Style.RESET_ALL}
        """)
token = input(f'Please enter your token:\n >')
guild_s = input('Please enter guild id you want to copy:\n >')
guild = input('Please enter guild id where you want to copy:\n >')
input_guild_id = guild_s  # <-- input guild id
output_guild_id = guild  # <-- output guild id
token = token  # <-- your Account token


print("  ")
print("  ")

@client.event
async def on_ready():
    extrem_map = {}
    print(f"Logged In as : {client.user}")
    print("Cloning Server")
    guild_from = client.get_guild(int(input_guild_id))
    guild_to = client.get_guild(int(output_guild_id))
    await Clone.guild_edit(guild_to, guild_from)
    await Clone.roles_delete(guild_to)
    await Clone.channels_delete(guild_to)
    await Clone.roles_create(guild_to, guild_from)
    await Clone.categories_create(guild_to, guild_from)
    await Clone.channels_create(guild_to, guild_from)
    print(f"""{Fore.GREEN}         dP                                  dP     a88P                                    dP                            .d888b. d88  888888P  a8888a  Y88o  
         88                                  88    d8'    dP dP                             88                            Y8' `88  88  88'     d8' ..8b   `8b 
.d8888b. 88 .d8888b. 88d888b. .d8888b. .d888b88    88    8888888 dP    dP 88d888b. .d8888b. 88 .d8888b. .d8888b. 88d888b. `8bad88  88  88baaa. 88 .P 88    88 
88'  `"" 88 88'  `88 88'  `88 88ooood8 88'  `88    88     88 88  88    88 88'  `88 88'  `"" 88 88ooood8 88'  `88 88'  `88     `88  88      `88 88 d' 88    88 
88.  ... 88 88.  .88 88    88 88.  ... 88.  .88    Y8.   8888888 88.  .88 88    88 88.  ... 88 88.  ... 88.  .88 88       d.  .88  88       88 Y8'' .8P   .8P 
`88888P' dP `88888P' dP    dP `88888P' `88888P8     Y88b  dP dP  `88888P' dP    dP `88888P' dP `88888P' `88888P8 dP       `8888P  d88P d88888P  Y8888P  d88Y  
                                                                                                                                                              
                                                                                                                                                              
    {Style.RESET_ALL}""")
    await asyncio.sleep(5)
    client.close()
