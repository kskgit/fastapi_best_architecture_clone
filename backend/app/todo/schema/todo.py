from datetime import datetime
from enum import Enum

from backend.common.schema import SchemaBase
from pydantic import Field


class TodoPriority(str, Enum):
    """TODO 優先度"""

    high = 'high'
    medium = 'medium'
    low = 'low'


class TodoStatus(str, Enum):
    """TODO ステータス"""

    pending = 'pending'
    in_progress = 'in_progress'
    completed = 'completed'
    canceled = 'canceled'


class TodoSchemaBase(SchemaBase):
    """ベースパラメータ"""

    title: str = Field(..., description='タイトル')
    description: str | None = Field(None, description='説明')
    due_date: datetime | None = Field(None, description='期日')
    priority: TodoPriority = Field(TodoPriority.medium, description='優先度')
    status: TodoStatus = Field(TodoStatus.pending, description='ステータス')


class TodoCreateParam(TodoSchemaBase):
    """Todo作成パラメータ"""
