import sys
import platform
from pathlib import Path


#checks whether the extension of the file is in the list of extensions of the filetype;
#arguments passed: file_name - name of the file to be sorted;
#                  filetype - type of file;

def sortfiles(file_name , filetype):
	file_extension = str(file_name).split(".")[-1]
	if(file_extension in filetype):
		return True
	else:
		return False
	 	
	 	
def main():
	#assigns the value of forward or backward slach according to the os
	if(platform.system() == 'Windows'):
		slash = "\\"
	else:
		slash = "/"	
	#checks whether source and destination paths are passed
	if(len(sys.argv) < 3):
		print("Usage:sortFiles <SrcPath> <DestPath>;\nPlease give valid SrcPath and DestPath directories")
		sys.exit(-1)
	source = Path(sys.argv[1])
	#checks whether the source path exists or not
	if(not source.exists()):
		print("The source directory <$" + source + "> doesn't exist")
		sys.exit(-1)
	else:
		#dictionary containing various filetypes and extensions associated with them
		filetypes = dict(
		c_programs = ['c'],
		java_programs = ['class','java'],
		images = ['jpg','JPG','gif','png','jpeg','bmp'],
		audio = ['mp3','wav','aiff','flac','aac'],
		videos = ['mp4','flv','m4v','mpeg','mov','mkv','mpg','mpe','wmv','MOV'],
		compressed = ['zip','tar','rar','deb','gz'],
		exe = ['exe'],
		documents = ['pdf','doc','docx','txt'],
		presentations = ['ppt','pptx']
		)
		#list of all the files present in the source folder
		file_list = [x for x in source.iterdir() if x.is_file()]
		#sorts files according to their extensions
		for filetype in filetypes:
			for files in (file_list):
				if(sortfiles(files,filetypes[filetype])):
					source_file = Path(str(files))	#source path of particular file
					destination = Path(sys.argv[2] + slash + filetype)	#destination path where the file is to moved
					if(not destination.exists()):	#creating destionation path if it doesn't exist
						Path.mkdir(destination)	
					source_file.rename(destination / source_file.name)	#moving file			

if(__name__ == "__main__"):
	main()

