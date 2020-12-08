import inquirer
from pprint import pprint


questions = [
    inquirer.Checkbox('interests',
                    message="Select Days to Stay?",
                    choices=['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday'],
                    ),
]
answers = inquirer.prompt(questions)

pprint(answers)

if answers == "Sanday":
    print("I selected Sunday")
