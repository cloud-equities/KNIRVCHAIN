// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

package knirvchaintransactionsdk_test

import (
	"context"
	"os"
	"testing"

	"github.com/stainless-sdks/knirvchain-transaction-sdk-go"
	"github.com/stainless-sdks/knirvchain-transaction-sdk-go/internal/testutil"
	"github.com/stainless-sdks/knirvchain-transaction-sdk-go/option"
)

func TestUsage(t *testing.T) {
	baseURL := "http://localhost:4010"
	if envURL, ok := os.LookupEnv("TEST_API_BASE_URL"); ok {
		baseURL = envURL
	}
	if !testutil.CheckTestServer(t, baseURL) {
		return
	}
	client := knirvchaintransactionsdk.NewClient(
		option.WithBaseURL(baseURL),
		option.WithAPIKey("My API Key"),
	)
	chain, err := client.Chain.Get(context.TODO())
	if err != nil {
		t.Fatalf("err should be nil: %s", err.Error())
	}
	t.Logf("%+v\n", chain.ChainID)
}
