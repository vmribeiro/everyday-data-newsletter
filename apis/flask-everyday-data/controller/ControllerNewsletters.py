
from model.Connection import Connection

class ControllerNewsletters():

    def __init__(self):
        self.status = 1


    def insertNewsletter(self, user_id, title, text, banner_url, category):
        try:
            
            connection = Connection()
            conn_obj = connection.conn
            cursor = conn_obj.cursor()

            insert_query = """ INSERT INTO EVERYDAY_DATA.NEWSLETTERS (    NEWSLETTER_USER_ID
                                                                        , NEWSLETTER_TITLE
                                                                        , NEWSLETTER_TEXT
                                                                        , NEWSLETTER_BANNER_URL
                                                                        , NEWSLETTER_CATEGORY    ) 
                                            VALUES                   (    %s
                                                                        , %s
                                                                        , %s
                                                                        , %s
                                                                        , %s                       )
                    """

            record_to_insert = ( user_id, title, text, banner_url, category )
            
            cursor.execute(insert_query, record_to_insert)
            conn_obj.commit()
            count = cursor.rowcount
            print(count, "Record inserted successfully into Newsletter table.")

            connection.close_connection(cursor = cursor, connection = conn_obj)

            return True

        except Exception as ex:

            print("Error during Newsletter insertion. Error: {}".format(str(ex)))
            return False


    def updateNewsletter(self, newsletter_id, title = "nan", text = "nan", banner_url = "nan", category = "nan"):
        try:
            
            connection = Connection()
            conn_obj = connection.conn
            cursor = conn_obj.cursor()

            sql_select_query = """SELECT NEWSLETTER_TITLE, NEWSLETTER_TEXT, NEWSLETTER_BANNER_URL, NEWSLETTER_CATEGORY FROM EVERYDAY_DATA.NEWSLETTERS WHERE NEWSLETTER_ID = %s"""
            fields_to_select = (newsletter_id)
            cursor.execute(sql_select_query, fields_to_select)
            record = cursor.fetchone()

            if record is None:
                print("Newsletter {} not found!".format(newsletter_id))
                return False

            print("Updating Newsletter: \n\n" + str(record) + "\n\n") # Use it as a backup in case of issues

            update_query = """ UPDATE EVERYDAY_DATA.NEWSLETTERS 
                               SET                                NEWSLETTER_TITLE      = %s
                                                                , NEWSLETTER_TEXT       = %s   
                                                                , NEWSLETTER_BANNER_URL = %s
                                                                , NEWSLETTER_CATEGORY = %s
                                WHERE NEWSLETTER_ID = %s
                            """

            if title != "nan": 
                treated_title = title
            else: 
                treated_title = record[0]

            if text != "nan": 
                treated_text = text
            else: 
                treated_text = record[1]

            if banner_url != "nan": 
                treated_banner_url = banner_url
            else: 
                treated_banner_url= record[2]

            if category != "nan": 
                treated_category = category
            else: 
                treated_category= record[3]


            fields_to_update = (  treated_title
                                , treated_text
                                , treated_banner_url
                                , treated_category
                                , newsletter_id  )
            
            cursor.execute(update_query, fields_to_update)
            conn_obj.commit()
            count = cursor.rowcount
            print(count, "Record updated successfully into newsletter table.")

            connection.close_connection(cursor = cursor, connection = conn_obj)

            return True

        except Exception as ex:

            print("Error during Newsletter update. Error: {}".format(str(ex)))
            return False
        

    def deleteNewsletter(self, newsletter_id):
        try:
            
            connection = Connection()
            conn_obj = connection.conn
            cursor = conn_obj.cursor()

            delete_query = """ DELETE FROM EVERYDAY_DATA.NEWSLETTERS 
                               WHERE NEWSLETTER_ID = %s
                            """

            ids_to_delete = ( newsletter_id )
            
            cursor.execute(delete_query, ids_to_delete)
            conn_obj.commit()
            count = cursor.rowcount
            print(count, "Record deleted successfully from newsletters table.")

            connection.close_connection(cursor = cursor, connection = conn_obj)

            return True

        except Exception as ex:

            print("Error during newsletter deletion. Error: {}".format(str(ex)))
            return False


    def findNewsletterById(self, newsletter_id):
        try:
            connection = Connection()
            conn_obj = connection.conn
            cursor = conn_obj.cursor()

            sql_select_query = """
            SELECT    N.NEWSLETTER_ID
                    , N.NEWSLETTER_USER_ID
                    , N.NEWSLETTER_TITLE
                    , TO_CHAR(N.NEWSLETTER_DATE :: DATE, 'Mon dd, yyyy') AS NEWSLETTER_DATE
                    , N.NEWSLETTER_TEXT
                    , N.NEWSLETTER_BANNER_URL
                    , N.NEWSLETTER_CATEGORY
                    , U.USER_NAME
                    , U.USER_PROFILE_NAME
                    , U.USER_JOB
                    
            FROM EVERYDAY_DATA.NEWSLETTERS N
                LEFT JOIN EVERYDAY_DATA.USERS U
                ON N.NEWSLETTER_USER_ID = U.USER_ID
            WHERE NEWSLETTER_ID = %s
            """
            fields_to_select = (newsletter_id)
            cursor.execute(sql_select_query, fields_to_select)
            record = cursor.fetchone()
            if record is None:
                print("Newsletter {} not found!".format(newsletter_id))
                return False

            newsletter = {
                      'newsletter_id':                   record[0]
                    , 'newsletter_user_id':              record[1]
                    , 'newsletter_title':                record[2]
                    , 'newsletter_date':                 record[3]
                    , 'newsletter_text':                 record[4]
                    , 'newsletter_banner_url':           record[5]
                    , 'newsletter_category':             record[6]
                    , 'newsletter_author_username':      record[7]
                    , 'newsletter_author_profile_name':  record[8]
                    , 'newsletter_author_job':           record[9]
            }
            
            count = cursor.rowcount
            print(count, "Record selected successfully from newsletter table.")

            connection.close_connection(cursor = cursor, connection = conn_obj)

            return newsletter

        except Exception as ex:

            print("Error during newsletter select. Error: {}".format(str(ex)))
            return False
            

    def findAllNewsletters(self):
        try:
            import json
            
            connection = Connection()
            conn_obj = connection.conn
            cursor = conn_obj.cursor()

            sql_select_query = """
            SELECT    N.NEWSLETTER_ID
                    , N.NEWSLETTER_USER_ID
                    , N.NEWSLETTER_TITLE
                    , TO_CHAR(N.NEWSLETTER_DATE :: DATE, 'Mon dd, yyyy') AS NEWSLETTER_DATE
                    , N.NEWSLETTER_TEXT
                    , N.NEWSLETTER_BANNER_URL
                    , N.NEWSLETTER_CATEGORY
                    , U.USER_NAME
                    , U.USER_PROFILE_NAME
                    , U.USER_JOB
                    
            FROM EVERYDAY_DATA.NEWSLETTERS N
                LEFT JOIN EVERYDAY_DATA.USERS U
                ON N.NEWSLETTER_USER_ID = U.USER_ID
            """
            cursor.execute(sql_select_query)
            rows = cursor.fetchall()

            list_newsletters = []
            for row in rows:
                list_newsletters.append({
                          'newsletter_id':                   row[0]
                        , 'newsletter_user_id':              row[1]
                        , 'newsletter_title':                row[2]
                        , 'newsletter_date':                 row[3]
                        , 'newsletter_text':                 row[4]
                        , 'newsletter_banner_url':           row[5]
                        , 'newsletter_category':             row[6]
                        , 'newsletter_author_username':      row[7]
                        , 'newsletter_author_profile_name':  row[8]
                        , 'newsletter_author_job':           row[9]
                })
            
            count = cursor.rowcount
            print(count, "Record selected successfully from newsletters table.")

            connection.close_connection(cursor = cursor, connection = conn_obj)

            return list_newsletters

        except Exception as ex:

            print("Error during newsletters select. Error: {}".format(str(ex)))
            return False


