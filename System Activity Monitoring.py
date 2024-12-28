import win32evtlog  # برای دسترسی به رویدادهای سیستم
import win32con

def read_system_logs():
    server = 'localhost'  # برای کامپیوتر محلی
    log_type = 'System'   # نوع لاگ‌ها (Application, System, Security)

    try:
        # باز کردن لاگ
        hand = win32evtlog.OpenEventLog(server, log_type)
        
        # خواندن رویدادها
        events = win32evtlog.ReadEventLog(hand, win32con.EVENTLOG_SEQUENTIAL_READ | win32con.EVENTLOG_FORWARDS_READ, 0)

        if events:
            for event in events:
                print(f"Event ID: {event.EventID}")
                print(f"Time Generated: {event.TimeGenerated}")
                print(f"Source Name: {event.SourceName}")
                print(f"Message: {event.StringInserts}")
                print('-' * 50)
        else:
            print("No events found.")
        
    except Exception as e:
        print(f"Error while reading event logs: {e}")

if __name__ == "__main__":
    read_system_logs()
