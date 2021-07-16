from service import delete_one
from service import add_person, show_all


texts={
    "greeting":"Welcome!",
    "intro":"This is software for saving contacts. Please, choose the action for the next step: Press 1 to add new contact, 2 in order to view contacts, and 3 to delete one of them",

}
print(texts["greeting"])
print(texts["intro"])
choice=int(input())
if choice==1:
    add_person(name=input("Please enter name:\n"), surname=input("Enter Surname: \n"), phone_number=input("Lastly, the phone number: \n"))
elif choice==2:
    people=show_all()
    for person in people:
        print(f'Name: {person["name"]} , Surname: {person["surname"]}, Phone Number: {person["phone_number"]}')
        print("---")
elif choice==3:
    delete_one(name=input("Please enter name:\n"), surname=input("Enter Surname: \n"), phone_number=input("Lastly, the phone number: \n"))