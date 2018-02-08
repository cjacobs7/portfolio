'''
Short script to help us take our potential private keys
and check to see if they have any bitcoins in their associated
wallets.

We use pybitcoin after we read in our CSV to hash a public key
from the presumed private key. Then we use the blockchain API
to access the amount of BTC in each wallet. Then we write out
the wallets, private keys, and values to a a text file.

@author CJacobs
@updated 1/12/18

'''

import requests
from pybitcoin import BitcoinPrivateKey
import time

#create set to add data
keys = set()

#read csv from BigQuery
with open('BitcoinBigQuery.csv') as file:
    for line in file.read().split("\n"):
        if line:
            repo, file, private_key = line.split(",")
            keys.add(private_key)

#prep output
output_filename = "AreWeRich.txt"
access = open(output_filename, "w")
            
for private in keys:
    try:
        #legit address check
        p = BitcoinPrivateKey(private)
        pub = p.public_key().address()
        #access info through blockchain API
        r = requests.get("https://blockchain.info/rawaddr/{}".format(pub))
        time.sleep(1)
        access.write("{} {} {:20} {:20} {:20}\n".format(private, pub,
                r.json()['final_balance'],
                r.json()['total_received'],
                r.json()['total_sent']))

    except(AssertionError, IndexError):
        pass
    except ValueError:
        print r
        print r.text