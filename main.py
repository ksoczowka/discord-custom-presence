from discordrp import Presence
import toga
from toga.style.pack import COLUMN, LEFT, RIGHT, ROW, Pack

client_id = "1199807115498365098"  # Replace this with your own client id
presence = Presence(client_id)

def build(app):
    default_box = toga.Box()
    custom1_box = toga.Box()
    custom2_box = toga.Box()
    box = toga.Box()

    default_label = toga.Label("Default", style=Pack(text_align=RIGHT))
    custom1_label = toga.Label("Custom 1", style=Pack(text_align=RIGHT))
    custom2_label = toga.Label("Custom 2", style=Pack(text_align=RIGHT))

    def pre_default(widget):
        presence.set(
                {
                    "state": "On Discord",
                    "details": "Arguing with people",
                    "assets": {
                        "large_image": "crab",
                        "large_text": "Crab",
                    },
                }
            )
    
    def pre_custom1(widget):
        presence.set(
                {
                    "state": "at Visual Studio Code",
                    "details": "Programming",
                    "assets": {
                        "large_image": "coding",
                        "large_text": "Crab",
                    },
                }
            )

    def pre_custom2(widget):
        presence.set(
                {
                    "state": "Idle",
                    "details": "Doing nothing",
                    "assets": {
                        "large_image": "watching",
                        "large_text": "Crab",
                    },
                }
            )

    default_button = toga.Button("Switch", on_press=pre_default)
    custom1_button = toga.Button("Switch", on_press=pre_custom1)
    custom2_button = toga.Button("Switch", on_press=pre_custom2)

    default_box.add(default_label)
    default_box.add(default_button)

    custom1_box.add(custom1_label)
    custom1_box.add(custom1_button)

    custom2_box.add(custom2_label)
    custom2_box.add(custom2_button)

    box.add(default_box)
    box.add(custom1_box)
    box.add(custom2_box)

    box.style.update(direction=COLUMN, padding=10)
    default_box.style.update(direction=ROW, padding=5)
    custom1_box.style.update(direction=ROW, padding=5)
    custom2_box.style.update(direction=ROW, padding=5)

    return box

def main():
    return toga.App("Discord Rich Presence", "org.higamidev.drp", startup=build)

if __name__ == "__main__":
    main().main_loop()