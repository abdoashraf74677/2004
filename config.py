from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "22574983"))
API_HASH = getenv("API_HASH", "7dcd89bd0218643888d4288eeff052ca")
BOT_TOKEN = getenv("BOT_TOKEN", "6134546060:AAGXFtGv3bSjZWy_ektgG0enlQV2Ijp4ypw")
SESSION_NAME = getenv("SESSION_NAME", "BAAn9UbolkvKncP-3qPW5VuHsXJ1sSBvuYtEzonI-6bo3DrPh3G3noUsTWfBqjVtGWrRxwOc_ty79ratlknd145ZQWIU2z24I0P2SNCcD3hkJZjmR3iW1_aoYEvGg3Slhbn4DSNdk0tktLg0f08aGOWpWAuwr_RKBc3yqSm8FMeksGKmH83sbFNATIJpKXWtljLHvKGwl4IG6XWjftMEG2LFiuTPUUGOs7gh60BhOswfUN3X0B2vjqOuQzUDZjcQ52jqbNbtnqUYh0g9p57TK8ZU18EkxjZ2gxfbwtWz-zeRu3lCDbBDGCJXmeI46YOIrIhrISrmIj4nLSMY5j3w1ak5AAAAAUNAabkA")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "T_N_T_A")
ALIVE_NAME = getenv("ALIVE_NAME", "song")
BOT_USERNAME = getenv("BOT_USERNAME", "BotDarbakamusicbot")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/STKR2/2004")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "VV_OG")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "xl444")

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID", "1854384004").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
