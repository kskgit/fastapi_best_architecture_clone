from backend.app.todo.model.todo import Todo
from backend.app.todo.schema.todo import TodoCreateParam
from sqlalchemy.ext.asyncio import AsyncSession


class CRUDTodo:
    @staticmethod
    async def create(db: AsyncSession, param: TodoCreateParam) -> None:
        todo = Todo(
            title=param.title,
            description=param.description,
            due_date=param.due_date,
            priority=param.priority,
            status=param.status,
        )
        db.add(todo)


crud_todo: CRUDTodo = CRUDTodo()
