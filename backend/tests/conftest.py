from typing import AsyncGenerator

import pytest

from backend.main import app
from httpx import AsyncClient


@pytest.fixture
async def async_client() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(base_url='http://test', app=app) as client:
        yield client
