def updateBlock(action, fileName, ipAddress, timestamp):
    url = "https://testnet2.matic.network"
    web3 = Web3(Web3.HTTPProvider(url))
    web3.eth.getBalance("0xe59D5d34749FaD3b70d0c5FD0B5229Bf9c4E7Dc4")

    abi = [{"type":"function","stateMutability":"nonpayable","payable":False,"outputs":[],"name":"setLogs","inputs":[{"type":"string","name":"_action","internalType":"string"},{"type":"string","name":"_filename","internalType":"string"},{"type":"string","name":"_ipaddress","internalType":"string"},{"type":"string","name":"_datetime","internalType":"string"}],"constant":False},{"type":"constructor","stateMutability":"nonpayable","payable":False,"inputs":[]}]


    contract = web3.eth.contract(address="0xf58CAA96eCa1fB2a42F25912ffFA4B37482544A8", abi=abi)

    account = web3.eth.account.create("KEYSMASH FJAFJKLDSKF7JKFDJ 1530")

    tx = {
        'nonce': 0,
        "from": account.address,
        'to': "0xf58CAA96eCa1fB2a42F25912ffFA4B37482544A8",
        'data': contract.encodeABI(fn_name ="setLogs", args= [action, fileName, ipAddress, timestamp]),
        'gas': 2000000,
        'gasPrice': "0x0",
    }

    # tx_hash = contract.functions.setLogs('HEELLL', "fadfdsf", "afdf", "34324").transact({"from": "0xe59D5d34749FaD3b70d0c5FD0B5229Bf9c4E7Dc4"})

    signed_tx = web3.eth.account.signTransaction(tx, account.privateKey)

    tx_h = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    # web3.eth.waitForTransactionReceipt(tx_hash)
    # print(web3.toHex(tx_hash))