from enum import Enum

from pydantic import BaseModel, Field
from typing import Optional, Union

class GenderEnum(str, Enum):
    male = "Male"
    female = "Female"
    diverse = "Diverse"

class DriverLicense(BaseModel):
    state: Optional[str] = Field(None, description="State of issuance, e.g., California, Pennsylvania")
    license_number: Optional[str] = Field(None, description="Driver's license number")
    full_name: Optional[str] = Field(None, description="Full name of the license holder")
    dob: Optional[str] = Field(None, description="Date of birth in YYYY-MM-DD format")
    expiration_date: Optional[str] = Field(None, description="License expiration date in YYYY-MM-DD format")
    issue_date: Optional[str] = Field(None, description="License issue date in YYYY-MM-DD format")
    address: Optional[str] = Field(None, description="Address of the license holder")
    gender: Optional[GenderEnum] = Field(None, description="Gender of the license holder")
    height: Optional[str] = Field(None, description="Height of the license holder")
    weight: Optional[str] = Field(None, description="Weight of the license holder")
    eye_color: Optional[str] = Field(None, description="Eye color of the license holder")
    hair_color: Optional[str] = Field(None, description="Hair color of the license holder")
    endorsements: Optional[str] = Field(None, description="Endorsements on the license")
    restrictions: Optional[str] = Field(None, description="Restrictions on the license")
    class_type: Optional[str] = Field(None, description="Class of the license, e.g., Class C")

class Passport(BaseModel):
    country: str = Field(None, description="Issuing country")  # Optional if None is provided as default
    passport_number: str = Field(None, description="Passport number")  # Optional if None is provided
    full_name: str = Field(None, description="Full name of the passport holder")  # Optional
    dob: str = Field(..., description="Date of birth of the passport holder. Convert to YYYY-MM-DD format")  # Required
    expiration_date: str = Field(..., description="Passport expiration date in YYYY-MM-DD format")  # Required
    issue_date: str = Field(..., description="Passport issue date in YYYY-MM-DD format")  # Required
    place_of_birth: str = Field(..., description="Place of birth of the passport holder")  # Required
    nationality: str = Field(..., description="Nationality of the passport holder")  # Required
    gender: GenderEnum = Field(None, description="Gender of the passport holder")  # Optional if None is provided

class DocumentTypeEnum(str, Enum):
    driver_license = "DriverLicense"
    passport = "Passport"
    micellaneous = "Miscellaneous"

class DocumentType(BaseModel):
    document_type: DocumentTypeEnum = Field(..., description="Type of the document, either 'DriverLicense' or 'Passport'")

class ModelOptionsEnum(Enum):
    LlamaVision90B = "accounts/fireworks/models/llama-v3p2-90b-vision-instruct"
    LlamaVision11B = "accounts/fireworks/models/llama-v3p2-11b-vision-instruct"
    Phi3Vision = "accounts/fireworks/models/phi-3-vision-128k-instruct"

    @property
    def technical_value(self) -> str:
        return self.value