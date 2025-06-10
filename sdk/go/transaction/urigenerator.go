// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

package knirvchaintransactionsdk

import (
	"context"
	"net/http"

	"github.com/stainless-sdks/knirvchain-transaction-sdk-go/internal/apijson"
	"github.com/stainless-sdks/knirvchain-transaction-sdk-go/internal/requestconfig"
	"github.com/stainless-sdks/knirvchain-transaction-sdk-go/option"
	"github.com/stainless-sdks/knirvchain-transaction-sdk-go/packages/param"
	"github.com/stainless-sdks/knirvchain-transaction-sdk-go/packages/respjson"
)

// UriGeneratorService contains methods and other services that help with
// interacting with the knirvchain-transaction-sdk API.
//
// Note, unlike clients, this service does not read variables from the environment
// automatically. You should not instantiate this service directly, and instead use
// the [NewUriGeneratorService] method instead.
type UriGeneratorService struct {
	Options []option.RequestOption
}

// NewUriGeneratorService generates a new service that applies the given options to
// each request. These options are applied after the parent client's options (if
// there is one), and before any request-specific options.
func NewUriGeneratorService(opts ...option.RequestOption) (r UriGeneratorService) {
	r = UriGeneratorService{}
	r.Options = opts
	return
}

// Generates a new URI and announces it to the network
func (r *UriGeneratorService) New(ctx context.Context, body UriGeneratorNewParams, opts ...option.RequestOption) (res *UriGeneratorNewResponse, err error) {
	opts = append(r.Options[:], opts...)
	path := "uriGenerator"
	err = requestconfig.ExecuteNewRequest(ctx, http.MethodPost, path, body, &res, opts...)
	return
}

type UriGeneratorNewResponse struct {
	// Additional information
	Message string `json:"message"`
	// Resource ID
	ResourceID string `json:"resource_id"`
	// Whether the operation was successful
	Success bool `json:"success"`
	// Generated URI
	Uri string `json:"uri"`
	// JSON contains metadata for fields, check presence with [respjson.Field.Valid].
	JSON struct {
		Message     respjson.Field
		ResourceID  respjson.Field
		Success     respjson.Field
		Uri         respjson.Field
		ExtraFields map[string]respjson.Field
		raw         string
	} `json:"-"`
}

// Returns the unmodified JSON received from the API
func (r UriGeneratorNewResponse) RawJSON() string { return r.JSON.raw }
func (r *UriGeneratorNewResponse) UnmarshalJSON(data []byte) error {
	return apijson.UnmarshalRoot(data, r)
}

type UriGeneratorNewParams struct {
	// Hash of the content
	ContentHash param.Opt[string] `json:"content_hash,omitzero"`
	// Owner address
	Owner param.Opt[string] `json:"owner,omitzero"`
	// Type of resource
	ResourceType param.Opt[string] `json:"resource_type,omitzero"`
	// Additional metadata
	Metadata map[string]any `json:"metadata,omitzero"`
	paramObj
}

func (r UriGeneratorNewParams) MarshalJSON() (data []byte, err error) {
	type shadow UriGeneratorNewParams
	return param.MarshalObject(r, (*shadow)(&r))
}
func (r *UriGeneratorNewParams) UnmarshalJSON(data []byte) error {
	return apijson.UnmarshalRoot(data, r)
}
