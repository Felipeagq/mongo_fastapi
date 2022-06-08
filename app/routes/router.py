from fastapi import APIRouter,status,Request,Body,Response
from app.schemas import schemas
from app.services import mongo_crud



router = APIRouter()


@router.get("/")
async def read_all():
    query = await mongo_crud.read_all()
    return schemas.usersEntity(query)



@router.post(
    "/",
    status_code= status.HTTP_201_CREATED,
    summary="Create a user"
)
async def create(
    request: Request,
    user: schemas.UserSchema = Body(...)
):
    r = await mongo_crud.create(user)
    return Response(
        status_code= status.HTTP_201_CREATED,
        content="ok"
    )