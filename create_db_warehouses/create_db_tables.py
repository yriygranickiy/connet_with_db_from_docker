import conection

con = conection.connection_db()

cursor = con.cursor()


def create_tables():

    commands = (

        """
            CREATE TABLE IF NOT EXISTS category (
                category_id INTEGER PRIMARY KEY,
                category_name TEXT NOT NULL,
                description TEXT NOT NULL
            )
        """,

        """
           CREATE TABLE IF NOT EXISTS suppliers (
               supplier_id INTEGER PRIMARY KEY,
               supplier_name TEXT NOT NULL,
               contact_person TEXT NOT NULL,
               phone_number TEXT NOT NULL,
               email TEXT NOT NULL,
               address TEXT NOT NULL
           )
       """,

        """
           CREATE TABLE IF NOT EXISTS employee (
               employee_id INTEGER PRIMARY KEY,
               first_name TEXT NOT NULL,
               last_name TEXT NOT NULL,
               position TEXT NOT NULL,
               phone TEXT NOT NULL,
               email TEXT NOT NULL
           )
       """,

        """
           CREATE TABLE IF NOT EXISTS products (
               product_id INTEGER PRIMARY KEY,
               product_name TEXT NOT NULL,
               category_id INTEGER NOT NULL ,
               supplier_id INTEGER NOT NULL,
               quantity INTEGER NOT NULL,
               price DECIMAL(10,2) NOT NULL,
               description TEXT NOT NULL,
               created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
               FOREIGN KEY (category_id) REFERENCES category (category_id),
               FOREIGN KEY (supplier_id) REFERENCES suppliers (supplier_id)
           )
       """,


        """
            CREATE TABLE IF NOT EXISTS warehouse_transaction(
                transaction_id INTEGER PRIMARY KEY,
                product_id INTEGER NOT NULL,
                transaction_type TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                employee_id INTEGER NOT NULL,
                comments TEXT NOT NULL,
                FOREIGN KEY (product_id) REFERENCES products (product_id),
                FOREIGN KEY (employee_id) REFERENCES employee (employee_id)
            )
        """,

        """
            CREATE TABLE IF NOT EXISTS orders (
                order_id INTEGER PRIMARY KEY,
                product_id INTEGER NOT NULL,
                quantity INTEGER NOT NULL,
                order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                order_status TEXT NOT NULL,
                supplier_id INTEGER NOT NULL,
                FOREIGN KEY (product_id) REFERENCES products (product_id),
                FOREIGN KEY (supplier_id) REFERENCES suppliers (supplier_id)
            )
        """,
        """
            CREATE TABLE IF NOT EXISTS warehouse (
                warehouse_id INTEGER PRIMARY KEY,
                warehouse_name TEXT NOT NULL,
                location TEXT NOT NULL
            )
        """
    )

    try:
        for command in commands:
            cursor.execute(command)
            con.commit()
            print("Command executed successfully")
    except Exception as e:
        print(e)
    finally:
        if con is not None:
            con.close()