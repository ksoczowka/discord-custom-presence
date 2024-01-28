# Discord Rich Presence API
from discordrp import Presence

import json

class CustomPresence():
    def __init__(self, path):
        self.path = path
        self.presence_config = json.loads(open(path, 'r').read())
        self.client_id = str(self.presence_config["default_app"]["client_id"])

        self.presence = Presence(self.client_id)
        self.presence.set(self.presence_config["default_app"]["profiles"]["default"])

    def get_app_list(self):
        arr = []
        for app in self.presence_config:
            arr.append(app)
        return arr
    
    def get_profiles_list(self, app):
        return self.presence_config[app]