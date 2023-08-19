# coding=utf-8
from core import HackingTool
from core import HackingToolsCollection


class KawaiiDeauther(HackingTool):
    TITLE = "KawaiiDeauther"
    DESCRIPTION = "Kawaii Deauther is a pentest toolkit whose goal is to perform \n " \
                  "jam on WiFi clients/routers and spam many fake AP for testing purposes."
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/aryanrtm/KawaiiDeauther.git",
        "cd KawaiiDeauther;sudo bash install.sh"
    ]
    RUN_COMMANDS = ["cd KawaiiDeauther;sudo bash KawaiiDeauther.sh"]
    PROJECT_URL = "https://github.com/aryanrtm/KawaiiDeauther"


class WifiJammingTools(HackingToolsCollection):
    TITLE = "Wifi Deauthenticate"
    TOOLS = [
        KawaiiDeauther()
    ]
