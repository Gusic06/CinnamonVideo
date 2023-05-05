from _initialiser import CinnamonInit

if __name__ == "__main__":
    CinnamonInit().initialise()

from rich import *
from rich.rule import *
from rich.color import *
from rich.style import *
from rich.theme import *
from rich.traceback import install
from rich.console import Console

from os import system, listdir
from os.path import exists, abspath, isdir
from glob import glob

class CinnamonSetup:

    def __init__(self):
        self.videos: dict = {}
        self._videos: list = []
        self.debug_mode: bool = True
        self.video_index: int = 1
        self.folder_list: list[str] = []
        self.cinnamon_theme = Theme({
            "input": "light_goldenrod2",
            "message": "light_goldenrod3",
            "process": "tan",
            "query": "wheat1",
            "error": "bold red"
        })

    def set_videos_folder(self, folder_list: Optional[list[str]] = [], debug: Optional[bool] = True):
        console = Console(theme=self.cinnamon_theme)
        system("cls")
        console.print("[bold][message]── Cinnamon Setup ───────────────────────────────────────────────[/]", width=65)
        console.print("[bold][tan]\n── Available Folders ────────────────────────────────[/]")
        for self.folders in listdir():
            if self.folders in ("__pycache__", "settings", "videos_database") or isdir(self.folders) is False:
                pass
            if self.folders not in ("__pycache__", "settings", "videos_database") and isdir(self.folders):
                console.print(f"[bold][process]{self.folders}[/]")
        console.print("[bold][tan]─────────────────────────────────────────────────────[/]")
        self._folder = console.input("[bold][input]\nWhat is the directory that you want to search? -> [/]")
        console.print("[bold][message]─────────────────────────────────────────────────────────────────[/]")
        self.get_videos(videos_folder=self._folder, folder_list=folder_list, debug=debug)

    def get_videos(self, videos_folder, folder_list: Optional[list[str]] = [], debug: Optional[bool] = True):
        self.debug_mode = debug
        self.video_index = 1
        console = Console(theme=self.cinnamon_theme)
        if videos_folder in folder_list:
            return videos_folder
        if exists(videos_folder) is True:
            if exists(f".\\videos_database\\{videos_folder}") is False:
                system(f"cd videos_database && mkdir {videos_folder}")
                system("cd ..")
                self.folder_list.append(videos_folder)
                with open(".\\settings\\folders.txt", "w") as file:
                    file.write(f"{self.folder_list}")
            for self.items in glob(fr"./{videos_folder}/*.mp4"):
                if self.debug_mode is True:
                    console.print(f"[bold][process]Adding [/][query]'{self.items[(len(videos_folder)+3):]}'[/][process] to the list..[/]")
                self._videos.append(f"{self.items}")
                with open(fr".\\videos_database\\{videos_folder}\\{self.items[(len(videos_folder)+3):-4]}.txt", "w") as file:
                    self.videos.update({"path": f"{abspath(f'{videos_folder}//'+(self.items[len(videos_folder)+3:]))}"}) #Do not touch!! Black magic here
                    self.videos.update({"index": f"{self.video_index}"})
                    self.video_index += 1
                    try:
                        file.write(f"{self.videos}")
                    except UnicodeEncodeError:
                        file.write(str(f"{self.videos}".encode('utf-8')))
                with open(fr".\\settings\\dir.txt", "w") as file:
                    file.write(videos_folder)
            if len(self.videos) == 0:
                console.print(f"\n[error]'{videos_folder}' didn't contain any video files..\n[/][bold][query]Are you sure this was the correct directory?[/]")
            #return videos_folder
        elif exists(videos_folder) is False:
            console.print(f"[error]'{videos_folder}' either doesn't exist on this pc or isn't in the current directory..[/]")
            return Exception

if __name__ == '__main__':
    CinnamonSetup().set_videos_folder()
    