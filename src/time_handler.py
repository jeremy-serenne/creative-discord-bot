from datetime import datetime
import pytz

def get_current_time(current_timezone: str) -> str:
  return (datetime.now(pytz.timezone(current_timezone)).strftime("%H:%M:%S"))
