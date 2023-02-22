from initialiser import CinnamonInit

CinnamonInit().initialise()

from rich import *
from rich.rule import *
from rich.color import *
from rich.style import *
from rich.theme import *
from rich.traceback import install
from rich.console import Console
import os
import glob
import json
import pathlib

class CinnamonSetup:

    def __init__(self):
        self.videos: dict = {}
        self._videos: list = []
        self.debug_mode: bool = True
        self.video_index: int = 1
        self.cinnamon_theme = Theme({
            "input": "light_goldenrod2",
            "message": "light_goldenrod3",
            "process": "tan",
            "query": "wheat1",
            "error": "bold red"
        })

    def set_videos_folder(self):
        console = Console(theme=self.cinnamon_theme)
        os.system("cls")
        console.print("[bold][message]── Cinnamon Setup ───────────────────────────────────────────────[/]", width=65)
        self._folder = console.input("[bold][input]\nWhat is the directory that you want to search? -> [/]")
        self.get_videos(self._folder)

    def get_videos(self, videos_folder):
        console = Console(theme=self.cinnamon_theme)
        if os.path.exists(videos_folder) is True:
            for self.items in glob.glob(fr"./{videos_folder}/*.mp4"):
                if self.debug_mode is True:
                    console.print(f"[bold][process]Adding [/][query]'{self.items[(len(videos_folder)+3):]}'[/][process] to the list..[/]")
                self._videos.append(f"{self.items}")
                with open(fr".\\videos_database\\{self.items[(len(videos_folder)+3):-4]}.txt", "w") as file:
                    self.videos.update({"path": f"{os.path.abspath(f'{videos_folder}//'+(self.items[len(videos_folder)+3:]))}"}) #Do not touch!! Black magic here
                    self.videos.update({"index": f"{self.video_index}"})
                    self.video_index += 1
                    file.write(f"{self.videos}")
                with open(fr".\\settings\\dir.txt", "w") as file:
                    file.write(videos_folder)
            if len(self.videos) == 0:
                console.print(f"\n[error]'{videos_folder}' didn't contain any video files..\n[/][bold][query]Are you sure this was the correct directory?[/]")
            return self.videos, videos_folder
        elif os.path.exists(videos_folder) is False:
            console.print("[error]{videos_folder} either doesn't exist on this pc or isn't in the current directory..[/]")
            return Exception

if __name__ == '__main__':
    CinnamonSetup().set_videos_folder()
    