import re
import os
from os import environ, getenv
from Script import script

# Utility functions
id_pattern = re.compile(r'^.\d+$')

def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# ============================
# Bot Information Configuration
# ============================
SESSION = environ.get('SESSION', 'dreamxbotz_search')   # Session name for the bot
API_ID = int(environ.get('API_ID', '25059287')) # API ID from my.telegram.org
API_HASH = environ.get('API_HASH', '5e7701953107a273724b07f2beaf8f17')  # API Hash from my.telegram.org
BOT_TOKEN = environ.get('BOT_TOKEN', "")    # Bot token from @BotFather

# ============================
# Bot Settings Configuration
# ============================
CACHE_TIME = int(environ.get('CACHE_TIME', 300))    # Cache time in seconds (default: 5 minutes)
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))  # Use caption filter for search results (default: True)
INDEX_CAPTION = bool(environ.get('SAVE_CAPTION', False)) # Save caption db when idexing make it False if you dont use USE_CAPTION_FILTER for search results (default: True)
#Making it false will not save caption in db SO you can save some storage space


PICS = (environ.get('PICS', 'https://graph.org/file/aac9d058fdc57fa21c4ac-ebc88f0d6c0d599af4.jpg https://graph.org/file/4f73c4da8414fe3d99e59-4bfcfa416f9e132c3c.jpg https://graph.org/file/9c8cae5bfebfaa0944bcd-d907c34f86c8628a12.jpg https://graph.org/file/5411b2565f786ede69445-20d07b07f96a62121a.jpg https://graph.org/file/6caeb1a45c840d7140d71-8c2ca4b57c768bced9.jpg https://graph.org/file/fc5571f6f92b5b73142a3-042977d96690b574db.jpg https://graph.org/file/c978e7bd8232e808921ef-b49f4b7bb863a9db9f.jpg')).split()  # Sample pic
NOR_IMG = environ.get("NOR_IMG", "https://graph.org/file/aac9d058fdc57fa21c4ac-ebc88f0d6c0d599af4.jpg")
MELCOW_PHOTO = environ.get("MELCOW_PHOTO", "https://graph.org/file/aac9d058fdc57fa21c4ac-ebc88f0d6c0d599af4.jpg")
SPELL_IMG = environ.get("SPELL_IMG", "https://graph.org/file/036ccc74b772ccac734b2-1d58ffdb5e8d071131.jpg")
SUBSCRIPTION = (environ.get('SUBSCRIPTION', 'https://graph.org/file/242b7f1b52743938d81f1.jpg'))
FSUB_PICS = (environ.get('FSUB_PICS', 'https://graph.org/file/95cefa3272feec077b28a-78591fe27d4215c260.jpg')).split()  # Fsub pic

# ============================
# Admin, Channels & Users Configuration
# ============================
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6964203412').split()] # Replace with the actual admin ID(s) to add
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002153653982 -1002701318235 -1002623667730').split()]  # Channel id for auto indexing (make sure bot is admin)

LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002583655280'))  # Log channel id (make sure bot is admin)
BIN_CHANNEL = int(environ.get('BIN_CHANNEL', '-1002635477308'))  # Bin channel id (make sure bot is admin)
PREMIUM_LOGS = int(environ.get('PREMIUM_LOGS', '-1002596920866'))  # Premium logs channel id
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '-100').split()] #(make sure bot is admin)
support_chat_id = environ.get('SUPPORT_CHAT_ID', '-1002655119999')  # Support group id (make sure bot is admin)
reqst_channel = environ.get('REQST_CHANNEL_ID', '-1002635477308')  # Request channel id (make sure bot is admin)
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'https://t.me/disscus_moviehub4u')  # Support group link (make sure bot is admin)

# FORCE_SUB 
auth_req_channels = environ.get("AUTH_REQ_CHANNELS", "-1003178961495")# requst to join Channel for force sub (make sure bot is admin) only for bot ADMINS  
auth_channels     = environ.get("AUTH_CHANNELS", "-1002282783745 -1002393557941 -1002594005991 -1002497307753")# Channels for force sub (make sure bot is admin)

# ============================
# Payment Configuration
# ============================
QR_CODE = environ.get('QR_CODE', 'https://graph.org/file/ae32e6ff985e883b2b015-18135dd65f2560c993.jpg')    # QR code image for payments
OWNER_UPI_ID = environ.get('OWNER_UPI_ID', 'moviehub4uofficial0@okicici')    # Owner UPI ID for payments

STAR_PREMIUM_PLANS = {
    10: "7day",
    20: "15day",    
    40: "1month", 
    55: "45day",
    75: "60day",
}  # Premium plans with their respective durations in days

# ============================
# MongoDB Configuration
# ============================
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://Dvlnaruto:Dvlnaruto@cluster0.kstnhv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  # MongoDB URI for the database
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0") # Database name (default: cluster)
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'dreamcinezone_files') # Collection name (default: dreamcinezone_files)

# If MULTIPLE_DB Is True Then Fill DATABASE_URI2 Value Else You Will Get Error.
MULTIPLE_DB = is_enabled(os.environ.get('MULTIPLE_DB', "True"), False) # Type True For Turn On MULTIPLE DB FUNTION 
DATABASE_URI2 = environ.get('DATABASE_URI2', "mongodb+srv://Harshil:Harshil@cluster0.0esrpqa.mongodb.net/?appName=Cluster0")  # MongoDB URI for the second database (if MULTIPLE_DB is True)
# ============================
# Movie Notification & Update Settings
# ============================
MOVIE_UPDATE_NOTIFICATION = bool(environ.get('MOVIE_UPDATE_NOTIFICATION', False))  # Notification On (True) / Off (False)
MOVIE_UPDATE_CHANNEL = int(environ.get('MOVIE_UPDATE_CHANNEL', '-100'))  # Notification of sent to your channel
DREAMXBOTZ_IMAGE_FETCH = bool(environ.get('DREAMXBOTZ_IMAGE_FETCH', True))  # On (True) / Off (False)
LINK_PREVIEW = bool(environ.get('LINK_PREVIEW', False)) # Shows link preview in notification msg instead of image
ABOVE_PREVIEW = bool(environ.get('ABOVE_PREVIEW', True)) # Shows link preview above the text in notification msg if True else below the msg
TMDB_API_KEY = environ.get('TMDB_API_KEY', '') # preffer to use your own tmdb API Key get it from https://www.themoviedb.org/settings/api
TMDB_POSTER = bool(environ.get('TMDB_POSTER', True)) # Shows TMDB poster in notification msg
LANDSCAPE_POSTER = bool(environ.get('LANDSCAPE_POSTER', True)) # Shows landscape poster in notification msg

# ============================
# Verification Settings
# ============================
IS_VERIFY = is_enabled('IS_VERIFY', False)  # Verification On (True) / Off (False)
LOG_VR_CHANNEL = int(environ.get('LOG_VR_CHANNEL', '-1002583655280')) #Verification Channel Id 
LOG_API_CHANNEL = int(environ.get('LOG_API_CHANNEL', '-1002583655280')) #If Anyone Set Your Bot In Any Group And Set Shortner In That Group Then In This Channel The All Details Come
VERIFY_IMG = environ.get("VERIFY_IMG", "https://graph.org/file/c72893caf2195f8b1b978-711f8a3c7bbe091a91.jpg")

TUTORIAL = environ.get("TUTORIAL", "https://t.me/moviehub4u_update")   # Tutorial link for verification
TUTORIAL_2 = environ.get("TUTORIAL_2", "https://t.me/moviehub4u_update")   # Second tutorial link for verification
TUTORIAL_3 = environ.get("TUTORIAL_3", "https://t.me/moviehub4u_update")   # Third tutorial link for verification

# Verification (Must Fill All Veriables. Else You Got Error
SHORTENER_API = environ.get("SHORTENER_API", "bb50d67eb901568a535bf733205757422e1cd404") # Shortener API key
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", "shrinkearn.com") # Shortener website

SHORTENER_API2 = environ.get("SHORTENER_API2", "")  # Shortener API key for second website
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", "") # Shortener website for second website

SHORTENER_API3 = environ.get("SHORTENER_API3", "")  
SHORTENER_WEBSITE3 = environ.get("SHORTENER_WEBSITE3", "") # Shortener website for third website

TWO_VERIFY_GAP = int(environ.get('TWO_VERIFY_GAP', "43200")) # Time gap for two-step verification in seconds (default: 20 minutes)
THREE_VERIFY_GAP = int(environ.get('THREE_VERIFY_GAP', "43200"))    

# ============================
# Channel & Group Links Configuration
# ============================
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/movies_search_zone') # Group link for the bot
OWNER_LNK = environ.get('OWNER_LNK', 'https://t.me/disscus_moviehub4u') # Owner link for the bot
UPDATE_CHNL_LNK = environ.get('UPDATE_CHNL_LNK', 'https://t.me/moviehub4u_update') # Update channel link for the bot

# ============================
# User Configuration
# ============================
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
PREMIUM_USER = [int(user) if id_pattern.search(user) else user for user in environ.get('PREMIUM_USER', '').split()]

# ============================
# Miscellaneous Configuration
# ============================
ULTRA_FAST_MODE = is_enabled(environ.get('ULTRA_FAST_MODE', "True"), True) # Set to True for fast search, False for original search

MAX_B_TN = environ.get("MAX_B_TN", "10") # Maximum number of buttons in a row (default: 5)
PORT = int(environ.get("PORT", "8080"))  # Port for the web server (default: 8080)
MSG_ALRT = environ.get('MSG_ALRT', 'Welcome to Hidden Leaf Village 🌿') # Alert message for users
DELETE_TIME = int(environ.get("DELETE_TIME", "300"))  #  deletion time in seconds (default: 5 minutes). Adjust as per your needs.
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")   # Custom caption for files
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION) # Custom caption for batch files
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")     # Custom IMDB template 
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None) # Maximum number of elements in a list (default: None, no limit)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))  # Index Request Channel ID (make sure bot is admin)
NO_RESULTS_MSG = bool(environ.get("NO_RESULTS_MSG", True))  # True if you want no results messages in Log Channel
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)    # Max Button On (True) / Off (False)
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)    # P_TTI_SHOW_OFF On (True) / Off (False)
IMDB = is_enabled((environ.get('IMDB', "False")), False)    # IMDB Results On (True) / Off (False)
TMDB_ON_SEARCH = is_enabled((environ.get('TMDB_ON_SEARCH', "False")), False)    # Use TMDB Poster On Search Results
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True) # Auto Filter On (True) / Off (False)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True) # Auto Delete On (True) / Off (False)
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False) # Long IMDB Description On (True) / Off (False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True) # Spell Check Mode On (True) / Off (False)
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "False")), False) # Melcow New Users On (True) / Off (False)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False) # Protect Content On (True) / Off (False)
PM_SEARCH = bool(environ.get('PM_SEARCH', True))  # PM Search On (True) / Off (False)
EMOJI_MODE = bool(environ.get('EMOJI_MODE', False))  # Emoji status On (True) / Off (False)
BUTTON_MODE = is_enabled((environ.get('BUTTON_MODE', "False")), False) # pm & Group button or link mode (True) / Off (False)
STREAM_MODE = bool(environ.get('STREAM_MODE', False)) # Set Stream mode True or False
PREMIUM_STREAM_MODE = bool(environ.get('PREMIUM_STREAM_MODE', False)) # Set Stream mode True or False only for premium users


# ============================
# Bot Configuration
# ============================

AUTH_REQ_CHANNELS = [int(ch) for ch in auth_req_channels.split() if ch and id_pattern.match(ch)] 
AUTH_CHANNELS = [int(ch) for ch in auth_channels.split() if ch and id_pattern.match(ch)]
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
LANGUAGES = {"ᴍᴀʟᴀʏᴀʟᴀᴍ":"mal","ᴛᴀᴍɪʟ":"tam","ᴇɴɢʟɪsʜ":"eng","ʜɪɴᴅɪ":"hin","ᴛᴇʟᴜɢᴜ":"tel","ᴋᴀɴɴᴀᴅᴀ":"kan","ɢᴜᴊᴀʀᴀᴛɪ":"guj","ᴍᴀʀᴀᴛʜɪ":"mar","ᴘᴜɴᴊᴀʙɪ":"pun"}
QUALITIES = ["360P", "480P", "720P", "1080P", "1440P", "2160P", "4K"]

SEASON_COUNT = 12
SEASONS = [f"S{str(i).zfill(2)}" for i in range(1, SEASON_COUNT + 1)]

BAD_WORDS = {
    "PrivateMovieZ",
    "toonworld4all",
    "themoviesboss",
    "1tamilmv",
    "tamilblasters",
    "1tamilblasters",
    "skymovieshd",
    "extraflix",
    "hdm2",
    "moviesmod",
    "hdhub4u",
    "mkvcinemas",
    "primefix",
    "join",
    "www",
    "villa",
    "tg",
    "original"
    "Hdhub4u", 
    "cinevood",
    "skymoviedHD,",
    "original",
    "tg",
    "www",
    "villa",
    "join",
    "PrivateMovieZ",
    "toonworld4all",
    "themoviesboss",
    "1tamilmv",
    "tamilblasters",
    "1tamilblasters",
    "skymovieshd",
    "extraflix",
    "hdm2", 
    "moviesmod",
    "hdhub4u",
    "mkvcinemas",
    "www", "join",
    "primefix",
    "sbanime", 
    "sbanimes"
} # Set of bad words to filter out
   

# ============================
# Server & Web Configuration
# ============================

NO_PORT = bool(environ.get('NO_PORT', False))
APP_NAME = None
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = environ.get('APP_NAME')
else:
    ON_HEROKU = False
BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
URL = "https://{}/".format(FQDN) if ON_HEROKU or NO_PORT else "https://{}/".format(FQDN, PORT)
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
WORKERS = int(environ.get('WORKERS', '4'))
SESSION_NAME = str(environ.get('SESSION_NAME', 'dreamXBotz'))
MULTI_CLIENT = False
name = str(environ.get('name', 'DREAMXBOTZ'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = str(getenv('APP_NAME'))
else:
    ON_HEROKU = False
HAS_SSL = bool(getenv('HAS_SSL', True))
if HAS_SSL:
    URL = "https://{}/".format(FQDN)
else:
    URL = "http://{}/".format(FQDN)

# ============================
# Reactions Configuration
# ============================
REACTIONS = ["🤝", "😇", "🤗", "😍", "👍", "🎅", "😐", "🥰", "🤩", "😱", "🤣", "😘", "👏", "😛", "😈", "🎉", "⚡️", "🫡", "🤓", "😎", "🏆", "🔥", "🤭", "🌚", "🆒", "👻", "😁"]

# ============================
# Commands Bot
# ============================
Bot_cmds = {
    "start": "Sᴛᴀʀᴛ Mᴇ Bᴀʙʏ",
    "stats": "Gᴇᴛ Bᴏᴛ Sᴛᴀᴛs",
    "alive": " Cʜᴇᴄᴋ Bᴏᴛ Aʟɪᴠᴇ ᴏʀ Nᴏᴛ ",
    "settings": "ᴄʜᴀɴɢᴇ sᴇᴛᴛɪɴɢs",
    "id": "ɢᴇᴛ ɪᴅ ᴛᴇʟᴇɢʀᴀᴍ ",
    "info": "Gᴇᴛ Usᴇʀ ɪɴғᴏ ",
    "del_msg": "ʀᴇᴍᴏᴠᴇ ғɪʟᴇ ɴᴀᴍᴇ ᴄᴏʟʟᴇᴄᴛɪᴏɴ ɴᴏтɪғɪᴄᴀᴛɪᴏɴ...",
    "movie_update": "ᴏɴ ᴏғғ ᴀᴄᴄᴏʀᴅɪɴɢ ʏᴏᴜʀ ɴᴇᴇᴅᴇᴅ...",
    "pm_search": "ᴘᴍ sᴇᴀʀᴄʜ ᴏɴ ᴏғғ ᴀᴄᴄᴏʀᴅɪɴɢ ʏᴏᴜʀ ɴᴇᴇᴅᴇᴅ...",
    "trendlist": "Gᴇᴛ Tᴏᴘ Tʀᴀɴᴅɪɴɢ Sᴇᴀʀᴄʜ Lɪsᴛ",
    "broadcast": "ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴀʟʟ ᴜꜱᴇʀꜱ.",
    "grp_broadcast": "ʙʀᴏᴀᴅᴄᴀsᴛ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ɢʀᴏᴜᴘs",
    "send": "ꜱᴇɴᴅ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴜꜱᴇʀ.",
    "add_premium": "ᴀᴅᴅ ᴀɴʏ ᴜꜱᴇʀ ᴛᴏ ᴘʀᴇᴍɪᴜᴍ.",
    "remove_premium": "ʀᴇᴍᴏᴠᴇ ᴀɴʏ ᴜꜱᴇʀ ꜰʀᴏᴍ ᴘʀᴇᴍɪᴜᴍ.",
    "premium_users": "ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀꜱ.",
    "restart": "ʀᴇꜱᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ.",
    "group_cmd": "ɢʀᴏᴜᴘ ᴄᴏᴍᴍᴀɴᴅ ʟɪsᴛ",
    "admin_cmd": "ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅs ʟɪsᴛ.",
    "reset_group": "Group Setting Default",
    "trial_reset": "User Trial Reset",
    "remove_fsub": "Remove Forced Subscription (group admin only)",
}


#Don't Change Anything Here
if MULTIPLE_DB == False:
    DATABASE_URI = DATABASE_URI
    DATABASE_URI2 = DATABASE_URI
else:
    DATABASE_URI = DATABASE_URI
    DATABASE_URI2 = DATABASE_URI2

# ============================
# Logs Configuration
# ============================
LOG_STR = "Current Customized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for your queries.\n" if IMDB else "IMDB Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found, Users will be redirected to send /start to Bot PM instead of sending file directly.\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled, files will be sent in PM instead of starting the bot.\n")
LOG_STR += ("BUTTON_MODE is found, filename and file size will be shown in a single button instead of two separate buttons.\n" if BUTTON_MODE else "BUTTON_MODE is disabled, filename and file size will be shown as different buttons.\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be sent along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled, Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode is enabled, bot will be suggesting related movies if movie name is misspelled.\n" if SPELL_CHECK_REPLY else "Spell Check Mode is disabled.\n")
