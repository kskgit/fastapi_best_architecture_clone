#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime

from pydantic import ConfigDict, Field

from backend.common.enums import StatusType
from backend.common.schema import SchemaBase


class DictTypeSchemaBase(SchemaBase):
    """Dictionary type base model"""

    name: str = Field(description='Dictionary name')
    code: str = Field(description='Dictionary code')
    status: StatusType = Field(StatusType.enable, description='Status')
    remark: str | None = Field(None, description='Remark')


class CreateDictTypeParam(DictTypeSchemaBase):
    """Create dictionary type parameters"""


class UpdateDictTypeParam(DictTypeSchemaBase):
    """Update dictionary type parameters"""


class GetDictTypeDetail(DictTypeSchemaBase):
    """Dictionary type details"""

    model_config = ConfigDict(from_attributes=True)

    id: int = Field(description='Dictionary type ID')
    created_time: datetime = Field(description='Creation time')
    updated_time: datetime | None = Field(None, description='Update time')
