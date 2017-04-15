import MySQLdb as mysql

print """
-----------------------------------------
    WELCOME TO THE TO DO LIST MANAGER
-----------------------------------------

\033[92mtype help to view help\033[0m
"""

h = """\033[1mcreate todo <todo list name> \033[0m -- to create a todo list\n
\033[1mopen todo <todo list name> \033[0m -- to change focus to the selected todo list\n
\033[1madd item <item name> \033[0m -- to add items to the selected todo list\n
\033[1mlist todos \033[0m -- to view all todo list\n
\033[1mlist items <todo list name> \033[0m -- to view all items in the todo list\n
"""