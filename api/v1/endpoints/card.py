from typing import List

from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.card_model import CardModel

from schemas.card_schema import CardSchema

from core.deps import get_session

router = APIRouter()
