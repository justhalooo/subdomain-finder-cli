import requests
import socket
from rich.console import Console
from rich.table import Table
from rich.progress import Progress

console = Console()

def find_subdomains(domain):
    console.print(f"[bold cyan][+] Searching subdomains for:[/bold cyan] {domain}")
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            console.print(f"[bold red][-] crt.sh returned status code {response.status_code}[/bold red]")
            return []

        entries = response.json()
        subdomains = set()
        for entry in entries:
            name_value = entry.get('name_value', '')
            for subdomain in name_value.splitlines():
                if subdomain.endswith(domain):
                    subdomains.add(subdomain.strip())
        
        return sorted(subdomains)

    except Exception as e:
        console.print(f"[bold red][-] Error: {e}[/bold red]")
        return []

def check_dns_resolution(subdomains):
    active_subdomains = []
    with Progress() as progress:
        task = progress.add_task("[cyan]Checking DNS resolution...", total=len(subdomains))
        for sub in subdomains:
            try:
                ip = socket.gethostbyname(sub)
                active_subdomains.append((sub, ip))
            except socket.gaierror:
                pass
            progress.update(task, advance=1)
    return active_subdomains

def main():
    console.print("[bold green]Subdomain Finder CLI[/bold green]")
    domain = console.input("[bold yellow]Input domain finder: [/bold yellow]").strip()
    resolve = console.input("[bold yellow]Check DNS resolution? (y/n): [/bold yellow]").lower().strip() == 'y'

    subs = find_subdomains(domain)
    if subs:
        console.print(f"[bold green][+] Found {len(subs)} subdomains.[/bold green]")
        active_subs = []
        if resolve:
            active_subs = check_dns_resolution(subs)
            console.print(f"[bold green][+] {len(active_subs)} active subdomains resolved.[/bold green]")

            table = Table(title="Active Subdomains")
            table.add_column("Subdomain", style="cyan")
            table.add_column("IP Address", style="magenta")
            for sub, ip in active_subs:
                table.add_row(sub, ip)
            console.print(table)
        else:
            table = Table(title="Subdomains Found")
            table.add_column("Subdomain", style="cyan")
            for s in subs:
                table.add_row(s)
            console.print(table)
    else:
        console.print("[bold red][-] No subdomains found.[/bold red]")

if __name__ == "__main__":
    main()
