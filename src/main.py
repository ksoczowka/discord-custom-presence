# Toga for GUI building
import toga
from toga.style.pack import COLUMN, LEFT, RIGHT, ROW, Pack

# My class to easier manage custom rich presence
from custom_presence import CustomPresence

custom_presence = CustomPresence("presence.json")

apps = custom_presence.get_app_list()

def build(app):
    def apply(widget):
        print("Applied!")
    def preview(widget):
        print("Showing preview!")

    main_box = toga.Box()
    selection_box = toga.Box()
    selection_left_box = toga.Box()
    selection_right_box = toga.Box()
    preview_box = toga.Box()

    select_app = toga.Selection(items=apps)
    select_profile = toga.Selection()

    select_app_label = toga.Label("App: ", style=Pack(text_align=RIGHT))
    select_profile_label = toga.Label("Profile: ", style=Pack(text_align=RIGHT))

    apply_button = toga.Button("Apply", on_press=apply)
    preview_button = toga.Button("Preview", on_press=preview)
    
    
    selection_left_box.add(select_app_label)
    selection_left_box.add(select_app)
    selection_left_box.add(select_profile_label)
    selection_left_box.add(select_profile)

    selection_right_box.add(apply_button)
    selection_right_box.add(preview_button)

    selection_box.add(selection_left_box)
    selection_box.add(selection_right_box)

    main_box.add(selection_box)
    main_box.add(preview_box)

    main_box.style.update(direction=COLUMN, padding=10)
    selection_box.style.update(direction=ROW, padding=10)
    selection_left_box.style.update(direction=ROW, padding=0, flex=1)
    selection_right_box.style.update(direction=ROW, padding=0, flex=1, width=100, alignment=RIGHT)
    preview_box.style.update(direction=ROW, padding=10)

    return main_box


def main():
    return toga.App("Discord Custom Presence", "custom-presence", startup=build)

if __name__ == "__main__":
    main().main_loop()