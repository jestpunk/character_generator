import sys, os

path = os.path.abspath(__file__)
paths = path.split("\\")
new_path = "\\"
size = len(paths)
new_path = new_path.join(paths[: size - 2 :])
sys.path.append(new_path)
