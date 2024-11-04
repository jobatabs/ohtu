from player import PlayerReader, PlayerStats
from rich import print
from rich.prompt import Prompt
from rich.console import Console
from rich.table import Table
import signal, sys

def main(console):
    console.print("[italic grey]NHL statistics by nationality")
    season = Prompt.ask("Select season [bold purple][2022-23/2023-24/2024-25][/bold purple]")
    while True:
        nationality = Prompt.ask("Select nationality [bold purple][FIN/LAT/AUT/CZE][/bold purple]")
        url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
        reader = PlayerReader(url)
        stats = PlayerStats(reader)
        players = stats.top_scorers_by_nationality(nationality)

        table = Table(title=f"Top scorers of {nationality} season {season}")
        table.add_column("name", justify="left", style="cyan")
        table.add_column("team", style="purple")
        table.add_column("goals", justify="right", style="green")
        table.add_column("assists", justify="right", style="green")
        table.add_column("points", justify="right", style="green")

        for p in players:
            table.add_row(p.name, p.team, str(p.goals), str(p.assists), str(p.goals+p.assists))
        
        console.print(table)

def signal_hander(sig, frame):
    console.print("\nExiting")
    sys.exit(0)

if __name__ == "__main__":
    console = Console()
    signal.signal(signal.SIGINT, signal_hander)
    main(console)