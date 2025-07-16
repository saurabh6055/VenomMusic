from VenomMusic.core.bot import Venom
from VenomMusic.core.dir import dirr
from VenomMusic.core.git import git
from VenomMusic.core.userbot import Userbot
from VenomMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Venom()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
