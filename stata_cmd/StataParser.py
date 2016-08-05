import os

class StataParser:

	def __init__(self, pathToStata):
		self.path = pathToStata


	def do(self, pathToDo, pathToData, args):
		argStr = ""
		for arg in args:
			argStr = argStr + str(arg) + " "
		cmd = self.path + " /e do " + pathToDo + " " + pathToData + " " + argStr
		os.system(cmd)


	def make_do(self, pathToData, stataCmds, outputDoFile):
		f = open(outputDoFile, 'w')
		file = "use " + pathToData + ", clear\n"
		for cmd in stataCmds:
			file = file + cmd + "\n"
		f.write(file)
		f.close()


	def run_stata(self, pathToData, stataCmds):
		make_do(self, pathToData, stataCmds, "temp.do")
		do(self, "temp.do", pathToData)
		os.remove("temp.do")

	def get_exe_path(self):
		return self.path