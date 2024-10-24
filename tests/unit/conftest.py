import pytest
import pytest_asyncio
from tartiflette.schema.registry import SchemaRegistry


@pytest.fixture
def clean_registry():
    SchemaRegistry.clean()
    yield SchemaRegistry
    SchemaRegistry.clean()
