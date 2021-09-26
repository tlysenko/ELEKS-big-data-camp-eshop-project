from faker import Faker

class User(object):

    def __init__(self,
                 first_name: str,
                 last_name: str,
                 age: int,
                 gender:str,
                 email:str,
                 address:str,
                 has_children_under_16:bool
                 ):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.email = email
        self.address = address
        self.has_children_under_16 = has_children_under_16

    def to_json(self) -> dict:
        return self.__dict__

    @staticmethod
    def generate_random_user():
        fake = Faker()
        fake_gender = fake.random_element(elements=('F','M'))
        fake_first_name = fake.first_name_female() if fake_gender == 'F' else fake.first_name_male()
        fake_last_name = fake.last_name_female() if fake_gender == 'F' else fake.last_name_male()
        fake_age:int = fake.pyint(min_value=12, max_value=78, step = 1)

        return User(
            email=fake.email(),
            first_name=fake_first_name,
            last_name=fake_last_name,
            address=fake.address(),
            age=fake_age,
            gender=fake_gender,
            has_children_under_16=fake.pybool() if fake_age in (19,60) else False)

