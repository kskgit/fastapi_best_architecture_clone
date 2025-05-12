#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Sequence

from backend.common.exception import errors
from backend.database.db import async_db_session
from backend.plugin.code_generator.crud.crud_column import gen_model_dao
from backend.plugin.code_generator.enums import GenModelMySQLColumnType
from backend.plugin.code_generator.model import GenColumn
from backend.plugin.code_generator.schema.column import CreateGenModelParam, UpdateGenModelParam
from backend.plugin.code_generator.utils.type_conversion import sql_type_to_pydantic


class GenModelService:
    """Code generation model service class"""

    @staticmethod
    async def get(*, pk: int) -> GenColumn:
        """
        Get the model with the specified ID

        :param pk: Model ID
        :return:
        """
        async with async_db_session() as db:
            model = await gen_model_dao.get(db, pk)
            if not model:
                raise errors.NotFoundError(msg='Code generation model does not exist')
            return model

    @staticmethod
    async def get_types() -> list[str]:
        """Get all MySQL column types"""
        types = GenModelMySQLColumnType.get_member_keys()
        types.sort()
        return types

    @staticmethod
    async def get_by_business(*, business_id: int) -> Sequence[GenColumn]:
        """
        Get all models for the specified business

        :param business_id: Business ID
        :return:
        """
        async with async_db_session() as db:
            return await gen_model_dao.get_all_by_business(db, business_id)

    @staticmethod
    async def create(*, obj: CreateGenModelParam) -> None:
        """
        Create model

        :param obj: Model creation parameters
        :return:
        """
        async with async_db_session.begin() as db:
            gen_models = await gen_model_dao.get_all_by_business(db, obj.gen_business_id)
            if obj.name in [gen_model.name for gen_model in gen_models]:
                raise errors.ForbiddenError(msg='Prohibit adding the same column to the same model table')

            pd_type = sql_type_to_pydantic(obj.type)
            await gen_model_dao.create(db, obj, pd_type=pd_type)

    @staticmethod
    async def update(*, pk: int, obj: UpdateGenModelParam) -> int:
        """
        Update model

        :param pk: Model ID
        :param obj: Model update parameters
        :return:
        """
        async with async_db_session.begin() as db:
            model = await gen_model_dao.get(db, pk)
            if obj.name != model.name:
                gen_models = await gen_model_dao.get_all_by_business(db, obj.gen_business_id)
                if obj.name in [gen_model.name for gen_model in gen_models]:
                    raise errors.ForbiddenError(msg='Model column name already exists')

            pd_type = sql_type_to_pydantic(obj.type)
            return await gen_model_dao.update(db, pk, obj, pd_type=pd_type)

    @staticmethod
    async def delete(*, pk: int) -> int:
        """
        Delete model

        :param pk: Model ID
        :return:
        """
        async with async_db_session.begin() as db:
            return await gen_model_dao.delete(db, pk)


gen_model_service: GenModelService = GenModelService()
