'''
Mode	Description
'r'	    This is the default mode. It Opens file for reading.
'w'	    This Mode Opens file for writing.
            If file does not exist, it creates a new file.
            If file exists it truncates the file.
'x'	    Creates a new file. If file already exists, the operation fails.
'a'	    Open file in append mode.
            If file does not exist, it creates a new file.
't'	    This is the default mode. It opens in text mode.
'b'	    This opens in binary mode.
'+'	    This will open a file for reading and writing (updating)

source:  https://www.guru99.com/reading-and-writing-files-in-python.html
'''


## Getting Where To Save File
where = raw_input('Where Do You Want To Save Your File? ')

## Start File in Path
file = open("D:\\PythonDemoFile.txt", "a")
print(file.read())

## Writing It
file.write("Now the file has more content!")
file.close()

## Append to file
file.write("Appended line %d\r\n" % (i + 1))