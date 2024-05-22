import os
from datetime import datetime, timedelta, timezone
import glob

def read_log_file(file_path):
    """Read log file and calculate total active time in minutes."""
    total_minutes = 0
    with open(file_path, 'r') as log_file:
        for line in log_file:
            if 'Active' in line:
                total_minutes += 5
    return total_minutes

def write_summary_file(date, total_minutes):
    """Write summary file with total active time for a given date."""
    summary_file_path = os.path.join(script_dir, "summaries/daily", f"summary_file_{date}.txt")
    hours, minutes = divmod(total_minutes, 60)
    with open(summary_file_path, 'w') as summary_file:
        summary_file.write(f"Total active time for {date}: {hours} hours and {minutes} minutes\n")

def generate_summaries():
    log_files = sorted(glob.glob(os.path.join(script_dir, "logs", "activity_log_*.txt")))
    today = datetime.now(timezone.utc).date()
    for log_file in log_files:
        date_str = os.path.basename(log_file).replace("activity_log_", "").replace(".txt", "")
        log_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        summary_file_path = os.path.join(script_dir, "summaries/daily", f"summary_file_{date_str}.txt")
        
        if log_date < today and not os.path.exists(summary_file_path):
            total_minutes = read_log_file(log_file)
            write_summary_file(date_str, total_minutes)

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    generate_summaries()
