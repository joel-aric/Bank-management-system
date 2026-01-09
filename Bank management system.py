import tkinter as tk
from tkinter import messagebox

# -------------------------------
# Bank Data (In-Memory Database)
# -------------------------------
accounts = {}

# -------------------------------
# Functions
# -------------------------------

def create_account():
    acc_no = entry_acc_no.get()
    name = entry_name.get()
    balance = entry_balance.get()

    if acc_no == "" or name == "" or balance == "":
        messagebox.showerror("Error", "All fields required")
        return

    if acc_no in accounts:
        messagebox.showerror("Error", "Account already exists")
        return

    accounts[acc_no] = {
        "name": name,
        "balance": float(balance)
    }

    print(f"[TERMINAL LOG] Account Created | Acc No: {acc_no}, Name: {name}, Balance: {balance}")
    messagebox.showinfo("Success", "Account created successfully")
    clear_entries()


def deposit():
    acc_no = entry_acc_no.get()
    amount = entry_amount.get()

    if acc_no not in accounts:
        messagebox.showerror("Error", "Account not found")
        return

    accounts[acc_no]["balance"] += float(amount)

    print(f"[TERMINAL LOG] Deposit | Acc No: {acc_no}, Amount: {amount}")
    messagebox.showinfo("Success", "Amount deposited successfully")
    clear_entries()


def withdraw():
    acc_no = entry_acc_no.get()
    amount = entry_amount.get()

    if acc_no not in accounts:
        messagebox.showerror("Error", "Account not found")
        return

    if accounts[acc_no]["balance"] < float(amount):
        messagebox.showerror("Error", "Insufficient balance")
        return

    accounts[acc_no]["balance"] -= float(amount)

    print(f"[TERMINAL LOG] Withdraw | Acc No: {acc_no}, Amount: {amount}")
    messagebox.showinfo("Success", "Amount withdrawn successfully")
    clear_entries()


def check_balance():
    acc_no = entry_acc_no.get()

    if acc_no not in accounts:
        messagebox.showerror("Error", "Account not found")
        return

    bal = accounts[acc_no]["balance"]
    print(f"[TERMINAL LOG] Balance Check | Acc No: {acc_no}, Balance: {bal}")
    messagebox.showinfo("Balance", f"Current Balance: Rs {bal}")


def view_accounts():
    data = ""
    for acc, info in accounts.items():
        data += f"Acc No: {acc}, Name: {info['name']}, Balance: Rs {info['balance']}\n"

    print("[TERMINAL LOG] Viewed All Accounts")
    messagebox.showinfo("All Accounts", data if data else "No accounts found")


def delete_account():
    acc_no = entry_acc_no.get()

    if acc_no not in accounts:
        messagebox.showerror("Error", "Account not found")
        return

    del accounts[acc_no]

    print(f"[TERMINAL LOG] Account Deleted | Acc No: {acc_no}")
    messagebox.showinfo("Success", "Account deleted successfully")
    clear_entries()


def clear_entries():
    entry_acc_no.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_balance.delete(0, tk.END)
    entry_amount.delete(0, tk.END)

# -------------------------------
# GUI Design
# -------------------------------
root = tk.Tk()
root.title("Bank Management System")
root.geometry("450x550")
root.config(bg="#e6f2ff")

tk.Label(root, text="🏦 Bank Management System", font=("Arial", 18, "bold"), bg="#e6f2ff").pack(pady=10)

tk.Label(root, text="Account Number").pack()
entry_acc_no = tk.Entry(root)
entry_acc_no.pack()

tk.Label(root, text="Customer Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Initial Balance").pack()
entry_balance = tk.Entry(root)
entry_balance.pack()

tk.Label(root, text="Amount (Deposit/Withdraw)").pack()
entry_amount = tk.Entry(root)
entry_amount.pack()

tk.Button(root, text="Create Account", width=25, command=create_account).pack(pady=5)
tk.Button(root, text="Deposit", width=25, command=deposit).pack(pady=5)
tk.Button(root, text="Withdraw", width=25, command=withdraw).pack(pady=5)
tk.Button(root, text="Check Balance", width=25, command=check_balance).pack(pady=5)
tk.Button(root, text="View All Accounts", width=25, command=view_accounts).pack(pady=5)
tk.Button(root, text="Delete Account", width=25, command=delete_account).pack(pady=5)

tk.Button(root, text="Exit", width=25, bg="red", fg="white", command=root.quit).pack(pady=10)

print("[TERMINAL LOG] Bank Management System Started")

root.mainloop()