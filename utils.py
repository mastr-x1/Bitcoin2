def serialize_transaction(tx):
    return f"{tx['sender']}{tx['recipient']}{tx['amount']}".encode()