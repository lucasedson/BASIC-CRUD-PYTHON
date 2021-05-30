from Config import conect_database, create_table_user, insert_user, execute_sql

Name = "Lucas"
Age = 25
Email = "lucasedson654@gmail.com"
Password = ";)"

if __name__ == '__main__':
    conect_database()
    create_table_user()
    insert_user(Name, Age, Email, Password)
    #execute_sql("UPDATE user SET NAME = 'JonhDoe' WHERE ID = '1';")
    #execute_sql("DELETE from user")
    print(execute_sql("SELECT * FROM user"))
