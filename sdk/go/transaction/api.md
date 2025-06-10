# Chain

Response Types:

- <a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go">knirvchaintransactionsdk</a>.<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go#ChainGetResponse">ChainGetResponse</a>

Methods:

- <code title="get /chain">client.Chain.<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go#ChainService.Get">Get</a>(ctx <a href="https://pkg.go.dev/context">context</a>.<a href="https://pkg.go.dev/context#Context">Context</a>) (<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go">knirvchaintransactionsdk</a>.<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go#ChainGetResponse">ChainGetResponse</a>, <a href="https://pkg.go.dev/builtin#error">error</a>)</code>

# Block

Params Types:

- <a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go">knirvchaintransactionsdk</a>.<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go#BlockParam">BlockParam</a>

Response Types:

- <a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go">knirvchaintransactionsdk</a>.<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go#Block">Block</a>
- <a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go">knirvchaintransactionsdk</a>.<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go#BlockSubmitResponse">BlockSubmitResponse</a>

Methods:

- <code title="post /block">client.Block.<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go#BlockService.Submit">Submit</a>(ctx <a href="https://pkg.go.dev/context">context</a>.<a href="https://pkg.go.dev/context#Context">Context</a>, body <a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go">knirvchaintransactionsdk</a>.<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go#BlockSubmitParams">BlockSubmitParams</a>) (<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go">knirvchaintransactionsdk</a>.<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go#BlockSubmitResponse">BlockSubmitResponse</a>, <a href="https://pkg.go.dev/builtin#error">error</a>)</code>

# Transaction

Params Types:

- <a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go">knirvchaintransactionsdk</a>.<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go#TransactionParam">TransactionParam</a>

Response Types:

- <a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go">knirvchaintransactionsdk</a>.<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go#Transaction">Transaction</a>
- <a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go">knirvchaintransactionsdk</a>.<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go#TransactionSubmitResponse">TransactionSubmitResponse</a>

Methods:

- <code title="post /transaction">client.Transaction.<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go#TransactionService.Submit">Submit</a>(ctx <a href="https://pkg.go.dev/context">context</a>.<a href="https://pkg.go.dev/context#Context">Context</a>, body <a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go">knirvchaintransactionsdk</a>.<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go#TransactionSubmitParams">TransactionSubmitParams</a>) (<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go">knirvchaintransactionsdk</a>.<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go#TransactionSubmitResponse">TransactionSubmitResponse</a>, <a href="https://pkg.go.dev/builtin#error">error</a>)</code>

# TxnPool

Methods:

- <code title="get /txn_pool">client.TxnPool.<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go#TxnPoolService.Get">Get</a>(ctx <a href="https://pkg.go.dev/context">context</a>.<a href="https://pkg.go.dev/context#Context">Context</a>) ([]<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go">knirvchaintransactionsdk</a>.<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go#Transaction">Transaction</a>, <a href="https://pkg.go.dev/builtin#error">error</a>)</code>

# Info

Response Types:

- <a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go">knirvchaintransactionsdk</a>.<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go#InfoGetResponse">InfoGetResponse</a>

Methods:

- <code title="get /info">client.Info.<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go#InfoService.Get">Get</a>(ctx <a href="https://pkg.go.dev/context">context</a>.<a href="https://pkg.go.dev/context#Context">Context</a>) (<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go">knirvchaintransactionsdk</a>.<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go#InfoGetResponse">InfoGetResponse</a>, <a href="https://pkg.go.dev/builtin#error">error</a>)</code>

# Health

Response Types:

- <a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go">knirvchaintransactionsdk</a>.<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go#HealthCheckResponse">HealthCheckResponse</a>

Methods:

- <code title="get /health">client.Health.<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go#HealthService.Check">Check</a>(ctx <a href="https://pkg.go.dev/context">context</a>.<a href="https://pkg.go.dev/context#Context">Context</a>) (<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go">knirvchaintransactionsdk</a>.<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go#HealthCheckResponse">HealthCheckResponse</a>, <a href="https://pkg.go.dev/builtin#error">error</a>)</code>

# Ping

Methods:

- <code title="get /ping">client.Ping.<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go#PingService.Check">Check</a>(ctx <a href="https://pkg.go.dev/context">context</a>.<a href="https://pkg.go.dev/context#Context">Context</a>) (<a href="https://pkg.go.dev/builtin#string">string</a>, <a href="https://pkg.go.dev/builtin#error">error</a>)</code>

# Peers

Response Types:

- <a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go">knirvchaintransactionsdk</a>.<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go#PeerListResponse">PeerListResponse</a>

Methods:

- <code title="get /peers">client.Peers.<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go#PeerService.List">List</a>(ctx <a href="https://pkg.go.dev/context">context</a>.<a href="https://pkg.go.dev/context#Context">Context</a>) ([]<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go">knirvchaintransactionsdk</a>.<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go#PeerListResponse">PeerListResponse</a>, <a href="https://pkg.go.dev/builtin#error">error</a>)</code>

# UriGenerator

Response Types:

- <a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go">knirvchaintransactionsdk</a>.<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go#UriGeneratorNewResponse">UriGeneratorNewResponse</a>

Methods:

- <code title="post /uriGenerator">client.UriGenerator.<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go#UriGeneratorService.New">New</a>(ctx <a href="https://pkg.go.dev/context">context</a>.<a href="https://pkg.go.dev/context#Context">Context</a>, body <a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go">knirvchaintransactionsdk</a>.<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go#UriGeneratorNewParams">UriGeneratorNewParams</a>) (<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go">knirvchaintransactionsdk</a>.<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go#UriGeneratorNewResponse">UriGeneratorNewResponse</a>, <a href="https://pkg.go.dev/builtin#error">error</a>)</code>

# Mcp

Response Types:

- <a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go">knirvchaintransactionsdk</a>.<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go#ContextRecord">ContextRecord</a>

Methods:

- <code title="get /mcp/context/{context_id}">client.Mcp.<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go#McpService.Get">Get</a>(ctx <a href="https://pkg.go.dev/context">context</a>.<a href="https://pkg.go.dev/context#Context">Context</a>, contextID <a href="https://pkg.go.dev/builtin#string">string</a>) (<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go">knirvchaintransactionsdk</a>.<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go#ContextRecord">ContextRecord</a>, <a href="https://pkg.go.dev/builtin#error">error</a>)</code>
- <code title="get /mcp/capabilities">client.Mcp.<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go#McpService.GetCapabilities">GetCapabilities</a>(ctx <a href="https://pkg.go.dev/context">context</a>.<a href="https://pkg.go.dev/context#Context">Context</a>, query <a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go">knirvchaintransactionsdk</a>.<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go#McpGetCapabilitiesParams">McpGetCapabilitiesParams</a>) ([]<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go">knirvchaintransactionsdk</a>.<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go#CapabilityDescriptorUnion">CapabilityDescriptorUnion</a>, <a href="https://pkg.go.dev/builtin#error">error</a>)</code>
- <code title="get /mcp/contexts">client.Mcp.<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go#McpService.GetContexts">GetContexts</a>(ctx <a href="https://pkg.go.dev/context">context</a>.<a href="https://pkg.go.dev/context#Context">Context</a>, query <a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go">knirvchaintransactionsdk</a>.<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go#McpGetContextsParams">McpGetContextsParams</a>) ([]<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go">knirvchaintransactionsdk</a>.<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go#ContextRecord">ContextRecord</a>, <a href="https://pkg.go.dev/builtin#error">error</a>)</code>

## Capability

Params Types:

- <a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go">knirvchaintransactionsdk</a>.<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go#BaseDescriptorParam">BaseDescriptorParam</a>
- <a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go">knirvchaintransactionsdk</a>.<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go#CapabilityDescriptorUnionParam">CapabilityDescriptorUnionParam</a>

Response Types:

- <a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go">knirvchaintransactionsdk</a>.<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go#BaseDescriptor">BaseDescriptor</a>
- <a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go">knirvchaintransactionsdk</a>.<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go#CapabilityDescriptorUnion">CapabilityDescriptorUnion</a>
- <a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go">knirvchaintransactionsdk</a>.<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go#McpCapabilityUpdateResponse">McpCapabilityUpdateResponse</a>
- <a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go">knirvchaintransactionsdk</a>.<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go#McpCapabilityInvokeResponse">McpCapabilityInvokeResponse</a>
- <a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go">knirvchaintransactionsdk</a>.<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go#McpCapabilityPrepareRegistrationResponse">McpCapabilityPrepareRegistrationResponse</a>

Methods:

- <code title="get /mcp/capability/{capability_id}">client.Mcp.Capability.<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go#McpCapabilityService.Get">Get</a>(ctx <a href="https://pkg.go.dev/context">context</a>.<a href="https://pkg.go.dev/context#Context">Context</a>, capabilityID <a href="https://pkg.go.dev/builtin#string">string</a>) (<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go">knirvchaintransactionsdk</a>.<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go#CapabilityDescriptorUnion">CapabilityDescriptorUnion</a>, <a href="https://pkg.go.dev/builtin#error">error</a>)</code>
- <code title="post /mcp/capability/update">client.Mcp.Capability.<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go#McpCapabilityService.Update">Update</a>(ctx <a href="https://pkg.go.dev/context">context</a>.<a href="https://pkg.go.dev/context#Context">Context</a>, body <a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go">knirvchaintransactionsdk</a>.<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go#McpCapabilityUpdateParams">McpCapabilityUpdateParams</a>) (<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go">knirvchaintransactionsdk</a>.<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go#McpCapabilityUpdateResponse">McpCapabilityUpdateResponse</a>, <a href="https://pkg.go.dev/builtin#error">error</a>)</code>
- <code title="post /mcp/capability/invoke">client.Mcp.Capability.<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go#McpCapabilityService.Invoke">Invoke</a>(ctx <a href="https://pkg.go.dev/context">context</a>.<a href="https://pkg.go.dev/context#Context">Context</a>, body <a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go">knirvchaintransactionsdk</a>.<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go#McpCapabilityInvokeParams">McpCapabilityInvokeParams</a>) (<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go">knirvchaintransactionsdk</a>.<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go#McpCapabilityInvokeResponse">McpCapabilityInvokeResponse</a>, <a href="https://pkg.go.dev/builtin#error">error</a>)</code>
- <code title="post /mcp/capability/prepare_registration">client.Mcp.Capability.<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go#McpCapabilityService.PrepareRegistration">PrepareRegistration</a>(ctx <a href="https://pkg.go.dev/context">context</a>.<a href="https://pkg.go.dev/context#Context">Context</a>, body <a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go">knirvchaintransactionsdk</a>.<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go#McpCapabilityPrepareRegistrationParams">McpCapabilityPrepareRegistrationParams</a>) (<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go">knirvchaintransactionsdk</a>.<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go#McpCapabilityPrepareRegistrationResponse">McpCapabilityPrepareRegistrationResponse</a>, <a href="https://pkg.go.dev/builtin#error">error</a>)</code>
- <code title="get /mcp/capability/{capability_id}/invocations">client.Mcp.Capability.<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go#McpCapabilityService.GetInvocations">GetInvocations</a>(ctx <a href="https://pkg.go.dev/context">context</a>.<a href="https://pkg.go.dev/context#Context">Context</a>, capabilityID <a href="https://pkg.go.dev/builtin#string">string</a>) ([]<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go">knirvchaintransactionsdk</a>.<a href="https://pkg.go.dev/github.com/stainless-sdks/knirvchain-transaction-sdk-go#ContextRecord">ContextRecord</a>, <a href="https://pkg.go.dev/builtin#error">error</a>)</code>
