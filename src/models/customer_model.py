from database.db import get_connection
from .entities.customer import customer
import sys

class customerModel():
    @classmethod
    def get_customers(self):
        try:
            connection=get_connection()
            customers=[]

            with connection.cursor() as cursor:
                cursor.execute("SELECT \"Id\", \"FirstName\", \"LastName\", \"Phone\", \"Email\", \"Address\" FROM customer ORDER BY \"Id\" ASC")
                resultset=cursor.fetchall()
                for row in resultset:
                    #customers.append(customer(row[0],row[1],row[2],row[3],row[4],row[5]).to_JSON())
                    customers.append(customer(row[0],row[1],row[2],row[3],row[4],row[5]).to_JSON())
            connection.close()
            return customers
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_customer(self, id):
        try:
            connection=get_connection()
            _customer=None
            with connection.cursor() as cursor:
                cursor.execute("SELECT \"Id\", \"FirstName\", \"LastName\", \"Phone\", \"Email\", \"Address\" FROM public.customer WHERE \"Id\"= %s", (id,))
                row =cursor.fetchone()
                if row != None:
                    _customer = customer(row[0],row[1],row[2],row[3],row[4],row[5]).to_JSON()
            connection.close()
            return _customer
        except Exception as ex:
            raise Exception(ex)