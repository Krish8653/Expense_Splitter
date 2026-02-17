# Simple-Splitwise-Python

A lightweight, efficient debt-settlement engine built in Python. This project calculates group expenses and private transfers to find the most efficient way to settle debts with the minimum number of transactions.

## The Goal
When a group of friends goes on a trip, everyone spends different amounts, and some people pay each other back partially during the trip. This script takes that messy data and answers one simple question: **"Who needs to pay whom exactly how much to settle everything?"**

## How the Logic Works
The program follows a four-step process to ensure accuracy and efficiency:

1. **Calculate the Fair Share:** It sums all group expenses and divides by the number of participants.
2. **Calculate Net Contribution:** For every person, it calculates:
   * `(Amount Spent on Bills + Money Sent to Friends) - (Fair Share + Money Received from Friends)`
3. **Identify Debtors & Creditors:** People with a negative balance owe the group; people with a positive balance are owed.
4. **The Greedy Settlement:** The algorithm pairs the person who owes the most (biggest debtor) with the person who is owed the most (biggest creditor). It settles at least one person's account per transaction, ensuring the group is settled in the fewest steps possible.



## Usage
You can modify the `my_spent` dictionary and `my_transfers` list in the script to reflect your own trip data.

```python
# Example Data
my_spent = {
    "Krish": 19433,
    "Abhijit": 3600,
    "Shyamal": 2650,
    "Bishal": 9500
}

my_transfers = [
    ("Krish", "Bishal", 2000),
    ("Abhijit", "Krish", 2000)
    # ... more transfers
]

Total Spent: 35183 | Individual Share: 8795.75

--- PAYMENT STEPS ---
👉 Abhijit pays Krish: 1195.75
👉 Bishal pays Krish: 441.50
👉 Bishal pays Shyamal: 354.25

💡 Key Features
Minimal Transactions: Guaranteed to settle a group of N people in N-1 transfers or fewer.
Precision: Handles decimal values to ensure every rupee is accounted for.
Simple Logic: No complex database or libraries required—just pure Python.
