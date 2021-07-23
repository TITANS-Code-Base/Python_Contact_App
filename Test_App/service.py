from entities import Person
import json


def add_person(name, surname, phone_number, db="db/db.json"):
    new_person=Person(name, surname, phone_number)
    new_person_as_dict=new_person.__dict__

    with open (db, "r") as file:
        content_as_list_of_dict=json.loads(file.read())
        content_as_list_of_dict.append(new_person_as_dict)
    
    with open (db, "w") as file:
        file.write(json.dumps(content_as_list_of_dict))




def show_all(db="db/db.json"):
    with open (db, "r") as file:
        content_as_list_of_dict=json.loads(file.read())
        return (content_as_list_of_dict)
    

def delete_one(name,surname, phone_number, db="db/db.json"):
    with open (db, "r") as file:
        content_as_list_of_dict=json.loads(file.read())
    for dict in content_as_list_of_dict:
        if dict['name']==name and dict['surname']==surname and dict['phone_number']==phone_number:
            content_as_list_of_dict.remove(dict)
    with open ("db/db.json", "w") as file:
        file.write(json.dumps(content_as_list_of_dict))

def select_and_list(name, surname,  db='db/db.json'):
    with open (db, "r") as file:
        content_as_list_of_dict=json.loads(file.read())
    for dict in content_as_list_of_dict:
        if dict['name'].lower()==name.lower() and dict['surname'].lower()==surname.lower():
            print(f"Name: {dict['name']},  Surname: {dict['surname']}, Phone Number: {dict['phone_number']}")


def update_record(name, surname, new_name, new_surname, new_phone_number, db="db/db.json"):
    with open (db, "r") as file:
        content_as_list_of_dict=json.loads(file.read())
    for dict in content_as_list_of_dict:
        if dict['name'].lower()==name.lower() and dict['surname'].lower()==surname.lower():
            if new_name!="":
                dict['name']=new_name.strip()
            if new_surname!="":
                dict['surname']=new_surname.strip()
            if new_phone_number!="":
                dict['phone_number']=new_phone_number.strip()
    with open (db, "w") as file:
        file.write(json.dumps(content_as_list_of_dict))        
