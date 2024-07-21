from fastapi import APIRouter
from typing import List

from app.memes.dao import MemeDAO
from app.memes.schemas import SMemes, SNewMemes

router = APIRouter(
    prefix="/memes",
    tags=["Мемы"]
)

@router.get("")
async def get_memes() -> List[SMemes]:
    return await MemeDAO.find_all()

@router.get("/{meme_id}")
async def get_meme_by_id(meme_id: int) -> SMemes:
    return await MemeDAO.find_one_or_none(id=meme_id)

@router.post("")
async def add_meme(data: SNewMemes):
    return await MemeDAO.add(title=data.title, image_url=str(data.image_url), description=data.description, category=data.category)

@router.put("/{meme_id}")
async def update_meme(meme_id: int, data: SNewMemes):
    return await MemeDAO.update(meme_id, title=data.title, image_url=data.image_url, description=data.description, category=data.category)

@router.delete("/{meme_id}")
async def delete_meme(meme_id: int):
    return await MemeDAO.delete(id=meme_id)

