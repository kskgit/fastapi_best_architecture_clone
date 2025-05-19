from backend.app.todo.schema.todo import TodoCreateParam
from backend.app.todo.service.todo_service import todo_service
from backend.common.response.response_schema import ResponseModel, response_base
from fastapi import APIRouter

router = APIRouter()


@router.post('', summary='Create todo')
async def create_todo(obj: TodoCreateParam) -> ResponseModel:
    await todo_service.create(obj=obj)
    return response_base.success(schema=None)
