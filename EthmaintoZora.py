import json
from web3 import Web3
import decimal
import random
import time
from tqdm import tqdm

def sleeping(from_sleep, to_sleep):
    x = random.randint(from_sleep, to_sleep)
    for i in tqdm(range(x), desc='sleep ', bar_format='{desc}: {n_fmt}/{total_fmt}'):
        time.sleep(1)

def wallet():
    with open('wallets.txt', 'r') as f:
        wallets = f.read().splitlines()
        return wallets


RPC = "https://rpc.ankr.com/eth"
web3 = Web3(Web3.HTTPProvider(RPC))

########################### ИЗМЕНЯЕМЫЕ ПАРАМЕТРЫ ##############################################################################
proc_gETH_min = 20 # от 20 процентов аккаунта слать в другую тестовую сеть
proc_gETH_max = 25 # 25 %
sleep_min = 60  # Спим между кошельками
sleep_max = 140
Gwei = 20  # если газ выше уходим в ожидание
############################################################################################################################

def bridge():
    wallets = wallet()
    random.shuffle(wallets)
    bridge_abi ='[{"inputs":[{"internalType":"contract L2OutputOracle","name":"_l2Oracle","type":"address"},{"internalType":"address","name":"_guardian","type":"address"},{"internalType":"bool","name":"_paused","type":"bool"},{"internalType":"contract SystemConfig","name":"_config","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint8","name":"version","type":"uint8"}],"name":"Initialized","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Paused","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":true,"internalType":"uint256","name":"version","type":"uint256"},{"indexed":false,"internalType":"bytes","name":"opaqueData","type":"bytes"}],"name":"TransactionDeposited","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Unpaused","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"withdrawalHash","type":"bytes32"},{"indexed":false,"internalType":"bool","name":"success","type":"bool"}],"name":"WithdrawalFinalized","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"withdrawalHash","type":"bytes32"},{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"WithdrawalProven","type":"event"},{"inputs":[],"name":"GUARDIAN","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"L2_ORACLE","outputs":[{"internalType":"contract L2OutputOracle","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"SYSTEM_CONFIG","outputs":[{"internalType":"contract SystemConfig","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_value","type":"uint256"},{"internalType":"uint64","name":"_gasLimit","type":"uint64"},{"internalType":"bool","name":"_isCreation","type":"bool"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"depositTransaction","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"donateETH","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"components":[{"internalType":"uint256","name":"nonce","type":"uint256"},{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"target","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256","name":"gasLimit","type":"uint256"},{"internalType":"bytes","name":"data","type":"bytes"}],"internalType":"struct Types.WithdrawalTransaction","name":"_tx","type":"tuple"}],"name":"finalizeWithdrawalTransaction","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"name":"finalizedWithdrawals","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bool","name":"_paused","type":"bool"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_l2OutputIndex","type":"uint256"}],"name":"isOutputFinalized","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"l2Sender","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint64","name":"_byteCount","type":"uint64"}],"name":"minimumGasLimit","outputs":[{"internalType":"uint64","name":"","type":"uint64"}],"stateMutability":"pure","type":"function"},{"inputs":[],"name":"params","outputs":[{"internalType":"uint128","name":"prevBaseFee","type":"uint128"},{"internalType":"uint64","name":"prevBoughtGas","type":"uint64"},{"internalType":"uint64","name":"prevBlockNum","type":"uint64"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"pause","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"paused","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"components":[{"internalType":"uint256","name":"nonce","type":"uint256"},{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"target","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256","name":"gasLimit","type":"uint256"},{"internalType":"bytes","name":"data","type":"bytes"}],"internalType":"struct Types.WithdrawalTransaction","name":"_tx","type":"tuple"},{"internalType":"uint256","name":"_l2OutputIndex","type":"uint256"},{"components":[{"internalType":"bytes32","name":"version","type":"bytes32"},{"internalType":"bytes32","name":"stateRoot","type":"bytes32"},{"internalType":"bytes32","name":"messagePasserStorageRoot","type":"bytes32"},{"internalType":"bytes32","name":"latestBlockhash","type":"bytes32"}],"internalType":"struct Types.OutputRootProof","name":"_outputRootProof","type":"tuple"},{"internalType":"bytes[]","name":"_withdrawalProof","type":"bytes[]"}],"name":"proveWithdrawalTransaction","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"name":"provenWithdrawals","outputs":[{"internalType":"bytes32","name":"outputRoot","type":"bytes32"},{"internalType":"uint128","name":"timestamp","type":"uint128"},{"internalType":"uint128","name":"l2OutputIndex","type":"uint128"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"unpause","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"version","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"stateMutability":"payable","type":"receive"}]'
    BaseBridge = web3.to_checksum_address('0x1a0ad011913A150f69f6A19DF447A0CfD9551054') # contract ZORA deposit
    bridge = web3.eth.contract(address=BaseBridge, abi=bridge_abi)


    num = 0
    for wall in wallets:
      while True:
        current_gas_price = web3.eth.gas_price
        current_gas_price_gwei = web3.from_wei(current_gas_price, 'gwei')
        #print('GWEI', round(current_gas_price_gwei))
        if current_gas_price_gwei <= Gwei:
            num = num+1
            key = wall
            account = web3.eth.account.from_key(key).address
            nonce = web3.eth.get_transaction_count(account)
            gas_price = web3.eth.gas_price
            proc_gETH = round(random.uniform(proc_gETH_min, proc_gETH_max), 3)
            balance_gas = web3.eth.get_balance(account)
            balance_gas_2dec = balance_gas / (10**18)
            value_2dec = round(balance_gas_2dec * (proc_gETH / 100),6)

            _value = int(value_2dec * (10 ** 18))
            _to = account
            _gasLimit = 100000
            _isCreation = False
            data_k = ''
            _data = bytes(data_k, 'ascii')
            gasLimit = web3.eth.estimate_gas(
                {'to': Web3.to_checksum_address(account), 'from': Web3.to_checksum_address(account),
                 'value': web3.to_wei(0.0001, 'ether')}) + random.randint(10000, 30000)
            tx = bridge.functions.depositTransaction(_to, _value, _gasLimit, _isCreation, _data
                ).build_transaction({
                'value': _value,
                'from': account,
                'gas': int(gasLimit*3),
                'gasPrice': int(gas_price),
                'nonce': web3.eth.get_transaction_count(account),
                })
            signed_tx = web3.eth.account.sign_transaction(tx, key)
            tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            account = web3.eth.account.from_key(key).address
            print(num, account, key)
            print(f'Transaction hash: https://etherscan.io/tx/{tx_hash.hex()}')
            print('Waiting for receipt...')
            tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
            print('Отправил')
            break
        else:
            print('GWEI', round(current_gas_price_gwei, 1))
            print('Ждем нормальный газ')
            sleeping(sleep_min,sleep_max)    # спим и снова проверяем газ

      sleeping(sleep_min, sleep_max)  # задержка между кошельками


if __name__ == '__main__':
    bridge()
