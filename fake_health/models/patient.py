"""
AUTHORS: Rick Moton
OBJECTIVE: This file will contain the Patient model
NOTES:
"""

from abc import ABC, abstractmethod

from faker import Faker

# ==============================================================================


class Patient:
    """
    This class will contain the Patient model
    """

    def __init__(self, faker: Faker, profile: dict = None):
        self.first_name, self.last_name = faker.name().split(" ")
        self.dob = faker.date_of_birth(minimum_age=18, maximum_age=100)
        self.gender = faker.random_element(elements=("M", "F"))
        self.email = faker.email()
        self.phone = faker.phone_number()
        self.address = faker.address()
        self.city = faker.city()
        self.state = faker.state()
        self.zip_code = faker.zipcode()

        self.eligbility = faker.

    def __str__(self):
        return str(tuple(vars(self).values()))
