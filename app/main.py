import sys


def main():
    
    sys.stdout.write("$ ")
    command=input()
    if command == "exit 0":
        exit()
    else if command=="echo":
        print(f"{command}")
    main()


if __name__ == "__main__":
    main()
