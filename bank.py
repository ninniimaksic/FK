from enum import Enum
from gettext import translation

from customer import Customer
from transaction import Transaction

class TransactionType(Enum):
    DEPOSIT = "deposit"
    WITHDRAW = "withdraw"
    DISPUTE = "dispute"
    RESOLVE = "resolve"
    CHARGEBACK = "chargeback"


class Bank:
    
    def __init__(self):
        self.customers = {}
        self.transactions = {}           


    def handle_transaction(self, transaction):
        type = transaction["type"]
        if type == TransactionType.DEPOSIT.value:
            self.deposit(transaction["customer"], transaction["amount"], transaction["id"])
        elif type == TransactionType.WITHDRAW.value:
            self.withdraw(transaction["customer"], transaction["amount"], transaction["id"])
        elif type == TransactionType.DISPUTE.value:
            self.dispute(transaction["customer"], transaction["id"])
        elif type == TransactionType.RESOLVE.value:
            self.resolve(transaction["customer"], transaction["id"])
        elif type == TransactionType.CHARGEBACK.value:
            self.chargeback(transaction["customer"], transaction["id"])

    def deposit(self, customer_id, amount, transaction_id):
        amount = float(amount)
        if customer_id not in self.customers:
            transaction = Transaction("deposit", customer_id, transaction_id, amount)
            customer = Customer(customer_id, amount, 0, 0, False, {})
            customer.transactions[transaction_id] = transaction
            self.customers[customer_id] = customer
        
        else:
            customer = self.customers[customer_id]
            if not customer.frozen:
                customer.available += amount
                transaction = Transaction("deposit", customer_id, transaction_id, amount)
                customer.transactions[transaction_id] = transaction

            else:
                print("Account frozen, not possible to deposit!")

    def withdraw(self, customer_id, amount, transaction_id):
        amount = float(amount)
        if customer_id not in self.customers:
            print("Can not withdraw from a non existent account!")
            return
        
        customer = self.customers[customer_id]
        if not customer.frozen and customer.available >= amount:
            customer.available -= amount
            transaction = Transaction("withdraw", customer_id, transaction_id, amount)
            customer.transactions[transaction_id] = transaction

        else:
            print("Account frozen, not possible to withdraw!")


    def get_customer_and_transaction(self, customer_id, transaction_id):
        if customer_id not in self.customers:
            print("Cannot dispute on a non-existent account!")
            return None, None

        customer = self.customers[customer_id]
        if transaction_id not in customer.transactions:
            print(customer_id, transaction_id)
            print("Cannot dispute a non-existent transaction!")
            return None, None

        transaction = customer.transactions[transaction_id]
        return customer, transaction

    def dispute(self, customer_id, transaction_id):
        customer, transaction = self.get_customer_and_transaction(customer_id, transaction_id)
        if not customer or not transaction:
            return

        if transaction.type == 'deposit' and not customer.frozen:
            amount = transaction.amount
            customer.available -= amount
            customer.hold += amount
        else:
            print("Only deposits can be disputed")

    def resolve(self, customer_id, transaction_id):
        customer, transaction = self.get_customer_and_transaction(customer_id, transaction_id)
        if not customer or not transaction:
            return

        if transaction.type == 'deposit' and not customer.frozen:
            amount = transaction.amount
            customer.hold -= amount
            customer.available += amount
        else:
            print("Only deposits can be disputed")

    def chargeback(self, customer_id, transaction_id):
        customer, transaction = self.get_customer_and_transaction(customer_id, transaction_id)
        if not customer or not transaction:
            return

        if transaction.type == 'deposit' and not customer.frozen:
            amount = transaction.amount
            customer.hold -= amount
            customer.frozen = True
        else:
            print("Only deposits can be disputed")


            