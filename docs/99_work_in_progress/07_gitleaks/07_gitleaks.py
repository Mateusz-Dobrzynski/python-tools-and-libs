# /// script
# dependencies = ["marimo"]
# requires-python = ">=3.13"
# ///

import marimo

__generated_with = "0.23.10"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Detecting secrets with `gitleaks`
    """)
    return


@app.cell
def _():
    # Set to True to recreate demo files
    write_demo_files = False
    return (write_demo_files,)


@app.cell(hide_code=True)
def _(write_demo_files):
    import subprocess

    from pathlib import Path
    from textwrap import dedent

    def write_demo_file(path: str, content: str) -> Path:
        demo_path = Path(path)
        if not write_demo_files:
            return demo_path
        demo_path.write_text(dedent(content).lstrip("\n"))
        return demo_path

    def preview_file(path: str) -> str:
        demo_path = Path(path)
        return f"{demo_path.name}\n```py\n{demo_path.read_text()}\n```"

    def run_bash_commands(commands: str):
        return [run_bash_command(command.strip()) for command in commands.splitlines() if command.strip()]

    def run_bash_command(command: str):
        print(f"$ {command}")
        return subprocess.run(command, shell=True)

    return (run_bash_command,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Fragment of https://github.com/debatecore/tau/blob/9cf455c8b0c847a2ef7d7f5c2483dfe402569fa2/scripts/set_up_server.py:
    """)
    return


@app.cell(hide_code=True)
def _():
    """
    set_up_server.py
    ================
    Full setup + verification script for the Granda Debate Tournament Planner.
    Endpoints verified against /openapi.json
 
    Valid roles (from API spec Role enum): Organizer, Judge, Marshal
 
    Usage:
      pip install requests
      python scripts/set_up_server.py
    """
 
    import requests
    import secrets
    import string
    import json
    import sys
 
    # ─────────────────────────────────────────────
    #  CONFIG
    # ─────────────────────────────────────────────
 
    BASE_URL   = "https://granda-backend.debateco.re"              # switch to https://granda-backend.debateco.re for prod
    ADMIN_USER = "admin"
    ADMIN_PASS = "even&headless&fastball&wager&reprise&unblessed&scorebook"                              # local default; prod uses the long passphrase
 
    ORGANIZATIONS = ["DebateLab", "ZSK", "Buster"]
 
    # Valid roles per API spec: Organizer | Judge | Marshal
    # "Tabmaster" does NOT exist in the API — replaced with "Organizer"
    ROLES         = ["Organizer", "Judge", "Marshal"]
    TOURNAMENTS_N = 3
 
    # ─────────────────────────────────────────────
    #  CONSOLE COLOURS
    # ─────────────────────────────────────────────
 
    BOLD   = "\033[1m"
    GREEN  = "\033[92m"
    RED    = "\033[91m"
    CYAN   = "\033[96m"
    YELLOW = "\033[93m"
    RESET  = "\033[0m"
 
    def ok(msg):   print(f"  {GREEN}✓{RESET} {msg}")
    def err(msg):  print(f"  {RED}✗{RESET} {msg}")
    def warn(msg): print(f"  {YELLOW}!{RESET} {msg}")
    def hdr(msg):  print(f"\n{BOLD}{CYAN}{'─'*55}\n  {msg}\n{'─'*55}{RESET}")
 
    def base_url(path: str) -> str:
        return BASE_URL.rstrip("/") + path
 
    def generate_password(length: int = 20) -> str:
        alphabet = string.ascii_letters + string.digits + "!@#$%^&*-_"
        pwd = [
            secrets.choice(string.ascii_uppercase),
            secrets.choice(string.ascii_lowercase),
            secrets.choice(string.digits),
            secrets.choice("!@#$%^&*-_"),
        ]
        pwd += [secrets.choice(alphabet) for _ in range(length - 4)]
        secrets.SystemRandom().shuffle(pwd)
        return "".join(pwd)
 
    # ─────────────────────────────────────────────
    #  STEP 0 — Connectivity
    # ─────────────────────────────────────────────
 
    def check_connectivity():
        hdr("STEP 0 — Connectivity check")
        try:
            r = requests.get(BASE_URL, timeout=8)
            ok(f"Backend reachable at {BASE_URL}  (HTTP {r.status_code})")
        except requests.exceptions.ConnectionError:
            err(f"Cannot reach {BASE_URL}")
            print("     → Is the server running? Try: cargo run")
            sys.exit(1)
 
    # ─────────────────────────────────────────────
    #  STEP 1 — Login
    #  POST /auth/login
    #  Body: {"login": "...", "password": "..."}
    #  Response: text/plain raw token string
    # ─────────────────────────────────────────────
 
    def login() -> dict:
        hdr("STEP 1 — Admin login")
        r = requests.post(
            base_url("/auth/login"),
            json={"login": ADMIN_USER, "password": ADMIN_PASS},
        )
        if r.status_code not in (200, 201):
            err(f"Login failed  HTTP {r.status_code}: {r.text[:200]}")
            sys.exit(1)
 
        token = r.text.strip()
        if not token:
            err("Login returned an empty token.")
            sys.exit(1)
 
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type":  "application/json",
        }
        ok(f"Logged in as '{ADMIN_USER}'  token: {token[:24]}…")
        return headers

    # ─────────────────────────────────────────────
    #  MAIN
    # ─────────────────────────────────────────────
 
    def main():
        print(f"\n{BOLD}{'═'*55}")
        print(f"  Granda Tournament Setup Script")
        print(f"  Target: {BASE_URL}")
        print(f"{'═'*55}{RESET}")
 
        check_connectivity()
        headers         = login() 
        print(f"\n{GREEN}{BOLD}All done.{RESET}\n")
 
 
    if __name__ == "__main__":
        main()
 
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## gitleaks installation
    """)
    return


@app.cell
def _(run_bash_command):
    variant = "docker"

    def install_gitleaks():
        if variant == "docker":
            run_bash_command("docker pull ghcr.io/gitleaks/gitleaks:latest")
        elif variant == "apt":
            run_bash_command("sudo apt install gitleaks")
            

    install_gitleaks()

    return (variant,)


@app.cell
def _(run_bash_command, variant):
    def run_gitleaks(arguments: str):
        if variant == "docker":
            run_bash_command(f"docker run -v .:/path ghcr.io/gitleaks/gitleaks:latest {arguments}")
        else:
            run_bash_command(f"gitleaks {arguments}")



    return


if __name__ == "__main__":
    app.run()
