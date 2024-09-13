# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .transitions import (
    TransitionsResource,
    AsyncTransitionsResource,
    TransitionsResourceWithRawResponse,
    AsyncTransitionsResourceWithRawResponse,
    TransitionsResourceWithStreamingResponse,
    AsyncTransitionsResourceWithStreamingResponse,
)

__all__ = ["ExecutionsResource", "AsyncExecutionsResource"]


class ExecutionsResource(SyncAPIResource):
    @cached_property
    def transitions(self) -> TransitionsResource:
        return TransitionsResource(self._client)

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


class AsyncExecutionsResource(AsyncAPIResource):
    @cached_property
    def transitions(self) -> AsyncTransitionsResource:
        return AsyncTransitionsResource(self._client)

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


class ExecutionsResourceWithRawResponse:
    def __init__(self, executions: ExecutionsResource) -> None:
        self._executions = executions

    @cached_property
    def transitions(self) -> TransitionsResourceWithRawResponse:
        return TransitionsResourceWithRawResponse(self._executions.transitions)


class AsyncExecutionsResourceWithRawResponse:
    def __init__(self, executions: AsyncExecutionsResource) -> None:
        self._executions = executions

    @cached_property
    def transitions(self) -> AsyncTransitionsResourceWithRawResponse:
        return AsyncTransitionsResourceWithRawResponse(self._executions.transitions)


class ExecutionsResourceWithStreamingResponse:
    def __init__(self, executions: ExecutionsResource) -> None:
        self._executions = executions

    @cached_property
    def transitions(self) -> TransitionsResourceWithStreamingResponse:
        return TransitionsResourceWithStreamingResponse(self._executions.transitions)


class AsyncExecutionsResourceWithStreamingResponse:
    def __init__(self, executions: AsyncExecutionsResource) -> None:
        self._executions = executions

    @cached_property
    def transitions(self) -> AsyncTransitionsResourceWithStreamingResponse:
        return AsyncTransitionsResourceWithStreamingResponse(self._executions.transitions)
