import pandas as pd
import random

companies = [
    "ABC Bank", "XYZ Corp", "Global Finance", "Tech Innovations Ltd", "Prime Mortgage", 
    "Acme Corp", "Apex Industries", "Nexa Tech", "Quantum Logic", "Stark Industries", 
    "Wayne Enterprises", "Cyberdyne Systems", "Oscorp", "Umbrella Corp", "Weyland-Yutani",
    "Blue Horizon Inc", "Apex Capital", "Summit Technologies", "Zephyr Holdings", "Nova Inc"
]

amounts = [
    "$1M", "$500K", "$2.5M", "$50,000", "$10M", "$100K", "$250,000", "$3M", "$7.5M", 
    "$20M", "€5M", "£2M", "$15,000", "$1.2M", "$800K", "$4M", "$600K", "$350,000", "$1.5M", "$90,000"
]

dates = [
    "2030", "December 2025", "Q4 2024", "January 15, 2027", "2028", "March 2026", 
    "October 2029", "the end of 2025", "July 1, 2032", "2035", "November 2024", 
    "May 2027", "August 2028", "2031", "September 2033", "2029", "April 2026", "2040"
]

verbs = [
    "agrees to repay", "will transfer", "is obligated to pay", "promises to deliver", 
    "will fund", "has committed to invest", "shall distribute", "guarantees the payment of", 
    "will compensate", "agrees to settle"
]

data = []

for _ in range(105):  # Generates around 100+ sentences
    c = random.choice(companies)
    a = random.choice(amounts)
    d = random.choice(dates)
    v = random.choice(verbs)
    
    rnd = random.random()
    if rnd < 0.33:
        text = f"{c} {v} {a} before {d}."
    elif rnd < 0.66:
        text = f"By {d}, {c} {v} {a} in full."
    else:
        text = f"An amount of {a} will be repaid by {c} on or before {d}."
        
    data.append({"contract_text": text})

# Add a few hardcoded examples from assignments
data.insert(0, {"contract_text": "ABC Bank agrees to repay $5M before 2030."})

df = pd.DataFrame(data)
df.to_csv("contracts.csv", index=False)
print("Successfully generated 100+ contract sentences dataset as 'contracts.csv'.")
