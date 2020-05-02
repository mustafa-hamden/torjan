import os


def run(**arg):
    print("dir list moduler")
    files = os.listdir(".")
    return str(files)
