"""
mini-budget V1 
Ogrenci: Deniz Yücel Uzunay (251478081)

--- V1 GÖREV LİSTESİ (TASKS) ---
1. Görev 1: `list` komutunu `while` döngüsü kullanarak implemente et.
2. Görev 2: SPEC dosyasına eklenen "Negatif tutar girilemez" kuralını `add` komutuna ekle.
3. Görev 3: Projeye README.md dosyası ekleyerek V0 -> V1 farkını açıkla.
4. BONUS: Yapay zeka ile `balance` komutunu implemente et.
--------------------------------
"""
import sys
import os

def initialize():
    if os.path.exists(".minibudget"):
        return "Already initialized"
    os.mkdir(".minibudget")
    f = open(".minibudget/transactions.dat", "w")
    f.close()
    return "Initialized empty minibudget in .minibudget/"

def add_transaction(t_type, amount, description):
    if not os.path.exists(".minibudget"):
        return "Not initialized. Run: python minibudget.py init"
    if int(amount) < 0:
        return "Error: Amount must be positive."
    
    f = open(".minibudget/transactions.dat", "r")
    content = f.read()
    f.close()
    
    transaction_id = content.count("\n") + 1
    
    f = open(".minibudget/transactions.dat", "a")
    record = str(transaction_id) + "|" + t_type + "|" + str(amount) + "|" + description + "|2026-03-16\n"
    f.write(record)
    f.close()
    return "Added transaction #" + str(transaction_id) + ": " + t_type + " " + str(amount)

def list_transactions():
    if not os.path.exists(".minibudget/transactions.dat"):
        return "Not initialized. Run: python minibudget.py init"
    
    f = open(".minibudget/transactions.dat", "r")
    first_char = f.read(1)
    if not first_char:
        f.close()
        return "No transactions found."
    
    f.seek(0)
    result = ""
    line = f.readline()
    while line != "":
        clean_line = line.replace("|", " - ")
        result = result + clean_line
        line = f.readline()
        
    f.close()
    return result.strip()

def calculate_balance():
    """Yapay Zeka (Gemini) tarafindan uretilen bakiye hesaplama fonksiyonu."""
    if not os.path.exists(".minibudget/transactions.dat"):
        return "Not initialized. Run: python minibudget.py init"
    
    f = open(".minibudget/transactions.dat", "r")
    total_balance = 0
    line = f.readline()
    
    while line != "":
        if "INCOME" in line:
            parts = line.split("|") 
            amount = int(parts[2])
            total_balance = total_balance + amount
        elif "EXPENSE" in line:
            parts = line.split("|")
            amount = int(parts[2])
            total_balance = total_balance - amount
        line = f.readline()
        
    f.close()
    return "Current Balance: " + str(total_balance)

def show_not_implemented(command_name):
    return "Command '" + command_name + "' will be implemented in future weeks."

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
    # Yapay zekanin yazdigi fonksiyonu buraya bagladik!
    print(calculate_balance())
elif sys.argv[1] == "delete":
    print(show_not_implemented("delete"))
else:
    print("Unknown command: " + sys.argv[1])
