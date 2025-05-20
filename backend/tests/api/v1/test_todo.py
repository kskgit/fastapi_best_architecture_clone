import pytest

from backend.app.todo.schema.todo import TodoPriority, TodoStatus
from httpx import AsyncClient

pytestmark = pytest.mark.asyncio


async def test_create_todo_validation_error_missing_title(async_client: AsyncClient):
    """Todo作成時のバリデーションエラーテスト - titleが欠けている場合"""

    # テストケース: 必須フィールド（title）が欠けている
    invalid_data = {
        'description': 'テスト用の説明',
        'priority': TodoPriority.medium.value,
        'status': TodoStatus.pending.value,
    }

    response = await async_client.post('/api/v1/todo', json=invalid_data)
    assert response.status_code == 422
    error_detail = response.json()
    assert 'detail' in error_detail
    assert any(error['loc'] == ['body', 'title'] for error in error_detail['detail'])
