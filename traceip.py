import requests
import json
import asyncio
from datetime import datetime
from pyrogram import Client, filters
from pyrogram.types import Message
from config import API_ID, API_HASH, BOT_TOKEN 
#edit config.py for self host
from functools import partial
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

command = partial(filters.command, prefixes=["!", "/"])

start_text = f"Hola ! , Thank You For Using me, I can Help You Search Info of an IP\n**Syntax:** `/ip [ip]`\n\nI won't force anyone to Join Our Channel by adding a Force Sub, But it would be very nice if you join our channel @CrAzIe_BoTz for more such botz ."

app = Client("traceip", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(command("start"))
async def start(_, message):
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="Source Code", url="https://github.com/CuTePsYcHo_110/TraceIP"
                ),
                InlineKeyboardButton(
                    text="Dev", url="https://t.me/CuTePsYcHo_110"
                )
            ]
        ]
    )
    await message.reply_text(start_text, reply_markup=keyboard)
    
@app.on_message(command("help"))
async def help(_, message):
    await message.reply_text("Use the Following Syntax\n/ip [ip], Commands starts with either / or ! \n\n Report Errors in @CrAzIe_BoTz_ChAt")
    

@app.on_message(command("ip"))
async def ip(_, message): 
    searchip = message.text.split(" ", 1)
    if len(searchip) == 1:
        await message.reply_text("**Usage:**\n/ip [ip]")
        return
    else:
        searchip = searchip[1]
        m = await message.reply_text("Searching...")
    try:
        url = requests.get(f"http://ip-api.com/json/{searchip}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query")
        response = json.loads(url.text)
        text = f"""
**IP Address:** `{response['query']}`
**Status:** `{response['status']}`
**Continent Code:** `{response['continentCode']}`
**Country:** `{response['country']}`
**Country Code :** `{response['countryCode']}`
**Region:** `{response['region']}`
**Region Name :** `{response['regionName']}`
**City:** `{response['city']}`
**District:** `{response['district']}`
**ZIP:** `{response['zip']}`
**Latitude:** `{response['lat']}`
**Longitude:** `{response['lon']}`
**Time Zone:** `{response['timezone']}`
**Offset:** `{response['offset']}`
**Currency:** `{response['currency']}`
**ISP:** `{response['isp']}`
**Org:** `{response['org']}`
**As:** `{response['as']}`
**Asname:** `{response['asname']}`
**Reverse:** `{response['reverse']}`
**User is on Mobile:** `{response['mobile']}`
**Proxy:** `{response['proxy']}`
**Hosting:** `{response['hosting']}`"""
        await m.edit_text(text, parse_mode="markdown")
    except:
        await m.edit_text("Unable To Find Info!")


app.run()
