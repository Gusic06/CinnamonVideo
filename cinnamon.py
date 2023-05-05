from _initialiser import CinnamonInit
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

from os import system, startfile, remove, rmdir, mkdir
from os.path import exists, abspath, split
#from pathlib import Path
#add_dll_directory(fr'{pathlib.home().drive}\\Program Files\\VideoLAN\\VLC')
#try:
#    import vlc
#except FileNotFoundError or OSError:
#    add_dll_directory(fr'{pathlib.home().drive}\\Program Files\\VideoLAN\\VLC')
#    import vlc
import glob

install()

class Cinnamon(CinnamonSetup):

    def __init__(self):
        self.cinnamon_theme = Theme({
            "input": "light_goldenrod2",
            "message": "light_goldenrod3",
            "process": "tan",
            "query": "wheat1",
            "error": "bold red"
        })
        self.debug_mode = False
        self.videos_list: list = []
        self._videos: list = []
        self.videos: dict = {}
        self.video_index: int = 1
        self.valid_video_indexs: List[int] = []

        if exists(r".\\videos_database") is False:
            self.set_videos_folder()
        if exists(".\\settings\\dir.txt"):
            with open(".\\settings\\dir.txt", "r") as file:
                self.videos_folder = file.read()
        else:
            self.set_videos_folder()
            with open(".\\settings\\dir.txt", "r") as file:
                self.videos_folder = file.read()

        if exists(".\\settings\\folders.txt"):
            with open(".\\settings\\folders.txt", "r") as file:
                self.folder_list = file.read()
        else:
            self.folder_list: list[str] = []
        
        self.debug_mode = False
        self._dir = abspath(f"videos_database\\{self.videos_folder}")
        self.dir = glob.glob(fr"{self._dir}\\*.txt")
        #self.player = vlc.Instance()
        self.startfile_streaming = True if exists(".\\settings\\streaming_preference.txt") is False else False
        self.subprocess_streaming = False
        if exists(".\\settings\\streaming_preference.txt") is True:
            with open(".\\settings\\streaming_preference.txt", "r") as file:
                self._contents = file.read()
                self.startfile_streaming = True if self._contents == "startfile_streaming" else False
                self.subprocess_streaming = True if self._contents == "subprocess_streaming" else False

    def get_videos_from_folder(self):
        console = Console(theme=self.cinnamon_theme)
        if exists(f".\\videos_database\\{self.videos_folder}") is True:

            if self.debug_mode is True:
                console.print("[bold][message]Successfully found videos_folder.txt..[/]")

            try:
                for self.item in self.dir:    
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
                    print(self.dir)

                    for self.item in self.dir:
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
        system("cls")
        console = Console(theme=self.cinnamon_theme)
        console.print("[bold][message]─── Cinnamon ───────────────────────────────────────────────\n  │\n  │ 1. Watch Video\n  │\n  │ 2. List Videos\n  │\n  │ 3. Settings\n  │\n  │ 4. Exit\n  │\n────────────────────────────────────────────────────────────\n  │ Select an option (1-4)\n────────────────────────────────────────────────────────────[/]")
        self.user_input = console.input("[bold][input] -> [/]")
        return self.user_input


    def menu_logic(self):
        console = Console(theme=self.cinnamon_theme)
        system("cls")
        if exists(".\\videos_database") is False:
            self.set_videos_folder()
            self.get_videos_from_folder()
        elif exists(".\\videos_database") is True:
            self.get_videos_from_folder()
        while True:
            self.user_input = self.main_menu()

            if self.user_input in ("1", 1):
                system("cls")
                console.print(f"[bold][message]Folder: {self.videos_folder.title()}\n────────────────────────────────────────────────────────────[/]")
                for self._item in self.videos_list:
                    self._print = True
                    self.item = self._item.split(sep=", ", maxsplit=2)
                    self.filename = split(self.item[0])
                    self._videos.append(self.filename[1][:-1])
                    self._index_number = self.item[1].split(": ", 2)
                    self.index_number = self._index_number[1].replace("}", "")
                    self.index_number = self.index_number.replace("'", "")
                    if int(self.index_number) <= 9:
                        console.print(f"[bold][message]Index ({self.index_number})   │ {self.filename[1][:-1]}[/]") if self._print is True else print("")
                        self._print = False
                    if int(self.index_number) > 9 and int(self.index_number) < 99:
                        console.print(f"[bold][message]Index ({self.index_number})  │ {self.filename[1][:-1]}[/]") if self._print is True else print("")
                        self._print = False
                    if int(self.index_number) > 99 and int(self.index_number) < 999:
                        console.print(f"[bold][message]Index ({self.index_number}) │ {self.filename[1][:-1]}[/]") if self._print is True else print("")
                        self._print = False
                    if int(self.index_number) > 999 and int(self.index_number) < 9999:
                        console.print(f"[bold][message]Index ({self.index_number})│ {self.filename[1][:-1]}[/]") if self._print is True else print("")
                        self._print = False
                        
                self.video_input = console.input("[bold][input]────────────────────────────────────────────────────────────\nWhat video do you want to watch? (Please use the index number) -> [/]")
                try:
                    if int(self.video_input) in self.valid_video_indexs:
                        if self.startfile_streaming is True:
                            startfile(fr".\\{self.videos_folder}\\{self._videos[int(self.video_input) - 1]}")
                        if self.subprocess_streaming is True:
                            self.media_list = self.player.media_list_new()
                            self.media_player = self.player.media_list_player_new()
                            self.media = self.player.media_new_path(fr".\\{self.videos_folder}\\{self._videos[int(self.video_input) - 1]}")
                            self.media_list.add_media(self.media)
                            self.media_player.set_media_list(self.media_list)
                            self.media_player.play()
                except ValueError:
                    console.print("[bold][error]The index number you specified was incorrect..[/]")
                    time.sleep(1)


            if self.user_input in ("2", 2):
                self._ = True
                while self._ is True:
                    system("cls")
                    console.print(f"[bold][message]Folder: {self.videos_folder.title()}\n────────────────────────────────────────────────────────────[/]")
                    for self._item in self.videos_list:
                        self.item = self._item.split(sep=", ", maxsplit=2)
                        self.filename = split(self.item[0])
                        self._videos.append(self.filename[1][:-1])
                        self._index_number = self.item[1].split(": ", 2)
                        self.index_number = self._index_number[1].replace("}", "")
                        self.index_number = self.index_number.replace("'", "")
                        if int(self.index_number) <= 9:
                            console.print(f"[bold][message]Index ({self.index_number})   │ {self.filename[1][:-1]}[/]")
                        if int(self.index_number) > 9:
                            console.print(f"[bold][message]Index ({self.index_number})  │ {self.filename[1][:-1]}[/]")
                        if int(self.index_number) > 99:
                            console.print(f"[bold][message]Index ({self.index_number}) │ {self.filename[1][:-1]}[/]")
                    self.exit_input = console.input("[bold][message]────────────────────────────────────────────────────────────\nDo you want to exit this menu? (Y/N) -> [/]").title()
                    if self.exit_input in ("Y", "Yes"):
                        self._ = False
                        system("cls")
                    if self.exit_input in ("N", "No"):
                        pass
                    if self.exit_input not in ("Y", "Yes", "N", "No"):
                        console.print(f"[bold][error]'{self.exit_input}' is not a valid input..[/]")
                        time.sleep(2)


            if self.user_input in ("3", 3):
                self.settings_loop = True
                while self.settings_loop is True:
                    system("cls")
                    console.print("[bold][message]─── Settings ───────────────────────────────────────────────\n  │\n  │ 1. Change Streaming Type\n  │\n  │ 2. Refresh Database\n  │\n  │ 3. Change Videos Folder\n  │\n  │ 4. Exit to Main Menu\n  │\n────────────────────────────────────────────────────────────\n  │ Select an option (1-4)\n────────────────────────────────────────────────────────────[/]")
                    self.settings_input = console.input("[bold][message] > [/]")

                    if self.settings_input in ("1", 1):
                        self.streaming_menu_loop = True
                        while self.streaming_menu_loop is True:
                            system("cls")
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
                                system("cls")
                                self.set_videos_folder()
                                with open(".\\settings\\dir.txt", "r") as file:
                                    self.videos_folder = file.read()
                                time.sleep(2)

                            if self.streaming_input in ("4", 4):
                                self.streaming_menu_loop = False
                    

                    if self.settings_input in ("2", 2):
                        system("cls")
                        for self._item in self.dir:
                            remove(self._item)
                        rmdir("videos_database")
                        mkdir("videos_database")
                        self.get_videos(self.videos_folder)
                        self.dir = glob.glob(fr"{self._dir}\\*.txt")
                        console.print("[bold][message]────────────────────────────────────────────────────────────\nSuccessfully refreshed database!\n[yellow]NOTE: You may need to reset cinnamon to see the effects.[/]\n────────────────────────────────────────────────────────────[/]")
                        time.sleep(2)

                    if self.settings_input in ("3", 3):
                        system("cls")
                        self.set_videos_folder(folder_list=self.folder_list)
                        time.sleep(1)

                    if self.settings_input in ("4", 4):
                        self.settings_loop = False


            if self.user_input in ("4", 4):
                return False


    def run(self):
        self.menu_logic()


if __name__ == '__main__':
    cinnamon = Cinnamon()
    cinnamon.run()

    