from pydantic import BaseModel, AnyUrl
from datetime import datetime
from decimal import Decimal
from typing import Optional

class SMemes(BaseModel):
    title: str
    image_url: AnyUrl
    description: Optional[str]
    category: str

class SNewMemes(BaseModel):
    title: str
    image_url: AnyUrl
    description: Optional[str]
    category: str