# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open("{}/Xbot/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 17881110  # integer value, dont use ""
    API_HASH = "41d02175c2858cae93b745ffa4aaed24"
    TOKEN = "5625036376:AAHJS3Tkf13qV8oz10vbYf-ePQY92NH5fj8"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 5523873067  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "@ASSISTANT_FOR_OFFICALQUEEN0"
    SUPPORT_CHAT = "Team_udanpirappu"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        -1001351412926
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1001351412926
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
    ALLOW_CHATS="awoo"
    HEROKU_API_KEY="awoo"
    HEROKU_APP_NAME="awoo"
    TEMP_DOWNLOAD_DIRECTORY="awoo"
    OPENWEATHERMAP_ID="awoo"
    ARQ_API_KEY="awoo"
    ARQ_API_URL="awoo"
    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "postgresql://doadmin:AVNS_Ah1gcp8RRgLwZGGH1Z6@db-postgresql-nyc1-65692-do-user-12193171-0.b.db.ondigitalocean.com:25060/defaultdb"  # needed for any database modules
    LOAD = []
    START_IMG ="https://te.legra.ph/file/74f97b1978c493689fe6e.mp4"
    MONGO_DB_URI="mongodb+srv://logesh:logesh@cluster0.z75dh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = ""  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list("elevated_users.json", "sudos")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list("elevated_users.json", "supports")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "awooPUWW57GBXS052JS1"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "UGJE9H6VIU03"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "awoo"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
