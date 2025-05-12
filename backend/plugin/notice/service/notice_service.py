#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Sequence

from sqlalchemy import Select

from backend.common.exception import errors
from backend.database.db import async_db_session
from backend.plugin.notice.crud.crud_notice import notice_dao
from backend.plugin.notice.model import Notice
from backend.plugin.notice.schema.notice import CreateNoticeParam, UpdateNoticeParam


class NoticeService:
    """Notice announcement service class"""

    @staticmethod
    async def get(*, pk: int) -> Notice:
        """
        Get notice announcement

        :param pk: Notice announcement ID
        :return:
        """
        async with async_db_session() as db:
            notice = await notice_dao.get(db, pk)
            if not notice:
                raise errors.NotFoundError(msg='Notice announcement does not exist')
            return notice

    @staticmethod
    async def get_select() -> Select:
        """Get notice announcement query object"""
        return await notice_dao.get_list()

    @staticmethod
    async def get_all() -> Sequence[Notice]:
        """Get all notice announcement"""
        async with async_db_session() as db:
            notices = await notice_dao.get_all(db)
            return notices

    @staticmethod
    async def create(*, obj: CreateNoticeParam) -> None:
        """
        Create notice announcement

        :param obj: Create notice announcement parameters
        :return:
        """
        async with async_db_session.begin() as db:
            await notice_dao.create(db, obj)

    @staticmethod
    async def update(*, pk: int, obj: UpdateNoticeParam) -> int:
        """
        Update notice announcement

        :param pk: Notice announcement ID
        :param obj: Update notice announcement parameters
        :return:
        """
        async with async_db_session.begin() as db:
            notice = await notice_dao.get(db, pk)
            if not notice:
                raise errors.NotFoundError(msg='Notice announcement does not exist')
            count = await notice_dao.update(db, pk, obj)
            return count

    @staticmethod
    async def delete(*, pk: list[int]) -> int:
        """
        Delete notice announcement

        :param pk: Notice announcement ID list
        :return:
        """
        async with async_db_session.begin() as db:
            count = await notice_dao.delete(db, pk)
            return count


notice_service: NoticeService = NoticeService()
