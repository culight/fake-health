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
        self.dob = faker.date_of_birth(minimum_age=65, maximum_age=100)
        self.gender = faker.random_element(elements=("M", "F"))
        self.email = faker.email()
        self.address = faker.address()
        self.city = faker.city()
        self.county = faker.county()
        self.state = faker.state()
        self.zip_code = faker.zipcode()

        # eligbility = faker.date_between()
        # self.elig_year = eligbility.year
        # self.elig_month = eligbility.month

    def __str__(self):
        return str(tuple(vars(self).values()))
