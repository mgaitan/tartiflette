from unittest.mock import Mock

import pytest
import pytest_asyncio

@pytest.mark.asyncio
async def test_non_introspectable_introspection():
    from tartiflette.directive.builtins.non_introspectable import (
        NonIntrospectableDirective,
    )

    assert (
        await NonIntrospectableDirective().on_introspection(
            Mock(), Mock(), Mock(), Mock(), Mock()
        )
        is None
    )
