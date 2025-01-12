import sys


def main():
    # Uncomment this block to pass the first stage
    sys.stdout.write("$ ")
    while True:
        command=input()
        print(f"{command}: command not found\n")
        main()


if __name__ == "__main__":
    main()
