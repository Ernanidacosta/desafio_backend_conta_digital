from typing import List
from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from core.deps import get_session
from models.person_model import PersonModel
from schemas.person_schema import PersonSchema

router = APIRouter()


# POST Person
@router.post(
    '/person',
    status_code=status.HTTP_201_CREATED,
    response_model=PersonSchema,
)
async def post_person(
    person: PersonSchema, db: AsyncSession = Depends(get_session)
):
    new_person = PersonModel(
        first_name=person.first_name,
        last_name=person.last_name,
        birthday=person.birthday,
        password=person.password,
        username=person.username,
        user_id=person.user_id,
    )
    db.add(new_person)
    await db.commit()
    return new_person


# GET Persons List
@router.get('/persons', response_model=List[PersonSchema])
async def get_persons(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(PersonModel)
        result = await session.execute(query)
        persons: List[PersonModel] = result.scalars().all()

        return persons
