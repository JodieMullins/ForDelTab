import sqlite3 as db

def CreateForDel():

    """

    Establishes foundation for Fordel store's database. 
    Executes 3 tables: 
                1) Orders - customers and delivery address
                2) Returns 
                3) Sales representatives and regions
    
    """

    con = db.connect('Fordel.db')

    #mc for mouseclick
    mc = con.cursor()

    # ORDERS
   
    orders = pd.read_csv('orders.csv', index_col=None)

    orders_table = pd.orders.to_sql('orders', if_exists='replace')


    # save changes from INSERT
    con.commit()