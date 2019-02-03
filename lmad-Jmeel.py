from os import *
system("export MSF_DATABASE_CONFIG=database.yml")
system("export MSF_DATABASE_CONFIG=/home/xroot7/.msf4/database.yml")
system("MSF_DATABASE_CONFIG=/home/xroot7/.msf4/database.yml")
system("service postgresql start")
system("service apache2 start")
