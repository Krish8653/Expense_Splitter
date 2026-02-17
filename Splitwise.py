def settle_up(spent, transfers):
    # --- STEP 1: INITIAL SETUP ---
    names = list(spent.keys())
    num_people = len(names)
    
    # Calculate the total amount the group spent together
    total_spent = sum(spent.values())
    # Calculate what each person's bill should be (the target)
    share = total_spent / num_people
    
    # --- STEP 2: CALCULATE NET TRANSFERS ---
    # We start everyone at 0 for private transfers
    net_transfers = {name: 0.0 for name in names}
    for sender, receiver, amount in transfers:
        net_transfers[sender] += amount    # Sending money is a "contribution"
        net_transfers[receiver] -= amount  # Receiving money is like "withdrawing"
        
    # --- STEP 3: CALCULATE FINAL BALANCES ---
    # This tells us if a person is a Creditor (+) or a Debtor (-)
    balances = {}
    for name in names:
        # Final Score = (Bill Payments + Money Sent) - (Fair Share + Money Received)
        net_position = (spent[name] + net_transfers[name]) - share
        balances[name] = round(net_position, 2)

    # --- STEP 4: SEPARATE DEBTORS AND CREDITORS ---
    # We put them in lists like [["Name", Amount]]
    debtors = [[n, b] for n, b in balances.items() if b < 0]
    creditors = [[n, b] for n, b in balances.items() if b > 0]

    # --- STEP 5: THE SETTLEMENT LOOP (The "Greedy" Logic) ---
    print(f"Total Spent: {total_spent} | Individual Share: {share:.2f}\n")
    print("--- PAYMENT STEPS ---")

    # While there are still people in both lists...
    while debtors and creditors:
        # SORTING: We sort every time to ensure the biggest debtor 
        # meets the biggest creditor. This is the "Greedy" part.
        debtors.sort(key=lambda x: x[1])            # Most negative first
        creditors.sort(key=lambda x: x[1], reverse=True) # Most positive first

        d_name, d_amt = debtors[0]
        c_name, c_amt = creditors[0]

        # How much can we move? The smaller of the two magnitudes.
        # If I owe 10 but you are owed 5, I only give you 5.
        payment = min(abs(d_amt), c_amt)

        print(f"👉 {d_name} pays {c_name}: {payment:.2f}")

        # Update the numbers in our lists
        debtors[0][1] += payment
        creditors[0][1] -= payment

        # If a person's balance is now (roughly) zero, remove them from the list
        if abs(debtors[0][1]) < 0.01: 
            debtors.pop(0)
        if abs(creditors[0][1]) < 0.01: 
            creditors.pop(0)

# --- YOUR DATA ---
my_spent = {
    "Krish": 19433,
    "Abhijit": 3600,
    "Shyamal": 2650,
    "Bishal": 9500
}

my_transfers = [
    ("Krish", "Bishal", 2000),
    ("Abhijit", "Bishal", 2000),
    ("Shyamal", "Bishal", 2000),
    ("Bishal", "Krish", 4500),
    ("Shyamal", "Krish", 4500),
    ("Abhijit", "Krish", 2000)
]

# Run the function
settle_up(my_spent, my_transfers)
