from typing import List, TYPE_CHECKING

import strawberry
from strawberry import Info

from core.schema.enums import QualityEnum
from core.utils import UpperCaseExtension

if TYPE_CHECKING:
    from core.models import SocialClub, Member, Guest, Product


# DOCS https://strawberry.rocks/docs/types/private

@strawberry.type
class SocialClubType:
    instance: strawberry.Private["SocialClub"]

    @strawberry.field
    def id(self, info: Info) -> strawberry.ID:
        return self.instance.id

    @strawberry.field
    def name(self, info: Info) -> str:
        return self.instance.name

    @strawberry.field
    def uppercase_name(self, info: Info) -> str:
        return self.instance.name.upper()

    @strawberry.field(extensions=[UpperCaseExtension()])
    def uppercase_name_ext(self, info: Info) -> str:
        return self.instance.name

    @strawberry.field
    def street(self, info: Info) -> str:
        return self.instance.street

    @strawberry.field
    def zip(self, info: Info) -> str:
        return self.instance.zip

    @strawberry.field
    def members(self, info: Info) -> List["MemberType"]:
        return [MemberType.from_obj(member) for member in self.instance.member_set.all()]

    @strawberry.field
    def guests(self, info: Info) -> List["GuestType"]:
        return [GuestType.from_obj(guest) for guest in self.instance.guest_set.all()]

    @strawberry.field
    def products(self, info: Info) -> List["ProductType"]:
        return [ProductType.from_obj(product) for product in self.instance.product_set.all()]

    # DOCS: https://strawberry.rocks/docs/guides/field-extensions#field-extensions
    # TODO 7: Add an extra field name_uppercase_ext with a FieldExtension to make it uppercase
    # HINT: You can find a prepared UpperCaseExtension in core.utils

    # QUESTION: Do you know some pro/cons for more boilerplate in types but less logic in queries?


@strawberry.type
class ProductType:
    id: strawberry.ID
    name: str
    price: int
    quality: QualityEnum
    social_club: SocialClubType

    @classmethod
    def from_obj(cls, product: "Product") -> "ProductType":
        return ProductType(
            id=product.id,
            name=product.name,
            price=product.price,
            quality=product.quality,
            social_club=product.social_club
        )
        # TODO 8: return a ProductType
        # HINT: Care with social club - it must be a type not a model instance


@strawberry.type
class MemberType:
    id: strawberry.ID
    first_name: str
    last_name: str
    age: int
    social_club: SocialClubType

    @classmethod
    def from_obj(cls, member: "Member") -> "MemberType":
        return MemberType(
            id=member.id,
            first_name=member.first_name,
            last_name=member.last_name,
            age=member.age,
            social_club=member.social_club
        )
        # HINT: Care with social club - it must be a type not a model instance


@strawberry.type
class GuestType:
    id: strawberry.ID
    first_name: str
    last_name: str
    rating: int
    social_club: SocialClubType

    @classmethod
    def from_obj(cls, guest: "Guest") -> "GuestType":
        return GuestType(
            id=guest.id,
            first_name=guest.first_name,
            last_name=guest.last_name,
            rating=guest.rating,
            social_club=guest.social_club
        )