from pydantic import BaseModel

class HouseRequest(BaseModel):
    location: str
    total_sqft: float
    bath: int
    balcony: int
    bhk: int