from web3 import Web3
rpc = 'https://rpcapi.fantom.network/'
w3 = Web3(Web3.HTTPProvider(rpc))
f = open('wallets.txt', 'a', encoding="utf-8")


n_wallets = int(input('Number of wallets to be created: '))
for i in range(n_wallets):
    acc = w3.eth.account.create()
    print(f'[{i+1}]: {acc.address}')
    f.write(f'[{i+1}]: {acc.address}\n')
    f.write(f'[{i+1}]: key {w3.toHex(acc.key)}\n')
    
f.write('\n')