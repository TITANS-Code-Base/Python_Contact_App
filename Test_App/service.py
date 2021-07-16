from entities import Person
import json


def add_person(name, surname, phone_number):
    new_person=Person(name, surname, phone_number)
    new_person_as_dict=new_person.__dict__

    with open ("db/db.json", "r") as file:
        content_as_list_of_dict=json.loads(file.read())
        content_as_list_of_dict.append(new_person_as_dict)
    
    with open ("db/db.json", "w") as file:
        file.write(json.dumps(content_as_list_of_dict))




def show_all():
    with open ("db/db.json", "r") as file:
        content_as_list_of_dict=json.loads(file.read())
        return (content_as_list_of_dict)
    

def delete_one(name,surname, phone_number):
    with open ("db/db.json", "r") as file:
        content_as_list_of_dict=json.loads(file.read())
    for dict in content_as_list_of_dict:
        if dict['name']==name and dict['surname']==surname and dict['phone_number']==phone_number:
            content_as_list_of_dict.remove(dict)
    with open ("db/db.json", "w") as file:
        file.write(json.dumps(content_as_list_of_dict))
