from pydantic import BaseModel
from pydantic import Field
from datetime import date, datetime


class SuccessResponse(BaseModel):

    status: str = "success"
    code: int = 200


class IncomingAgeGender(BaseModel):

    customer_id: int = Field(..., alias="Customer ID")
    age: int = Field(..., alias="Age")
    gender: str = Field(..., alias="Gender")
    marital_status: str = Field(..., alias="Marital Status")
    education_level: str = Field(..., alias="Education Level")
    geographic_information: str = Field(..., alias="Geographic Information")
    occupation: str = Field(..., alias="Occupation")
    income_level: int = Field(..., alias="Income Level")
    behavioral_data: str = Field(..., alias="Behavioral Data")
    purchase_history: date = Field(..., alias="Purchase History")
    interactions_with_customer_service: str = Field(
        ..., alias="Interactions with Customer Service"
    )

    insurance_products_owned: str = Field(..., alias="Insurance Products Owned")
    coverage_amount: int = Field(..., alias="Coverage Amount")
    premium_amount: int = Field(..., alias="Premium Amount")
    policy_type: str = Field(..., alias="Policy Type")
    customer_preferences: str = Field(..., alias="Customer Preferences")
    preferred_communication_channel: str = Field(
        ..., alias="Preferred Communication Channel"
    )
    preferred_contact_time: str = Field(..., alias="Preferred Contact Time")
    preferred_language: str = Field(..., alias="Preferred Language")
    segmentation_group: str = Field(..., alias="Segmentation Group")
    holiday_name: str = Field(..., alias="HOLIDAY_NAME")
    row_num: int = Field(..., alias="row_num")


class ListIncomingAgeGender(BaseModel):

    data: list[IncomingAgeGender] = Field([])
