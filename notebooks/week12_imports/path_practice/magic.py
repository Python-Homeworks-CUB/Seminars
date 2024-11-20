import os

def file_not_found_handler(func):
    def wrapper(path, *args, **kwargs):
        try:
            return func(path, *args, **kwargs)
        except FileNotFoundError as e:
            print("File not found:", e)
            print(f"Path used: {path}")
            print(f"Python looked for file: {os.path.abspath(path)}")
            print(f"Current working directory: {os.getcwd()}")
    return wrapper