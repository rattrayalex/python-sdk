# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Dict, List, Iterable, Optional, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.sessions import chat_create_params
from ...types.sessions.chat_create_response import ChatCreateResponse

__all__ = ["ChatsResource", "AsyncChatsResource"]


class ChatsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ChatsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/julep-python#accessing-raw-response-data-eg-headers
        """
        return ChatsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChatsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/julep-python#with_streaming_response
        """
        return ChatsResourceWithStreamingResponse(self)

    def create(
        self,
        session_id: str,
        *,
        messages: Iterable[chat_create_params.Message],
        agent: Optional[str] | NotGiven = NOT_GIVEN,
        frequency_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        length_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        logit_bias: Optional[Dict[str, float]] | NotGiven = NOT_GIVEN,
        max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        min_p: Optional[float] | NotGiven = NOT_GIVEN,
        model: Optional[str] | NotGiven = NOT_GIVEN,
        presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        recall: bool | NotGiven = NOT_GIVEN,
        repetition_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        response_format: Optional[chat_create_params.ResponseFormat] | NotGiven = NOT_GIVEN,
        save: bool | NotGiven = NOT_GIVEN,
        seed: Optional[int] | NotGiven = NOT_GIVEN,
        stop: List[str] | NotGiven = NOT_GIVEN,
        stream: bool | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        tool_choice: Optional[chat_create_params.ToolChoice] | NotGiven = NOT_GIVEN,
        tools: Iterable[chat_create_params.Tool] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCreateResponse:
        """
        Chat

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return cast(
            ChatCreateResponse,
            self._post(
                f"/sessions/{session_id}/chat",
                body=maybe_transform(
                    {
                        "messages": messages,
                        "agent": agent,
                        "frequency_penalty": frequency_penalty,
                        "length_penalty": length_penalty,
                        "logit_bias": logit_bias,
                        "max_tokens": max_tokens,
                        "min_p": min_p,
                        "model": model,
                        "presence_penalty": presence_penalty,
                        "recall": recall,
                        "repetition_penalty": repetition_penalty,
                        "response_format": response_format,
                        "save": save,
                        "seed": seed,
                        "stop": stop,
                        "stream": stream,
                        "temperature": temperature,
                        "tool_choice": tool_choice,
                        "tools": tools,
                        "top_p": top_p,
                    },
                    chat_create_params.ChatCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, ChatCreateResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncChatsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncChatsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/julep-python#accessing-raw-response-data-eg-headers
        """
        return AsyncChatsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChatsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/julep-python#with_streaming_response
        """
        return AsyncChatsResourceWithStreamingResponse(self)

    async def create(
        self,
        session_id: str,
        *,
        messages: Iterable[chat_create_params.Message],
        agent: Optional[str] | NotGiven = NOT_GIVEN,
        frequency_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        length_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        logit_bias: Optional[Dict[str, float]] | NotGiven = NOT_GIVEN,
        max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        min_p: Optional[float] | NotGiven = NOT_GIVEN,
        model: Optional[str] | NotGiven = NOT_GIVEN,
        presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        recall: bool | NotGiven = NOT_GIVEN,
        repetition_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        response_format: Optional[chat_create_params.ResponseFormat] | NotGiven = NOT_GIVEN,
        save: bool | NotGiven = NOT_GIVEN,
        seed: Optional[int] | NotGiven = NOT_GIVEN,
        stop: List[str] | NotGiven = NOT_GIVEN,
        stream: bool | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        tool_choice: Optional[chat_create_params.ToolChoice] | NotGiven = NOT_GIVEN,
        tools: Iterable[chat_create_params.Tool] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCreateResponse:
        """
        Chat

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return cast(
            ChatCreateResponse,
            await self._post(
                f"/sessions/{session_id}/chat",
                body=await async_maybe_transform(
                    {
                        "messages": messages,
                        "agent": agent,
                        "frequency_penalty": frequency_penalty,
                        "length_penalty": length_penalty,
                        "logit_bias": logit_bias,
                        "max_tokens": max_tokens,
                        "min_p": min_p,
                        "model": model,
                        "presence_penalty": presence_penalty,
                        "recall": recall,
                        "repetition_penalty": repetition_penalty,
                        "response_format": response_format,
                        "save": save,
                        "seed": seed,
                        "stop": stop,
                        "stream": stream,
                        "temperature": temperature,
                        "tool_choice": tool_choice,
                        "tools": tools,
                        "top_p": top_p,
                    },
                    chat_create_params.ChatCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, ChatCreateResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class ChatsResourceWithRawResponse:
    def __init__(self, chats: ChatsResource) -> None:
        self._chats = chats

        self.create = to_raw_response_wrapper(
            chats.create,
        )


class AsyncChatsResourceWithRawResponse:
    def __init__(self, chats: AsyncChatsResource) -> None:
        self._chats = chats

        self.create = async_to_raw_response_wrapper(
            chats.create,
        )


class ChatsResourceWithStreamingResponse:
    def __init__(self, chats: ChatsResource) -> None:
        self._chats = chats

        self.create = to_streamed_response_wrapper(
            chats.create,
        )


class AsyncChatsResourceWithStreamingResponse:
    def __init__(self, chats: AsyncChatsResource) -> None:
        self._chats = chats

        self.create = async_to_streamed_response_wrapper(
            chats.create,
        )
