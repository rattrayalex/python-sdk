# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from julep import Julep, AsyncJulep
from julep.types import (
    User,
    UserListResponse,
    UserCreateResponse,
    UserDeleteResponse,
    UserSearchResponse,
    UserUpdateResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Julep) -> None:
        user = client.users.create()
        assert_matches_type(UserCreateResponse, user, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Julep) -> None:
        user = client.users.create(
            about="about",
            metadata={},
            name="name",
        )
        assert_matches_type(UserCreateResponse, user, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Julep) -> None:
        response = client.users.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserCreateResponse, user, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Julep) -> None:
        with client.users.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserCreateResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Julep) -> None:
        user = client.users.retrieve(
            "user_id",
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Julep) -> None:
        response = client.users.with_raw_response.retrieve(
            "user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(User, user, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Julep) -> None:
        with client.users.with_streaming_response.retrieve(
            "user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Julep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Julep) -> None:
        user = client.users.update(
            user_id="user_id",
        )
        assert_matches_type(UserUpdateResponse, user, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Julep) -> None:
        user = client.users.update(
            user_id="user_id",
            about="about",
            metadata={},
            name="name",
        )
        assert_matches_type(UserUpdateResponse, user, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Julep) -> None:
        response = client.users.with_raw_response.update(
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserUpdateResponse, user, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Julep) -> None:
        with client.users.with_streaming_response.update(
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserUpdateResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Julep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.with_raw_response.update(
                user_id="",
            )

    @parametrize
    def test_method_list(self, client: Julep) -> None:
        user = client.users.list()
        assert_matches_type(UserListResponse, user, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Julep) -> None:
        user = client.users.list(
            direction="asc",
            limit=0,
            metadata_filter="metadata_filter",
            offset=0,
            sort_by="created_at",
        )
        assert_matches_type(UserListResponse, user, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Julep) -> None:
        response = client.users.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserListResponse, user, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Julep) -> None:
        with client.users.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserListResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Julep) -> None:
        user = client.users.delete(
            "user_id",
        )
        assert_matches_type(UserDeleteResponse, user, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Julep) -> None:
        response = client.users.with_raw_response.delete(
            "user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserDeleteResponse, user, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Julep) -> None:
        with client.users.with_streaming_response.delete(
            "user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserDeleteResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Julep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_search_overload_1(self, client: Julep) -> None:
        user = client.users.search(
            user_id="user_id",
            text="text",
        )
        assert_matches_type(UserSearchResponse, user, path=["response"])

    @parametrize
    def test_method_search_with_all_params_overload_1(self, client: Julep) -> None:
        user = client.users.search(
            user_id="user_id",
            text="text",
            lang="en-US",
            limit=1,
        )
        assert_matches_type(UserSearchResponse, user, path=["response"])

    @parametrize
    def test_raw_response_search_overload_1(self, client: Julep) -> None:
        response = client.users.with_raw_response.search(
            user_id="user_id",
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserSearchResponse, user, path=["response"])

    @parametrize
    def test_streaming_response_search_overload_1(self, client: Julep) -> None:
        with client.users.with_streaming_response.search(
            user_id="user_id",
            text="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserSearchResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_search_overload_1(self, client: Julep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.with_raw_response.search(
                user_id="",
                text="text",
            )

    @parametrize
    def test_method_search_overload_2(self, client: Julep) -> None:
        user = client.users.search(
            user_id="user_id",
            vector=[0, 0, 0],
        )
        assert_matches_type(UserSearchResponse, user, path=["response"])

    @parametrize
    def test_method_search_with_all_params_overload_2(self, client: Julep) -> None:
        user = client.users.search(
            user_id="user_id",
            vector=[0, 0, 0],
            confidence=0,
            lang="en-US",
            limit=1,
        )
        assert_matches_type(UserSearchResponse, user, path=["response"])

    @parametrize
    def test_raw_response_search_overload_2(self, client: Julep) -> None:
        response = client.users.with_raw_response.search(
            user_id="user_id",
            vector=[0, 0, 0],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserSearchResponse, user, path=["response"])

    @parametrize
    def test_streaming_response_search_overload_2(self, client: Julep) -> None:
        with client.users.with_streaming_response.search(
            user_id="user_id",
            vector=[0, 0, 0],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserSearchResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_search_overload_2(self, client: Julep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.with_raw_response.search(
                user_id="",
                vector=[0, 0, 0],
            )

    @parametrize
    def test_method_search_overload_3(self, client: Julep) -> None:
        user = client.users.search(
            user_id="user_id",
            text="text",
            vector=[0, 0, 0],
        )
        assert_matches_type(UserSearchResponse, user, path=["response"])

    @parametrize
    def test_method_search_with_all_params_overload_3(self, client: Julep) -> None:
        user = client.users.search(
            user_id="user_id",
            text="text",
            vector=[0, 0, 0],
            alpha=0,
            confidence=0,
            lang="en-US",
            limit=1,
        )
        assert_matches_type(UserSearchResponse, user, path=["response"])

    @parametrize
    def test_raw_response_search_overload_3(self, client: Julep) -> None:
        response = client.users.with_raw_response.search(
            user_id="user_id",
            text="text",
            vector=[0, 0, 0],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserSearchResponse, user, path=["response"])

    @parametrize
    def test_streaming_response_search_overload_3(self, client: Julep) -> None:
        with client.users.with_streaming_response.search(
            user_id="user_id",
            text="text",
            vector=[0, 0, 0],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserSearchResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_search_overload_3(self, client: Julep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.with_raw_response.search(
                user_id="",
                text="text",
                vector=[0, 0, 0],
            )


class TestAsyncUsers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncJulep) -> None:
        user = await async_client.users.create()
        assert_matches_type(UserCreateResponse, user, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncJulep) -> None:
        user = await async_client.users.create(
            about="about",
            metadata={},
            name="name",
        )
        assert_matches_type(UserCreateResponse, user, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncJulep) -> None:
        response = await async_client.users.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserCreateResponse, user, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncJulep) -> None:
        async with async_client.users.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserCreateResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncJulep) -> None:
        user = await async_client.users.retrieve(
            "user_id",
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncJulep) -> None:
        response = await async_client.users.with_raw_response.retrieve(
            "user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(User, user, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncJulep) -> None:
        async with async_client.users.with_streaming_response.retrieve(
            "user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncJulep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncJulep) -> None:
        user = await async_client.users.update(
            user_id="user_id",
        )
        assert_matches_type(UserUpdateResponse, user, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncJulep) -> None:
        user = await async_client.users.update(
            user_id="user_id",
            about="about",
            metadata={},
            name="name",
        )
        assert_matches_type(UserUpdateResponse, user, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncJulep) -> None:
        response = await async_client.users.with_raw_response.update(
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserUpdateResponse, user, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncJulep) -> None:
        async with async_client.users.with_streaming_response.update(
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserUpdateResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncJulep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.with_raw_response.update(
                user_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncJulep) -> None:
        user = await async_client.users.list()
        assert_matches_type(UserListResponse, user, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncJulep) -> None:
        user = await async_client.users.list(
            direction="asc",
            limit=0,
            metadata_filter="metadata_filter",
            offset=0,
            sort_by="created_at",
        )
        assert_matches_type(UserListResponse, user, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncJulep) -> None:
        response = await async_client.users.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserListResponse, user, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncJulep) -> None:
        async with async_client.users.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserListResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncJulep) -> None:
        user = await async_client.users.delete(
            "user_id",
        )
        assert_matches_type(UserDeleteResponse, user, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncJulep) -> None:
        response = await async_client.users.with_raw_response.delete(
            "user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserDeleteResponse, user, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncJulep) -> None:
        async with async_client.users.with_streaming_response.delete(
            "user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserDeleteResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncJulep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_search_overload_1(self, async_client: AsyncJulep) -> None:
        user = await async_client.users.search(
            user_id="user_id",
            text="text",
        )
        assert_matches_type(UserSearchResponse, user, path=["response"])

    @parametrize
    async def test_method_search_with_all_params_overload_1(self, async_client: AsyncJulep) -> None:
        user = await async_client.users.search(
            user_id="user_id",
            text="text",
            lang="en-US",
            limit=1,
        )
        assert_matches_type(UserSearchResponse, user, path=["response"])

    @parametrize
    async def test_raw_response_search_overload_1(self, async_client: AsyncJulep) -> None:
        response = await async_client.users.with_raw_response.search(
            user_id="user_id",
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserSearchResponse, user, path=["response"])

    @parametrize
    async def test_streaming_response_search_overload_1(self, async_client: AsyncJulep) -> None:
        async with async_client.users.with_streaming_response.search(
            user_id="user_id",
            text="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserSearchResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_search_overload_1(self, async_client: AsyncJulep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.with_raw_response.search(
                user_id="",
                text="text",
            )

    @parametrize
    async def test_method_search_overload_2(self, async_client: AsyncJulep) -> None:
        user = await async_client.users.search(
            user_id="user_id",
            vector=[0, 0, 0],
        )
        assert_matches_type(UserSearchResponse, user, path=["response"])

    @parametrize
    async def test_method_search_with_all_params_overload_2(self, async_client: AsyncJulep) -> None:
        user = await async_client.users.search(
            user_id="user_id",
            vector=[0, 0, 0],
            confidence=0,
            lang="en-US",
            limit=1,
        )
        assert_matches_type(UserSearchResponse, user, path=["response"])

    @parametrize
    async def test_raw_response_search_overload_2(self, async_client: AsyncJulep) -> None:
        response = await async_client.users.with_raw_response.search(
            user_id="user_id",
            vector=[0, 0, 0],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserSearchResponse, user, path=["response"])

    @parametrize
    async def test_streaming_response_search_overload_2(self, async_client: AsyncJulep) -> None:
        async with async_client.users.with_streaming_response.search(
            user_id="user_id",
            vector=[0, 0, 0],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserSearchResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_search_overload_2(self, async_client: AsyncJulep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.with_raw_response.search(
                user_id="",
                vector=[0, 0, 0],
            )

    @parametrize
    async def test_method_search_overload_3(self, async_client: AsyncJulep) -> None:
        user = await async_client.users.search(
            user_id="user_id",
            text="text",
            vector=[0, 0, 0],
        )
        assert_matches_type(UserSearchResponse, user, path=["response"])

    @parametrize
    async def test_method_search_with_all_params_overload_3(self, async_client: AsyncJulep) -> None:
        user = await async_client.users.search(
            user_id="user_id",
            text="text",
            vector=[0, 0, 0],
            alpha=0,
            confidence=0,
            lang="en-US",
            limit=1,
        )
        assert_matches_type(UserSearchResponse, user, path=["response"])

    @parametrize
    async def test_raw_response_search_overload_3(self, async_client: AsyncJulep) -> None:
        response = await async_client.users.with_raw_response.search(
            user_id="user_id",
            text="text",
            vector=[0, 0, 0],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserSearchResponse, user, path=["response"])

    @parametrize
    async def test_streaming_response_search_overload_3(self, async_client: AsyncJulep) -> None:
        async with async_client.users.with_streaming_response.search(
            user_id="user_id",
            text="text",
            vector=[0, 0, 0],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserSearchResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_search_overload_3(self, async_client: AsyncJulep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.with_raw_response.search(
                user_id="",
                text="text",
                vector=[0, 0, 0],
            )
