# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.txn_pool_retrieve_response import TxnPoolRetrieveResponse

__all__ = ["TxnPoolResource", "AsyncTxnPoolResource"]


class TxnPoolResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TxnPoolResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/knirvchain-transaction-sdk-python#accessing-raw-response-data-eg-headers
        """
        return TxnPoolResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TxnPoolResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/knirvchain-transaction-sdk-python#with_streaming_response
        """
        return TxnPoolResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TxnPoolRetrieveResponse:
        """Retrieves the current transaction pool"""
        return self._get(
            "/txn_pool",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TxnPoolRetrieveResponse,
        )


class AsyncTxnPoolResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTxnPoolResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/knirvchain-transaction-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTxnPoolResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTxnPoolResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/knirvchain-transaction-sdk-python#with_streaming_response
        """
        return AsyncTxnPoolResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TxnPoolRetrieveResponse:
        """Retrieves the current transaction pool"""
        return await self._get(
            "/txn_pool",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TxnPoolRetrieveResponse,
        )


class TxnPoolResourceWithRawResponse:
    def __init__(self, txn_pool: TxnPoolResource) -> None:
        self._txn_pool = txn_pool

        self.retrieve = to_raw_response_wrapper(
            txn_pool.retrieve,
        )


class AsyncTxnPoolResourceWithRawResponse:
    def __init__(self, txn_pool: AsyncTxnPoolResource) -> None:
        self._txn_pool = txn_pool

        self.retrieve = async_to_raw_response_wrapper(
            txn_pool.retrieve,
        )


class TxnPoolResourceWithStreamingResponse:
    def __init__(self, txn_pool: TxnPoolResource) -> None:
        self._txn_pool = txn_pool

        self.retrieve = to_streamed_response_wrapper(
            txn_pool.retrieve,
        )


class AsyncTxnPoolResourceWithStreamingResponse:
    def __init__(self, txn_pool: AsyncTxnPoolResource) -> None:
        self._txn_pool = txn_pool

        self.retrieve = async_to_streamed_response_wrapper(
            txn_pool.retrieve,
        )
