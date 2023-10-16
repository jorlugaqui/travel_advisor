from fastapi import APIRouter
from ..schemas import Advise


router = APIRouter(
    prefix="/travels",
    tags=["travels"],
)


@router.post("/")
async def ask_for_advise(advice: Advise):
    advice.instructions = ["Take the bus", "Take the train"]
    return {"advise": advice}
