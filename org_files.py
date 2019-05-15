#!/usr/bin/python

# This script is for organizing specified folders in the main Desktop. link to schedule to run weekly/monthly

import os
from glob import glob
import shutil
import time



folders = ["c:\\Users\\joseph\\Desktop",
	   "c:\\Users\\joseph\\Downloads",
	   "c:\\Users\\joseph\\Documents"]



d = [{'file_type': ['*.csv', '*.xlsx', '*.xls', '*.xlsm'], 'folder': 'c:\\Users\\joseph\\Documents\\excel_files'},
     {'file_type': ['*.ppt', '*.pptx'], 'folder': 'c:\\Users\\joseph\\Documents\\slide_shows'},
     {'file_type': ['*.pdf'], 'folder': 'c:\\Users\\joseph\\Documents\\pdf_files'},
     {'file_type': ['*.doc', '*.docx'], 'folder': 'c:\\Users\\joseph\\Documents\\word_documents'},
     {'file_type': ['*.txt'], 'folder': 'c:\\Users\\joseph\\Documents\\text_files'},
     {'file_type': ['*.zip', '*.exe', '*.msi', '*.gz', '*.7z', '*.rar'], 'folder': 'c:\\Users\\joseph\\Documents\\setup_files'},
     {'file_type': ['*.jpg', '*.png'], 'folder': 'c:\\Users\\joseph\\Documents\\image_files'},
     {'file_type': ['*.tmp', '*.msg', '*.ica', '*.cr', '*.pkt', '*.pka', '*.dat', '*.ini'], 'folder': 'c:\\Users\\joseph\\Documents\\other_files'}]



def find_files(type, find_path):
	files = glob('%s/%s' % (find_path, type))
	return files



def move_org(files, move_path):
	for file in files:
		try:
			# First try to move the file
			shutil.move(file, move_path)

		except:
			# only if exception is faced -- rename file when moving to destination
			# params for new destination filename
			dt = time.strftime("%Y%m%d%H%M%S")
			ctime = os.stat(file).st_ctime
			base = os.path.basename(file)
			file_name = os.path.splitext(base)[0]
			file_ext = os.path.splitext(base)[1]
			
																    
			# give new moved file a new name
			new_name = "%s.%s.%s%s" % (file_name, dt, ctime, file_ext)

			# new full path of the moved file
			new_full_path = "%s/%s" %(move_path, new_name)
																	            
			# move
			shutil.move(file, new_full_path)



# check if we have all our destination directories:
def check_folders(path):
	if not os.path.exists(path):
		os.makedirs(path)



def main():
	#for each item in d
	for entry in d:
		check_folders(entry['folder'])

		# Find the files to be moved and move them:
		for ext in entry['file_type']:
			for folder in folders:
				files = find_files(ext, folder)
				if len(files) > 0:
					move_org(files, entry['folder'])



if __name__ == '__main__':
	main()

