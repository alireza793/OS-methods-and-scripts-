import sys
import os

def list_dir(path):
    """List all files/folders in the given path"""
    try:
        items = os.listdir(path)
    except FileNotFoundError:
        print(f"Path not found: {path}")
        return
    except PermissionError:
        print(f"Permission denied for path: {path}")
        return

    print(f"Contents of: {path}")
    print(items)
    for name in items:
        full = os.path.join(path, name)
        print(full)
        if os.path.isdir(full):
            print(f"[DIR]  {name}")
        else:
            print(f"       {name}")

if __name__ == "__main__":
    # If no path argument is given, use the current working directory
    if len(sys.argv) > 1:
        target = sys.argv[1]
    else:
        target = os.getcwd()

    list_dir(target)
