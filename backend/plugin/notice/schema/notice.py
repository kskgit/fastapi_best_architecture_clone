#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime

from pydantic import ConfigDict, Field

from backend.common.enums import StatusType
from backend.common.schema import SchemaBase


class NoticeSchemaBase(SchemaBase):
    """Notice announcement base model"""

    title: str = Field(description='Title')
    type: int = Field(description='Type (0: Notification, 1: Announcement)')
    author: str = Field(description='Author')
    source: str = Field(description='Source of information')
    status: StatusType = Field(StatusType.enable, description='Status (0: Hidden, 1: Displayed)')
    content: str = Field(description='Content')


class CreateNoticeParam(NoticeSchemaBase):
    """Create notice announcement parameters"""


class UpdateNoticeParam(NoticeSchemaBase):
    """Update notice announcement parameters"""


class GetNoticeDetail(NoticeSchemaBase):
    """Notice announcement details"""

    model_config = ConfigDict(from_attributes=True)

    id: int = Field(description='Notice announcement ID')
    created_time: datetime = Field(description='Creation time')
    updated_time: datetime | None = Field(None, description='Update time')
