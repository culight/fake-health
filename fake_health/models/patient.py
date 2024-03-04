"""
AUTHORS: Rick Moton
OBJECTIVE: This file will contain the Patient model
NOTES:
"""
from abc import ABC, abstractmethod

from faker import Faker
#==============================================================================

class Patient(ABC):
    def __init__(self):
        self.fake = Faker()
        self.patient = {
            "first_name": self.fake.first_name(),
            "last_name": self.fake.last_name(),
            "dob": self.fake.date_of_birth(minimum_age=18, maximum_age=100
        }