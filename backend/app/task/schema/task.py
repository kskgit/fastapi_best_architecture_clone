#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Any

from pydantic import Field

from backend.common.schema import SchemaBase


class RunParam(SchemaBase):
    """任务运行参数"""

    name: str = Field(description='任务名称')
    args: list[Any] | None = Field(None, description='任务函数位置参数')
    kwargs: dict[str, Any] | None = Field(None, description='任务函数关键字参数')


class TaskResult(SchemaBase):
    """任务执行结果"""

    result: str = Field(description='任务执行结果')
    traceback: str = Field(description='错误堆栈信息')
    status: str = Field(description='任务状态')
    name: str = Field(description='任务名称')
    args: list[Any] | None = Field(None, description='任务函数位置参数')
    kwargs: dict[str, Any] | None = Field(None, description='任务函数关键字参数')
    worker: str = Field(description='执行任务的 worker')
    retries: int | None = Field(None, description='重试次数')
    queue: str | None = Field(None, description='任务队列')


class TodoCreate(SchemaBase):
    """TODO 作成"""

    title: str = Field(..., description='タイトル')
    description: str | None = Field(None, description='説明')
    due_date: datetime | None = Field(None, description='期日')
    priority: TodoPriority = Field(TodoPriority.medium, description='優先度')


class TodoUpdate(SchemaBase):
    """TODO 更新"""

    title: str | None = Field(None, description='タイトル')
    description: str | None = Field(None, description='説明')
    due_date: datetime | None = Field(None, description='期日')
    status: TodoStatus | None = Field(None, description='ステータス')
    priority: TodoPriority | None = Field(None, description='優先度')


class TodoRead(SchemaBase):
    """TODO 読取"""

    id: int = Field(..., description='ID')
    title: str = Field(..., description='タイトル')
    description: str | None = Field(None, description='説明')
    due_date: datetime | None = Field(None, description='期日')
    status: TodoStatus = Field(..., description='ステータス')
    priority: TodoPriority = Field(..., description='優先度')
