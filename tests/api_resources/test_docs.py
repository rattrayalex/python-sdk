# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from julep import Julep, AsyncJulep
from julep.types import EmbedQueryResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDocs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_embed(self, client: Julep) -> None:
        doc = client.docs.embed(
            text="string",
        )
        assert_matches_type(EmbedQueryResponse, doc, path=["response"])

    @parametrize
    def test_raw_response_embed(self, client: Julep) -> None:
        response = client.docs.with_raw_response.embed(
            text="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        doc = response.parse()
        assert_matches_type(EmbedQueryResponse, doc, path=["response"])

    @parametrize
    def test_streaming_response_embed(self, client: Julep) -> None:
        with client.docs.with_streaming_response.embed(
            text="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            doc = response.parse()
            assert_matches_type(EmbedQueryResponse, doc, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDocs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_embed(self, async_client: AsyncJulep) -> None:
        doc = await async_client.docs.embed(
            text="string",
        )
        assert_matches_type(EmbedQueryResponse, doc, path=["response"])

    @parametrize
    async def test_raw_response_embed(self, async_client: AsyncJulep) -> None:
        response = await async_client.docs.with_raw_response.embed(
            text="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        doc = await response.parse()
        assert_matches_type(EmbedQueryResponse, doc, path=["response"])

    @parametrize
    async def test_streaming_response_embed(self, async_client: AsyncJulep) -> None:
        async with async_client.docs.with_streaming_response.embed(
            text="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            doc = await response.parse()
            assert_matches_type(EmbedQueryResponse, doc, path=["response"])

        assert cast(Any, response.is_closed) is True
