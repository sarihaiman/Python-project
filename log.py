import datetime

def server_log_decorator(log_file):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # קבלת השעה והתאריך הנוכחי
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # נסיון לקרוא לפונקציה
            try:
                result = func(*args, **kwargs)
                success = True
            except Exception as e:
                result = str(e)
                success = False

            # פתיחת קובץ לוג לכתיבה
            with open(log_file, 'a') as f:
                # כתיבת הרשומה לקובץ הלוג
                f.write(f"Function: {func.__name__}, Time: {current_time}, Success: {success}\n")
            return result
        return wrapper
    return decorator






