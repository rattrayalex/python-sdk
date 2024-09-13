# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from julep import Julep, AsyncJulep
from tests.utils import assert_matches_type
from julep.types.sessions import ChatCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChats:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Julep) -> None:
        chat = client.sessions.chats.create(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            messages=[
                {
                    "content": "string",
                    "role": "user",
                }
            ],
        )
        assert_matches_type(ChatCreateResponse, chat, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Julep) -> None:
        chat = client.sessions.chats.create(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            messages=[
                {
                    "content": "string",
                    "role": "user",
                    "continue": True,
                    "name": "name",
                }
            ],
            agent="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            frequency_penalty=-2,
            length_penalty=0,
            logit_bias={"foo": -100},
            max_tokens=1,
            min_p=0,
            model="model",
            presence_penalty=-2,
            recall=True,
            repetition_penalty=0,
            response_format={"type": "text"},
            save=True,
            seed=-1,
            stop=["string", "string", "string"],
            stream=True,
            temperature=0,
            tool_choice="auto",
            tools=[
                {
                    "function": {
                        "description": "description",
                        "name": {},
                        "parameters": {},
                    },
                    "name": "name",
                    "api_call": {},
                    "integration": {},
                    "system": {},
                    "type": "function",
                },
                {
                    "function": {
                        "description": "description",
                        "name": {},
                        "parameters": {},
                    },
                    "name": "name",
                    "api_call": {},
                    "integration": {},
                    "system": {},
                    "type": "function",
                },
                {
                    "function": {
                        "description": "description",
                        "name": {},
                        "parameters": {},
                    },
                    "name": "name",
                    "api_call": {},
                    "integration": {},
                    "system": {},
                    "type": "function",
                },
            ],
            top_p=0,
        )
        assert_matches_type(ChatCreateResponse, chat, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Julep) -> None:
        response = client.sessions.chats.with_raw_response.create(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            messages=[
                {
                    "content": "string",
                    "role": "user",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(ChatCreateResponse, chat, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Julep) -> None:
        with client.sessions.chats.with_streaming_response.create(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            messages=[
                {
                    "content": "string",
                    "role": "user",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(ChatCreateResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Julep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.sessions.chats.with_raw_response.create(
                session_id="",
                messages=[
                    {
                        "content": "string",
                        "role": "user",
                    }
                ],
            )


class TestAsyncChats:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncJulep) -> None:
        chat = await async_client.sessions.chats.create(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            messages=[
                {
                    "content": "string",
                    "role": "user",
                }
            ],
        )
        assert_matches_type(ChatCreateResponse, chat, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncJulep) -> None:
        chat = await async_client.sessions.chats.create(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            messages=[
                {
                    "content": "string",
                    "role": "user",
                    "continue": True,
                    "name": "name",
                }
            ],
            agent="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            frequency_penalty=-2,
            length_penalty=0,
            logit_bias={"foo": -100},
            max_tokens=1,
            min_p=0,
            model="model",
            presence_penalty=-2,
            recall=True,
            repetition_penalty=0,
            response_format={"type": "text"},
            save=True,
            seed=-1,
            stop=["string", "string", "string"],
            stream=True,
            temperature=0,
            tool_choice="auto",
            tools=[
                {
                    "function": {
                        "description": "description",
                        "name": {},
                        "parameters": {},
                    },
                    "name": "name",
                    "api_call": {},
                    "integration": {},
                    "system": {},
                    "type": "function",
                },
                {
                    "function": {
                        "description": "description",
                        "name": {},
                        "parameters": {},
                    },
                    "name": "name",
                    "api_call": {},
                    "integration": {},
                    "system": {},
                    "type": "function",
                },
                {
                    "function": {
                        "description": "description",
                        "name": {},
                        "parameters": {},
                    },
                    "name": "name",
                    "api_call": {},
                    "integration": {},
                    "system": {},
                    "type": "function",
                },
            ],
            top_p=0,
        )
        assert_matches_type(ChatCreateResponse, chat, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncJulep) -> None:
        response = await async_client.sessions.chats.with_raw_response.create(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            messages=[
                {
                    "content": "string",
                    "role": "user",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(ChatCreateResponse, chat, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncJulep) -> None:
        async with async_client.sessions.chats.with_streaming_response.create(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            messages=[
                {
                    "content": "string",
                    "role": "user",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(ChatCreateResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncJulep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.sessions.chats.with_raw_response.create(
                session_id="",
                messages=[
                    {
                        "content": "string",
                        "role": "user",
                    }
                ],
            )
