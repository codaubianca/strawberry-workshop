import strawberry
from typing import List
from core.schema.enums import QualityEnum


# DOCS: https://strawberry.rocks/docs/general/schema-basics#object-types

@strawberry.type
class SocialClubType:
    id: strawberry.ID
    name: str
    street: str
    zip: str
    members: List["MemberType"]
    guests: List["GuestType"]
    products: List["ProductType"]

@strawberry.type
class ProductType:
    id: strawberry.ID
    name: str
    price: int
    quality: QualityEnum
    # QUESTION: uh oh - this could go evilly wrong in future...
    # HINT: Maybe we should use one or more schema extensions? https://strawberry.rocks/docs/extensions
    social_club: SocialClubType


@strawberry.type
class MemberType:
    id: strawberry.ID
    first_name: str
    last_name: str
    age: int
    social_club: SocialClubType


@strawberry.type
class GuestType:
    id: strawberry.ID
    first_name: str
    last_name: str
    rating: int
    social_club: SocialClubType
