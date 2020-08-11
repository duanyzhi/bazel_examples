import os


f = open("data/end.txt", "r")
print(f.read())

cwd = os.path.dirname(os.path.abspath(__file__))
print(cwd)
