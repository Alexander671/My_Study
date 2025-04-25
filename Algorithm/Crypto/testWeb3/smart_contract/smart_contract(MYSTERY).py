from web3 import Web3, HTTPProvider

from web3.middleware import geth_poa_middleware

import environ # Initialise environment variables
env = environ.Env()
environ.Env.read_env()

INFURA_PROJECT_ID = env('WEB3_INFURA_PROJECT_ID')
ADDRESS_CONTRACT_2 = env('ADDRESS_CONTRACT_2')

ABI_2 = env('ABI_2')

w3 = Web3(Web3.HTTPProvider(INFURA_PROJECT_ID))

w3.middleware_onion.inject(geth_poa_middleware, layer=0)

assert True is w3.isConnected()

print('----Network connected!-----')
print(f'----{w3.api}-----')
print(f'----{w3.clientVersion}-----')
print('----------------------------')

block = w3.eth.get_block('latest').number
gas_price = w3.eth.gas_price

print('\n--Info from Ethereum:--')
print(f'Latest block number in Ethereum: {block}')
print(f'Gas Price: {gas_price}')


contract_instance = w3.eth.contract(address=ADDRESS_CONTRACT_2, abi=ABI_2)

name = contract_instance.functions.name().call()
max_supply = contract_instance.functions.MAX_SUPPLY().call()
owner = contract_instance.functions.owner().call()
totalSupply = contract_instance.functions.totalSupply().call()
print('\n--Info about smart-contract:--')
print(f'Name of smart-contract: {name}')
print(f'Smart-contract owner: {owner}')
print(f'Total Supply: {totalSupply}')