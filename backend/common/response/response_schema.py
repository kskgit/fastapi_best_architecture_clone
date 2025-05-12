#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Any, Generic, TypeVar

from fastapi import Response
from pydantic import BaseModel, Field

from backend.common.response.response_code import CustomResponse, CustomResponseCode
from backend.utils.serializers import MsgSpecJSONResponse

SchemaT = TypeVar('SchemaT')


class ResponseModel(BaseModel):
    """
    Generic unified return model without a return data schema

    Example::

        @router.get('/test', response_model=ResponseModel)
        def test():
            return ResponseModel(data={'test': 'test'})


        @router.get('/test')
        def test() -> ResponseModel:
            return ResponseModel(data={'test': 'test'})


        @router.get('/test')
        def test() -> ResponseModel:
            res = CustomResponseCode.HTTP_200
            return ResponseModel(code=res.code, msg=res.msg, data={'test': 'test'})
    """

    code: int = Field(CustomResponseCode.HTTP_200.code, description='Return status code')
    msg: str = Field(CustomResponseCode.HTTP_200.msg, description='Return information')
    data: Any | None = Field(None, description='Return data')


class ResponseSchemaModel(ResponseModel, Generic[SchemaT]):
    """
    Generic unified return model containing a return data schema

    Example::

        @router.get('/test', response_model=ResponseSchemaModel[GetApiDetail])
        def test():
            return ResponseSchemaModel[GetApiDetail](data=GetApiDetail(...))


        @router.get('/test')
        def test() -> ResponseSchemaModel[GetApiDetail]:
            return ResponseSchemaModel[GetApiDetail](data=GetApiDetail(...))


        @router.get('/test')
        def test() -> ResponseSchemaModel[GetApiDetail]:
            res = CustomResponseCode.HTTP_200
            return ResponseSchemaModel[GetApiDetail](code=res.code, msg=res.msg, data=GetApiDetail(...))
    """

    data: SchemaT


class ResponseBase:
    """Unified return method"""

    @staticmethod
    def __response(
        *,
        res: CustomResponseCode | CustomResponse,
        data: Any | None,
    ) -> ResponseModel | ResponseSchemaModel:
        """
        Common method for request return

        :param res: Return information
        :param data: Return data
        :return:
        """
        if isinstance(res, CustomResponseCode):
            return ResponseModel(code=res.code, msg=res.msg, data=data)
        else:
            return ResponseModel(code=res.code, msg=res.msg, data=data)

    def success(
        self,
        *,
        res: CustomResponseCode | CustomResponse = CustomResponseCode.HTTP_200,
        data: Any | None = None,
        schema: Any = None,
    ) -> ResponseModel | ResponseSchemaModel:
        """
        Successful response

        :param res: Return information
        :param data: Return data
        :param schema: Return data model
        :return:
        """
        if schema:
            return ResponseSchemaModel[schema](code=res.code, msg=res.msg, data=data)
        return ResponseModel(code=res.code, msg=res.msg, data=data)

    def fail(
        self,
        *,
        res: CustomResponseCode | CustomResponse = CustomResponseCode.HTTP_400,
        data: Any = None,
    ) -> ResponseModel | ResponseSchemaModel:
        """
        Failed response

        :param res: Return information
        :param data: Return data
        :return:
        """
        return self.__response(res=res, data=data)

    @staticmethod
    def fast_success(
        *,
        res: CustomResponseCode | CustomResponse = CustomResponseCode.HTTP_200,
        data: Any | None = None,
    ) -> Response:
        """
        This method was created to improve the interface response speed, and has significant performance improvements when parsing large json, but will lose pydantic parsing and validation

        .. warning::

            When using this return method, you cannot specify the interface parameters response_model and arrow return type

        :param res: Return information
        :param data: Return data
        :return:
        """
        return MsgSpecJSONResponse({'code': res.code, 'msg': res.msg, 'data': data})


response_base: ResponseBase = ResponseBase()
