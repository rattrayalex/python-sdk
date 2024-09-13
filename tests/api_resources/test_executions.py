# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from julep import Julep, AsyncJulep
from julep.types import Execution
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExecutions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update_overload_1(self, client: Julep) -> None:
        execution = client.executions.update(
            execution_id="execution_id",
        )
        assert_matches_type(object, execution, path=["response"])

    @parametrize
    def test_method_update_with_all_params_overload_1(self, client: Julep) -> None:
        execution = client.executions.update(
            execution_id="execution_id",
            input={},
            status="running",
        )
        assert_matches_type(object, execution, path=["response"])

    @parametrize
    def test_raw_response_update_overload_1(self, client: Julep) -> None:
        response = client.executions.with_raw_response.update(
            execution_id="execution_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execution = response.parse()
        assert_matches_type(object, execution, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_1(self, client: Julep) -> None:
        with client.executions.with_streaming_response.update(
            execution_id="execution_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execution = response.parse()
            assert_matches_type(object, execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_overload_1(self, client: Julep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `execution_id` but received ''"):
            client.executions.with_raw_response.update(
                execution_id="",
            )

    @parametrize
    def test_method_update_overload_2(self, client: Julep) -> None:
        execution = client.executions.update(
            execution_id="execution_id",
        )
        assert_matches_type(object, execution, path=["response"])

    @parametrize
    def test_method_update_with_all_params_overload_2(self, client: Julep) -> None:
        execution = client.executions.update(
            execution_id="execution_id",
            reason="reason",
            status="cancelled",
        )
        assert_matches_type(object, execution, path=["response"])

    @parametrize
    def test_raw_response_update_overload_2(self, client: Julep) -> None:
        response = client.executions.with_raw_response.update(
            execution_id="execution_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execution = response.parse()
        assert_matches_type(object, execution, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_2(self, client: Julep) -> None:
        with client.executions.with_streaming_response.update(
            execution_id="execution_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execution = response.parse()
            assert_matches_type(object, execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_overload_2(self, client: Julep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `execution_id` but received ''"):
            client.executions.with_raw_response.update(
                execution_id="",
            )

    @parametrize
    def test_method_get(self, client: Julep) -> None:
        execution = client.executions.get(
            "execution_id",
        )
        assert_matches_type(Execution, execution, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Julep) -> None:
        response = client.executions.with_raw_response.get(
            "execution_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execution = response.parse()
        assert_matches_type(Execution, execution, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Julep) -> None:
        with client.executions.with_streaming_response.get(
            "execution_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execution = response.parse()
            assert_matches_type(Execution, execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Julep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `execution_id` but received ''"):
            client.executions.with_raw_response.get(
                "",
            )


class TestAsyncExecutions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update_overload_1(self, async_client: AsyncJulep) -> None:
        execution = await async_client.executions.update(
            execution_id="execution_id",
        )
        assert_matches_type(object, execution, path=["response"])

    @parametrize
    async def test_method_update_with_all_params_overload_1(self, async_client: AsyncJulep) -> None:
        execution = await async_client.executions.update(
            execution_id="execution_id",
            input={},
            status="running",
        )
        assert_matches_type(object, execution, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_1(self, async_client: AsyncJulep) -> None:
        response = await async_client.executions.with_raw_response.update(
            execution_id="execution_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execution = await response.parse()
        assert_matches_type(object, execution, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_1(self, async_client: AsyncJulep) -> None:
        async with async_client.executions.with_streaming_response.update(
            execution_id="execution_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execution = await response.parse()
            assert_matches_type(object, execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_overload_1(self, async_client: AsyncJulep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `execution_id` but received ''"):
            await async_client.executions.with_raw_response.update(
                execution_id="",
            )

    @parametrize
    async def test_method_update_overload_2(self, async_client: AsyncJulep) -> None:
        execution = await async_client.executions.update(
            execution_id="execution_id",
        )
        assert_matches_type(object, execution, path=["response"])

    @parametrize
    async def test_method_update_with_all_params_overload_2(self, async_client: AsyncJulep) -> None:
        execution = await async_client.executions.update(
            execution_id="execution_id",
            reason="reason",
            status="cancelled",
        )
        assert_matches_type(object, execution, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_2(self, async_client: AsyncJulep) -> None:
        response = await async_client.executions.with_raw_response.update(
            execution_id="execution_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execution = await response.parse()
        assert_matches_type(object, execution, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_2(self, async_client: AsyncJulep) -> None:
        async with async_client.executions.with_streaming_response.update(
            execution_id="execution_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execution = await response.parse()
            assert_matches_type(object, execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_overload_2(self, async_client: AsyncJulep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `execution_id` but received ''"):
            await async_client.executions.with_raw_response.update(
                execution_id="",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncJulep) -> None:
        execution = await async_client.executions.get(
            "execution_id",
        )
        assert_matches_type(Execution, execution, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncJulep) -> None:
        response = await async_client.executions.with_raw_response.get(
            "execution_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execution = await response.parse()
        assert_matches_type(Execution, execution, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncJulep) -> None:
        async with async_client.executions.with_streaming_response.get(
            "execution_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execution = await response.parse()
            assert_matches_type(Execution, execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncJulep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `execution_id` but received ''"):
            await async_client.executions.with_raw_response.get(
                "",
            )
