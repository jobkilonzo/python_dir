import os

os.chdir('/home/scusi/Codes/python/')

for dirpath, dirnames, filenames in os.walk('/home/scusi/Codes/python/'):
	print('Current path: ', dirpath)
	print('Directories: ', dirnames)
	print('Files: ', filenames)