import os
import eel

from engine.features import *
from engine.command import *
eel.init("www")

playAssistantSound()



os.system('start msedge.exe --app="http://localhost:5500/jarvis/www/"')

eel.start('jarvis//www//index.html', mode=None, host='localhost', block=True)