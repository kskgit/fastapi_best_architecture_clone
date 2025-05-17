#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime

from sqlalchemy import DateTime, String
from sqlalchemy.orm import Mapped, mapped_column, declared_attr

from backend.common.model import Base, id_key
from backend.app.todo.schema.todo import TodoStatus, TodoPriority
from backend.utils.timezone import timezone


class Todo(Base):
    """TODO"""

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return 'todo'

    id: Mapped[id_key] = mapped_column(init=False)
    title: Mapped[str] = mapped_column(String(100), index=True, comment='タイトル')
    description: Mapped[str | None] = mapped_column(
        String(500), nullable=True, default=None, comment='説明'
    )
    due_date: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), nullable=True, default=None, comment='期日'
    )
    status: Mapped[TodoStatus] = mapped_column(
        default=TodoStatus.pending, index=True, comment='ステータス'
    )
    priority: Mapped[TodoPriority] = mapped_column(
        default=TodoPriority.medium, comment='優先度'
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), init=False, default_factory=timezone.now, comment='作成日時'
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), init=False, onupdate=timezone.now, comment='更新日時'
    )