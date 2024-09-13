# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from julep import Julep, AsyncJulep
from julep.types import (
    History,
    Session,
    SessionListResponse,
    SessionCreateResponse,
    SessionDeleteResponse,
    SessionUpdateResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSessions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Julep) -> None:
        session = client.sessions.create()
        assert_matches_type(SessionCreateResponse, session, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Julep) -> None:
        session = client.sessions.create(
            agent="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agents=[
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ],
            context_overflow="truncate",
            metadata={},
            render_templates=True,
            situation="situation",
            token_budget=0,
            user="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            users=[
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ],
        )
        assert_matches_type(SessionCreateResponse, session, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Julep) -> None:
        response = client.sessions.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionCreateResponse, session, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Julep) -> None:
        with client.sessions.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionCreateResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Julep) -> None:
        session = client.sessions.retrieve(
            "session_id",
        )
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Julep) -> None:
        response = client.sessions.with_raw_response.retrieve(
            "session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Julep) -> None:
        with client.sessions.with_streaming_response.retrieve(
            "session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Julep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.sessions.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Julep) -> None:
        session = client.sessions.update(
            session_id="session_id",
        )
        assert_matches_type(SessionUpdateResponse, session, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Julep) -> None:
        session = client.sessions.update(
            session_id="session_id",
            context_overflow="truncate",
            metadata={},
            render_templates=True,
            situation="situation",
            token_budget=0,
        )
        assert_matches_type(SessionUpdateResponse, session, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Julep) -> None:
        response = client.sessions.with_raw_response.update(
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionUpdateResponse, session, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Julep) -> None:
        with client.sessions.with_streaming_response.update(
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionUpdateResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Julep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.sessions.with_raw_response.update(
                session_id="",
            )

    @parametrize
    def test_method_list(self, client: Julep) -> None:
        session = client.sessions.list()
        assert_matches_type(SessionListResponse, session, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Julep) -> None:
        session = client.sessions.list(
            direction="asc",
            limit=0,
            metadata_filter="metadata_filter",
            offset=0,
            sort_by="created_at",
        )
        assert_matches_type(SessionListResponse, session, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Julep) -> None:
        response = client.sessions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionListResponse, session, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Julep) -> None:
        with client.sessions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionListResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Julep) -> None:
        session = client.sessions.delete(
            "session_id",
        )
        assert_matches_type(SessionDeleteResponse, session, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Julep) -> None:
        response = client.sessions.with_raw_response.delete(
            "session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionDeleteResponse, session, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Julep) -> None:
        with client.sessions.with_streaming_response.delete(
            "session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionDeleteResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Julep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.sessions.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_history(self, client: Julep) -> None:
        session = client.sessions.history(
            "session_id",
        )
        assert_matches_type(History, session, path=["response"])

    @parametrize
    def test_raw_response_history(self, client: Julep) -> None:
        response = client.sessions.with_raw_response.history(
            "session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(History, session, path=["response"])

    @parametrize
    def test_streaming_response_history(self, client: Julep) -> None:
        with client.sessions.with_streaming_response.history(
            "session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(History, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_history(self, client: Julep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.sessions.with_raw_response.history(
                "",
            )


class TestAsyncSessions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncJulep) -> None:
        session = await async_client.sessions.create()
        assert_matches_type(SessionCreateResponse, session, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncJulep) -> None:
        session = await async_client.sessions.create(
            agent="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agents=[
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ],
            context_overflow="truncate",
            metadata={},
            render_templates=True,
            situation="situation",
            token_budget=0,
            user="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            users=[
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ],
        )
        assert_matches_type(SessionCreateResponse, session, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncJulep) -> None:
        response = await async_client.sessions.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionCreateResponse, session, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncJulep) -> None:
        async with async_client.sessions.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionCreateResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncJulep) -> None:
        session = await async_client.sessions.retrieve(
            "session_id",
        )
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncJulep) -> None:
        response = await async_client.sessions.with_raw_response.retrieve(
            "session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncJulep) -> None:
        async with async_client.sessions.with_streaming_response.retrieve(
            "session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncJulep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.sessions.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncJulep) -> None:
        session = await async_client.sessions.update(
            session_id="session_id",
        )
        assert_matches_type(SessionUpdateResponse, session, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncJulep) -> None:
        session = await async_client.sessions.update(
            session_id="session_id",
            context_overflow="truncate",
            metadata={},
            render_templates=True,
            situation="situation",
            token_budget=0,
        )
        assert_matches_type(SessionUpdateResponse, session, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncJulep) -> None:
        response = await async_client.sessions.with_raw_response.update(
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionUpdateResponse, session, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncJulep) -> None:
        async with async_client.sessions.with_streaming_response.update(
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionUpdateResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncJulep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.sessions.with_raw_response.update(
                session_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncJulep) -> None:
        session = await async_client.sessions.list()
        assert_matches_type(SessionListResponse, session, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncJulep) -> None:
        session = await async_client.sessions.list(
            direction="asc",
            limit=0,
            metadata_filter="metadata_filter",
            offset=0,
            sort_by="created_at",
        )
        assert_matches_type(SessionListResponse, session, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncJulep) -> None:
        response = await async_client.sessions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionListResponse, session, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncJulep) -> None:
        async with async_client.sessions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionListResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncJulep) -> None:
        session = await async_client.sessions.delete(
            "session_id",
        )
        assert_matches_type(SessionDeleteResponse, session, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncJulep) -> None:
        response = await async_client.sessions.with_raw_response.delete(
            "session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionDeleteResponse, session, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncJulep) -> None:
        async with async_client.sessions.with_streaming_response.delete(
            "session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionDeleteResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncJulep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.sessions.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_history(self, async_client: AsyncJulep) -> None:
        session = await async_client.sessions.history(
            "session_id",
        )
        assert_matches_type(History, session, path=["response"])

    @parametrize
    async def test_raw_response_history(self, async_client: AsyncJulep) -> None:
        response = await async_client.sessions.with_raw_response.history(
            "session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(History, session, path=["response"])

    @parametrize
    async def test_streaming_response_history(self, async_client: AsyncJulep) -> None:
        async with async_client.sessions.with_streaming_response.history(
            "session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(History, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_history(self, async_client: AsyncJulep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.sessions.with_raw_response.history(
                "",
            )
