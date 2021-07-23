from service import delete_one
from service import add_person, show_all, select_and_list, update_record


texts={
    "greeting":"Welcome!",
    "intro":"This is software for saving contacts. Please, choose the action for the next step: Press 1 to add new contact, 2 in order to view contacts, 3 to delete one of them, 4 to show specific one, 5 to update record ",

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

elif choice==4:
    select_and_list(name=input("Please enter name:\n"), surname=input("Enter Surname: \n"))

elif choice==5:
    update_record(name=input("Please enter name:\n"), surname=input("Enter Surname: \n"), new_name=input("Enter new name: -- If do not want to change, press enter  -- \n"), new_surname= input("Enter new surname: -- If do not want to change, press enter  -- \n"), new_phone_number=input("Enter new phone number: -- If do not want to change, press enter  -- \n"))