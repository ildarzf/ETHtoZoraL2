# ETHtoZoraL2 and Mint NFT (ERC-1152 standart)
ETH Mainnet to ZORA L2 and Mint NFT (ERC-1152 standart)

Выводит ETH через официальный мост в ZORA L2. Если в сети Zora не нулевой баланс то депозит не будет сделан.
Затем минтит фри НФТ . Плата только за минт комиссия Zora. (около 1,5$)  При включенном параметре заниженного газа

wallets.txt вводим приватники 1 приватник одна строчка.

Кошельки перемешиваются

Добавил контроль Газа

########################### ИЗМЕНЯЕМЫЕ ПАРАМЕТРЫ ########################

tokenID = random.randint(1, 7) # ИД НФТ который надо минтит Минтим НФТ стандарта 1155

Quant = 1   # количество  одинаковых НФТ минтить на один кошелек

DEP_FROM = 0.0021# от в ETH

DEP_TO = 0.0035 # до в ETH

sleep_min = 60  # Спим между кошельками

sleep_max = 140

sleep_action_min = 10   # Спим между действиями

sleep_action_max = 25

time_to_conf = 260 #ожидание подтверждения транзакций

Gwei = 20  # если газ выше уходим в ожидание

depos_if = 0.001 # Депозитить если в сети Zora меньше этого значения в ETH иначе переходим к минту

rpc_zora = "https://rpc.zora.co/"   # Нода Майннет Басе

rpc_eth = "https://rpc.ankr.com/eth"    # Нода Эфира

shuffle = True      # False / True Перемешивать кошельки или нет

mint_nft = True     # False / True Минтить НФТ  или нет

low_gas_zora = True # False / True Если не работает на низком газе поставить False или повысить значение в строчке 80


#####################################################################

DONATE на тесты скриптов и благодарность сюда (evm сети) : 0xe7b5cb9f137C663D07EF2539678392650c8e3645

Telegram channel https://t.me/ildar_scripts

Telegram https://t.me/ildarzf

Telegram chat https://t.me/ildarscriptschat
