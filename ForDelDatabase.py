import sqlite3 as db
import pandas as pd

"""
#def CreateForDel():



    Establishes foundation for Fordel store's database. 
    Executes 3 tables: 
                1) Orders - customers and delivery address
                2) Returns 
                3) Sales representatives and regions
    

    # establish connection to SQL database
con = db.connect('Fordel.db')

    #mc for mouseclick
mc = con.cursor()

    # ORDERS
   
orders = pd.read_csv('Orders.csv', index_col=None)

orders_table = pd.orders.to_sql(name=orders, con=mc, if_exists='replace')

    # RETURNS

returns = pd.read_csv('Returns.csv', index_col=None)

returns_table = pd.returns.to_sql(name=returns, con=mc, if_exists='replace')

    # PEOPLE

people = pd.read_csv('People.csv', index_col=None)

people_table = pd.people.to_sql(name=people, con=mc, if_exists='replace')

    # save changes from INSERT
con.commit()

con.close()


    def main():
        CreateForDel()

if __name__ == "__main__":
    main()

"""


"""

# establish connection to SQL database
conn = db.connect('Fordel.db')

# mc for mouseclick
mc = conn.cursor()


excel_df = pd.read_excel('tabstoreUpdated.xlsx', sheet_name=None)
# read in excel file
# iterate through sheets
    # > each sheet is table within database

conn.commit()

conn.close()

"""