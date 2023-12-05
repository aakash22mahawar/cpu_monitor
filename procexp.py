import time
import psutil
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def colorize(value, bars, color_code):
    reset_code = "\033[0m"   # ANSI escape code to reset color

    percent = value / 100.0
    colored_bar = '█' * int(percent * bars)
    remaining_bar = '-' * int((1 - percent) * bars)

    return f"{color_code}|{colored_bar}{remaining_bar}| {value:.2f}%{reset_code}"

def cpu_monitor(cpu_usage, mem_usage, bars=30):
    clear_console()

    cpu_output = colorize(cpu_usage, bars, "\033[92m")  # Green color
    mem_output = colorize(mem_usage, bars, "\033[93m")  # Yellow color

    print(f"CPU Usage: {cpu_output}")
    print(f"MEM Usage: {mem_output}")

if __name__ == "__main__":
    while True:
        cpu_monitor(psutil.cpu_percent(), psutil.virtual_memory().percent)
        time.sleep(0.5)
