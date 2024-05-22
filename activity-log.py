import os
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

def log_activity():
    current_date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    script_dir = os.path.dirname(os.path.abspath(__file__))
    log_file_path = os.path.join(script_dir, "logs", f"activity_log_{current_date}.txt")
    with open(log_file_path, "a") as log_file:
        rounded_time = round_time().isoformat()
        log_file.write(f"{rounded_time} - Active\n")

if __name__ == "__main__":
    log_activity()
