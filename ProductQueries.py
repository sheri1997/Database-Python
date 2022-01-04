from DatabaseConnection import DataBase

database = DataBase.connection_database()
cursor = database.cursor(buffered=None)


class ProductQueries:
    @staticmethod
    def add(item, price, amount, yearofmanufacture, section):
        '''
        Performing the Create Operation
        :return: Will return the user which has been added successfully
        '''
        user_add = (
            "insert into products""(item, price, amount, yearofmanufacture, section)""values(%("
            "item)s,%(price)s,%(amount)s,%(yearofmanufacture)s,%(section)s)")
        info = {
            'item': item,
            'price': price,
            'amount': amount,
            'yearofmanufacture': yearofmanufacture,
            'section': section
        }
        cursor.execute(user_add, info)
        database.commit()
        return "User Added Successfully"

    @staticmethod
    def retrieve():
        '''
        Preforming the Retrieve Operation
        :return: will return the retrieved database
        '''
        user_retrieve = "select * from products"
        cursor.execute(user_retrieve)
        data = [i for i in cursor]
        return data

    @staticmethod
    def inner_join():
        '''
        Performing the inner join here
        :return: will return the inner join values here
        '''
        user_join = "SELECT details.mobile_no AS Detail, products.item AS favorite FROM details INNER JOIN products "
        # "ON details.last_name = products.section "
        cursor.execute(user_join)
        result = cursor.fetchall()
        for x in result:
            return x

    @staticmethod
    def left_join():
        '''
        Performing the left join here
        :return: will return the executed left join
        '''
        user_join = "SELECT details.mobile_no AS Detail, products.item AS favorite FROM details LEFT JOIN products ON " \
                    "details.first_name = products.amount "
        cursor.execute(user_join)
        result = cursor.fetchall()
        for x in result:
            return x

    @staticmethod
    def right_join():
        '''
        Performing the right join here
        :return: will return the executed right join
        '''
        user_join = "SELECT details.mobile_no AS Detail, products.item AS favorite FROM details RIGHT JOIN products ON " \
                    "details.first_name = products.amount "
        cursor.execute(user_join)
        result = cursor.fetchall()
        for x in result:
            return x


ss = ProductQueries()
print(ss)
