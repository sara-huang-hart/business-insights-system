# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 09:28:38 2018

@author: huang
"""

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
xl = pd.ExcelFile("FA18SalesData.xlsx")
SalesData = xl.parse("Orders")
lines = '-' * 45
dbl_lines = '=' * 45


def homepage():
    print(dbl_lines)
    print("\nWelcome to Office Solutions Recommendation System")
    print("Login to get started.")

def login():   
    conn = sqlite3.connect('OS_Employee.db')
    with conn:
        cur=conn.cursor()
        print("\n------------------- LOGIN -------------------")
        userEmail = input("Please enter your email: ")
        userEmail = userEmail.strip()
        while not userEmail:
             userEmail = input("Please enter your email: ")
             userEmail = userEmail.strip()
             userEmail = userEmail.lower()
        while True:
            if userEmail.find("@") == -1:
                userEmail = input("Please provide a valid email: ")
                userEmail = userEmail.strip()
                userEmail = userEmail.lower()
            elif userEmail == " ":
                userEmail = input("Please provide a valid email: ")
                userEmail = userEmail.strip()
                userEmail = userEmail.lower()
            else:
                break
        userPassword = input("Please enter your password: ")
        userPassword = userPassword.strip()
        while not userPassword:
            userPassword = input ("Please enter your password: ")
            userPassword = userPassword.strip()
        if ' ' in userPassword:
            userPassword = input("Password must not contain any spaces. Please enter a valid password: ")
        cur.execute("SELECT COUNT (*) FROM Employee WHERE(Email = '" + userEmail.lower() + "' AND Password = '" + userPassword +"')")        
        results = cur.fetchone()  
        if results[0] == 1:
            print(lines)
            print("\nLogin Successful")
            main_menu()
        else:
            print(lines)
            print("\nLogin Unsuccessful. Please try logging in again.")
            login()
    conn.close()

def main_menu():
    print("\n----------------- MAIN MENU -----------------")
    print("\n1 - Register a new user")
    print("2 - View by product sales outlook")
    print("3 - View by customer loyalty")
    print("4 - View by dates")
    print("5 - View by regions")
    print("6 - Logout")
    try:        
        userInput = input("Please enter a number from the list above: ").strip()
        while userInput != '1' and userInput != '2' and userInput != '3' and userInput != '4' and userInput != '5' and userInput != '6':
            if userInput != '1':
                userInput = input("\nInvalid input. Please enter a number from the list above: ")
            elif userInput != '2':
                userInput = input("\nInvalid input. Please enter a number from the list above: ")
            elif userInput != '3':
                userInput = input("\nInvalid input. Please enter a number from the list above: ")
            elif userInput != '4':
                userInput = input("\nInvalid input. Please enter a number from the list above: ")
            elif userInput != '5':
                userInput = input("\nInvalid input. Please enter a number from the list above: ")
            elif userInput != '6':
                userInput = input("\nInvalid input. Please enter a number from the list above: ")
            else:
                break
        if userInput == '1':
            registration()
        elif userInput == '2':
            product_menu()
        elif userInput == '3':
            customer_menu()   
        elif userInput == '4':
            date_menu()
        elif userInput == '5':
            region_menu()
        elif userInput == '6':
            print(lines)
            print("\nThank you for visiting Office Solutions Recommendation System. See you next time!")
    except (KeyError) as e:
        print("\nInvalid input.")

def registration():
    print("\n--------------- REGISTRATION ----------------")
    print("\nTo register a new user,")
    conn = sqlite3.connect('OS_Employee.db')
    with conn:
        cur = conn.cursor()
        try:
            Employee_ID = input("Please enter a employee ID: ").strip()
            while not Employee_ID or len(Employee_ID) != 4:
                if not Employee_ID:
                    Employee_ID = input("Employee ID cannot be blank. Please enter a 4 digit ID number: ")
                elif len(Employee_ID) != 4:
                    Employee_ID = input("Employee ID must be 4 digits long. Please enter a valid ID number: ")
            cur.execute("SELECT COUNT (*) FROM Employee WHERE(EmployeeID = '" + Employee_ID + "')")
            results = cur.fetchone()    
            while results[0] == 1:
                Employee_ID = input("Employee ID is taken. Please enter a different one: ")
                Employee_ID = Employee_ID.strip()
                while not Employee_ID or len(Employee_ID) != 4:
                    if not Employee_ID:
                        Employee_ID = input("Employee ID cannot be blank. Please enter a 4 digit ID number: ")
                    elif len(Employee_ID) != 4:
                        Employee_ID = input("Employee ID must be 4 digits long. Please enter a valid ID number: ")
                cur.execute("SELECT COUNT (*) FROM Employee WHERE(EmployeeID = '" + Employee_ID + "')")
                results = cur.fetchone()   
            print("\nEmployee ID " + Employee_ID + " is accepted.")
            print(lines)
            First_Name = input("Please enter the employee's first name: ")  
            First_Name = First_Name.title()
            while not First_Name:
                First_Name = input("First name cannot be blank. Please enter a valid name: ")
                if First_Name.isalpha() != True:
                    First_Name = input("First name must contain only letters. Please enter a valid name:")
                    First_Name = First_Name.strip()
                    First_Name = First_Name.title()
                else:
                    break
            Last_Name = input("Please enter the employee's last name: ")
            Last_Name = Last_Name.title()
            while not Last_Name:
                Last_Name = input("Last name cannot be blank. Please enter a valid last name: ")
                if Last_Name.isalpha() != True:
                    Last_Name = input("Last name must contain only letters. Please enter a valid last name: ")
                    Last_Name = Last_Name.strip()
                    Last_Name = Last_Name.title()
                else:
                    break
            Email = input("Please enter the employee's email: ")
            Email = Email.lower()
            while not Email:
                Email = input("Email cannot be blank. Please enter a valid email address: ")
            while True:
                if Email.find("@") == -1:
                    Email = input("Email is not complete. Please provide a valid email address: ")
                elif Email.find(".") == -1:
                    Email = input("Email is not complete. Please provide a valid email address: ")
                else:
                    break 
            Password = input("Please enter a password: ")
            while not Password:
                if not Password:
                    Password = input("Password cannot be blank. Please enter a valid password: ")
                else:
                    break           
            New_User = "INSERT INTO Employee VALUES ('{}', '{}', '{}', '{}', '{}')".format(Employee_ID, First_Name, Last_Name, Email, Password)
            cur.execute(New_User)
            print(lines)
            print("\nNew user is registered.")  
        except Exception as e:
            print("Connection Failed " + str(e))
    conn.close()
    main_menu()

def product_menu():
    print("\n----------- PRODUCT SALES OUTLOOK -----------")
    print("\nView by:")
    print("\n1 - Subcategories")
    print("2 - Products")
    print("    or")
    print("3 - Return to Main Menu")
    try:
        userInput = input("\nPlease enter a number from the list above: ") 
        while userInput != '1' and userInput != '2' and userInput != '3':
                if userInput != '1':
                    userInput = input("\nInvalid input. Please enter a number from the list above: ")
                elif userInput != '2':
                    userInput = input("\nInvalid input. Please enter a number from the list above: ")
                elif userInput != '3':
                    userInput = input("\nInvalid input. Please enter a number from the list above: ")
                else:
                    break
        if userInput == '1':
             product_subcategories()
        elif userInput == '2':
            product_products()
        elif userInput == '3':
            main_menu()
    except (KeyError) as e:
        print("\nInvalid input.")
    
def product_subcategories():    
    print("\n-------------- BY SUBCATEGORIES --------------")
    print("\nView by:")
    print("\n1 - Profit")
    print("2 - Quantity sold")
    print("    or")
    print("3 - Return to Product Sales Outlook Menu")
    userInput = input("\nPlease enter a number from the list above: ")
    while userInput != '1' and userInput != '2' and userInput != '3':
        if userInput != '1':
            userInput = input("\nInvalid input. Please enter a number from the list above: ")
        elif userInput != '2':
            userInput = input("\nInvalid input. Please enter a number from the list above: ")
        elif userInput != '3':
            userInput = input("\nInvalid input. Please enter a number from the list above: ")
        else:
            break
    if userInput == '1':
        print(lines)
        print("\nVew the Most Profitable Subcategory in:")
        print("\n1 - Furniture")
        print("2 - Office Supplies")
        print("3 - Technology")
        ctgry_choice = input("Please enter a number from the list above: ")
        while ctgry_choice != '1' and ctgry_choice != '2' and ctgry_choice != '3':
            if ctgry_choice != '1':
                ctgry_choice = input("\nInvalid input. Please enter a number from the list above: ")
            elif ctgry_choice != '2':
                ctgry_choice = input("\nInvalid input. Please enter a number from the list above: ")
            elif ctgry_choice != '3':
                ctgry_choice = input("\nInvalid input. Please enter a number from the list above: ")
            else:
                break
        if ctgry_choice == '1':        
            category = "Furniture"
        elif ctgry_choice == '2':
            category = "Office Supplies"
        elif ctgry_choice == '3':
            category = "Technology"
        prod_sub_columns = SalesData[["Category", "Sub-Category", "Profit"]]
        sub_select = prod_sub_columns.loc[prod_sub_columns["Category"]== str(category)]
        prod_sub = sub_select.groupby(by= "Sub-Category").sum().sort_values(by= "Profit", ascending = False)
        print(lines)
        print("\nThe most profitable subcategory in the " + category + " category is: ")
        print(prod_sub.head(1))
        print(dbl_lines)
        userInput = input("\nEnter 1 to see all subcategories in " + category + ", or Enter 2 to return to the Product Sales Outlook Menu: ")
        while userInput != '1' and userInput != '2':
            if userInput != '1':
                userInput = input("\nInvalid input. Please enter a number from the list above: ")
            elif userInput != '2':
                userInput = input("\nInvalid input. Please enter a number from the list above: ")
            else:
                break
        if userInput == '1':
            print(lines)
            print("\nIn the " + category + " category, the order of most profitable subcategories is as follows: ")
            print(prod_sub.head())
        elif userInput == '2': 
            product_menu()
    elif userInput == '2':
        print(lines)
        print("\nChoose a category:")
        print("\n1 - Furniture")
        print("2 - Office Supplies")
        print("3 - Technology")
        ctgry_choice = input("\nPlease enter a number from the list above: ")
        while ctgry_choice != '1' and ctgry_choice != '2' and ctgry_choice != '3':
            if ctgry_choice != '1':
                ctgry_choice = input("\nInvalid input. Please enter a number from the list above: ")
            elif ctgry_choice != '2':
                ctgry_choice = input("\nInvalid input. Please enter a number from the list above: ")
            elif ctgry_choice != '3':
                ctgry_choice = input("\nInvalid input. Please enter a number from the list above: ")
            else:
                break
        if ctgry_choice == '1':
            category = "Furniture"
        elif ctgry_choice == '2':
            category = "Office Supplies"
        elif ctgry_choice == '3':
            category = "Technology"
        subctgry_qsold = SalesData[["Category", "Sub-Category", "Quantity"]]
        ctgry_select = subctgry_qsold.loc[subctgry_qsold["Category"]== category]
        ctgry_sub_qsold = ctgry_select[["Category", "Sub-Category", "Quantity"]]
        subctgry_order = ctgry_sub_qsold.groupby(by= "Sub-Category").sum().sort_values(by= "Quantity", ascending= False)
        print(lines)
        print("\nThe number of items sold in the " + category + " category: ")
        print(subctgry_order.head(10))      
    elif userInput == '3':
        product_menu()
    print(dbl_lines)           
    return_userInput = input("\nEnter 1 to return to the Subcategories Menu, or Enter 2 to return to the Product Sales Outlook Menu: ")
    while return_userInput != '1' and return_userInput != '2':
            if return_userInput != '1':
                return_userInput = input("\nInvalid input. Please enter a number from the list above: ")
            elif return_userInput != '2':
                return_userInput = input("\nInvalid input. Please enter a number from the list above: ")
            else:
                break
    if return_userInput == '1':
        product_subcategories()
    elif return_userInput == '2':
        product_menu()
   
def product_products():
    print("\n--------------- BY PRODUCTS ---------------")
    print("\nView the Most Profitable Products and the Least Profitable Products.")
    print("\nFirst, choose a category:")
    print("\n1 - Furniture")
    print("2 - Office Supplies")
    print("3 - Technology")
    print("    or")
    print("4 - View All Products")
    ctgry_choice = input("\nPlease enter a number from the list above: ")   
    while ctgry_choice != '1' and ctgry_choice != '2' and ctgry_choice != '3' and ctgry_choice != '4':
        if ctgry_choice != '1':
            ctgry_choice = input("\nInvalid input. Please enter a number from the list above: ")
        elif ctgry_choice != '2':
            ctgry_choice = input("\nInvalid input. Please enter a number from the list above: ")
        elif ctgry_choice != '3':
            ctgry_choice = input("\nInvalid input. Please enter a number from the list above: ")
        elif ctgry_choice != '4':
            ctgry_choice = input("\nInvalid input. Please enter a number from the list above: ")
        else:
            break
    if ctgry_choice == '1':
        print(lines)
        print("\nNow, choose a subcategory:")
        print("\n1 - Bookcases")
        print("2 - Chairs")
        print("3 - Furnishings")
        print("4 - Tables")
        sub_choice = input("\nEnter the number that corresponds to the subcategory you wish to see: ")
        while sub_choice != '1' and sub_choice != '2' and sub_choice != '3' and sub_choice != '4':
            if sub_choice != '1':
                sub_choice = input("\nInvalid input. Please enter a number from the list above: ")
            elif sub_choice != '2':
                sub_choice = input("\nInvalid input. Please enter a number from the list above: ")
            elif sub_choice != '3':
                sub_choice = input("\nInvalid input. Please enter a number from the list above: ")
            elif sub_choice != '4':
                sub_choice = input("\nInvalid input. Please enter a number from the list above: ")
            else:
                break
        if sub_choice == '1':
            sub_key = "Bookcases"
            sub_display = "Bookcase"    
        elif sub_choice == '2':
            sub_key = "Chairs"
            sub_display = "Chair"
        elif sub_choice == '3':
            sub_key = "Furnishings"
            sub_display = "Furnishing"
        elif sub_choice == '4':
            sub_key = "Tables"
            sub_display = "Table"       
        sub_prd_columns = SalesData[["Sub-Category", "Product Name", "Profit"]]    
        prd_select = sub_prd_columns.loc[sub_prd_columns["Sub-Category"] == str(sub_key)]
        prd_group = prd_select.groupby(by= "Product Name").sum().sort_values(by= "Profit", ascending = False)        
        print(lines)
    # error checking here v    
        num_prds = SalesData["Product Name"].value_counts()
        total_products = num_prds.shape
        userInput = input("\nThere are " + str(total_products) + " products total. How many products would you like to see? Please enter a number: ")
        invalid = True
        while invalid:
            if userInput.isnumeric() != True:
                userInput = input("Invalid input. Please enter a number: ")
            else:
                invalid = False
        print(lines)
        int_userInput = int(userInput)
        print("\nThe top " + str(userInput) + " most profitable " + sub_display + " products are:")
        print(prd_group.head(int_userInput))
        print(dbl_lines)
        userInput = input("\nEnter 1 to view the least profitable products in the " + sub_display + " subcategory, or Enter 2 to return to the Product Sales Outlook Menu: ") 
        while userInput != '1' and userInput != '2':
            if userInput != '1':
                userInput = input("\nInvalid input. Please enter a number from the list above: ")
            elif userInput != '2':
                userInput = input("\nInvalid input. Please enter a number from the list above: ")
            else:
                break
        if userInput == '1':
            print(lines)
            print("\nThe least profitable products in the " + sub_display + " subcategory are: ")
            print(prd_group.tail(10))
            print(dbl_lines)
        elif userInput == '2':
            product_menu()
    elif ctgry_choice == '2':
        print(lines)
        print("\nNow, choose a subcategory:")
        print("\n1 - Appliances")
        print("2 - Art")
        print("3 - Binders")
        print("4 - Envelopes")
        print("5 - Fasteners")
        print("6 - Labels")
        print("7 - Papers")
        print("8 - Storage")
        print("9 - Supplies")
        sub_choice = input("\nEnter the number that corresponds to the subcategory you wish to see: ")
        while sub_choice != '1' and sub_choice != '2' and sub_choice != '3' and sub_choice != '4' and sub_choice != '5' and sub_choice != '6' and sub_choice != '7' and sub_choice != '8' and sub_choice != '9':
            if sub_choice != '1':
                sub_choice = input("\nInvalid input. Please enter a number from the list above: ")
            elif sub_choice != '2':
                sub_choice = input("\nInvalid input. Please enter a number from the list above: ")
            elif sub_choice != '3':
                sub_choice = input("\nInvalid input. Please enter a number from the list above: ")
            elif sub_choice != '4':
                sub_choice = input("\nInvalid input. Please enter a number from the list above: ")
            elif sub_choice != '5':
                sub_choice = input("\nInvalid input. Please enter a number from the list above: ")
            elif sub_choice != '6':
                sub_choice = input("\nInvalid input. Please enter a number from the list above: ")
            elif sub_choice != '7':
                sub_choice = input("\nInvalid input. Please enter a number from the list above: ")
            elif sub_choice != '8':
                sub_choice = input("\nInvalid input. Please enter a number from the list above: ")
            elif sub_choice != '9':
                sub_choice = input("\nInvalid input. Please enter a number from the list above: ")
            else:
                break
        if sub_choice == '1':
            sub_key = "Appliances"
            sub_display = "Appliance"    
        elif sub_choice == '2':
            sub_key = "Art"
            sub_display = "Art"
        elif sub_choice == '3':
            sub_key = "Binders"
            sub_display = "Binder"
        elif sub_choice == '4':
            sub_key = "Envelopes"
            sub_display = "Envelope"
        elif sub_choice == '5':
            sub_key = "Fasteners"
            sub_display = "Fastener"
        elif sub_choice == '6':
            sub_key = "Labels"
            sub_display = "Label"
        elif sub_choice == '7':
            sub_key = "Paper" 
            sub_display = "Paper"
        elif sub_choice == '8':
            sub_key = "Storage"
            sub_display = "Storage"
        elif sub_choice == '9':
            sub_key = "Supplies"
            sub_display = "Supply"
        sub_prd_columns = SalesData[["Sub-Category", "Product Name", "Profit"]]    
        prd_select = sub_prd_columns.loc[sub_prd_columns["Sub-Category"] == str(sub_key)]
        prd_group = prd_select.groupby(by= "Product Name").sum().sort_values(by= "Profit", ascending = False)
        print(lines)   
    # error checking here v
        num_prds = SalesData["Product Name"].value_counts()
        total_products = num_prds.shape
        userInput = input("\nThere are " + str(total_products) + " products total. How many products would you like to see? Please enter a number: ")
        invalid = True
        while invalid:
            if userInput.isnumeric() != True:
                userInput = input("Invalid input. Please enter a number: ")
            else:
                invalid = False
        print(lines)
        int_userInput = int(userInput)
        print("\nThe top " + str(userInput) + " most profitable " + sub_display + " products are:")
        print(prd_group.head(int_userInput))    
        print(dbl_lines) 
        userInput = input("\nEnter 1 to view the least profitable products in the " + sub_display + " subcategory, or Enter 2 to return to the Product Sales Outlook Menu: ")
        while userInput != '1' and userInput != '2':
            if userInput != '1':
                userInput = input("\nInvalid input. Please enter a number from the list above: ")
            elif userInput != '2':
                userInput = input("\nInvalid input. Please enter a number from the list above: ")
            else:
                break
        if userInput == '1':
            print(lines)
            print("\nThe least profitable products in the " + sub_display + " subcategory are: ")
            print(prd_group.tail(10))
            print(dbl_lines)
        elif userInput == '2':
            product_menu()   
    elif ctgry_choice == '3':
        print(lines)
        print("\nNow, choose a subcategory:")
        print("\n1 - Accessories")
        print("2 - Copiers")
        print("3 - Machines")
        print("4 - Phones")
        sub_choice = input("\nEnter the number that corresponds to the subcategory you wish to see: ")
        while sub_choice != '1' and sub_choice != '2' and sub_choice != '3' and sub_choice != '4':
            if sub_choice != '1':
                sub_choice = input("\nInvalid input. Please enter a number from the list above: ")
            elif sub_choice != '2':
                sub_choice = input("\nInvalid input. Please enter a number from the list above: ")
            elif sub_choice != '3':
                sub_choice = input("\nInvalid input. Please enter a number from the list above: ")
            elif sub_choice != '4':
                sub_choice = input("\nInvalid input. Please enter a number from the list above: ")
            else:
                break
        if sub_choice == '1':
            sub_key = "Accessories"
            sub_display = "Accessory"    
        elif sub_choice == '2':
            sub_key = "Copiers"
            sub_display = "Copier"
        elif sub_choice == '3':
            sub_key = "Machines"
            sub_display = "Machine"
        elif sub_choice == '4':
            sub_key = "Phones"
            sub_display = "Phone"
        sub_prd_columns = SalesData[["Sub-Category", "Product Name", "Profit"]]    
        prd_select = sub_prd_columns.loc[sub_prd_columns["Sub-Category"] == str(sub_key)]
        prd_group = prd_select.groupby(by= "Product Name").sum().sort_values(by= "Profit", ascending = False)
        print(lines)     
    # error checking here v  
        num_prds = SalesData["Product Name"].value_counts()
        total_products = num_prds.shape
        userInput = input("\nThere are " + str(total_products) + " products total. How many products would you like to see? Please enter a number: ")
        invalid = True
        while invalid:
            if userInput.isnumeric() != True:
                userInput = input("Invalid input. Please enter a number: ")
            else:
                invalid = False
        print(lines)
        int_userInput = int(userInput)
        print("\nThe top " + str(userInput) + " most profitable " + sub_display + " products are:")
        print(prd_group.head(int_userInput))    
        print(dbl_lines)
        userInput = input("\nEnter 1 to view the least profitable products in the " + sub_display + " subcategory, or Enter 2 to return to the Product Sales Outlook Menu: ")
        while userInput != '1' and userInput != '2':
            if userInput != '1':
                userInput = input("\nInvalid input. Please enter a number from the list above: ")
            if userInput != '2':
                userInput = input("\nInvalid input. Please enter a number from the list above: ")
            else:
                break
        if userInput == '1':
            print(lines)
            print("\nThe least profitable products in the " + sub_display + " subcategory are: ")
            print(prd_group.tail(10))
            print(dbl_lines)
        elif userInput == '2':
            product_menu()
    elif ctgry_choice == '4':
        print("\n---------------- ALL PRODUCTS ----------------")
        print("\n1 - View the most profitable products")
        print("2 - View the least profitable products")
        userInput = input("\nPlease enter a number from the list above: ")
        while userInput != '1' and userInput != '2':
            if userInput != '1':
                userInput = input("\nInvalid input. Please enter a number from the list above: ")
            elif userInput != '2':
                userInput = input("\nInvalid input. Please enter a number from the list above: ")
            else:
                break
        print(lines)
        prod_prf_columns = SalesData[["Profit", "Product Name"]]
        all_products = prod_prf_columns.groupby(by= "Product Name").sum().sort_values(by= "Profit", ascending = False)
        num_prds = SalesData["Product Name"].value_counts()
        total_products = num_prds.shape 
        num_choice = input("\nThere are " + str(total_products) + " products total. How many products would you like to see? Please enter a number: ")
        invalid = True
        while invalid:
            if num_choice.isnumeric() != True:
                num_choice = input("Invalid input. Please enter a number: ")
            else:
                invalid = False
        print(lines)
        int_num_choice = int(num_choice)
        if userInput == '1':
            print("\nThe top " + num_choice + " most profitable products are:")
            print(all_products.head(int_num_choice))
            print(dbl_lines)
        elif userInput == '2':
            print("\nThe top " + num_choice + " least profitable products are:")
            print(all_products.tail(int_num_choice))
            print(dbl_lines)
    back = input("\nEnter 1 to return to the Product Sales Outlook Menu, or Enter 2 to return to the Main Menu: ")
    while back != '1' and back != '2':
        if back != '1':
            back = input("\nInvalid input. Please enter a number from the list above: ")
        elif back != '2':
            back = input("\nInvalid input. Please enter a number from the list above: ") 
        else:
            break
    if back == '1':
        product_menu()
    elif back == '2':
        main_menu()

def customer_menu():
    print("\n-------------- CUSTOMER LOYALTY --------------")
    print("\nView customers by:")
    print("\n1 - Purchase amount")
    print("2 - Frequency")
    print("3 - Recency")
    print("4 - Customer type")
    print("    or")
    print("5 - Return to the Main Menu")
    userInput = input("\nPlease enter a number from the list above: ")
    while userInput != '1' and userInput != '2' and userInput != '3' and userInput != '4' and userInput != '5':
        if userInput != '1':
            userInput = input("\nInvalid input. Please enter a number from the list above: ")
        elif userInput != '2':
            userInput = input("\nInvalid input. Please enter a number from the list above: ")
        elif userInput != '3':
            userInput = input("\nInvalid input. Please enter a number from the list above: ")
        elif userInput != '4':
            userInput = input("\nInvalid input. Please enter a number from the list above: ")
        elif userInput != '5':
            userInput = input("\nInvalid input. Please enter a number from the list above: ")
        else:
            break
    if userInput == '1':
        purchase_amount()
    elif userInput == '2':
        frequency()
    elif userInput == '3':
        recency()
    elif userInput == '4':
        customer_type()    
    elif userInput == '5':
        main_menu()

def purchase_amount():
    print("\n--------------- BY PURCHASE AMOUNT ---------------")
    print("\nView customers' purchase amount by:")
    print("\n1 - Sales")
    print("2 - Profits")
    print("3 - Quantity")
    print("    or")
    print("4 - Return to Customer Loyalty Menu")
    userInput = input("\nPlease enter a number from the list above: ") 
    while userInput != '1' and userInput != '2' and userInput != '3' and userInput != '4':
        if userInput != '1':
            userInput = input("\nInvalid input. Please enter a number from the list above: ")
        elif userInput != '2':
            userInput = input("\nInvalid input. Please enter a number from the list above: ")
        elif userInput != '3':
            userInput = input("\nInvalid input. Please enter a number from the list above: ")
        elif userInput != '4':
            userInput = input("\nInvalid input. Please enter a number from the list above: ")
        else:
            break
    if userInput == '1':
        customer_sales = SalesData[["Customer ID", "Customer Name", "Sales"]]
        most_sales = customer_sales.groupby(["Customer ID", "Customer Name"]).sum().sort_values(by= "Sales", ascending = False) 
        most_frequent = SalesData["Customer Name"].value_counts()
        total_customers = most_frequent.shape
        print(lines)
        invalid = True
        num_cust = input("There are " +  str(total_customers) + " total customers. How many customers would you like to view? Please enter a number: ")
        while invalid:
            if num_cust.isnumeric() != True:
                num_cust = input("Invalid input. Please enter a number: ")
            else:
                invalid = False
        print(lines)
        int_num_cust = int(num_cust)
        print("\nThe top " + num_cust + " most profitable customers, in terms of sales, are:")
        print(most_sales.head(int_num_cust))
        print(dbl_lines)
        least_sales = input("\nEnter 1 to view the least profitable customers, in terms of sales, or Enter 2 to return to the Customer Loyalty Menu: ")
        while least_sales != '1' and least_sales != '2':
            if least_sales != '1':
                least_sales = input("\nInvalid input. Please enter a number from the list above: ")
            elif least_sales != '2':
                least_sales = input("\nInvalid input. Please enter a number from the list above: ")
            else:
                break
        if least_sales == '1':
            print(lines)
            print("\nThe least profitable customers, in terms of sales, are:")
            print(most_sales.tail(10))
        elif least_sales == '2':
            customer_menu()
        print(dbl_lines)
    elif userInput == '2':
        customer_prf = SalesData[["Customer ID", "Customer Name", "Profit"]]
        most_prf_cus = customer_prf.groupby(["Customer ID", "Customer Name"]).sum().sort_values(by= "Profit", ascending = False)
        most_frequent = SalesData["Customer Name"].value_counts()
        total_customers = most_frequent.shape
        print(lines)
        invalid = True
        num_cust = input("There are " +  str(total_customers) + " total customers. How many customers would you like to view? Please enter a number: ")
        while invalid:
            if num_cust.isnumeric() != True:
                num_cust = input("Invalid input. Please enter a number: ")
            else:
                invalid = False
        print(lines)
        int_num_cust = int(num_cust)
        print("\nThe most profitable customers are:")
        print(most_prf_cus.head(int_num_cust))
        print(dbl_lines)
        least_prf_cus = input("\nEnter 1 to view the least profitable customers, or Enter 2 to return to the Purchase Amount Menu: ")
        while least_prf_cus != '1' and least_prf_cus != '2':
            if least_prf_cus != '1':
                least_prf_cus = input("\nInvalid input. Please enter a number from the list above: ")
            elif least_prf_cus != '2':
                least_prf_cus = input("\nInvalid input. Please enter a number from the list above: ")
            else:
                break
        if least_prf_cus == '1':
            print(lines)
            print("\nThe least profitable customers are:")
            print(most_prf_cus.tail(10))
        elif least_prf_cus == '2':
            purchase_amount()
        print(dbl_lines)
    elif userInput == '3':
        customer_quantity = SalesData[["Customer ID", "Customer Name", "Quantity"]]
        most_quantity = customer_quantity.groupby(["Customer ID", "Customer Name"]).sum().sort_values(by= "Quantity", ascending = False)
        most_frequent = SalesData["Customer Name"].value_counts()
        total_customers = most_frequent.shape
        print(lines)
        invalid = True
        num_cust = input("There are " +  str(total_customers) + " total customers. How many customers would you like to view? Please enter a number: ")
        while invalid:
            if num_cust.isnumeric() != True:
                num_cust = input("Invalid input. Please enter a number: ")
            else:
                invalid = False
        print(lines)
        int_num_cust = int(num_cust)
        print("\nThe customers who bought the most items are:\n")
        print(most_quantity.head(int_num_cust))
        print(dbl_lines)
        least_quantity = input("Enter 1 to view the customers who purchaed the least number of items, or Enter 2 to return to the Purchase Amount Menu: ")
        while least_quantity != '1' and least_quantity != '2':
            if least_quantity != '1':
                 least_quantity = input("\nInvalid input. Please enter a number from the list above: ")
            elif least_quantity != '2':
                least_quantity = input("\nInvalid input. Please enter a number from the list above: ")
            else:
                break
        if least_quantity == '1':
            print(lines)
            print("\nThe customers who purchased the least number of items are:")
            print(most_quantity.tail(10))
        elif least_quantity == '2':
            purchase_amount()
        print(dbl_lines)
    elif userInput == '4':
        customer_menu()
    return_userInput = input("\nEnter 1 to return to Customer Loyalty Menu, or Enter 2 to return to the Main Menu: ")
    while return_userInput != '1' and return_userInput != '2':
        if return_userInput != '1':
            return_userInput = input("\nInvalid input. Please enter a number from the list above: ")
        elif return_userInput != '2':
            return_userInput = input("\nInvalid input. Please enter a number from the list above: ")
        else:
            break
    if return_userInput == '1':
        customer_menu()
    elif return_userInput == '2':
        main_menu()
        
def frequency():
    print("\n------------- BY FREQUENCY -------------")
    print("\nView the:")
    print("\n1 - The most number of purchases made by customers")
    print("2 - The least number of purchses made by customers")
    print("    or")
    print("3 - Return to the Customer Loyalty Menu")
    choice_freq = input("\nPlease enter a number from the list above: ")
    while choice_freq != '1' and choice_freq != '2' and choice_freq != '3':
        if choice_freq != '1':
            choice_freq = input("\nInvalid input. Please enter a number from the list above: ")
        elif choice_freq != '2':
            choice_freq = input("\nInvalid input. Please enter a number from the list above: ")
        elif choice_freq != '3':
            choice_freq = input("\nInvalid input. Please enter a number from the list above: ")
        else:
             break
    if choice_freq == '1': 
        print(lines)
        print("\nView the Most Number of Purchases Made")
        print(lines)
        most_frequent = SalesData["Customer Name"].value_counts()
        total_customers = most_frequent.shape
        invalid = True
        num_cust = input("There are " +  str(total_customers) + " total customers. How many customers would you like to view? Please enter a number: ")
        print(lines)
        most_frequent = SalesData["Customer Name"].value_counts()
        int_num_cust = int(num_cust)
        print("\nCustomers Who Made the Most Number of Puchases:\n")
        print(most_frequent.head(int_num_cust))
    elif choice_freq == '2':
        print(lines)
        print("\nView the Least Number of Purchases Made")
        print(lines)
        most_frequent = SalesData["Customer Name"].value_counts()
        total_customers = most_frequent.shape
        invalid = True
        num_cust = input("There are " +  str(total_customers) + " total customers. How many customers would you like to view? Please enter a number: ")
        while invalid:
            if num_cust.isnumeric() != True:
                num_cust = input("Invalid input. Please enter a number: ")
            else:
                invalid = False
        most_frequent = SalesData["Customer Name"].value_counts()
        int_num_cust = int(num_cust)
        print(lines)
        print("\nCustomers Who Made the Least Number of Purchases:\n")
        print(most_frequent.tail(int_num_cust))
    elif choice_freq == '3':    
        customer_menu()
    print(dbl_lines)
    cust_back = input("\nEnter 1 to return the Frequency Menu, or 2 to return to the Customer Loyalty menu: ")
    while cust_back != '1' and cust_back != '2':
        if cust_back != '1':
            cust_back = input("\nInvalid input. Please enter a number from the list above: ")
        elif cust_back != '2':
            cust_back = input("\nInvalid input. Please enter a number from the list above: ")
    if cust_back == '1':
        frequency()
    elif cust_back == '2':
        customer_menu()

def recency():
    print("\n----------------- BY RECENCY ----------------")
    print("\nView the Customers and the Dates of the Most Recent Purchases")
    most_frequent = SalesData["Customer Name"].value_counts()
    total_customers = most_frequent.shape 
    print(lines)
    invalid = True
    num_cust = input("There are " +  str(total_customers) + " total customers. How many customers would you like to view? Please enter a number: ")
    while invalid:
        if num_cust.isnumeric() != True:
            num_cust = input("\nInvalid input. Please enter a number: ")
        else:
            invalid = False
    int_num_cust = int(num_cust)
    Customer_OrderDate = SalesData[["Customer Name", "Order Date"]]
    SortDates = Customer_OrderDate.sort_values(by = "Order Date", ascending = False)
    SortDates_noDuplicates =SortDates.drop_duplicates()
    int_num_cust = int(num_cust)
    print(lines)
    print("\nThe most recent purchases made by customers are:")
    print(SortDates_noDuplicates.head(int_num_cust))
    print(dbl_lines)
    cust_back = input("\nEnter 1 to return the Frequency Menu, or 2 to return to the Customer Loyalty menu: ")
    while cust_back != '1' and cust_back != '2':
        if cust_back != '1':
            cust_back = input("\nInvalid input. Please enter a number from the list above: ")  
        elif cust_back != '2':
            cust_back = input("\nInvalid input. Please enter a number from the list above: ")  
        else:
            break
    if cust_back == '1':
        frequency()
    elif cust_back == '2':
        customer_menu()
    
def customer_type():
    print("\n--------------- CUSTOMER TYPE ---------------")
    print("\nView by:")
    print("\n1 - Profit")
    print("2 - Quantity Sold")
    print("    or")
    print("3 - Return to the Customer Loyalty Menu")
    userInput = input("\nPlease enter a number from the list above: ")
    while userInput != '1' and userInput != '2' and userInput != '3':
        if userInput != '1':
            userInput = input("\nInvalid input. Please enter a number from the list above: ")
        elif userInput != '2':
            userInput = input("\nInvalid input. Please enter a number from the list above: ")
        elif userInput != '3':
            userInput = input("\nInvalid input. Please enter a number from the list above: ")
        else:
            break
    if userInput == '1':
        type_prf_columns = SalesData[["Segment", "Profit"]]
        type_prf = type_prf_columns.groupby(by= "Segment").sum().sort_values(by= "Profit", ascending = False)
        print(lines)
        print("\nCustomer Type by Profit:")
        print(type_prf.head())
    elif userInput == '2':
        type_prf_columns = SalesData[["Segment", "Quantity"]]
        type_prf = type_prf_columns.groupby(by= "Segment").sum().sort_values(by= "Quantity", ascending = False)
        print(lines)
        print("\nCustomer Type by Quantity Sold:")
        print(type_prf.head())
    elif userInput == '3':
        customer_menu()
    print(dbl_lines)
    back = input("\nEnter 1 to return to the Customer Type Menu, or 2 to return to the Customer Loyalty Menu: ")
    while back != '1' and back != '2':
        if back != '1':    
            back = input("\nInvalid input. Please enter a number from the list above: ")
        elif userInput != '2':
            back = input("\nInvalid input. Please enter a number from the list above: ")
        else:
            break
    if back == '1':
        customer_type()
    elif back == '2':
        customer_menu()

def date_menu():
    print("\n------------------- DATES -------------------")
    print("\nView by:")
    print("\n1 - Months")
    print("2 - Quarters")
    print("3 - Years")
    print("    or")
    print("4 - Return to the Main Menu")
    userInput = input("\nPlease enter a number from the list above: ")
    while userInput != '1' and userInput != '2' and userInput != '3' and userInput != '4':
        if userInput != '1':
            userInput = input("\nInvalid input. Please enter a number from the list above: ")
        elif userInput != '2':
            userInput = input("\nInvalid input. Please enter a number from the list above: ")
        elif userInput != '3':
            userInput = input("\nInvalid input. Please enter a number from the list above: ")
        elif userInput != '4':
            userInput = input("\nInvalid input. Please enter a number from the list above: ")
        else:
            break
    if userInput == '1': 
        print(lines)
        print("\nProfit by Months")
        profit_month = SalesData
        profit_month["Month"] = profit_month["Order Date"].dt.month
        monthly_data = profit_month[["Month", "Profit"]]
        monthly_data_sum = monthly_data.groupby(by= "Month").sum()
        print(monthly_data_sum)
        print(dbl_lines)
        monthly_data_sum = monthly_data_sum.reset_index()
        plt.style.use('ggplot')
        months = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        months_index = range(len(months))
        profit_amounts = [9, 10, 28, 11, 22, 21, 13, 21, 36, 31, 35, 43]
        fig = plt.figure()
        ax1 = fig.add_subplot(1,1,1)
        ax1.bar(months_index, profit_amounts, align= 'center', color= 'orange')
        ax1.xaxis.set_ticks_position('bottom')
        ax1.yaxis.set_ticks_position('left')
        plt.xticks(months_index, months, rotation=0, fontsize='x-large')
        plt.xlabel('Month', fontsize='xx-large')
        plt.ylabel('Dollars (in thousands)', fontsize='xx-large')
        plt.title('Profit by Months', fontsize='xx-large')
        plt.show()
    elif userInput == '2':
        print(lines)
        print("\nProfit by Quarters")
        profit_quarter = SalesData
        profit_quarter["Quarter"] = profit_quarter["Order Date"].dt.quarter
        quarterly_data = profit_quarter[["Quarter", "Profit"]]
        quarterly_data_sum = quarterly_data.groupby(by= "Quarter").sum()
        print(quarterly_data_sum)
        print(dbl_lines)
        quarterly_data_sum = quarterly_data_sum.reset_index()
        plt.style.use('ggplot')
        quarters = ['1', '2', '3', '4']
        quarters_index = range(len(quarters))
        profit_amounts = [49, 56, 73, 111]
        fig = plt.figure()
        ax1 = fig.add_subplot(1,1,1)
        ax1.bar(quarters_index, profit_amounts, align= 'center', color= 'orange')
        ax1.xaxis.set_ticks_position('bottom')
        ax1.yaxis.set_ticks_position('left')
        plt.xticks(quarters_index, quarters, rotation=0, fontsize='x-large')
        plt.xlabel('Quarter', fontsize='xx-large')
        plt.ylabel('Dollars (in thousands)', fontsize='xx-large')
        plt.title('Profit by Quarters', fontsize='xx-large')
        plt.show()
    elif userInput == '3':
        print(lines)
        print("\nProfit by Years")
        profit_year = SalesData
        profit_year["Year"] = profit_year["Order Date"].dt.year
        yearly_data = profit_year[["Year", "Profit"]]
        yearly_data_sum = yearly_data.groupby(by= "Year").sum()
        print(yearly_data_sum)
        print(dbl_lines)
        yearly_data_sum = yearly_data_sum.reset_index()
        plt.style.use('ggplot')
        years = ['2014', '2015', '2016', '2017']
        years_index = range(len(years))
        profit_amounts = [50, 62, 82, 94]
        fig = plt.figure()
        ax1 = fig.add_subplot(1,1,1)
        ax1.bar(years_index, profit_amounts, align= 'center', color= 'orange')
        ax1.xaxis.set_ticks_position('bottom')
        ax1.yaxis.set_ticks_position('left')
        plt.xticks(years_index, years, rotation=0, fontsize='x-large')
        plt.xlabel('Year', fontsize='xx-large')
        plt.ylabel('Dollars (in thousands)', fontsize='xx-large')
        plt.title('Profit by Years', fontsize='xx-large')
        plt.show()
    elif userInput == '4':    
        main_menu()
    print(dbl_lines)
    back = input("\nEnter 1 to return to the Dates Menu, or 2 to return to the Main Menu: ")
    while back != '1' and back != '2':
        if back != '1':
            back = input("\nInvalid input. Please enter a number from the list above: ")
        elif back != '2':
            back = input("\nInvalid input. Please enter a number from the list above: ")
        else:
            break
    if back == '1':
        date_menu()
    elif back == '2':
        main_menu()  

def region_menu():    
    print("\n------------------- REGION ------------------")
    print("\n1 - View products by region")
    print("2 - View profits by region")
    print("3 - View the most profitable region, the West")
    print("4 - Return to the Main Menu")
    rgn_userInput = input("\nPlease enter a number from the list above: ")   
    while rgn_userInput != '1' and rgn_userInput != '2'and rgn_userInput != '3' and rgn_userInput != '4':
        if rgn_userInput != '1':
            rgn_userInput = input("\nInvalid input. Please enter a number from the list above: ")
        elif rgn_userInput != '2':
            rgn_userInput = input("\nInvalid input. Please enter a number from the list above: ")
        elif rgn_userInput != '3':
            rgn_userInput = input("\nInvalid input. Please enter a number from the list above: ")
        elif rgn_userInput != '4':
            rgn_userInput = input("\nInvalid input. Please enter a number from the list above: ")
        else:
            break
    if rgn_userInput == '1':
        rgn_products()
    elif rgn_userInput == '2':
        rgn_profits()
    elif rgn_userInput == '3':
        the_west()
    elif rgn_userInput == '4':
        main_menu()
    
def rgn_products():
    print(lines)
    print("\nMost Profitable Products by Region")
    print(lines)
    print("\nWhich region would you like to see?")
    print("1 - Central")
    print("2 - East")
    print("3 - South")
    print("4 - West")
    userInput_region = input("\nPlease enter a number corresponding to the region you would like to see: ")
    while userInput_region != '1' and userInput_region != '2' and userInput_region != '3' and userInput_region != '4':
        if userInput_region != '1':
            userInput_region = input("\nInvalid input. Please enter a number from the list above: ")
        elif userInput_region != '2':
            userInput_region = input("\nInvalid input. Please enter a number from the list above: ")
        elif userInput_region != '3':
            userInput_region = input("\nInvalid input. Please enter a number from the list above: ")
        elif userInput_region != '4':
            userInput_region = input("\nInvalid input. Please enter a number from the list above: ")
        elif userInput_region != '5':
            userInput_region = input("\nInvalid input. Please enter a number from the list above: ")
        else:
            break
    if userInput_region == '1':
        region = "Central"
    elif userInput_region == '2':
        region = "East"
    elif userInput_region == '3':
        region = "South"
    elif userInput_region == '4':
        region = "West"
    print(lines)
    prod_prf_columns = SalesData[["Region", "Profit", "Product Name"]]
    rgn_select = prod_prf_columns.loc[SalesData["Region"] == region]
    prod_prf= rgn_select.groupby(by= "Product Name").sum().sort_values(by= "Profit", ascending = False)
    num_prds = SalesData["Product Name"].value_counts()
    total_products = num_prds.shape 
    userInput = input("\nThere are " + str(total_products) + " products total. How many products would you like to see? Please enter a number: ")
    invalid = True
    while invalid:
        if userInput.isnumeric() != True:
            userInput = input("Invalid input. Please enter a number: ")
        else:
            invalid = False
    print(lines)    
    int_userInput = int(userInput)
    print("\nThe top " + userInput + " products in the " + region + " are:")
    print(prod_prf.head(int_userInput)) 
    print(dbl_lines)
    back = input("\nEnter 1 to return to the Regions Menu, or Enter 2 to return to the Main Menu: ")
    while back != '1' and back != '2':
        if back != '1':
            back = input("\nInvalid input. Please enter a number from the list above: ")
        elif back != '2':
            back = input("\nInvalid input. Please enter a number from the list above: ")
        else:
            break
    if back == '1':
        region_menu()
    elif back == '2':
        main_menu()

def rgn_profits():
    print(lines)
    print("\nRegions in Terms of Profitability")
    print(lines)
    print("\nHow would you like to see the regions? By: ")
    print("1 - Profits")
    print("2 - Sales")
    print("3 - Quantity sold")
    userInput_rgn_prf = input("Please enter a number corresponding to how you would like to view the regions: ")
    while userInput_rgn_prf != '1' and userInput_rgn_prf != '2' and userInput_rgn_prf != '3':
        if userInput_rgn_prf!= '1':
            userInput_rgn_prf = input("\nInvalid input. Please enter a number from the list above: ")
        elif userInput_rgn_prf != '2':
            userInput_rgn_prf = input("\nInvalid input. Please enter a number from the list above: ")
        elif userInput_rgn_prf != '3':
            userInput_rgn_prf = input("\nInvalid input. Please enter a number from the list above: ")
        else:
            break
    if userInput_rgn_prf == '1':
        rgn_prf()
    elif userInput_rgn_prf == '2':
        rgn_sales()
    elif userInput_rgn_prf == '3':
        rgn_qsold()
    
def rgn_prf():
    print(lines)
    print("\nRegion by Profit")
    rgn_prf_columns = SalesData[["Region", "Profit"]]
    rgn_by_prf = rgn_prf_columns.groupby(by= "Region").sum().sort_values(by= "Profit", ascending = False)
    print(rgn_by_prf)
    print(lines)
    rgn_by_prf = rgn_by_prf.reset_index()
    plt.figure(figsize = (6,6))
    plt.title("Region Profit, in terms of Percentages", fontdict={'fontsize':20})
    plt.pie(rgn_by_prf.Profit, labels=rgn_by_prf.Region, autopct='%1.1f%%', textprops={'fontsize':15})
    plt.show()
    print(dbl_lines)
    back = input("Enter 1 to return to the Region Menu, or Enter 2 to return to the Main Menu: ")
    while back != '1' and back != '2':
        if back != '1':
            back = input("\nInvalid input. Please enter a number from the list above: ")
        elif back != '2':
            back = input("\nInvalid input. Please enter a number from the list above: ")
        else:
            break
    if back == '1':
        region_menu()
    elif back == '2':
        main_menu() 
    
def rgn_sales():
    print(lines)
    print("\nRegion by Sales")
    rgn_sales_columns = SalesData[["Region", "Sales"]]
    rgn_by_sales = rgn_sales_columns.groupby(by= "Region").sum().sort_values(by= "Sales", ascending = False)
    print(rgn_by_sales)
    print(dbl_lines)
    back = input("Enter 1 to return to the Region Menu, or Enter 2 to return to the Main Menu: ")
    while back != '1' and back != '2':
        if back != '1':
            back = input("\nInvalid input. Please enter a number from the list above: ")
        elif back != '2':
            back = input("\nInvalid input. Please enter a number from the list above: ")
        else:
            break
    if back == '1':
        region_menu()
    elif back == '2':
        main_menu()

def rgn_qsold():
    print(lines)
    print("\nRegion by Quantity Sold")
    rgn_qsold_columns = SalesData[["Region", "Quantity"]]
    rgn_by_qsold = rgn_qsold_columns.groupby(by= "Region").sum().sort_values(by= "Quantity", ascending = False)
    print(rgn_by_qsold)
    rgn_by_qsold = rgn_by_qsold.reset_index()
    print(lines)
    regions = ['Central', 'East', 'South', 'West']
    regions_index = range(len(regions))
    qsold_amounts = [8780, 10618, 6209, 12266]
    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1)
    ax1.bar(regions_index, qsold_amounts, align='center', color='purple')
    ax1.xaxis.set_ticks_position('bottom') 
    ax1.yaxis.set_ticks_position('left')
    plt.xticks(regions_index, regions, rotation=0, fontsize='x-large')
    plt.xlabel('Region', fontsize='xx-large')
    plt.ylabel('Units Sold', fontsize='xx-large')
    plt.title('Quantity Sold by Region', fontsize='xx-large')
    plt.show()
    print(dbl_lines)
    back = input("Enter 1 to return to the Region Menu, or Enter 2 to return to the Main Menu: ")
    while back != '1' and back != '2':
        if back != '1':
            back = input("\nInvalid input. Please enter a number from the list above: ")
        elif back != '2':
            back = input("\nInvalid input. Please enter a number from the list above: ")
        else:
            break
    if back == '1':
        region_menu()
    elif back == '2':
        main_menu()

def the_west():
    print("\n------------------ THE WEST -----------------")
    print("\nThe West is the most profitable region. Let's explore this region.")
    print(lines)
    print("\nView the:")
    print("\n1 - Profitability of states in this region")
    print("2 - Customer types in this region")
    print("    or")
    print("3 - Return to the Regions Menu")
    userInput = input("\nPlease enter a number from the list above: ")
    while userInput != '1' and userInput != '2' and userInput != '3':
        if userInput != '1':
            userInput = input("\nInvalid input. Please enter a number from the list above: ")
        elif userInput != '2':
            userInput = input("\nInvalid input. Please enter a number from the list above: ")
        elif userInput != '3':
            userInput = input("\nInvalid input. Please enter a number from the list above: ")
        else:
            break
    if userInput == '1':
        prf_rgn_columns = SalesData[["Region", "State", "Profit"]]
        rgn_select = prf_rgn_columns.loc[prf_rgn_columns["Region"]== "West"]
        prf_state = rgn_select.groupby(by= "State").sum().sort_values(by= "Profit", ascending= False)
        print(lines)
        print("\nThe most profitable states in the West are:")
        print(prf_state.head(8))
        print(dbl_lines)
        cont = input("\nEnter 1 to view the unprofitable states in the West: ")
        print(lines)
        while cont != '1':
            if cont != '1':
                cont = input("\nInvalid input. Please enter the number 1 to continue: ")
            else:
                break
        if cont == '1':
            print(lines)
            print("\nThe unprofitable states in the West are:")
            print(prf_state.tail(3))
            print(dbl_lines)
        userInput = input("\nEnter 1 to return to the West Menu, or Enter 2 to return to the Regions Menu: ")
        while userInput != '1' and userInput != '2':
            if userInput != '1':
                userInput = input("\nInvalid input. Please enter a number from the list above: ")
            elif userInput != '2':
                userInput = input("\nInvalid input. Please enter a number from the list above: ")
            else:
                break
        if userInput == '1':
            the_west()
        elif userInput == '2':
            region_menu()
    elif userInput == '2':
        cust_rgn_columns = SalesData[["Region", "Segment"]]
        rgn_select = cust_rgn_columns.loc[cust_rgn_columns["Region"]== "West"]
        cust_rgn = rgn_select["Segment"].value_counts()
        print(lines)
        print("\nThe customer type in the West is as follows:")
        print(cust_rgn.head())
        print(dbl_lines)
        userInput = input("\nEnter 1 to return to the West Menu, or Enter 2 to return to the Regions Menu: ")
        while userInput != '1' and userInput != '2':
            if userInput != '1':
                userInput = input("\nInvalid input. Please enter a number from the list above: ")
            elif userInput != '2':
                userInput = input("\nInvalid input. Please enter a number from the list above: ")
            else:
                break
        if userInput == '1':
            the_west()
        elif userInput == '2':
            region_menu()
    elif userInput == '3':
        region_menu()
   

homepage()
login()
