from initialiser import CinnamonInit
from cinnamon_setup import CinnamonSetup

CinnamonInit().initialise()

from rich import *
from rich.rule import *
from rich.color import *
from rich.style import *
from rich.theme import *
from rich.traceback import install
from rich.console import Console

from ursina.audio import *
from ursina import *

import os
import glob
import pathlib

class Cinnamon(CinnamonSetup):

    def __init__(self):
        self.videos_list: list = []
        self._videos: list = []
        self.videos: dict = {}
        self.video_index: int = 1
        self.valid_video_indexs: List[int] = []
        with open(".\\settings\\dir.txt", "r") as file:
            self.videos_folder = file.read()
        self.debug_mode = False
        self._dir = os.path.abspath("videos_database")
        self.cinnamon_theme = Theme({
            "input": "light_goldenrod2",
            "message": "light_goldenrod3",
            "process": "tan",
            "query": "wheat1",
            "error": "bold red"
        })
        self.dir = glob.glob(fr"{self._dir}\\*.txt")
        self.startfile_streaming = True if os.path.exists(".\\settings\\streaming_preference.txt") is False else False
        self.subprocess_streaming = False

    def get_videos_from_folder(self):
        console = Console(theme=self.cinnamon_theme)
        if os.path.exists(".\\videos_database") is True:
            if self.debug_mode is True:
                console.print("[bold][message]Successfully found videos_folder.txt..[/]")
            for self.item in self.dir:
                try:
                    with open(fr"{self.item}", "r") as file:
                        self.contents = file.read()
                        self.videos_list.append(self.contents)
                        self._item = self.contents.split(", ", 2)
                        self.index_number = self._item[1].split(": ", 2)
                        self.index_number = self.index_number[1].replace("}", "")
                        self.index_number = self.index_number.replace("'", "")
                        self.valid_video_indexs.append(int(self.index_number))
                except IndexError: # Attempting to repair database
                    self.get_videos(self.videos_folder)
                    with open(fr"{self.item}", "r") as file:
                        self.contents = file.read()
                        self.videos_list.append(self.contents)
                        self._item = self.contents.split(", ", 2)
                        self.index_number = self._item[1].split(": ", 2)
                        self.index_number = self.index_number[1].replace("}", "")
                        self.index_number = self.index_number.replace("'", "")
                        self.valid_video_indexs.append(int(self.index_number))
            if self.debug_mode is True:
                console.print("[bold][message]Read from videos file..[/]")
                print(self.videos_list)

    def main_menu(self):
        os.system("cls")
        console = Console(theme=self.cinnamon_theme)
        console.print("[bold][message]─── Cinnamon ───────────────────────────────────────────────\n  │\n  │ 1. Watch Video\n  │\n  │ 2. List Videos\n  │\n  │ 3. Settings\n  │\n  │ 4. Exit\n  │\n────────────────────────────────────────────────────────────\n  │ Select an option (1-4)\n────────────────────────────────────────────────────────────[/]")
        self.user_input = console.input("[bold][input] -> [/]")
        return self.user_input

    def run(self):
        console = Console(theme=self.cinnamon_theme)
        os.system("cls")
        if os.path.exists(".\\videos_database") is False:
            self.set_videos_folder()
            self.get_videos_from_folder()
        elif os.path.exists(".\\videos_database") is True:
            self.get_videos_from_folder()
        self.background_music = Audio(sound_file_name="Demon Slayer OST - Confrontation.mp3", autoplay=True, volume=100, loop=True)
        while True:
            self.user_input = self.main_menu()
            if self.user_input in ("1", 1):
                os.system("cls")
                console.print("[bold][message]────────────────────────────────────────────────────────────[/]")
                for self.item in self.videos_list:
                    self.item = self.item.split(sep=", ", maxsplit=2)
                    self.filename = os.path.split(self.item[0])
                    self._videos.append(self.filename[1][:-1])
                    self.index_number = self.item[1].split(": ", 2)
                    self.index_number = self.index_number[1].replace("}", "")
                    console.print(f"[bold][message]Index ({self.index_number[1]}) │ {self.filename[1][:-1]}[/]")
                self.user_input = console.input("[bold][input]────────────────────────────────────────────────────────────\nWhat video do you want to watch? (Please use the index number) -> [/]")
                if int(self.user_input) in self.valid_video_indexs:
                    if self.startfile_streaming is True:
                        os.startfile(fr".\\{self.videos_folder}\\{self._videos[int(self.user_input) - 1]}")
                    if self.subprocess_streaming is True:
                        subprocess.Popen(fr".\\{self.videos_folder}\\{self._videos[int(self.user_input) - 1]}")
                else: 
                    console.print("[bold][error]The index number you specified was incorrect..[/]"), time.sleep(1)

            if self.user_input in ("2", 2):
                self._ = True
                while self._ is True:
                    os.system("cls")
                    console.print("[bold][message]────────────────────────────────────────────────────────────[/]")
                    for self.item in self.videos:
                        self.item = self.item.split(sep=", ", maxsplit=2)
                        self.filename = os.path.split(self.item[0])
                        self._videos.append(self.filename[1][:-1])
                        self.index_number = str(self.item[1]).split(": ", 2)
                        self.index_number = self.index_number[1].replace("}", "")
                        console.print(f"[bold][message]Index ({self.index_number[1]}) │ {self.filename[1][:-1]}[/]")
                    self.exit_input = console.input("[bold][message]────────────────────────────────────────────────────────────\nDo you want to exit this menu? (Y/N) -> [/]").title()
                    if self.exit_input in ("Y", "Yes"):
                        self._ = False
                        os.system("cls")
                    if self.exit_input in ("N", "No"):
                        pass
                    if self.exit_input not in ("Y", "Yes", "N", "No"):
                        console.print(f"[bold][error]'{self.exit_input}' is not a valid input..[/]")
                        time.sleep(2)

            if self.user_input in ("3", 3):
                self.settings_loop = True
                while self.settings_loop is True:
                    os.system("cls")
                    console.print("[bold][message]─── Settings ───────────────────────────────────────────────\n  │\n  │ 1. Change Streaming Type\n  │\n  │ 2. Refresh Database\n  │\n  │ 3. Change Videos Folder\n  │\n  │ 4. Exit to Main Menu\n  │\n────────────────────────────────────────────────────────────\n  │ Select an option (1-4)\n────────────────────────────────────────────────────────────[/]")
                    self.settings_input = console.input("[bold][message] > [/]")

                    if self.settings_input in ("1", 1):
                        self.streaming_menu_loop = True
                        while self.streaming_menu_loop is True:
                            os.system("cls")
                            console.print("[bold][message]─── Streaming Type ─────────────────────────────────────────\n  │\n  │ 1. Streaming Type 1 (Startfile)\n  │\n  │ 2. Streaming Type 2 (Subprocess)\n  │\n  │ 3. Info\n  │\n  │ 4. Exit to Settings\n  │\n────────────────────────────────────────────────────────────\n  │ Select an option (1-4)\n────────────────────────────────────────────────────────────[/]")
                            self.streaming_input = console.input("[bold][message] > [/]")

                            if self.streaming_input in ("1", 1):
                                self.startfile_streaming = True
                                with open(".\\settings\\streaming_preference.txt", "w") as file:
                                    file.write("startfile_streaming")
                            
                            if self.streaming_input in ("2", 2):
                                self.subprocess_streaming = True
                                with open(".\\settings\\streaming_preference.txt", "w") as file:
                                    file.write("subprocess_streaming")

                            if self.streaming_input in ("3", 3):
                                console.print("[bold][message]the j[/]")

                            if self.streaming_input in ("4", 4):
                                self.streaming_menu_loop = False
                    
                    if self.settings_input in ("2", 2):
                        self.get_videos(self.videos_folder)

                    if self.settings_input in ("4", 4):
                        self.settings_loop = False

            if self.user_input in ("4", 4):
                return False

if __name__ == '__main__':
    Cinnamon().run()

    