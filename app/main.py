import sys


def main():
    
    sys.stdout.write("$ ")
    builtins=["exit", "echo", "type"]
    command=input().strip()
    args = command.split()
    
    match args:
        case ["type", command]:
            if command in builtins:
                print(f"{command} is a shell builtin")
            else:
                print(f"{command}: not found")
        case ["exit", "0"]:
            exit()
        case ["echo", *args]:
            print(*args)
        case _:
            print(f"{command}: command not found")
            
    main()


if __name__ == "__main__":
    main()
