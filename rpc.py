
from pypresence import Presence
import time

#config
state = "yesyesyes"
details = "Uploading Images!"
large_image = "yes"
client_id = "823735298894594059"
large_text = "Join lol"

#button1 config
Buton1Label = "Da Server"
Buton1Url = "https://discord.gg/wbfruZUhct"

#button2 config
Buton2Label = "Da Sellix"
Buton2Url = "https://sellix.io/Lush"

RPC = Presence(client_id=client_id)
RPC.connect()

RPC.update(state=state, details=details, large_image=large_image, large_text=large_text, buttons=[{"label": Buton1Label, "url": Buton1Url}, {"label": Buton2Label, "url": Buton2Url}]) # Can specify up to 2 buttons

while 1:
    time.sleep(15) #Can only update presence every 15 seconds
