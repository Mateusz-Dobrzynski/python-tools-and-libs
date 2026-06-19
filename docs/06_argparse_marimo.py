# /// script
# dependencies = ["marimo"]
# requires-python = ">=3.13"
# ///

import marimo

__generated_with = "0.23.10"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Creating CLI tools with `argparse`
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

    import marimo as mo
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

    def run_bash_command(command: str):
        print(f"$ {command}")
        return subprocess.run(command, shell=True)

    return mo, preview_file, run_bash_command, write_demo_file


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## `argv`
    """)
    return


@app.cell(hide_code=True)
def _(write_demo_file):
    write_demo_file(
        "argv.py",
        """
        from sys import argv

        print(argv)
        """,
    )
    return


@app.cell(hide_code=True)
def _(mo, preview_file):
    mo.md(preview_file("argv.py"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    >Source - https://stackoverflow.com/a/48522115. Posted by James. Retrieved 2026-06-18, License - CC BY-SA 3.0
    """)
    return


@app.cell(hide_code=True)
def _(run_bash_command):
    run_bash_command("uv run argv.py 1 2 3")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Further readings
    [sys — System-specific parameters and functions](https://docs.python.org/3/library/sys.html#sys.argv)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## `stdin`, `stdout`, and `stderr`

    >**Send output to `stdout`.** The primary output for your command should go to `stdout`. Anything that is machine readable should also go to `stdout`—this is where piping sends things by default.
    >
    >**Send messaging to `stderr`**. Log messages, errors, and so on should all be sent to `stderr`. This means that when commands are piped together, these messages are displayed to the user and not fed into the next command.
    >
    >~[Command Line Interface Guidelines](https://clig.dev/#the-basics)
    """)
    return


@app.cell(hide_code=True)
def _(write_demo_file):
    write_demo_file(
        "output.py",
        """
        from sys import stdout, stderr

        stdout.write("This is output without newline")
        print("This is output with newline")
        stderr.write("This is a message or error")
        """,
    )
    return


@app.cell(hide_code=True)
def _(mo, preview_file):
    mo.md(preview_file("output.py"))
    return


@app.cell
def _(run_bash_command):
    run_bash_command("uv run output.py")
    return


@app.cell
def _(run_bash_command):
    run_bash_command("uv run output.py 1>/dev/null")
    return


@app.cell
def _(run_bash_command):
    run_bash_command("uv run output.py 2>/dev/null")
    return


@app.cell
def _(run_bash_command):
    run_bash_command("uv run output.py 1>/dev/null 2>/dev/null")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Arguments
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Positional arguments
    """)
    return


@app.cell(hide_code=True)
def _(write_demo_file):
    write_demo_file(
        "positional_arguments_demo.py",
        """
        import argparse

        parser = argparse.ArgumentParser()
        parser.add_argument("arg1")
        parser.add_argument("arg2")
        parser.add_argument("arg3")

        args = parser.parse_args()
        print(vars(args))
        """,
    )
    return


@app.cell(hide_code=True)
def _(mo, preview_file):
    mo.md(preview_file("positional_arguments_demo.py"))
    return


@app.cell
def _(run_bash_command):
    run_bash_command("uv run positional_arguments_demo.py a b c")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Flags
    """)
    return


@app.cell(hide_code=True)
def _(write_demo_file):
    write_demo_file(
        "flags_demo.py",
        """
        from sys import stderr
        import argparse

        parser = argparse.ArgumentParser()
        parser.add_argument("--verbose", "-v", action="store_true")

        args = parser.parse_args()

        if args.verbose:
            stderr.write(f"verbose type: {type(args.verbose)}\\nverbose: {args.verbose}")
        """,
    )
    return


@app.cell(hide_code=True)
def _(mo, preview_file):
    mo.md(preview_file("flags_demo.py"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `action="store_true"` turns `--verbose` into a flag: a sort of switch.
    """)
    return


@app.cell
def _(run_bash_command):
    run_bash_command("uv run flags_demo.py")
    return


@app.cell
def _(run_bash_command):
    run_bash_command("uv run flags_demo.py --verbose")
    return


@app.cell
def _(run_bash_command):
    run_bash_command("uv run flags_demo.py -v")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Optional arguments
    """)
    return


@app.cell(hide_code=True)
def _(write_demo_file):
    write_demo_file(
        "demo_greeting.py",
        """
        import argparse

        parser = argparse.ArgumentParser()
        parser.add_argument("--lang")

        args = parser.parse_args()
        match args.lang:
            case "cr":
                print("Pozdrav svijete!")
            case "cz":
                print("Ahoj světe!")
            case "de":
                print("Hallo Welt!")
            case "pl":
                print("Witaj Świecie!")
            case _:
                print("Hello World!")
        """,
    )
    return


@app.cell(hide_code=True)
def _(mo, preview_file):
    mo.md(preview_file("demo_greeting.py"))
    return


@app.cell
def _(run_bash_command):
    run_bash_command("uv run demo_greeting.py")
    return


@app.cell
def _(run_bash_command):
    run_bash_command("uv run demo_greeting.py --lang pl")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Return codes
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    >**Return zero exit code on success, non-zero on failure.** Exit codes are how scripts determine whether a program succeeded or failed, so you should report this correctly. Map the non-zero exit codes to the most important failure modes.
    >
    >~[Command Line Interface Guidelines](https://clig.dev/#the-basics)
    """)
    return


@app.cell(hide_code=True)
def _(write_demo_file):
    write_demo_file(
        "exit_codes_demo.py",
        """
        from sys import stderr
        from argparse import ArgumentParser

        parser = ArgumentParser()
        parser.add_argument("number")
        args = parser.parse_args()
        number = args.number

        try:
            for _ in range(int(number)):
                print("Hello World!")
            exit(0)
        except Exception:
            stderr.write(f"Failed to parse {number} as a number")
            exit(1)
        """,
    )
    return


@app.cell(hide_code=True)
def _(mo, preview_file):
    mo.md(preview_file("exit_codes_demo.py"))
    return


@app.cell
def _(run_bash_command):
    run_bash_command("uv run exit_codes_demo.py 3")
    return


@app.cell
def _(run_bash_command):
    run_bash_command("uv run exit_codes_demo.py a_word")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Usage in scripts
    """)
    return


@app.cell
def _(run_bash_command):
    run_bash_command('uv run exit_codes_demo.py 3 && echo "Success"')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `&&` chains commands if they are successful
    """)
    return


@app.cell
def _(run_bash_command):
    run_bash_command('uv run exit_codes_demo.py a_word && echo "Success"')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Processing files from input

    https://docs.python.org/3/library/fileinput.html#module-fileinput
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## `argparse` in practice 🎯

    **TO-DO:** create a CLI utility to **calculate the number of days between two given dates**. If only one date is given, it should compare the argument with the current date.

    Example:
    ```bash
    $ uv run -m day_diff 2026.06.01 2026.06.12
    11

    # Assume today is 2026-06-12
    $ uv run -m day_diff 2026.06.13
    1

    $ uv run -m day_diff --verbose 2026.06.01 2026.06.12
    11 day(s)
    ```

    - Let the user choose a date format by selecting one of the options (e.g. `-dmy` for `dd.mm.yyyy` and `-ymd` for `yyyy-mm-dd`)
    - Report exit codes properly
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Further readings

    - [`argparse` tutorial](https://docs.python.org/3/howto/argparse.html)
    - [`argparse` reference](https://docs.python.org/3/library/argparse.html)
    - [Command Line Interface Guidelines](https://clig.dev/)
    """)
    return


if __name__ == "__main__":
    app.run()
