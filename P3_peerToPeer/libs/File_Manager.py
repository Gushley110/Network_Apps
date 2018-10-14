class File_Manager:

	def __init__(self,srcname = None,trgtname = None):
		self.srcname  = srcname
		self.trgtname = trgtname

	def get_text(self): #Returns the text of the file as a string encoded in utf-8
		with open(self.srcname, encoding='utf-8') as file:
			text = file.read()
		return text

	def get_text_bin(self): #Returns the text of the file as binary
		with open(self.srcname, 'rb') as file:
			text = file.read()
		return text

	def copy_text(self,n = 1):
		text = self.getText()

		with open(self.trgtname, mode='w', encoding='utf-8') as new_file:
				new_file.write(n * ("%s\n" % (text)))

	def create_file(self,text): #Creates or modifies a file in string encoded in utf-8
		with open(self.trgtname, mode='w', encoding='utf-8') as new_file:
				new_file.write("%s" % (text))

	def append_text(self,text):
		with open(self.trgtname, mode='a', encoding='utf-8') as new_file:
			new_file.write('{}\n'.format(text))

	def create_file_bin(self,text): #Creates or modifies a file in binary
		with open(self.trgtname, mode='wb') as new_file:
				new_file.write(text)

	


