
from model.Connection import Connection

class ControllerUsuario():

    def __init__(self):
        self.status = 1


    def insertUser(self, email, name, password, profile_name, birthday, job):
        try:
            
            connection = Connection()
            conn_obj = connection.conn
            cursor = conn_obj.cursor()

            insert_query = """ INSERT INTO EVERYDAY_DATA.USERS (  USER_EMAIL
                                                                , USER_NAME
                                                                , USER_PASSWORD
                                                                , USER_PROFILE_NAME
                                                                , USER_BIRTHDAY
                                                                , USER_JOB     ) 
                            VALUES                    (           %s
                                                                , %s
                                                                , %s
                                                                , %s
                                                                , %s
                                                                , %s            )
                    """

            record_to_insert = (                                  email
                                                                , name
                                                                , password
                                                                , profile_name
                                                                , birthday
                                                                , job  )
            
            cursor.execute(insert_query, record_to_insert)
            conn_obj.commit()
            count = cursor.rowcount
            print(count, "Record inserted successfully into user table.")

            connection.close_connection(cursor = cursor, connection = conn_obj)

            return True

        except Exception as ex:

            print("Error during user insertion. Error: {}".format(str(ex)))
            return False


    def updateUser(self, user_id, email = "nan", name = "nan", password = "nan", birthday = "nan", job = "nan", subscription = "nan"):
        try:
            
            connection = Connection()
            conn_obj = connection.conn
            cursor = conn_obj.cursor()

            sql_select_query = """SELECT * FROM EVERYDAY_DATA.USERS WHERE USER_ID = %s"""
            fields_to_select = (user_id)
            cursor.execute(sql_select_query, fields_to_select)
            record = cursor.fetchone()

            if record is None:
                print("User {} not found!".format(user_id))
                return False

            print("Updating user: \n\n" + str(record) + "\n\n") # Use it as a backup in case of issues

            update_query = """ UPDATE EVERYDAY_DATA.USERS 
                               SET                                USER_EMAIL         = %s
                                                                , USER_NAME          = %s
                                                                , USER_PASSWORD      = %s
                                                                , USER_BIRTHDAY      = %s
                                                                , USER_JOB           = %s   
                                                                , USER_SUBSCRIPTION  = %s
                                WHERE USER_ID = %s
                            """

            if email != "nan": 
                treated_email = email
            else: 
                treated_email = record[1]

            if name != "nan": 
                treated_name = name
            else: 
                treated_name = record[2]

            if password != "nan": 
                treated_password = password
            else: 
                treated_password = record[3]

            if birthday != "nan": 
                treated_birthday = birthday
            else: 
                treated_birthday = record[5]

            if job != "nan": 
                treated_job = job
            else: 
                treated_job = record[6]

            if subscription != "nan": 
                treated_subscription = subscription
            else: 
                treated_subscription = record[7]

            fields_to_update = (                                  treated_email
                                                                , treated_name
                                                                , treated_password
                                                                , treated_birthday
                                                                , treated_job
                                                                , treated_subscription
                                                                , user_id  )
            
            cursor.execute(update_query, fields_to_update)
            conn_obj.commit()
            count = cursor.rowcount
            print(count, "Record updated successfully into user table.")

            connection.close_connection(cursor = cursor, connection = conn_obj)

            return True

        except Exception as ex:

            print("Error during user update. Error: {}".format(str(ex)))
            return False
        

    def deleteUser(self, user_id):
        try:
            
            connection = Connection()
            conn_obj = connection.conn
            cursor = conn_obj.cursor()

            delete_query = """ DELETE FROM EVERYDAY_DATA.USERS 
                               WHERE USER_ID = %s
                            """

            ids_to_delete = ( user_id )
            
            cursor.execute(delete_query, ids_to_delete)
            conn_obj.commit()
            count = cursor.rowcount
            print(count, "Record deleted successfully from user table.")

            connection.close_connection(cursor = cursor, connection = conn_obj)

            return True

        except Exception as ex:

            print("Error during user deletion. Error: {}".format(str(ex)))
            return False


    def findUserById(self, user_id):
        try:
            
            connection = Connection()
            conn_obj = connection.conn
            cursor = conn_obj.cursor()

            sql_select_query = """SELECT * FROM EVERYDAY_DATA.USERS WHERE USER_ID = %s"""
            fields_to_select = (user_id)
            cursor.execute(sql_select_query, fields_to_select)
            record = cursor.fetchone()

            if record is None:
                print("User {} not found!".format(user_id))
                return False

            user = {
                      'id': record[0]
                    , 'email': record[1]
                    , 'name': record[2]
                    , 'password': record[3]
                    , 'profile_name': record[4]
                    , 'birthday': record[5]
                    , 'job': record[6]
                    , 'subscription': record[7]
            }   
            
            count = cursor.rowcount
            print(count, "Record selected successfully from user table.")

            connection.close_connection(cursor = cursor, connection = conn_obj)

            return user

        except Exception as ex:

            print("Error during user select. Error: {}".format(str(ex)))
            return False
            

    def findAllUsers(self):
        try:
            import json
            
            connection = Connection()
            conn_obj = connection.conn
            cursor = conn_obj.cursor()

            sql_select_query = """SELECT * FROM EVERYDAY_DATA.USERS"""
            cursor.execute(sql_select_query)
            rows = cursor.fetchall()

            list_users = []
            for row in rows:
                list_users.append({
                          'id':                 row[0]
                        , 'email':              row[1]
                        , 'name':               row[2]
                        , 'password':           row[3]
                        , 'profile_name':       row[4]
                        , 'birthday':           row[5]
                        , 'job':                row[6]
                        , 'subscription':       row[7]
                })
            
            count = cursor.rowcount
            print(count, "Record selected successfully from user table.")

            connection.close_connection(cursor = cursor, connection = conn_obj)

            return list_users

        except Exception as ex:

            print("Error during user select. Error: {}".format(str(ex)))
            return False


