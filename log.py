
# def log(original_func):
#     def wrapper(*args, **kwargs):
#         print(f'Running function {original_func.__name__} with args {args} and kwargs {kwargs}')  # print func name and its params
#         original_func(*args, **kwargs)  # original function execution
#         print(f'{original_func.__name__} is Done')  # printing that function is done
#
#     return wrapper  # return edited function that logs

# def log(original_func):
#     def wrapper(*args):
#         print(f'Running function {original_func.__name__} with args {args}')
#         original_func(*args)
#         print(f'{original_func.__name__} is Done')
#     return wrapper

import logging

def get_logger(log_file_name, log_sub_dir=""):
    """ Creates a Log File and returns Logger object """

    # Build Log File Full Path
    logPath = log_file_name if os.path.exists(log_file_name) else os.path.join(log_dir, (str(log_file_name) + '.log'))

    # Create logger object and set the format for logging and other attributes
    logger = logging.Logger(log_file_name)

    # Return logger object
    return logger



