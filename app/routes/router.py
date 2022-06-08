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
    return user






@router.put(
    "/{id}",
    status_code= status.HTTP_202_ACCEPTED,
    summary="Update a user"
)
async def update(
    id:str,
    user:schemas.UserSchema
):
    r = await mongo_crud.update(id,user)
    return Response(
        status_code= status.HTTP_201_CREATED,
        content=id
    )
    
    
    
@router.delete(
    "/{id}",
    status_code= status.HTTP_202_ACCEPTED,
    summary="Update a user"
)
async def delete(
    id:str
):
    r = await mongo_crud.delete(id)
    print(r)
    if not r:
        return Response(
            status_code= status.HTTP_201_CREATED,
            content="Dont exist"
        )
    return Response(
        status_code= status.HTTP_201_CREATED,
        content="Dont exist"
    )