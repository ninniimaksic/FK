import unittest
from bank import Bank, TransactionType
from transaction import Transaction
from customer import Customer

class TestBank(unittest.TestCase):
    def setUp(self):
        self.bank = Bank()

    def test_deposit(self):
        transaction = {
            "type": TransactionType.DEPOSIT.value,
            "customer": 1,
            "amount": 100.0,
            "id": 1
        }
        self.bank.handle_transaction(transaction)
        self.assertIn(1, self.bank.customers)
        self.assertEqual(self.bank.customers[1].available, 100.0)

    def test_withdraw(self):
        deposit_transaction = {
            "type": TransactionType.DEPOSIT.value,
            "customer": 1,
            "amount": 100.0,
            "id": 1
        }
        withdraw_transaction = {
            "type": TransactionType.WITHDRAW.value,
            "customer": 1,
            "amount": 50.0,
            "id": 2
        }
        self.bank.handle_transaction(deposit_transaction)
        self.bank.handle_transaction(withdraw_transaction)
        self.assertEqual(self.bank.customers[1].available, 50.0)

    def test_invalid_withdraw(self):
        withdraw_transaction = {
            "type": TransactionType.WITHDRAW.value,
            "customer": 1,
            "amount": 50.0,
            "id": 1
        }
        self.bank.handle_transaction(withdraw_transaction)
        self.assertNotIn(1, self.bank.customers)

if __name__ == '__main__':
    unittest.main()
