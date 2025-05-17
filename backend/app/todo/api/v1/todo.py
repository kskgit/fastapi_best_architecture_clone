from backend.app.todo.schema.todo import TodoCreateParam
from backend.app.todo.service.todo_service import todo_service
from backend.common.response.response_schema import ResponseSchemaModel
from fastapi import APIRouter

router = APIRouter()


@router.post('', summary='Create todo')
async def create_todo(obj: TodoCreateParam) -> ResponseSchemaModel[None]:
    await todo_service.create(obj=obj)
    return ResponseSchemaModel[None](code=200, msg='Success', data=None)
