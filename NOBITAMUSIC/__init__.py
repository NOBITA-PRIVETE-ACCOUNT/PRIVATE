
# All rights reserved.

from NOBITAMUSIC.core.bot import NOBITABot
from NOBITAMUSIC.core.dir import dirr
from NOBITAMUSIC.core.git import git
from NOBITAMUSIC.core.userbot import Userbot
from NOBITAMUSIC.misc import dbb, heroku, sudo

from .logging import LOGGER

# Bot Client

# Directories
dirr()

# Check Git Updates
git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

# Load Sudo Users from DB
sudo()

app = NOBITABot()

# Assistant Client
userbot = Userbot()

from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
HELPABLE = {}
