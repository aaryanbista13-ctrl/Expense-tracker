import pandas as  pd
import os
def load_expenses():
    if os.path.exists('expenses.csv'):
        return pd.read_csv('expenses.csv')
    else:
        return pd.DataFrame(columns=["Name","Amount","Category"])
def save_expenses(df):
        df.to_csv('expenses.csv',index=False)
def add_expenses(df):
    print("\nAdding new expenses...\n")
    name=input("Enter expense name:\n==> ").strip().title()
    if name  in df['Name'].values:
        print("\nDuplicate expense name!\n")
        return(df)
    try:
        amount=int(input("Enter your amount:\n==>Rs "))
    except ValueError:
        print("\nInvalid amount.")
        return(df)
    print("\n====Category====\n")
    print("1:Food")
    print("2:Travel")
    print("3:Shopping")
    choice=input("Enter your choice(1,2,3):\n==> ").strip()
    if choice=="1":
        category="Food"
    elif choice=="2":
        category="Travel"
    elif choice=="3":
        category="Shopping"
    else:
        print("\nInvalid choice.")
        return(df)
    new_row=pd.DataFrame([{"Name":name,
             "Amount":amount,
             "Category":category,
    }])
    df=pd.concat([df,new_row],ignore_index=True)
    save_expenses(df)
    print(f"\nExpenses added-{name}.Amount= Rs{amount} for {category}.\n")
    return(df)

def remove_expenses(df):
    print("\nRemoving expenses...\n")
    name=input("Enter expense name:\n==> ").strip().title()
    if name not in df['Name'].values:
        print("\nExpense not found.")
        return(df)
    df=df[df["Name"]!=name]
    df.to_csv('expenses.csv',index=False)
    print(f"\nExpenses {name} removed.\n")
    return(df)
def view_expenses(df):
    print("\nViewing expenses...\n")
    if len(df) == 0:
        print("\nNo expenses found.")
        return(df)
    print("\nAll expenses .\n")
    for index, row in df.iterrows():
        print(f"Expense= {row['Name']} - Amount= Rs {row['Amount']} for {row['Category']}")
    print(f"Total cost on expenses:{df['Amount'].sum()}")
    print(f"Expenses on basis of category:{df.groupby('Category')['Amount'].sum()}")
df=load_expenses()
while True:
    print("\n=======Expense Tracker\n========")
    print("1. Add new expenses.")
    print("2. Remove expenses.")
    print("3. View expenses.")
    print("4. Exit")
    choice=input("Enter your choice(1,2,3,4):\n==> ").strip()
    if choice=="1":
        df=add_expenses(df)
    elif choice=="2":
        df=remove_expenses(df)
    elif choice=="3":
        view_expenses(df)
    elif choice=="4":
        break
    else:
        print("\nInvalid choice.")
