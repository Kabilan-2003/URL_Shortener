from pydantic import BaseModel

class URLBase(BaseModel):
    original_url: str

class URL(URLBase):
    id: int
    short_url: str

    class Config:
        from_attributes = True

class URLCreate(URLBase):
    pass

class URLUpdate(URLBase):
    pass

class URLDelete(URLBase):
    pass