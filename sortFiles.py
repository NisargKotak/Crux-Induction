import sys
import os
import shutil
import platform
from pathlib import Path


#sorts files according to their extension;
#arguments passed: file_name - name of the file to be sorted;
#                  filetype - type of file;
#global variables used: none;

def sortfiles(file_name , filetype):
	file_extension = str(file_name).split(".")[-1]
	if(file_extension in filetype):
		return True
	else:
		return False
	 	

#local variables used: slash - forward or backward slash depending upon the os; class string
#                      source - path of the source folder; class string
#                      destination - path of the folder where you want the files sorted; class string
#                      filetypes - different categories in which the files can be sorted; class dict
#                      filetype - a particular category of filetypes; class dict_keys
#                      files - name of file to be sorted; class string
#global variables used: none;	 	
def main():
	if(platform.system() == 'Windows'):
		slash = "\\"
	else:
		slash = "/"
	if(len(sys.argv) < 3):
		print("Usage:sortFiles <SrcPath> <DestPath>;\nPlease give valid SrcPath and DestPath directories")
		sys.exit(-1)
	source = Path(sys.argv[1])
	if(not source.exists()):
		print("The source directory <$" + source + "> doesn't exist")
		sys.exit(-1)
	else:
		filetypes = {}
		filetypes.setdefault('c_programs' , []).append('c')
		filetypes.setdefault('java_programs' , []).append('java')
		filetypes.setdefault('java_programs' , []).append('class')
		filetypes.setdefault('python_programs' , []).append('py')
		filetypes.setdefault('images' , []).append('jpg')
		filetypes.setdefault('images' , []).append('JPG')
		filetypes.setdefault('images' , []).append('gif')
		filetypes.setdefault('images' , []).append('png')
		filetypes.setdefault('images' , []).append('jpeg')
		filetypes.setdefault('images' , []).append('bmp')
		filetypes.setdefault('audio' , []).append('mp3')
		filetypes.setdefault('audio' , []).append('wav')
		filetypes.setdefault('audio' , []).append('aiff')
		filetypes.setdefault('audio' , []).append('flac')
		filetypes.setdefault('audio' , []).append('aac')
		filetypes.setdefault('videos' , []).append('mp4')
		filetypes.setdefault('videos' , []).append('m4v')
		filetypes.setdefault('videos' , []).append('flv')
		filetypes.setdefault('videos' , []).append('mpeg')
		filetypes.setdefault('videos' , []).append('mov')
		filetypes.setdefault('videos' , []).append('mpg')
		filetypes.setdefault('videos' , []).append('mpe')
		filetypes.setdefault('videos' , []).append('wmv')
		filetypes.setdefault('videos' , []).append('MOV')
		filetypes.setdefault('videos' , []).append('mkv')
		filetypes.setdefault('compressed' , []).append('zip')
		filetypes.setdefault('compressed' , []).append('tar')
		filetypes.setdefault('compressed' , []).append('rar')
		filetypes.setdefault('compressed' , []).append('7')
		filetypes.setdefault('compressed' , []).append('deb')
		filetypes.setdefault('compressed' , []).append('gz')
		filetypes.setdefault('exe' , []).append('exe')		    
		filetypes.setdefault('documents' , []).append('doc')
		filetypes.setdefault('documents' , []).append('docx')
		filetypes.setdefault('documents' , []).append('txt')
		filetypes.setdefault('documents' , []).append('pdf')
		filetypes.setdefault('presentations' , []).append('ppt')
		filetypes.setdefault('presentations' , []).append('pptx')
		file_list = [x for x in source.iterdir() if x.is_file()]
		#print(file_list)
		for filetype in filetypes:
			for files in (file_list):
				if(sortfiles(files,filetypes[filetype])):
					source_file = Path(str(files))
					destination = Path(sys.argv[2] + slash + filetype)
					if(not destination.exists()):
						Path.mkdir(destination)	
					source_file.rename(destination / source_file.name)
				
						

main()

