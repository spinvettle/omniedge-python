from getpass import getpass
from typing import NewType


ToolName = NewType("ToolName", str)

# Simple ANSI color helpers (no extra dependencies)
RESET = "\033[0m"
BOLD = "\033[1m"
FG_GREEN = "\033[32m"
FG_RED = "\033[31m"
FG_YELLOW = "\033[33m"
FG_CYAN = "\033[36m"


def _style(text: str, *codes: str) -> str:
    return "".join(codes) + text + RESET


def info(message: str) -> None:
    print(_style(message, FG_CYAN))


def success(message: str) -> None:
    print(_style(message, FG_GREEN))


def warning(message: str) -> None:
    print(_style(message, FG_YELLOW))


def error(message: str) -> None:
    print(_style(message, FG_RED))


def header(message: str) -> None:
    print(_style(message, BOLD, FG_CYAN))


def prompt_text(message: str, *, color: str = FG_YELLOW) -> str:
    return input(_style(message, color)).strip()


def prompt_secret(message: str, *, color: str = FG_YELLOW) -> str:
    return getpass(_style(message, color)).strip()


if __name__ == "__main__":
    header("omniedge terminal style demo")
    info("This is an info message.")
    success("This is a success message.")
    warning("This is a warning message.")
    error("This is an error message.")
    name = prompt_text("Enter your name: ")
    secret = prompt_secret("Enter a secret (hidden): ")
    success(f"Hello, {name}! Your secret length is {len(secret)}.")
