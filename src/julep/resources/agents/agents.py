# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional, overload
from typing_extensions import Literal

import httpx

from .docs import (
    DocsResource,
    AsyncDocsResource,
    DocsResourceWithRawResponse,
    AsyncDocsResourceWithRawResponse,
    DocsResourceWithStreamingResponse,
    AsyncDocsResourceWithStreamingResponse,
)
from .tasks import (
    TasksResource,
    AsyncTasksResource,
    TasksResourceWithRawResponse,
    AsyncTasksResourceWithRawResponse,
    TasksResourceWithStreamingResponse,
    AsyncTasksResourceWithStreamingResponse,
)
from .tools import (
    ToolsResource,
    AsyncToolsResource,
    ToolsResourceWithRawResponse,
    AsyncToolsResourceWithRawResponse,
    ToolsResourceWithStreamingResponse,
    AsyncToolsResourceWithStreamingResponse,
)
from ...types import agent_list_params, agent_create_params, agent_search_params, agent_update_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    required_args,
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
from ...types.agent import Agent
from ..._base_client import make_request_options
from ...types.agent_list_response import AgentListResponse
from ...types.agent_create_response import AgentCreateResponse
from ...types.agent_delete_response import AgentDeleteResponse
from ...types.agent_search_response import AgentSearchResponse
from ...types.agent_update_response import AgentUpdateResponse

__all__ = ["AgentsResource", "AsyncAgentsResource"]


class AgentsResource(SyncAPIResource):
    @cached_property
    def tools(self) -> ToolsResource:
        return ToolsResource(self._client)

    @cached_property
    def docs(self) -> DocsResource:
        return DocsResource(self._client)

    @cached_property
    def tasks(self) -> TasksResource:
        return TasksResource(self._client)

    @cached_property
    def with_raw_response(self) -> AgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/julep-python#accessing-raw-response-data-eg-headers
        """
        return AgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/julep-python#with_streaming_response
        """
        return AgentsResourceWithStreamingResponse(self)

    def create(
        self,
        agent_id: str,
        *,
        about: str | NotGiven = NOT_GIVEN,
        default_settings: Optional[agent_create_params.DefaultSettings] | NotGiven = NOT_GIVEN,
        instructions: Union[str, List[str]] | NotGiven = NOT_GIVEN,
        metadata: Optional[object] | NotGiven = NOT_GIVEN,
        model: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentCreateResponse:
        """
        Create Or Update Agent

        Args:
          default_settings: Default settings for the chat session (also used by the agent)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._post(
            f"/agents/{agent_id}",
            body=maybe_transform(
                {
                    "about": about,
                    "default_settings": default_settings,
                    "instructions": instructions,
                    "metadata": metadata,
                    "model": model,
                    "name": name,
                },
                agent_create_params.AgentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentCreateResponse,
        )

    def retrieve(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Agent:
        """
        Get Agent Details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get(
            f"/agents/{agent_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Agent,
        )

    def update(
        self,
        agent_id: str,
        *,
        about: str | NotGiven = NOT_GIVEN,
        default_settings: Optional[agent_update_params.DefaultSettings] | NotGiven = NOT_GIVEN,
        instructions: Union[str, List[str]] | NotGiven = NOT_GIVEN,
        metadata: Optional[object] | NotGiven = NOT_GIVEN,
        model: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentUpdateResponse:
        """
        Update Agent

        Args:
          default_settings: Default settings for the chat session (also used by the agent)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._put(
            f"/agents/{agent_id}",
            body=maybe_transform(
                {
                    "about": about,
                    "default_settings": default_settings,
                    "instructions": instructions,
                    "metadata": metadata,
                    "model": model,
                    "name": name,
                },
                agent_update_params.AgentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentUpdateResponse,
        )

    def list(
        self,
        *,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        metadata_filter: str | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        sort_by: Literal["created_at", "updated_at"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentListResponse:
        """
        List Agents

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/agents",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "limit": limit,
                        "metadata_filter": metadata_filter,
                        "offset": offset,
                        "sort_by": sort_by,
                    },
                    agent_list_params.AgentListParams,
                ),
            ),
            cast_to=AgentListResponse,
        )

    def delete(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentDeleteResponse:
        """
        Delete Agent

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._delete(
            f"/agents/{agent_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentDeleteResponse,
        )

    @overload
    def search(
        self,
        agent_id: str,
        *,
        text: str,
        lang: Literal["en-US"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentSearchResponse:
        """
        Search Agent Docs

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def search(
        self,
        agent_id: str,
        *,
        vector: Iterable[float],
        confidence: float | NotGiven = NOT_GIVEN,
        lang: Literal["en-US"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentSearchResponse:
        """
        Search Agent Docs

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def search(
        self,
        agent_id: str,
        *,
        text: str,
        vector: Iterable[float],
        alpha: float | NotGiven = NOT_GIVEN,
        confidence: float | NotGiven = NOT_GIVEN,
        lang: Literal["en-US"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentSearchResponse:
        """
        Search Agent Docs

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["text"], ["vector"], ["text", "vector"])
    def search(
        self,
        agent_id: str,
        *,
        text: str | NotGiven = NOT_GIVEN,
        lang: Literal["en-US"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        vector: Iterable[float] | NotGiven = NOT_GIVEN,
        confidence: float | NotGiven = NOT_GIVEN,
        alpha: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentSearchResponse:
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._post(
            f"/agents/{agent_id}/search",
            body=maybe_transform(
                {
                    "text": text,
                    "lang": lang,
                    "limit": limit,
                    "vector": vector,
                    "confidence": confidence,
                    "alpha": alpha,
                },
                agent_search_params.AgentSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentSearchResponse,
        )


class AsyncAgentsResource(AsyncAPIResource):
    @cached_property
    def tools(self) -> AsyncToolsResource:
        return AsyncToolsResource(self._client)

    @cached_property
    def docs(self) -> AsyncDocsResource:
        return AsyncDocsResource(self._client)

    @cached_property
    def tasks(self) -> AsyncTasksResource:
        return AsyncTasksResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/julep-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/julep-python#with_streaming_response
        """
        return AsyncAgentsResourceWithStreamingResponse(self)

    async def create(
        self,
        agent_id: str,
        *,
        about: str | NotGiven = NOT_GIVEN,
        default_settings: Optional[agent_create_params.DefaultSettings] | NotGiven = NOT_GIVEN,
        instructions: Union[str, List[str]] | NotGiven = NOT_GIVEN,
        metadata: Optional[object] | NotGiven = NOT_GIVEN,
        model: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentCreateResponse:
        """
        Create Or Update Agent

        Args:
          default_settings: Default settings for the chat session (also used by the agent)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._post(
            f"/agents/{agent_id}",
            body=await async_maybe_transform(
                {
                    "about": about,
                    "default_settings": default_settings,
                    "instructions": instructions,
                    "metadata": metadata,
                    "model": model,
                    "name": name,
                },
                agent_create_params.AgentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentCreateResponse,
        )

    async def retrieve(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Agent:
        """
        Get Agent Details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._get(
            f"/agents/{agent_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Agent,
        )

    async def update(
        self,
        agent_id: str,
        *,
        about: str | NotGiven = NOT_GIVEN,
        default_settings: Optional[agent_update_params.DefaultSettings] | NotGiven = NOT_GIVEN,
        instructions: Union[str, List[str]] | NotGiven = NOT_GIVEN,
        metadata: Optional[object] | NotGiven = NOT_GIVEN,
        model: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentUpdateResponse:
        """
        Update Agent

        Args:
          default_settings: Default settings for the chat session (also used by the agent)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._put(
            f"/agents/{agent_id}",
            body=await async_maybe_transform(
                {
                    "about": about,
                    "default_settings": default_settings,
                    "instructions": instructions,
                    "metadata": metadata,
                    "model": model,
                    "name": name,
                },
                agent_update_params.AgentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentUpdateResponse,
        )

    async def list(
        self,
        *,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        metadata_filter: str | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        sort_by: Literal["created_at", "updated_at"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentListResponse:
        """
        List Agents

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/agents",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "direction": direction,
                        "limit": limit,
                        "metadata_filter": metadata_filter,
                        "offset": offset,
                        "sort_by": sort_by,
                    },
                    agent_list_params.AgentListParams,
                ),
            ),
            cast_to=AgentListResponse,
        )

    async def delete(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentDeleteResponse:
        """
        Delete Agent

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._delete(
            f"/agents/{agent_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentDeleteResponse,
        )

    @overload
    async def search(
        self,
        agent_id: str,
        *,
        text: str,
        lang: Literal["en-US"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentSearchResponse:
        """
        Search Agent Docs

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def search(
        self,
        agent_id: str,
        *,
        vector: Iterable[float],
        confidence: float | NotGiven = NOT_GIVEN,
        lang: Literal["en-US"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentSearchResponse:
        """
        Search Agent Docs

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def search(
        self,
        agent_id: str,
        *,
        text: str,
        vector: Iterable[float],
        alpha: float | NotGiven = NOT_GIVEN,
        confidence: float | NotGiven = NOT_GIVEN,
        lang: Literal["en-US"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentSearchResponse:
        """
        Search Agent Docs

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["text"], ["vector"], ["text", "vector"])
    async def search(
        self,
        agent_id: str,
        *,
        text: str | NotGiven = NOT_GIVEN,
        lang: Literal["en-US"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        vector: Iterable[float] | NotGiven = NOT_GIVEN,
        confidence: float | NotGiven = NOT_GIVEN,
        alpha: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentSearchResponse:
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._post(
            f"/agents/{agent_id}/search",
            body=await async_maybe_transform(
                {
                    "text": text,
                    "lang": lang,
                    "limit": limit,
                    "vector": vector,
                    "confidence": confidence,
                    "alpha": alpha,
                },
                agent_search_params.AgentSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentSearchResponse,
        )


class AgentsResourceWithRawResponse:
    def __init__(self, agents: AgentsResource) -> None:
        self._agents = agents

        self.create = to_raw_response_wrapper(
            agents.create,
        )
        self.retrieve = to_raw_response_wrapper(
            agents.retrieve,
        )
        self.update = to_raw_response_wrapper(
            agents.update,
        )
        self.list = to_raw_response_wrapper(
            agents.list,
        )
        self.delete = to_raw_response_wrapper(
            agents.delete,
        )
        self.search = to_raw_response_wrapper(
            agents.search,
        )

    @cached_property
    def tools(self) -> ToolsResourceWithRawResponse:
        return ToolsResourceWithRawResponse(self._agents.tools)

    @cached_property
    def docs(self) -> DocsResourceWithRawResponse:
        return DocsResourceWithRawResponse(self._agents.docs)

    @cached_property
    def tasks(self) -> TasksResourceWithRawResponse:
        return TasksResourceWithRawResponse(self._agents.tasks)


class AsyncAgentsResourceWithRawResponse:
    def __init__(self, agents: AsyncAgentsResource) -> None:
        self._agents = agents

        self.create = async_to_raw_response_wrapper(
            agents.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            agents.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            agents.update,
        )
        self.list = async_to_raw_response_wrapper(
            agents.list,
        )
        self.delete = async_to_raw_response_wrapper(
            agents.delete,
        )
        self.search = async_to_raw_response_wrapper(
            agents.search,
        )

    @cached_property
    def tools(self) -> AsyncToolsResourceWithRawResponse:
        return AsyncToolsResourceWithRawResponse(self._agents.tools)

    @cached_property
    def docs(self) -> AsyncDocsResourceWithRawResponse:
        return AsyncDocsResourceWithRawResponse(self._agents.docs)

    @cached_property
    def tasks(self) -> AsyncTasksResourceWithRawResponse:
        return AsyncTasksResourceWithRawResponse(self._agents.tasks)


class AgentsResourceWithStreamingResponse:
    def __init__(self, agents: AgentsResource) -> None:
        self._agents = agents

        self.create = to_streamed_response_wrapper(
            agents.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            agents.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            agents.update,
        )
        self.list = to_streamed_response_wrapper(
            agents.list,
        )
        self.delete = to_streamed_response_wrapper(
            agents.delete,
        )
        self.search = to_streamed_response_wrapper(
            agents.search,
        )

    @cached_property
    def tools(self) -> ToolsResourceWithStreamingResponse:
        return ToolsResourceWithStreamingResponse(self._agents.tools)

    @cached_property
    def docs(self) -> DocsResourceWithStreamingResponse:
        return DocsResourceWithStreamingResponse(self._agents.docs)

    @cached_property
    def tasks(self) -> TasksResourceWithStreamingResponse:
        return TasksResourceWithStreamingResponse(self._agents.tasks)


class AsyncAgentsResourceWithStreamingResponse:
    def __init__(self, agents: AsyncAgentsResource) -> None:
        self._agents = agents

        self.create = async_to_streamed_response_wrapper(
            agents.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            agents.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            agents.update,
        )
        self.list = async_to_streamed_response_wrapper(
            agents.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            agents.delete,
        )
        self.search = async_to_streamed_response_wrapper(
            agents.search,
        )

    @cached_property
    def tools(self) -> AsyncToolsResourceWithStreamingResponse:
        return AsyncToolsResourceWithStreamingResponse(self._agents.tools)

    @cached_property
    def docs(self) -> AsyncDocsResourceWithStreamingResponse:
        return AsyncDocsResourceWithStreamingResponse(self._agents.docs)

    @cached_property
    def tasks(self) -> AsyncTasksResourceWithStreamingResponse:
        return AsyncTasksResourceWithStreamingResponse(self._agents.tasks)
