import pandas as pd
import os
from matplotlib import pyplot as plt
def load_expenses():
    if os.path.exists("expenses1.csv"):
        return pd.read_csv("expenses1.csv")
    else:
        return pd.DataFrame(columns=["Name","Amount","Category"])
def save_expenses(df):
    df.to_csv('expenses1.csv',index=False)
def add_expenses(df):
    name=input("Enter the expense name :\n==> ").strip().title()
    try:
        amount=float(input("Enter the amount of the expense :\n==> "))
    except ValueError:
        print("Invalid input")
        return(df)
    print("\nCategory\n")
    print("1:Food")
    print("2:Travel")
    print("3:Shopping")
    print("4:Fitness")
    try:
        choice=input("Enter the category of the expense(1,2,3) :\n==> ")
        if choice=="1" or choice.lower() =="food":
            category="Food"
        elif choice=="2" or choice.lower() =="travel":
            category="Travel"
        elif choice=="3" or choice.lower()=="shopping":
            category="Shopping"
        elif choice=="4" or choice.lower()=="fitness":
            category="Fitness"
        else:
            print("Invalid input")
    except ValueError:
        print("Invalid input")
        return(df)
    new_row=pd.DataFrame([{
        "Name":name,
        "Amount":amount,
        "Category":category
    }])
    df=pd.concat([df,new_row],ignore_index=True)
    save_expenses(df)
    print(f"\nExpense name : {name} added of Amount = Rs{amount} for {category}.\n")
    return(df)
def remove_expenses(df):
    name=input("Enter the expense name :\n==> ").strip().title()
    if name not in df['Name'].values:
        print("Invalid input")
        return(df)
    df=df[df['Name']!=name]
    df.to_csv('expenses1.csv',index=False)
    print(f"\nExpense name {name} removed.\n")
    return(df)
def update_expenses(df):
    name=input("\nEnter the expense name :\n==> ").strip().title()
    if name not in df['Name'].values:
        print("\nExpense name not found.")
        return(df)
    print(f"\nExpense name {name} found successfully.")
    print("\nWhat do you want to update?")
    print("1:Name.")
    print("2:Amount.")
    print("3:Category.")
    choice=input("What you want to update?:\n==> ").title()
    if choice=="1":
        new_name=input("\nEnter the new expense name :\n==> ").strip().title()
        df.loc[df['Name'] == name, "Name"]=new_name
        print(f"\nNew expense name : {new_name} updated.")
    elif choice=="2":
        try:
            new_amount = float(input("\nEnter the new amount of the expense :\n==> "))
            df.loc[df['Name'] == name, "Amount"]=new_amount
            print(f"\nNew expense amount : {new_amount} updated.")
        except ValueError:
            print("Invalid input")
            return(df)
    elif choice=="3":
        print("\n====Category====\n")
        print("\nWhat do you want to update?")
        print("1:Food")
        print("2:Travel")
        print("3:Shopping")
        print("4:Fitness")
        choice=input("What you want to update?:\n==> ")
        categories={"1":"Food","2":"Travel","3":"Shopping","4":"Fitness"}
        if choice not in categories:
            print("Invalid input")
            return(df)
        new_category=categories[choice]
        df.loc[df['Name'] == name,'Category']=new_category
        print(f"\nNew expense category : {new_category} updated.")
        save_expenses(df)
        return(df)
    else:
        print("Invalid input")
        return(df)
    save_expenses(df)
    return(df)

def view_expenses(df):
    print("\nViewing expenses...\n")
    if len(df) == 0:
        print("\nNo expenses found.")
        return(df)
    for index,row in df.iterrows():
        print(f"\nName = {row['Name']} of Amount = Rs{row['Amount']} for {row['Category']}")
    print(f"\nTotal expenses: Rs {df['Amount'].sum()}")
    print(f"\nExpenses Tracker on basis of Category:\n{df.groupby('Category')['Amount'].sum()}")
def show_chart(df):
    if len(df) == 0:
        print("\nNo expenses found.")
        return(df)
    plt.bar(df["Name"], df["Amount"])
    plt.title("Expenses Chart")
    plt.xlabel("Expenses Name")
    plt.ylabel("Amount in Rs")
    plt.savefig("chart1_Expenses.png")
    plt.show()
    plt.clf()
    category_total=df.groupby('Category')['Amount'].sum()
    plt.pie(category_total, labels=category_total.index, autopct="%1.1f%%")
    plt.title("Spending by Category")
    plt.savefig("chart2_category.png")
    plt.show()
    plt.clf()
    category_total=df.groupby('Category')['Amount'].sum()
    plt.bar(category_total.index, category_total.values)
    plt.title("Total spent by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount in Rs")
    plt.savefig("chart3_category.png")
    plt.show()
    plt.clf()
df=load_expenses()
while True:
    print("\n<=====Expense-Tracker=====>\n")
    print("1:Add expenses...")
    print("2:Remove expenses...")
    print("3:View expenses...")
    print("4:Update expenses...")
    print("5:Show chart...")
    print("6:Exit")
    choice=input("\nEnter your choice:\n==> ")
    if choice=="1":
        df=add_expenses(df)
    elif choice=="2":
        df=remove_expenses(df)
    elif choice=="3":
        df=view_expenses(df)
    elif choice=="4":
        df=update_expenses(df)
    elif choice=="5":
        df=show_chart(df)
    elif choice=="6":
        print("\nExiting...")
        break
    else:
        print("Invalid input")




