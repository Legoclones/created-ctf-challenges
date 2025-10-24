from web3 import Web3


### CONSTANTS ###
RPC_URL = "http://localhost:8080/ad50400e-165f-42ad-86aa-c106f2e15be3"
PRIVKEY = "ef50430a43ef5b6aa18070845d8ca20ea115a0fee543a18e808e82f715c8fa94"
SETUP_CONTRACT_ADDR = "0xD84bd35B825CB2c85509B58D13a0CF3d66060590"
WALLET_ADDR = "0xBE1B4fCE6c7f57BB1411A4aa07A3f46577F22C23"


### INITIALIZATIONS ###
w3 = Web3(Web3.HTTPProvider(RPC_URL))
account = w3.eth.account.from_key(PRIVKEY)
CONTRACT_ABI = [
	{
		"inputs": [],
		"stateMutability": "payable",
		"type": "constructor"
	},
	{
		"inputs": [],
		"name": "isSolved",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "argument",
				"type": "string"
			}
		],
		"name": "solveChall",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	}
]
contract = w3.eth.contract(address=SETUP_CONTRACT_ADDR, abi=CONTRACT_ABI)


### SOLVE THE CHALLENGE ###
transaction = contract.functions.solveChall('hackerschallenge').build_transaction({
    'from': WALLET_ADDR,
    'nonce': w3.eth.get_transaction_count(WALLET_ADDR),
    'gas': 210000,
    'gasPrice': w3.to_wei('50', 'gwei')
})
signed_transaction = w3.eth.account.sign_transaction(transaction, PRIVKEY)
transaction_hash = w3.eth.send_raw_transaction(signed_transaction.raw_transaction)
transaction_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash)

print(f"Transaction hash: {transaction_hash.hex()}")
print(f"Transaction status: {transaction_receipt.status}")
print(dict(transaction_receipt))

print(contract.functions.isSolved().call())