# KNIRVCHAIN SDK

[![TypeScript](https://img.shields.io/badge/TypeScript-4.9%2B-blue)](https://www.typescriptlang.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

The KNIRVCHAIN SDK is a comprehensive toolkit for interacting with the KNIRVCHAIN network, a decentralized blockchain infrastructure. This SDK provides developers with the tools needed to build applications that can interact with the KNIRVCHAIN ecosystem.

## Overview

The KNIRVCHAIN SDK consists of two main components:

1. **Transaction SDK** - For interacting with the KNIRVCHAIN Transaction API
2. **Transmission SDK** - For resolving and accessing resources on the KNIRVCHAIN network

Together, these components provide a complete solution for building applications on the KNIRVCHAIN platform.

## Components

### Transaction SDK

The Transaction SDK provides convenient access to the KNIRVCHAIN Transaction REST API from server-side TypeScript or JavaScript. It allows developers to:

- Interact with blockchain data
- Retrieve chain information
- Handle transactions securely
- Manage API requests with built-in error handling and retries

Key features:
- Type-safe API with full TypeScript support
- Comprehensive error handling
- Automatic retries for transient errors
- Configurable timeouts and logging
- Support for multiple JavaScript runtimes (Node.js, browsers, Deno, Bun)

[Learn more about the Transaction SDK](./transaction/README.md)

### Transmission SDK

The Transmission SDK provides a high-level interface for interacting with the KNIRVCHAIN network's peer-to-peer layer. It simplifies:

- Parsing `knirv://` URIs
- Discovering peers on the private DHT
- Connecting to peers and fetching resources
- Handling network errors gracefully

Key features:
- URI parsing and manipulation
- Peer discovery on the KNIRVCHAIN DHT
- Resource fetching via libp2p streams
- Comprehensive error handling
- Promise-based API for easy integration
- Full TypeScript support

[Learn more about the Transmission SDK](./transmission/README.md)

#### KNIRV Tunnel Client

For nodes operating behind NAT, the KNIRV Tunnel Client establishes a persistent control connection with the central relay server, enabling:

- NAT traversal for KNIRVCHAIN nodes
- Automatic reconnection if the connection is lost
- Node identification with peer ID, chain ID, and other details

[Learn more about the KNIRV Tunnel Client](./transmission/knirv-tunnel-client/README.md)

## Installation

Each component can be installed separately depending on your needs:

### Transaction SDK

```bash
npm install knirvchain-transaction-sdk
```

### Transmission SDK

```bash
npm install knirv-transmission-sdk
```

### KNIRV Tunnel Client

```bash
# Navigate to the tunnel client directory
cd transmission/knirv-tunnel-client
npm install
```

## Usage Examples

### Transaction SDK

```typescript
import KnirvchainTransactionSDK from 'knirvchain-transaction-sdk';

const client = new KnirvchainTransactionSDK({
  apiKey: process.env['KNIRVCHAIN_TRANSACTION_SDK_API_KEY'],
});

// Retrieve chain information
const chain = await client.chain.retrieve();
console.log(chain.chain_id);
```

### Transmission SDK

```typescript
import { KnirvClient } from 'knirv-transmission-sdk';

async function main() {
  // Create a client with bootstrap peers
  const client = new KnirvClient({
    bootstrapPeers: [
      '/ip4/104.131.131.82/tcp/4001/p2p/QmaCpDMGvV2BGHeYERUEnRQAwe3N8SzbUtfsmvsqQLuvuJ',
    ],
    logEnabled: true
  });
  
  try {
    // Bootstrap the client (connect to DHT network)
    await client.bootstrap();
    
    // Fetch a resource
    const resource = await client.fetchResource('knirv://mychain-alpha.chain/block?number=123');
    
    // Use the resource data
    console.log(resource.toString());
  } finally {
    // Close the client
    await client.stop();
  }
}

main().catch(console.error);
```

## Requirements

- TypeScript >= 4.9
- Node.js 20 LTS or later
- Web browsers (Chrome, Firefox, Safari, Edge)
- Deno v1.28.0 or higher
- Bun 1.0 or later

## Error Handling

Both SDKs provide comprehensive error handling with specific error types to help with debugging and error management. See the individual component READMEs for detailed information on error handling.

## Documentation

For detailed documentation on each component:

- [Transaction SDK Documentation](./transaction/api.md)
- [Transmission SDK Documentation](./transmission/README.md)
- [KNIRV Tunnel Client Documentation](./transmission/knirv-tunnel-client/README.md)

## Examples

Check out the example directories for complete examples of using the SDKs:

- [Transaction SDK Examples](./transaction/examples)
- [Transmission SDK Examples](./transmission/examples)

## License

[MIT License](./transaction/LICENSE)