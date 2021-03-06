"""
Read file using while and for. Also play with formatted strings.
"""
def read_for(fd, limit):
    """
    Read file with forloop
    """
    for count, line in enumerate(fd):
        if count >= limit:
            break
        print(line.strip())

def read_while(fd, limit):
    """
    Read file with while loop
    """
    count = 0
    while count < limit:
        line = fd.readline().strip()
        if not line:
            break
        print(line)
        count += 1
        # argument = input("What to inject: ")
        # print(line.format(argument))

def count_file(fd):
    """
    Count number of characters in file
    """
    characters = fd.read()
    print(len(characters))
    print(characters.count("\n"))

def read_file():
    """
    Starting point of program.
    """
    choice = input("1. Read characters and newlines - 2. print x number of rows")

    try:
        with open("data.txt", "r") as myfile:
            if choice == "1":
                count_file(myfile)
            elif choice == "2":
                limit = int(input("How many lines? "))
                # read_while(myfile, limit)
                read_for(myfile, limit)
            else:
                print("Make real choice")
    except IOError:
        print("Kan inte öppna fil, finnds den?")
read_file()
