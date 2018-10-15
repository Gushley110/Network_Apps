import json
from os import listdir
from os.path import isfile, join
from File_Manager import *

class File_List():

	def __init__(self,path = 'share/', file_name = 'users'):
		self.path = path
		self.file_name = file_name

	def list_files(self):
		path = self.path
		files = [f for f in listdir(path) if isfile(join(path, f))]

		return files

	def create_file_from_json(self,json_list,file_name):
		fm = File_Manager(None,file_name)
		l = json.loads(json_list)
		for e in l:
			fm.append_text(e)

if __name__ == '__main__':

	fm = File_Manager('../ips.txt',None)

	print(fm.file_to_list())