import sys
import os.path
import argparse

class Manipulator:
    file_name = ''
    file_text = ''

    def __init__(self, inputFile):
        self.file_name = inputFile

    def setupFile(self):
        # open file for reading and writing
        self.file_name = open(self.file_name, 'r+')

    def readFile(self):
        self.file_text = self.file_name.read()

    def writeFile(self):
        # Just to be clear, this overwrites the file
        self.file_name.seek(0)
        self.file_name.truncate()
        self.file_name.write(self.file_text)

    def closeFile(self):
        self.file_name.close()

    def replaceText(self, ogString, neoString):
        self.file_text = self.file_text.replace(ogString, neoString)

def createSpaceSize(length):
    spaces = ""
    for i in range(length):
        spaces += " "
    return spaces

def process(file, ogString, neoString):
    rep = Manipulator(file)
    rep.setupFile()
    rep.readFile()
    rep.replaceText(ogString, neoString)
    rep.writeFile()
    rep.closeFile()

# ====== TO DO ======
# - Add options for certain conditions
#      - Variables only
#      - Strings only
#      - etc
# - Add option to only replace on/between certain lines

def main():
    parser = argparse.ArgumentParser(description="Simple program that replaces a specified instance x with a specified instance y. Note: If ether flag -t or -s is used then instance arguments are not required.")
    parser.add_argument("file", help="Target file for string replacement.")
    tabOption = parser.add_mutually_exclusive_group()
    tabOption.add_argument("-s", "--tabsToSpaces",
        help="Converts tabs to spaces. Default: 4 spaces equal 1 tab.",
        action="store_true")
    tabOption.add_argument("-t", "--spacesToTabs",
        help="Converts spaces to tabs. Default: 1 tab equals 4 spaces.",
        action="store_true")
    parser.add_argument("-l", "--tabLength",
        help="Specify the length of a tab. Default: 1 tab equals 4 spaces.",
        type=int,
        default=4)
    parser.add_argument("replacee",
        help="The instance to be replaced.",
        nargs="?",
        default="")
    parser.add_argument("replacer",
        help="The instance replacing the old instance.",
        nargs="?",
        default="")

    args = parser.parse_args()
    if os.path.isfile(args.file):
        flagCheck = False

        if args.tabsToSpaces:
            process(args.file, "    ", createSpaceSize(args.tabLength))
            flagCheck = True
        elif args.spacesToTabs:
            process(args.file, createSpaceSize(args.tabLength), "   ")
            flagCheck = True

        if args.replacee and not args.replacer:
            print("Error: Given target to replace without a replacement.")
        elif not args.replacee and args.replacer:
            print("Error: Given replacement but no target to replace.")
        elif args.replacee and args.replacer:
            process(args.file, args.replacee, args.replacer)
        elif not flagCheck:
            print("Error: Expected a target to replace.")
    else:
        print("ERROR: Invalid file argument.")

if __name__ == '__main__':
    main()
