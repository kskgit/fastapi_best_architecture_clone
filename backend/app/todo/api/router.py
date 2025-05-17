#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from backend.app.todo.api.v1.todo import router as todo_router
from backend.core.conf import settings
from fastapi import APIRouter

v1 = APIRouter(prefix=settings.FASTAPI_API_V1_PATH)

v1.include_router(todo_router, prefix='/todos', tags=['TODO'])
