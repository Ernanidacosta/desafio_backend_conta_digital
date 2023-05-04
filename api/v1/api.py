from fastapi import APIRouter

from api.v1.endpoints import bank, friend, person

api_router = APIRouter()
api_router.include_router(person.router, prefix='/person')
api_router.include_router(bank.router, prefix='/bank')
api_router.include_router(friend.router, prefix='/friend')
