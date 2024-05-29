import datetime


def server_log_decorator(log_file):
    def decorator(func):
        def wrapper(*args, **kwargs):
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            try:
                result = func(*args, **kwargs)

            except Exception as e:
                result = str(e)

            with open(log_file, 'a') as f:
                f.write(f"Function: {func.__name__}, Time: {current_time}\n")
            return result

        return wrapper

    return decorator
