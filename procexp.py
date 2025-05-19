import time
import psutil
import os
import sys

def clear_console():
    # Only clear console if we're running interactively
    if sys.stdout.isatty():
        os.system('cls' if os.name == 'nt' else 'clear')

def colorize(value, bars, color_code):
    reset_code = "\033[0m"
    percent = value / 100.0
    colored_bar = '█' * int(percent * bars)
    remaining_bar = '-' * int((1 - percent) * bars)
    return f"{color_code}|{colored_bar}{remaining_bar}| {value:.2f}%{reset_code}"

def cpu_monitor(cpu_usage, mem_usage, bars=30):
    clear_console()
    cpu_output = colorize(cpu_usage, bars, "\033[92m")
    mem_output = colorize(mem_usage, bars, "\033[93m")
    print(f"CPU Usage: {cpu_output}")
    print(f"MEM Usage: {mem_output}")

if __name__ == "__main__":
    for _ in range(3):  # Only run 3 times for CI visibility
        cpu_monitor(psutil.cpu_percent(), psutil.virtual_memory().percent)
        time.sleep(0.5)
