#!/usr/bin/env python3

############################################################################
## Author: Frederic Depuydt                                               ##
## Mail: frederic.depuydt@outlook.com                                     ##
############################################################################

## INCLUDES
from depuydt import echo
from depuydt import file
from depuydt.environment import Environment
from depuydt.system import Link

# CREATING SYMBOLIC LINKS
L = Link.create("./config", "~/docker/config/database")
echo.notice("Link created '" + str(L) + "' pointing to '" + str(L.target()) + "'")


if not file.exists("~/.env"):    
    file.create("~/.env")
env = Environment("~/.env")
db_container = env.require("DB_CONTAINER_NAME")
db_username  = env.require("DB_ROOT_USERNAME", "root")
db_password  = env.require("DB_ROOT_PASSWORD")
#env.export()
env.save()


if not file.exists("./config/.env"):
    file.create("./config/.env")
env = Environment("./config/.env")
db_username = env.require("MYSQL_USERNAME", db_username)
db_password = env.require("MYSQL_ROOT_PASSWORD", db_password)
env.save()

