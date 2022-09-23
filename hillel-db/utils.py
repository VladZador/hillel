import sqlite3
import os


db_pass = os.path.join(os.getcwd(), "chinook.db")


def _execute_query(db, query_sql: str) -> list:
    """
    Executes a given search query to the 'Chinook' database
    :param db: database file
    :param query_sql: a query
    :return: a list of query execution result
    """
    connection = sqlite3.connect(db)
    cur = connection.cursor()
    result = cur.execute(query_sql).fetchall()
    connection.close()
    return result


def get_filtered_customers(city=None,
                           state=None) -> list:
    """
    Returns clients, filtered by city and/or state (if necessary)
    :param city: str
    :param state: str
    :return: clients list
    """
    query_sql = '''
        SELECT *
          FROM customers
    '''
    if city and state:
        query_sql += f"WHERE City = '{city}' AND State = '{state}';"
    elif city:
        query_sql += f"WHERE City = '{city}';"
    elif state:
        query_sql += f"WHERE State = '{state}';"
    else:
        query_sql += ";"
    return _execute_query(db_pass, query_sql)


def get_number_of_customer_names():
    """
    Returns a list of tuples with the numbers of occurrences of names in the database
    :return: a list of name occurrences
    """
    query_sql = """
        SELECT FirstName, COUNT(CustomerId)
          FROM customers
          GROUP BY FirstName
          ORDER BY COUNT(CustomerId);
    """
    return list(_execute_query(db_pass, query_sql))


def get_total_profit() -> str:
    """
    Counts the orders profit
    :return: total profit
    """
    query_sql = """
    SELECT sum(UnitPrice * Quantity)
      FROM invoice_items;
    """
    return str(_execute_query(db_pass, query_sql)[0][0])

