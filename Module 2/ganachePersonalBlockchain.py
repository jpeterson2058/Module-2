# Imports

import os
from dotenv import load_dotenv
load_dotenv()
from mnemonic import Mnemonic
from bip44 import Wallet
from web3 import Account
from web3 import Web3
w3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))

# Create the Ethereum Wallet and Account Instances

# Use previously established mnemonic
mnemonic = 'elbow scale copper retreat surface jungle ocean bright square trap wage punch'

# Instantiate an new instance of wallet and pass to my mnemonic variable and reviewing the instance.
wallet = Wallet(mnemonic)

wallet

# Calling the derive_account method on the wallet instance and confirming the public key
private, public = wallet.derive_account('eth')

public

# Build the Ethereum account by calling the Account.privateKeyToAccount and passing to private key variable
account = Account.privateKeyToAccount(private)

# Printing address for copying
account_address = account.address
print(account_address)

# Access the balance of funds for the Ethereum account
wei_balance = w3.eth.get_balance(account_address)

# Convert the balance from a denom in wei to ether
ether = w3.fromWei(wei_balance, "ether")

# Print the balance of ether
ether