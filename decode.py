import sys

def decode(message_file):
    f = open(message_file)
    message = ""
    count = 1
    sets = 2
    lines = f.readlines()
    lines.sort(key=lambda x: int(x.split(" ")[0]))
    for x in range(len(lines)):
        if (x+1 == count):
            message += lines[x].split(" ")[1].strip("\n") + " "
            count = count + sets
            sets = sets + 1

    return message.strip()

if len(sys.argv) < 2:
    sys.exit()
message = decode(sys.argv[1])
print(message)