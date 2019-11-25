import fnmatch
import sys

commands = [
    "build",
    "run",
    "exit",
]

def build():
    print("Building...")

def run():
    print("Running...")

def exit():
    sys.exit()

def complete(cmd):
        options = fnmatch.filter(commands, cmd + "*")
        
        if len(options) == 0:
            print("No command found, please try again")
        elif len(options) == 1:
            globals()[options[0]]()
        else:
            print(options)

def main2():
    while True:
        cmd = input()
        compelte(cmd)

def main():
    while True:
        buf = sys.stdin.buffer.read(1)
        if buf == r"\t":
            complete(buf)
        print(buf)

if __name__ == "__main__":
    main()