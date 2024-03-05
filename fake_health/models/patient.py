"""
AUTHORS: Rick Moton
OBJECTIVE: This file will contain the Patient model
NOTES:
"""
from abc import ABC, abstractmethod

from faker import Faker
#==============================================================================

class Patient:
    """
    This class will contain the Patient model
    """
    def __init__(
            self,
            profile: dict
        ):
         self.init_patient_profile(profile)

    def init_patient_profile(self, profile: dict):
            self.first_name
            self.last_name
            self.gender
            self.dob
            ssn: str,
            address: str,
            city: str,
            state: str,
            zip_code: str,
            phone: str,
            email: str
        profile = 
        return profile

# create family class