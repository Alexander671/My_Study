from web3 import Web3, EthereumTesterProvider

w3 = Web3(Web3.HTTPProvider("https://rinkeby.infura.io/v3/95ade9432ee5463593c832ec436085a3"))

w3.isConnected()


print(w3.isConnected())