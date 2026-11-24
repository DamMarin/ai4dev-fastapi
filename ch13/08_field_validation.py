"""
Validation with Fields
"""

from pydantic import BaseModel, Field, ValidationError

class Item(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    price: float = Field(gt=1, description="The price of the item")
    tax: float| None = Field(default=None, ge=0, description="The tax of the item")
    tags: list[str] = Field(default=[], max_length=10)

try:
    item = Item(name="Ram", price="2") #pass
    # item = Item(name="Ram", price="2") #validation error
    print(item.model_dump())
except ValidationError as e:
    print(e)