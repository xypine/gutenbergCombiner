from pathlib import Path
import os
zips = []

print("Searching for compressed books...")
for filename in Path('').rglob('*.zip'):
    zips.append(filename)
print("Found " + str(len(zips)) + " books in total.")

import zipfile

str_list = []
out = ""

i = 0
print("Reading the books...")
for name in zips:
	print("[" + str(i) + "/"+ str(len(zips)) + "]", end="\r")
	archive = zipfile.ZipFile(name, 'r')
	out2 = ""
	for filename in archive.namelist():
		if not os.path.isdir(filename):
			# read the file
			for line in archive.open(filename):
				try:
					out2 = out2 + line.decode('cp1252')
				except Exception as e:
					e = ""
			archive.close()                # Close the file after opening it
	del archive                            # Cleanup (in case there's further work after this)
	try:
		out2 = out2.split("*** START OF THIS PROJECT GUTENBERG")[1]
		out2 = out2.split("***")[1]
	except Exception as e:
		e = ""
	try:
		out2 = out2.split("*** END OF THIS PROJECT GUTENBERG EBOOK")[0].split("End of the Project Gutenberg EBook")[0]
	except Exception as e:
		e = ""
	out2 = out2 + "\n----------------------\n"
	str_list.append(out2)
	#if i == -1:
	#	if input("q to exit (first book prompt): ") == "q":
	##		break
	#	i = 1
	i = i + 1
print("Compiling files...",end="")
out = ''.join(str_list)
with open("out.txt", "w+") as f:
	f.write(out)
print("Done")
print("Have a good day")