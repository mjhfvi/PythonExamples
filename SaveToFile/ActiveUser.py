import os
#######################  Open File ##############################
FolderRootPath = "D:\\Active\\"
FileActiveUserPath = "ActiveUser.txt"
############  Testing for an Existing Folder ####################
try:
    os.mkdir(FolderRootPath)
except OSError:
    print("Directory %s Exists" % FolderRootPath)
else:
    print("Successfully created the directory %s " % FolderRootPath)
############  Testing for an Existing File  #####################
try:
    open(FolderRootPath + FileActiveUserPath,)
except IOError:
    FileActiveUser = open(FolderRootPath + FileActiveUserPath, "w+")
    FileActiveUser.close()
    print("Successfully created the file %s " % FileActiveUserPath)
else:
    print("File %s Exists" % FileActiveUserPath)
#######################  Input User Info ########################
inputFirstName = input("Enter your First Name:   ").capitalize()
inputLastName = input("Enter your Last Name:    ").capitalize()
FileActiveUser = open(FolderRootPath + FileActiveUserPath, "w+")
FileActiveUser.write(str(1) + " " + str(inputFirstName) + "\n" + str(2) + " " + str(inputLastName))
FileActiveUser.close()
#######################  Check User Info ########################
ActiveUserInput = {}
with open(FolderRootPath + FileActiveUserPath, "r") as f:
    for line in f:
        (key, val) = line.split()
        ActiveUserInput[int(key)] = val
print(ActiveUserInput[1], ActiveUserInput[2])
print(ActiveUserInput)
FileActiveUser.close()
#######################  Remove File At The End ##################
os.remove(FolderRootPath + FileActiveUserPath)
print(FolderRootPath + FileActiveUserPath + " ***File Removed***")