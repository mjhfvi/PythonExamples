fileName = "D:\\Net4uTEST.txt"

def createFile():
    file = open(fileName, "w+")      # x will create new file and NOT overwrite the file is you have it
    file.close()

def userInput():
    file = open(fileName, "a")
    for i in range(2):
        file.write(input("Enter your IP Address:  ") + "\n")

def printInfo():
    file = open(fileName, "r")
    print("\n\nList of IP Address:  \n"+file.read())

    path = 'D:\\'
    remove_file = input("Enter file name: ")
    os.remove(path + remove_file)
    print(remove_file, "File Removed!")


createFile()
userInput()
printInfo()
userInput()
printInfo()