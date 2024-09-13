# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union

import httpx

from ..types import doc_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..types.doc import Doc
from .._base_client import make_request_options
from ..types.embed_query_response import EmbedQueryResponse

__all__ = ["DocsResource", "AsyncDocsResource"]


class DocsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DocsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/julep-python#accessing-raw-response-data-eg-headers
        """
        return DocsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DocsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/julep-python#with_streaming_response
        """
        return DocsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        text: Union[str, List[str]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmbedQueryResponse:
        """
        Embed

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/embed",
            body=maybe_transform({"text": text}, doc_create_params.DocCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmbedQueryResponse,
        )

    def retrieve(
        self,
        doc_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Doc:
        """
        Get Doc

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not doc_id:
            raise ValueError(f"Expected a non-empty value for `doc_id` but received {doc_id!r}")
        return self._get(
            f"/docs/{doc_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Doc,
        )


class AsyncDocsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDocsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/julep-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDocsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDocsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/julep-python#with_streaming_response
        """
        return AsyncDocsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        text: Union[str, List[str]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmbedQueryResponse:
        """
        Embed

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/embed",
            body=await async_maybe_transform({"text": text}, doc_create_params.DocCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmbedQueryResponse,
        )

    async def retrieve(
        self,
        doc_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Doc:
        """
        Get Doc

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not doc_id:
            raise ValueError(f"Expected a non-empty value for `doc_id` but received {doc_id!r}")
        return await self._get(
            f"/docs/{doc_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Doc,
        )


class DocsResourceWithRawResponse:
    def __init__(self, docs: DocsResource) -> None:
        self._docs = docs

        self.create = to_raw_response_wrapper(
            docs.create,
        )
        self.retrieve = to_raw_response_wrapper(
            docs.retrieve,
        )


class AsyncDocsResourceWithRawResponse:
    def __init__(self, docs: AsyncDocsResource) -> None:
        self._docs = docs

        self.create = async_to_raw_response_wrapper(
            docs.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            docs.retrieve,
        )


class DocsResourceWithStreamingResponse:
    def __init__(self, docs: DocsResource) -> None:
        self._docs = docs

        self.create = to_streamed_response_wrapper(
            docs.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            docs.retrieve,
        )


class AsyncDocsResourceWithStreamingResponse:
    def __init__(self, docs: AsyncDocsResource) -> None:
        self._docs = docs

        self.create = async_to_streamed_response_wrapper(
            docs.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            docs.retrieve,
        )
