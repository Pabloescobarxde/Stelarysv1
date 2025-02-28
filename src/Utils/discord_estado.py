from pypresence import Presence
import time

CLIENT_ID = ""
RPC = Presence(CLIENT_ID)

def init_discord():
    RPC.connect()

def update_presence():
    RPC.update(
    )
