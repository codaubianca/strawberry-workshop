import strawberry
from core.schema.enums import QualityEnum

# DOCS: https://strawberry.rocks/docs/types/scalars

@strawberry.type
class SocialClubType:
    id: strawberry.ID
    name: str
    street: str
    zip: str

@strawberry.type
class ProductType:
    id: strawberry.ID
    name: str
    price: int
    quality: QualityEnum

@strawberry.type
class MemberType:
    id: strawberry.ID
    first_name: str
    last_name: str
    age: int

@strawberry.type
class GuestType:
    id: strawberry.ID
    first_name: str
    last_name: str
    rating: int
