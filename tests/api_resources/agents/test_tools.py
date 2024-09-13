# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from julep import Julep, AsyncJulep
from tests.utils import assert_matches_type
from julep.pagination import SyncOffsetPagination, AsyncOffsetPagination
from julep.types.agents import ToolListResponse
from julep.types.shared import ResourceCreated

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTools:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Julep) -> None:
        tool = client.agents.tools.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            function={},
            name="name",
        )
        assert_matches_type(ResourceCreated, tool, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Julep) -> None:
        tool = client.agents.tools.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            function={
                "description": "description",
                "name": {},
                "parameters": {},
            },
            name="name",
            api_call={},
            integration={},
            system={},
            type="function",
        )
        assert_matches_type(ResourceCreated, tool, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Julep) -> None:
        response = client.agents.tools.with_raw_response.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            function={},
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ResourceCreated, tool, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Julep) -> None:
        with client.agents.tools.with_streaming_response.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            function={},
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ResourceCreated, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Julep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.tools.with_raw_response.create(
                agent_id="",
                function={},
                name="name",
            )

    @parametrize
    def test_method_list(self, client: Julep) -> None:
        tool = client.agents.tools.list(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncOffsetPagination[ToolListResponse], tool, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Julep) -> None:
        tool = client.agents.tools.list(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            direction="asc",
            limit=0,
            offset=0,
            sort_by="created_at",
        )
        assert_matches_type(SyncOffsetPagination[ToolListResponse], tool, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Julep) -> None:
        response = client.agents.tools.with_raw_response.list(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(SyncOffsetPagination[ToolListResponse], tool, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Julep) -> None:
        with client.agents.tools.with_streaming_response.list(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(SyncOffsetPagination[ToolListResponse], tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Julep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.tools.with_raw_response.list(
                agent_id="",
            )


class TestAsyncTools:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncJulep) -> None:
        tool = await async_client.agents.tools.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            function={},
            name="name",
        )
        assert_matches_type(ResourceCreated, tool, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncJulep) -> None:
        tool = await async_client.agents.tools.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            function={
                "description": "description",
                "name": {},
                "parameters": {},
            },
            name="name",
            api_call={},
            integration={},
            system={},
            type="function",
        )
        assert_matches_type(ResourceCreated, tool, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncJulep) -> None:
        response = await async_client.agents.tools.with_raw_response.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            function={},
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ResourceCreated, tool, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncJulep) -> None:
        async with async_client.agents.tools.with_streaming_response.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            function={},
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ResourceCreated, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncJulep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.tools.with_raw_response.create(
                agent_id="",
                function={},
                name="name",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncJulep) -> None:
        tool = await async_client.agents.tools.list(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncOffsetPagination[ToolListResponse], tool, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncJulep) -> None:
        tool = await async_client.agents.tools.list(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            direction="asc",
            limit=0,
            offset=0,
            sort_by="created_at",
        )
        assert_matches_type(AsyncOffsetPagination[ToolListResponse], tool, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncJulep) -> None:
        response = await async_client.agents.tools.with_raw_response.list(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(AsyncOffsetPagination[ToolListResponse], tool, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncJulep) -> None:
        async with async_client.agents.tools.with_streaming_response.list(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(AsyncOffsetPagination[ToolListResponse], tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncJulep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.tools.with_raw_response.list(
                agent_id="",
            )
