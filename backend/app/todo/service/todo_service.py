from backend.app.todo.crud.crud_todo import crud_todo
from backend.app.todo.schema.todo import TodoCreateParam
from backend.database.db import async_db_session


class TodoService:
    @staticmethod
    async def create(*, obj: TodoCreateParam) -> None:
        """
        Todoを作成する

        :param obj: Todo作成パラメータ
        :return:
        """
        async with async_db_session.begin() as db:
            await crud_todo.create(db, obj)


todo_service: TodoService = TodoService()
