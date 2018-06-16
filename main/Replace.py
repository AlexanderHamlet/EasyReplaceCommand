import sys
import os.path as path

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

def main():

    def isFlag(arg):
        if arg[0] == '-':
            return True
        else:
            return False

    def legitFlags(arg, validArgs):
        if arg in validArgs:
            return True
        else:
            return False

    args = sys.argv
    argLen = len(args)
    validFlags = ["-ts", "-st"]
    errorInvalidFile = "ERROR: Expected valid file location as argument."
    passedErrorCheck = True

    if argLen < 2:
        print(errorInvalidFile)
        passedErrorCheck = False
    elif isFlag(args[1]):
        if legitFlags(args[1], validFlags):
            if argLen > 2 and path.isfile(args[2]):
                if args[1] == '-ts':
                    file = args[2]
                    ogString = "    "
                    neoString = "    "
                elif args[1] == '-st':
                    file = args[2]
                    ogString = "    "
                    neoString = "    "
            else:
                print(errorInvalidFile)
                passedErrorCheck = False
        else:
            print("ERROR: " + args[1] + " is not a valid flag.")
            passedErrorCheck = False
    elif path.isfile(args[1]):
        file = args[1]
        if(argLen < 3):
            print("ERROR: Expected a string to be replaced as argument.")
            passedErrorCheck = False
        elif(argLen < 4):
            print("ERROR: Expected a string to replace the old with as argument.")
            passedErrorCheck = False
        ogString = args[2]
        neoString = args[3]
    else:
        print(errorInvalidFile)
        passedErrorCheck = False

    if(passedErrorCheck):
        rep = Manipulator(file)
        rep.setupFile()
        rep.readFile()
        rep.replaceText(ogString, neoString)
        rep.writeFile()
        rep.closeFile()

if __name__ == '__main__':
    main()
