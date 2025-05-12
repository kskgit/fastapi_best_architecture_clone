#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Annotated

from fastapi import APIRouter, Depends, Request, Response
from fastapi.security import HTTPBasicCredentials
from fastapi_limiter.depends import RateLimiter
from starlette.background import BackgroundTasks

from backend.app.admin.schema.token import GetLoginToken, GetNewToken, GetSwaggerToken
from backend.app.admin.schema.user import AuthLoginParam
from backend.app.admin.service.auth_service import auth_service
from backend.common.response.response_code import CustomResponseCode
from backend.common.response.response_schema import ResponseModel, ResponseSchemaModel, response_base
from backend.common.security.jwt import DependsJwtAuth

router = APIRouter()


@router.post('/login/swagger', summary='Swagger debug only', description='Used to quickly obtain a token for Swagger authentication')
async def swagger_login(obj: Annotated[HTTPBasicCredentials, Depends()]) -> GetSwaggerToken:
    token, user = await auth_service.swagger_login(obj=obj)
    return GetSwaggerToken(access_token=token, user=user)  # type: ignore


@router.post(
    '/login',
    summary='User login',
    description='JSON format login, only supports debugging in third-party API tools, such as: Postman',
    dependencies=[Depends(RateLimiter(times=5, minutes=1))],
)
async def user_login(
    request: Request, response: Response, obj: AuthLoginParam, background_tasks: BackgroundTasks
) -> ResponseSchemaModel[GetLoginToken]:
    data = await auth_service.login(request=request, response=response, obj=obj, background_tasks=background_tasks)
    return response_base.success(data=data, schema=GetLoginToken)


@router.post('/token/new', summary='Create new token')
async def create_new_token(request: Request) -> ResponseSchemaModel[GetNewToken]:
    data = await auth_service.new_token(request=request)
    return response_base.success(data=data, schema=GetNewToken)


@router.post('/logout', summary='User logout', dependencies=[DependsJwtAuth])
async def user_logout(request: Request, response: Response) -> ResponseModel:
    await auth_service.logout(request=request, response=response)
    return response_base.success()
