try:
    from rich import *
    from rich.console import *
    from rich.traceback import *
    from os import mkdir, system
except ModuleNotFoundError:
    from os import mkdir, system
    system("py -m pip install rich")
    from rich import *
    from rich.console import *
    from rich.traceback import *
from time import sleep
import sys
from os import mkdir, system
from os.path import exists
import subprocess
from typing import Optional
import platform

class CinnamonInit:

    def __init__(self):
        install()

    def initialise(self):

        console = Console()

        console.print(f"[dim]OS: {os.name}\nCPU Architecture: {platform.machine()}\n[/]")

        if exists("settings") is False:
            console.print("[bold white][ [yellow]WARN[/] ][/] -> Settings Folder")
            sleep(0.05)
            try:
                mkdir("settings")
                console.print("[bold white][ [green]OK[/] ][/] -> Settings Folder")
                sleep(0.05)
            except Exception as Err:
                console.print(f"[bold white][ [red]FATAL_ERR[/] ][/] -> Settings Folder -> Error Received ({Err})")
                sleep(1)
                sys.exit()
        else:
            console.print("[bold white][ [green]OK[/] ][/] -> Settings Folder")
            sleep(0.05)

        if exists("videos_database") is False:
            console.print("[bold white][ [yellow]WARN[/] ][/] -> Videos Database Folder")
            sleep(0.05)
            try:
                mkdir("videos_database")
                console.print("[bold white][ [green]OK[/] ][/] -> Videos Database Folder")
                sleep(0.05)
            except Exception as Err:
                console.print(f"[bold white][ [red]FATAL_ERR[/] ][/] -> Videos Database Folder -> Error Received ({Err})")
                sleep(1)
                sys.exit()
        else:
            console.print("[bold white][ [green]OK[/] ][/] -> Settings Folder")
            sleep(0.05)

        console.print("[bold white][ [green]OK[/] ][/] -> Rich")
        sleep(0.05)   

        console.print("\n[bold white]Launching [light_goldenrod3]Cinnamon[/] Now![/]")


if __name__ == '__main__':
    CinnamonInit().initialise()