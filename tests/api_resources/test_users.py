# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from julep import Julep, AsyncJulep
from julep.types import User
from tests.utils import assert_matches_type
from julep.pagination import SyncOffsetPagination, AsyncOffsetPagination
from julep.types.shared import ResourceCreated

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Julep) -> None:
        user = client.users.create()
        assert_matches_type(ResourceCreated, user, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Julep) -> None:
        user = client.users.create(
            about="about",
            metadata={},
            name="name",
        )
        assert_matches_type(ResourceCreated, user, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Julep) -> None:
        response = client.users.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(ResourceCreated, user, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Julep) -> None:
        with client.users.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(ResourceCreated, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Julep) -> None:
        user = client.users.list()
        assert_matches_type(SyncOffsetPagination[User], user, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Julep) -> None:
        user = client.users.list(
            direction="asc",
            limit=0,
            metadata_filter="metadata_filter",
            offset=0,
            sort_by="created_at",
        )
        assert_matches_type(SyncOffsetPagination[User], user, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Julep) -> None:
        response = client.users.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(SyncOffsetPagination[User], user, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Julep) -> None:
        with client.users.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(SyncOffsetPagination[User], user, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUsers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncJulep) -> None:
        user = await async_client.users.create()
        assert_matches_type(ResourceCreated, user, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncJulep) -> None:
        user = await async_client.users.create(
            about="about",
            metadata={},
            name="name",
        )
        assert_matches_type(ResourceCreated, user, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncJulep) -> None:
        response = await async_client.users.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(ResourceCreated, user, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncJulep) -> None:
        async with async_client.users.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(ResourceCreated, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncJulep) -> None:
        user = await async_client.users.list()
        assert_matches_type(AsyncOffsetPagination[User], user, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncJulep) -> None:
        user = await async_client.users.list(
            direction="asc",
            limit=0,
            metadata_filter="metadata_filter",
            offset=0,
            sort_by="created_at",
        )
        assert_matches_type(AsyncOffsetPagination[User], user, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncJulep) -> None:
        response = await async_client.users.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(AsyncOffsetPagination[User], user, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncJulep) -> None:
        async with async_client.users.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(AsyncOffsetPagination[User], user, path=["response"])

        assert cast(Any, response.is_closed) is True
