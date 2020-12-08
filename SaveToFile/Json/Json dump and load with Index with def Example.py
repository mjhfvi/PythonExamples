import json

file_name = "D:\\ComputerList.json"

def menu():
    def json_write(dict):
        json_file = open(file_name, "w")
        json.dump(dict, json_file, indent=4)
        json_file.close()

    def jason_read():
        json_file = open(file_name, 'r')
        json_object = json.load(json_file)
        json_file.close()
        return json_object

    def input_data():
        host_input = input('Enter Host Name: ')
        return host_input

    while True:

        host_input = input_data()
        dictionary = {0: {'host': host_input}}
        json_write(dictionary)
        choice = input('Continue? Y/N ').lower()

        if choice == "y":
            while True:

                jason_read()
                object = jason_read()

                count = 0
                for x in object:
                    if isinstance(object[x], dict):
                        count += len(object[x])

                host_input = input_data()
                dictionary_add = {count: {'host': host_input}}
                object.update(dictionary_add)

                json_write(object)

                choice = input('Continue? Y/N ').lower()
                if choice == "y":
                    continue

                if choice == "n":
                    break
                else:
                    print('--Only Enter Y/N --')

        if choice == "n":
            break
        else:
            print('--Only Enter Y/N --')

menu()