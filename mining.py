from blockchain import Blockchain
from transactions import Transaction

class Miner:
    def __init__(self, blockchain: Blockchain, miner_address: str):
        self.blockchain = blockchain
        self.miner_address = miner_address

    def calculate_reward(self, height):
        initial_reward = 50
        halving_interval = 210000
        halvings = height // halving_interval
        return initial_reward / (2 ** halvings)

    def mine(self):
        last_block = self.blockchain.get_last_block()
        reward = self.calculate_reward(last_block.index + 1)
        reward_tx = Transaction("network", self.miner_address, reward, "reward-signature")
        self.blockchain.add_new_transaction(reward_tx.to_dict())
        print(f"Mining block #{last_block.index + 1} with reward: {reward} BTC2...")
        index = self.blockchain.mine()
        return index