from datetime import datetime

def now_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
