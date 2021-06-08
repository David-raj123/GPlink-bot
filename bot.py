from os import environ
import aiohttp
from pyrogram import Client, Filters
InlineKeyboardButton, InlineKeyboardMarkup,

API_ID = environ.get('API_ID')
API_HASH = environ.get('API_HASH')
BOT_TOKEN = environ.get('BOT_TOKEN')
API_KEY = environ.get('API_KEY')


bot = Client('gplink bot', 
             api_id=API_ID, 
             api_hash=API_HASH,
             bot_token=BOT_TOKEN)


@bot.on_message(Filters.command('start') & Filters.private)
async def start(bot, message):
    await message.reply(
        f"**Hi {message.chat.first_name}!**\n\n"
        "I'm GPlink bot. Just send me link and get short link")
    
    
@bot.on_message(Filters.regex(r'https?://[^\s]+') & Filters.private)
async def link_handler(bot, message):
    link = message.matches[0].group(0)
    try:
        short_link = await get_shortlink(link)
    message= f"Here Is Your Converted Short Link"
    markup = InlineKeyboardMarkup([[InlineKeyboardButton("GP Link", url=short_link)]])
    await update.reply_text(text=message, reply_markup=markup, quote=True)
        )
    except Exception as e:
        await message.reply(f'Error: {e}', quote=True)
    
    
async def get_shortlink(link): 
    url = 'https://gplinks.in/api'
    params = {'api': API_KEY, 'url': link}
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, raise_for_status=True) as response:
            data = await response.json()
            return data["shortenedUrl"]
            
        
bot.run()
