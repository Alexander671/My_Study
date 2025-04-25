from web3 import Web3, EthereumTesterProvider

from web3.middleware import geth_poa_middleware

import environ # Initialise environment variables
env = environ.Env()
environ.Env.read_env()

INFURA_PROJECT_ID = env('WEB3_INFURA_PROJECT_ID')
ADDRESS_CONTRACT_1 = env('ADDRESS_CONTRACT_1')
ABI_1 = env('ABI_1')
ME = env('ME')
RANDOM_MEDIA = "https://pbs.twimg.com/profile_images/1173161429266030592/lJCNA_JC_400x400.jpg"



w3 = Web3(Web3.HTTPProvider(INFURA_PROJECT_ID))

w3.middleware_onion.inject(geth_poa_middleware, layer=0)

from random import choice
from string import ascii_letters

        

assert True is w3.isConnected()

print('----Network connected!-----')
print(f'----{w3.api}-----')
print(f'----{w3.clientVersion}-----')
print('----------------------------')
print()
block = w3.eth.get_block('latest').number
gas_price = w3.eth.gas_price

print(f'Latest block number in Ethereum: {block}')
print(f'Gas Price: {gas_price}')

print()

# инициализация контракта
contract_instance = w3.eth.contract(address=ADDRESS_CONTRACT_1, abi=ABI_1)

# создание случайной строки
unique_hash = ''.join(choice(ascii_letters + ''.join(map(str, range(0,10)))) for i in range(20))

# вызов функции на чтоение
a = contract_instance.functions.totalSupply().call() # ?
print(a)


# mnemonic private key
with open('.8bv1b0mAL') as keyfile:
    encrypted_key = keyfile.read()

# создаем аккаунт?
w3.eth.account.enable_unaudited_hdwallet_features()
account = w3.eth.account.from_mnemonic(encrypted_key)
print(account)
print('Данные аккаунта')
print(f'Address:\n{account.address}\n') # The address for the chosen path
print(f'Key:\n{account.key}')


nonce = w3.eth.get_transaction_count(ME)  

print(f'\n\nnonce:{nonce}')

w3.eth.default_account = ME
unicorn_txn = contract_instance.functions.mint(
            ME,
            unique_hash,
            RANDOM_MEDIA).buildTransaction({
        'from'  : ME,
        'nonce' : nonce})

print(f'{unicorn_txn}\n')
print(f'gas price:{w3.eth.gas_price}')
print(f'gas limit: {w3.eth.getBlock("latest").gasLimit}')
print(f'balance: {w3.eth.getBalance(ME)}') 
gas = unicorn_txn['gas']
print(f'{gas}')


signed = w3.eth.account.sign_transaction(unicorn_txn, account.privateKey)

# print(signed.rawTransaction)
# print(signed.hash)
# print(signed.s)
# print(signed.v)

hash_transaction = w3.eth.send_raw_transaction(signed.rawTransaction)  
print(hash_transaction)

