import csv
import sys
from bank import Bank


if len(sys.argv) < 2:
    print("Please provide the path to the CSV file as an argument")
    sys.exit(1)


bank = Bank()
file_path = sys.argv[1]

def read_csv(file_path):
    with open(file_path, mode='r', newline='') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            bank.handle_transaction(row)


def write_customers_to_csv(customers, file_path="output.csv"):
    with open(file_path, mode='w', newline='') as file:
        fieldnames = ['customer', 'available', 'hold', 'total', 'frozen']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for customer in customers.values():
            writer.writerow({
                'customer': customer.id,
                'available': customer.available,
                'hold': customer.hold,
                'total': customer.available + customer.hold,
                'frozen': customer.frozen
            })

read_csv(file_path)
write_customers_to_csv(bank.customers)
    