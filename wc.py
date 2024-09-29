import sys


def wc(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        linecount = len(lines)
        wordcount = sum(len(line.split()) for line in lines)
        charcount = sum(len(line) for line in lines)
        output = "lines:{0}\nwords:{1}\nchar:{2}".format(linecount, wordcount, charcount)
        return output


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: wc.py <filename>")
        sys.exit(1)
    else:
        arg = sys.argv[1]
        result = wc(arg)
        print(result)
