import sys


def main():
    
    sys.stdout.write("$ ")
    command=input()
    match command.split():
        case ["exit","0"]:
            exit()
        case ["echo", *args]:
            print(*args)
        case _:
            print(f"{command}: command not found")
            
    main()


if __name__ == "__main__":
    main()
