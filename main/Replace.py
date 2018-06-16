import sys

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
		print(self.file_text)


def main():
	args = sys.argv
	rep = Manipulator(args[1])
	rep.setupFile()
	rep.readFile()
	rep.replaceText("Alexander", "Hamlet")
	rep.writeFile()
	rep.closeFile()
	

if __name__ == '__main__':
	main()
