def query_table_user():
    sql = ('\n'
           '    \n'
           '            CREATE TABLE `user` (\n'
           '            `ID`	INTEGER PRIMARY KEY AUTOINCREMENT,\n'
           '            `NAME`	TEXT NOT NULL,\n'
           '            `AGE`	INTEGER NOT NULL,\n'
           '            `EMAIL`	INTEGER NOT NULL, \n'
           '            `PASSWORD` TEXT NOT NULL\n'
           '        );\n'
           '            ')
    return sql