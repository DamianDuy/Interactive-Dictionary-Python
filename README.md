# Interactive-Dictionary-Python
Interactive dictionary written in Python.
The user provides the word in English and receives the definition(s) of it. The app also has a feature of deleting the word/definition(s)
from dictionary as well as adding the new word with new defintion(s). The first version of the app will be command line based. It is planned
to change it to the web app in the future.
The problems with the program:
1. It uses json file instead of database so there would be a performence issues if the size of the file would grow too much.
2. It could be enhanced by using a database but then, there would be a problem with editing the dictionary (adding/deleting operations).