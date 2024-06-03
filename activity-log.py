import os
import subprocess
from datetime import datetime, timedelta, timezone

def round_time(dt=None, round_to=300):
    """Round a datetime object to any time laps in seconds
    dt : datetime.datetime object, default now.
    round_to : Closest number of seconds to round to, default 5 minutes.
    """
    if dt is None:
        dt = datetime.now(timezone.utc)
    seconds = (dt - dt.replace(hour=0, minute=0, second=0, microsecond=0)).seconds
    rounding = (seconds + round_to / 2) // round_to * round_to
    return dt + timedelta(0, rounding - seconds, -dt.microsecond)

def get_idle_time():
    """Get the system idle time in seconds."""
    try:
        idle_time = subprocess.check_output(
            "ioreg -c IOHIDSystem | awk '/HIDIdleTime/ {print $NF/1000000000; exit}'",
            shell=True
        )
        return float(idle_time.strip())
    except subprocess.CalledProcessError as e:
        print(f"Error checking idle time: {e}")
        return None

def format_idle_time(seconds):
    """Format idle time into minutes and seconds."""
    minutes, seconds = divmod(seconds, 60)
    formatted_time = f"{int(minutes)} minute{'s' if minutes != 1 else ''} {int(seconds)} second{'s' if seconds != 1 else ''}"
    return formatted_time

def log_activity():
    idle_time = get_idle_time()
    current_date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    if idle_time is not None and idle_time < 300:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        log_file_path = os.path.join(script_dir, "logs", f"activity_log_{current_date}.txt")
        with open(log_file_path, "a") as log_file:
            rounded_time = round_time().isoformat()
            log_file.write(f"{rounded_time} - Active\n")
            print(f"Logged activity at {rounded_time}")
        return
    meta_log_file = os.path.join(script_dir, f"meta_log_{current_date}.txt")
    with open(log_file_path, "a") as log_file:
            rounded_time = round_time().isoformat()
            formatted_idle_time = format_idle_time(idle_time)
            log_file.write(f"Idle time was {formatted_idle_time} - User is inactive\n")
            
        

if __name__ == "__main__":
    log_activity()
