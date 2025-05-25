from wallet import Wallet
from mining import Miner
from blockchain import Blockchain
from transactions import Transaction

blockchain = Blockchain()
wallet = Wallet()
miner = Miner(blockchain, wallet.get_address())

def display_menu():
    print("\n--- Bitcoin 2 CLI ---")
    print("1. Create new wallet")
    print("2. Show wallet address")
    print("3. Check balance")
    print("4. Send coins")
    print("5. Mine block")
    print("6. Show blockchain")
    print("0. Exit")

def get_balance(address):
    balance = 0
    for block in blockchain.chain:
        for tx in block.transactions:
            if tx['recipient'] == address:
                balance += tx['amount']
            if tx['sender'] == address:
                balance -= tx['amount']
    return balance

while True:
    display_menu()
    choice = input("Select: ")

    if choice == "1":
        wallet = Wallet()
        print("New wallet created.")
    elif choice == "2":
        print("Wallet Address:", wallet.get_address())
    elif choice == "3":
        bal = get_balance(wallet.get_address())
        print("Balance:", bal, "BTC2")
    elif choice == "4":
        recipient = input("Recipient Address: ")
        amount = float(input("Amount to send: "))
        msg = f"{wallet.get_address()}{recipient}{amount}".encode()
        signature = wallet.sign_transaction(msg)
        tx = Transaction(wallet.get_address(), recipient, amount, signature)
        blockchain.add_new_transaction(tx.to_dict())
        print("Transaction added.")
    elif choice == "5":
        mined_block = miner.mine()
        print(f"Block #{mined_block} mined successfully.")
    elif choice == "6":
        for block in blockchain.chain:
            print(block.__dict__)
    elif choice == "0":
        break
    else:
        print("Invalid choice.")