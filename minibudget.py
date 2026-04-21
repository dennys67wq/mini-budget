"""
mini-budget V2 
Ogrenci: Deniz Yücel Uzunay (251478081)

--- V2 GÖREV LİSTESİ (TASKS) ---
1. Görev 1: `balance` komutunu kalici olarak projeye entegre et.
2. Görev 2: SPEC dosyasina eklenen `delete` komutunu, girilen ID'yi bularak satiri silecek sekilde kodla.
3. Görev 3: Dosya okuma/yazma islemlerini guvenli hale getirmek icin hata mesajlarini duzenle.
--------------------------------
"""
import sys
import os

DB_FILE = ".minibudget/transactions.dat"

def initialize():
    if os.path.exists(".minibudget"):
        return "Already initialized"
    os.mkdir(".minibudget")
    f = open(DB_FILE, "w")
    f.close()
    return "Initialized empty minibudget in .minibudget/"

def add_transaction(t_type, amount, description):
    if not os.path.exists(".minibudget"):
        return "Not initialized. Run: python minibudget.py init"
    if int(amount) < 0:
        return "Error: Amount must be positive."
    
    f = open(DB_FILE, "r")
    content = f.read()
    f.close()
    
    transaction_id = content.count("\n") + 1
    
    f = open(DB_FILE, "a")
    record = str(transaction_id) + "|" + t_type + "|" + str(amount) + "|" + description + "|2026-04-21\n"
    f.write(record)
    f.close()
    return "Added transaction #" + str(transaction_id) + ": " + t_type + " " + str(amount)

def list_transactions():
    if not os.path.exists(DB_FILE):
        return "Not initialized."
    
    f = open(DB_FILE, "r")
    content = f.read()
    f.close()
    
    if not content:
        return "No transactions found."
    
    return content.replace("|", " - ").strip()

def calculate_balance():
    if not os.path.exists(DB_FILE):
        return "Not initialized."
    
    f = open(DB_FILE, "r")
    total_balance = 0
    line = f.readline()
    
    while line != "":
        if "INCOME" in line:
            parts = line.split("|") 
            total_balance += int(parts[2])
        elif "EXPENSE" in line:
            parts = line.split("|")
            total_balance -= int(parts[2])
        line = f.readline()
        
    f.close()
    return "Current Balance: " + str(total_balance)

def delete_transaction(target_id):
    if not os.path.exists(DB_FILE):
        return "Not initialized."
    
    f = open(DB_FILE, "r")
    lines = f.readlines()
    f.close()
    
    new_lines = []
    deleted = False
    
    for line in lines:
        if line.startswith(target_id + "|"):
            deleted = True
        else:
            new_lines.append(line)
            
    if not deleted:
        return "Error: Transaction not found."
        
    f = open(DB_FILE, "w")
    for line in new_lines:
        f.write(line)
    f.close()
    
    return "Transaction #" + target_id + " deleted successfully."

# --- Ana Program ---
if len(sys.argv) < 2:
    print("Usage: python minibudget.py <command> [args]")
elif sys.argv[1] == "init":
    print(initialize())
elif sys.argv[1] == "add":
    if len(sys.argv) < 5:
        print("Usage: python minibudget.py add <TYPE> <amount> <description>")
    else:
        print(add_transaction(sys.argv[2], sys.argv[3], sys.argv[4]))
elif sys.argv[1] == "list":
    print(list_transactions())
elif sys.argv[1] == "balance":
    print(calculate_balance())
elif sys.argv[1] == "delete":
    if len(sys.argv) < 3:
        print("Usage: python minibudget.py delete <id>")
    else:
        print(delete_transaction(sys.argv[2]))
else:
    print("Unknown command: " + sys.argv[1])
