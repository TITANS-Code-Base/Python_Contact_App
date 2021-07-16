from entities import Person
import unittest
from service import *
class People(unittest.TestCase):

    def test_add_person(self):
        a=Person("ada", "dada", "+13232")
        with open ("db/db.json", "r") as file:
            content_as_list_of_dict=json.loads(file.read())
            content_as_list_of_dict.append(a.__dict__)
        self.assertTrue( a.__dict__ in content_as_list_of_dict)
    
    def test_show_all(self):
        all=show_all()
        self.assertIsInstance(all, list)

    def test_delete_one(self):
        with open ("db/db.json", "r") as file:
            content_as_list_of_dict=json.loads(file.read())
            exdict={"name":"sas", "surname":"sasa", "phone_number":"sasas"}
            content_as_list_of_dict.append(exdict)
            for dict in content_as_list_of_dict:
                if dict['name']=="sas" and dict['surname']=="sasa" and dict['phone_number']=="sasas":
                    content_as_list_of_dict.remove(dict)   
        self.assertFalse( exdict in content_as_list_of_dict)


if __name__ == '__main__':
    unittest.main()