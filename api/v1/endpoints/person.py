from typing import List, Optional, Any
from fastapi import APIRouter, status, Depends, HTTPException, Response
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from core.deps import get_session, get_current_user
from core.security import generate_hash_password
from core.auth import authenticate, create_token_access
from models.person_model import PersonModel
from schemas.person_schema import PersonSchemaBase, PersonSchemaCreate, PersonSchemaUpdate

router = APIRouter()


# POST Person Signup
@router.post(
        '/person/new',
        status_code=status.HTTP_201_CREATED,
        response_model=PersonSchemaBase
)
async def post_person(person: PersonSchemaCreate, db: AsyncSession = Depends(get_session)):
    new_person = PersonModel(
        first_name=person.first_name,
        last_name=person.last_name,
        birthday=person.birthday,
        password=generate_hash_password(person.password),
        username=person.username,
        user_id=person.user_id,
    )
    async with db as session:
        session.add(new_person)
        await session.commit()
    return new_person



#PUT Person
@router.put(
    '/person/{person_id}',
    response_model=PersonSchemaUpdate,
    status_code=status.HTTP_200_OK
)
async def put_person(person_id: int, person: PersonSchemaUpdate, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(PersonModel).filter(PersonModel.id == person_id)
        result = await session.execute(query)
        person_update: PersonSchemaUpdate = result.scalars().unique().one_or_none()

        if person_update:
            if  person.first_name:
                person_update.first_name = person.first_name
            if person.last_name:
                person_update.last_name = person.last_name
            if person.birthday:
                person_update.birthday = person.birthday
            if person.password:
                person_update.password = generate_hash_password(person.password)
            if person.username:
                person_update.username = person.username
            if person.user_id:
                person_update.user_id = person.user_id

            await session.commit()
            return person_update

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Person with id {person_id} not found')


# GET Persons List
@router.get('/persons', response_model=List[PersonSchemaBase])
async def get_persons(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(PersonModel)
        result = await session.execute(query)
        persons: List[PersonSchemaBase] = result.scalars().unique().all()

        return persons


# GET Persons Logged
@router.get('/person/logged', response_model=PersonSchemaBase)
def get_person_logged(user_logged: PersonSchemaBase = Depends(get_current_user)):
    return user_logged


# GET Person by ID
@router.get('/person/{person_id}',
            response_model=PersonSchemaBase,
            status_code=status.HTTP_200_OK
            )
async def get_person_by_id(person_id: str, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(PersonModel).filter(PersonModel.id == person_id)
        result = await session.execute(query)
        person: PersonSchemaBase = result.scalars().unique().one_or_none()

        if result:
            return person

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Person with id {person_id} not found'
        )


# DELETE Person by ID
@router.delete('/person/{person_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_person_by_id(person_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(PersonModel).filter(PersonModel.id == person_id)
        result = await session.execute(query)
        person: PersonSchemaBase = result.scalars().unique().one_or_none()

        if person:
            await session.delete(person)
            await session.commit()

            return Response(status_code=status.HTTP_204_NO_CONTENT)
        
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Person with id {person_id} not found')


# POST Login
@router.post('/login')
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_session)):
    user = await authenticate(email=form_data.username, password=form_data.password, db=db)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect username or password'
        )

    return JSONResponse(content={"access_token": create_token_access(sub=user.id), "token_type": "bearer"}, status_code=status.HTTP_200_OK)
