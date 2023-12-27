from TeamXBharat.core.bot import CHAMPU
from TeamXBharat.core.dir import dirr
from TeamXBharat.core.git import git
from TeamXBharat.core.userbot import Userbot
from TeamXBharat.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER


GB = ["https://telegra.ph/file/c06d6e3a3abacecf36427.mp4"]

OP = ["https://graph.org/file/ba8d4fb6d3410bbbe1dfc.jpg" , "https://graph.org/file/4c0be5dc3f741bbca04fa.jpg" , "https://graph.org/file/fc4ab06c07e1cc4ba96b0.jpg" , "https://graph.org/file/4466e0a16e28ac94212a2.jpg" , "https://graph.org/file/f2f1f01676b6a8ea5e8a2.jpg" , "https://graph.org/file/9a3e0e44a046af159dc6a.jpg" , "https://graph.org/file/6607c444b4aec00d6d591.jpg"]

dirr()
git()
dbb()
heroku()

app = CHAMPU()
api = SafoneAPI()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
