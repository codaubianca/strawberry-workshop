from typing import List
from datetime import datetime
from django.utils import timezone

import strawberry
from strawberry import Info

from core.models import SocialClub, Product, Member, Guest
from exercise1.schema.types import SocialClubType, ProductType, MemberType, GuestType


@strawberry.type
class Query:

    @strawberry.field
    def social_clubs(self, info: Info) -> List[SocialClubType]:
        return [SocialClubType(
            id=sc.id,
            name=sc.name,
            street=sc.street, 
            zip=sc.zip 
        ) for sc in SocialClub.objects.all()]

    @strawberry.field
    def products(self, info: Info) -> List[ProductType]:
        return [ProductType(
            id=product.id,
            name=product.name,  
            price=product.price,  
            quality=product.quality  
        ) for product in Product.objects.all()]

    # DOCS: https://strawberry.rocks/docs/types/scalars#scalars
    # HINT: you can use datetime or django.utils.timezone
    # TODO 9: Add a field current_date_time and return the current datetime

    @strawberry.field
    def current_date_time(self, info: Info) -> datetime:
        return timezone.now()

    @strawberry.field
    def members(self, info: Info) -> List[MemberType]:
        return [MemberType(
            id=member.id,
            first_name=member.first_name,  
            last_name=member.last_name,  
            age=member.age  
        ) for member in Member.objects.all()]

    @strawberry.field
    def guests(self, info: Info) -> List[GuestType]:
        return [GuestType(
            id=guest.id,
            first_name=guest.first_name,  
            last_name=guest.last_name,  
            rating=guest.rating  
        ) for guest in Guest.objects.all()]
