package transaction

// Wallet represents a blockchain wallet
type Wallet struct {
	// Your wallet implementation fields
}

func (w *Wallet) GetAddress() string {
	// Your implementation
	return ""
}

func (w *Wallet) GetPublicKeyHex() string {
	// Your implementation
	return ""
}

func (w *Wallet) SignTransaction(txn *Transaction) error {
	// Your signing implementation
	return nil
}

type TransactionType string

const (
	TransactionTypeMCPRegisterCapability TransactionType = "mcp_register_capability"
	// Add other transaction types
)

// MCP Types (since they're in the same package)
type CapabilityType string
type ResourceType string



type ResourceDescriptor struct {
	ID           string       `json:"id"`
	ResourceType ResourceType `json:"resource_type"`
	ContentHash  string       `json:"content_hash"`
	Schema       struct {
		LocationHints []string `json:"location_hints"`
	} `json:"schema"`
}

const (
	ResourceTypePlugin ResourceType = "plugin"
	// Add other resource types
)

// Constructor function
func NewMCPTransaction(from, to string, value uint64, data []byte, txType TransactionType, fee uint64, timestamp int64) *Transaction {
	// Your transaction creation logic
	return &Transaction{
		TransactionHash: calculateHash(from, to, value, data, txType, fee, timestamp),
		// Set other fields
	}
}

// Helper function (implement your hash calculation)
func calculateHash(_ string, _ string, _ uint64, _ []byte, _ TransactionType, _ uint64, _ int64) string {
	// Your hash calculation logic
	return "calculated_hash"
}
