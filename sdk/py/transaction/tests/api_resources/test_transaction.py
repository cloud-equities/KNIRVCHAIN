# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from knirvchain_transaction_sdk import KnirvchainTransactionSDK, AsyncKnirvchainTransactionSDK
from knirvchain_transaction_sdk.types import TransactionSubmitResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTransaction:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_submit(self, client: KnirvchainTransactionSDK) -> None:
        transaction = client.transaction.submit(
            id="0xabcdef123456...",
            fee="fee",
            from_="from",
            public_key="public_key",
            signature="U3RhaW5sZXNzIHJvY2tz",
            timestamp=0,
            type="type",
            version=1,
        )
        assert_matches_type(TransactionSubmitResponse, transaction, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_submit_with_all_params(self, client: KnirvchainTransactionSDK) -> None:
        transaction = client.transaction.submit(
            id="0xabcdef123456...",
            fee="fee",
            from_="from",
            public_key="public_key",
            signature="U3RhaW5sZXNzIHJvY2tz",
            timestamp=0,
            type="type",
            version=1,
            data={"foo": "bar"},
            status="status",
            to="to",
            transaction_hash="transaction_hash",
            value="1000000000000000000",
        )
        assert_matches_type(TransactionSubmitResponse, transaction, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_submit(self, client: KnirvchainTransactionSDK) -> None:
        response = client.transaction.with_raw_response.submit(
            id="0xabcdef123456...",
            fee="fee",
            from_="from",
            public_key="public_key",
            signature="U3RhaW5sZXNzIHJvY2tz",
            timestamp=0,
            type="type",
            version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = response.parse()
        assert_matches_type(TransactionSubmitResponse, transaction, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_submit(self, client: KnirvchainTransactionSDK) -> None:
        with client.transaction.with_streaming_response.submit(
            id="0xabcdef123456...",
            fee="fee",
            from_="from",
            public_key="public_key",
            signature="U3RhaW5sZXNzIHJvY2tz",
            timestamp=0,
            type="type",
            version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = response.parse()
            assert_matches_type(TransactionSubmitResponse, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTransaction:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_submit(self, async_client: AsyncKnirvchainTransactionSDK) -> None:
        transaction = await async_client.transaction.submit(
            id="0xabcdef123456...",
            fee="fee",
            from_="from",
            public_key="public_key",
            signature="U3RhaW5sZXNzIHJvY2tz",
            timestamp=0,
            type="type",
            version=1,
        )
        assert_matches_type(TransactionSubmitResponse, transaction, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_submit_with_all_params(self, async_client: AsyncKnirvchainTransactionSDK) -> None:
        transaction = await async_client.transaction.submit(
            id="0xabcdef123456...",
            fee="fee",
            from_="from",
            public_key="public_key",
            signature="U3RhaW5sZXNzIHJvY2tz",
            timestamp=0,
            type="type",
            version=1,
            data={"foo": "bar"},
            status="status",
            to="to",
            transaction_hash="transaction_hash",
            value="1000000000000000000",
        )
        assert_matches_type(TransactionSubmitResponse, transaction, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_submit(self, async_client: AsyncKnirvchainTransactionSDK) -> None:
        response = await async_client.transaction.with_raw_response.submit(
            id="0xabcdef123456...",
            fee="fee",
            from_="from",
            public_key="public_key",
            signature="U3RhaW5sZXNzIHJvY2tz",
            timestamp=0,
            type="type",
            version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = await response.parse()
        assert_matches_type(TransactionSubmitResponse, transaction, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_submit(self, async_client: AsyncKnirvchainTransactionSDK) -> None:
        async with async_client.transaction.with_streaming_response.submit(
            id="0xabcdef123456...",
            fee="fee",
            from_="from",
            public_key="public_key",
            signature="U3RhaW5sZXNzIHJvY2tz",
            timestamp=0,
            type="type",
            version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = await response.parse()
            assert_matches_type(TransactionSubmitResponse, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True
