from entities import Person
from service import *

def test_add_person():
    a=Person("ada", "dada", "+13232")
    with open ("db/db.json", "r") as file:
        content_as_list_of_dict=json.loads(file.read())
        content_as_list_of_dict.append(a.__dict__)
    return a.__dict__ in content_as_list_of_dict
    # self.assertTrue( a.__dict__ in content_as_list_of_dict)
    
def test_show_all():
    all=show_all()
    return type(all)==list
    # self.assertIsInstance(all, list)

def test_delete_one():
    with open ("db/db.json", "r") as file:
        content_as_list_of_dict=json.loads(file.read())
        exdict={"name":"sas", "surname":"sasa", "phone_number":"sasas"}
        content_as_list_of_dict.append(exdict)
        for dict in content_as_list_of_dict:
            if dict['name']=="sas" and dict['surname']=="sasa" and dict['phone_number']=="sasas":
                content_as_list_of_dict.remove(dict)   
    assert ( exdict not in content_as_list_of_dict)
        # self.assertFalse( exdict in content_as_list_of_dict)

def test_select_and_list(name='javid', db='db/test.json', surname='dovlatov'):
    counter=0
    with open (db, "r") as file:
        content_as_list_of_dict=json.loads(file.read())
    for dict in content_as_list_of_dict:
        if dict['name'].lower()==name.lower() and dict['surname'].lower()==surname.lower():
            print(f"Name: {dict['name']},  Surname: {dict['surname']}, Phone Number: {dict['phone_number']}")

def test_update(db='db/test.json'):
    update_record('test_name', 'test_surname', 'new_name', 'new_surname', '', db=db)
    with open (db, 'r') as file:
        old_content=file.read()
    update_record('new_name', 'new_surname', 'test_name', 'test_surname', '',db=db)
    with open (db, 'r') as file:
        new_content=file.read()
    assert old_content!=new_content