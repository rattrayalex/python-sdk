# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

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
from ...types.tasks import execution_list_params, execution_create_params, execution_update_params
from ..._base_client import make_request_options
from ...types.tasks.execution_list_response import ExecutionListResponse
from ...types.tasks.execution_create_response import ExecutionCreateResponse
from ...types.tasks.execution_update_response import ExecutionUpdateResponse

__all__ = ["ExecutionsResource", "AsyncExecutionsResource"]


class ExecutionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExecutionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/julep-python#accessing-raw-response-data-eg-headers
        """
        return ExecutionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExecutionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/julep-python#with_streaming_response
        """
        return ExecutionsResourceWithStreamingResponse(self)

    def create(
        self,
        task_id: str,
        *,
        input: object,
        error: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Optional[object] | NotGiven = NOT_GIVEN,
        output: Optional[object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExecutionCreateResponse:
        """
        Create Task Execution

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return self._post(
            f"/tasks/{task_id}/executions",
            body=maybe_transform(
                {
                    "input": input,
                    "error": error,
                    "metadata": metadata,
                    "output": output,
                },
                execution_create_params.ExecutionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExecutionCreateResponse,
        )

    def update(
        self,
        execution_id: str,
        *,
        task_id: str,
        status: Literal["queued", "starting", "running", "awaiting_input", "succeeded", "failed", "cancelled"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExecutionUpdateResponse:
        """
        Patch Execution

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        if not execution_id:
            raise ValueError(f"Expected a non-empty value for `execution_id` but received {execution_id!r}")
        return self._patch(
            f"/tasks/{task_id}/executions/{execution_id}",
            body=maybe_transform({"status": status}, execution_update_params.ExecutionUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExecutionUpdateResponse,
        )

    def list(
        self,
        task_id: str,
        *,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        sort_by: Literal["created_at", "updated_at"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExecutionListResponse:
        """
        List Task Executions

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return self._get(
            f"/tasks/{task_id}/executions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "limit": limit,
                        "offset": offset,
                        "sort_by": sort_by,
                    },
                    execution_list_params.ExecutionListParams,
                ),
            ),
            cast_to=ExecutionListResponse,
        )


class AsyncExecutionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExecutionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/julep-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExecutionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExecutionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/julep-python#with_streaming_response
        """
        return AsyncExecutionsResourceWithStreamingResponse(self)

    async def create(
        self,
        task_id: str,
        *,
        input: object,
        error: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Optional[object] | NotGiven = NOT_GIVEN,
        output: Optional[object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExecutionCreateResponse:
        """
        Create Task Execution

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return await self._post(
            f"/tasks/{task_id}/executions",
            body=await async_maybe_transform(
                {
                    "input": input,
                    "error": error,
                    "metadata": metadata,
                    "output": output,
                },
                execution_create_params.ExecutionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExecutionCreateResponse,
        )

    async def update(
        self,
        execution_id: str,
        *,
        task_id: str,
        status: Literal["queued", "starting", "running", "awaiting_input", "succeeded", "failed", "cancelled"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExecutionUpdateResponse:
        """
        Patch Execution

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        if not execution_id:
            raise ValueError(f"Expected a non-empty value for `execution_id` but received {execution_id!r}")
        return await self._patch(
            f"/tasks/{task_id}/executions/{execution_id}",
            body=await async_maybe_transform({"status": status}, execution_update_params.ExecutionUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExecutionUpdateResponse,
        )

    async def list(
        self,
        task_id: str,
        *,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        sort_by: Literal["created_at", "updated_at"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExecutionListResponse:
        """
        List Task Executions

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return await self._get(
            f"/tasks/{task_id}/executions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "direction": direction,
                        "limit": limit,
                        "offset": offset,
                        "sort_by": sort_by,
                    },
                    execution_list_params.ExecutionListParams,
                ),
            ),
            cast_to=ExecutionListResponse,
        )


class ExecutionsResourceWithRawResponse:
    def __init__(self, executions: ExecutionsResource) -> None:
        self._executions = executions

        self.create = to_raw_response_wrapper(
            executions.create,
        )
        self.update = to_raw_response_wrapper(
            executions.update,
        )
        self.list = to_raw_response_wrapper(
            executions.list,
        )


class AsyncExecutionsResourceWithRawResponse:
    def __init__(self, executions: AsyncExecutionsResource) -> None:
        self._executions = executions

        self.create = async_to_raw_response_wrapper(
            executions.create,
        )
        self.update = async_to_raw_response_wrapper(
            executions.update,
        )
        self.list = async_to_raw_response_wrapper(
            executions.list,
        )


class ExecutionsResourceWithStreamingResponse:
    def __init__(self, executions: ExecutionsResource) -> None:
        self._executions = executions

        self.create = to_streamed_response_wrapper(
            executions.create,
        )
        self.update = to_streamed_response_wrapper(
            executions.update,
        )
        self.list = to_streamed_response_wrapper(
            executions.list,
        )


class AsyncExecutionsResourceWithStreamingResponse:
    def __init__(self, executions: AsyncExecutionsResource) -> None:
        self._executions = executions

        self.create = async_to_streamed_response_wrapper(
            executions.create,
        )
        self.update = async_to_streamed_response_wrapper(
            executions.update,
        )
        self.list = async_to_streamed_response_wrapper(
            executions.list,
        )
