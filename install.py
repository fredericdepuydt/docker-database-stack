#!/usr/bin/env python3

############################################################################
## Raspberry-Pi installation script                                       ##
## Author: Frederic Depuydt                                               ##
## Mail: frederic.depuydt@outlook.com                                     ##
##                                                                        ##
## Executing this script requires the 'depuydt' python libraries          ##
############################################################################

## INCLUDES
import sys
sys.path.insert(1, '/home/pi/installation/lib/depuydt/python/');
#sys.path.insert(1, '/usr/local/lib/depuydt/python/')

from echo import echo
from docker import docker
from environment import environment
from mysql import mysql

## TITLE
echo.section("DOCKER DEPLOYING", "Database Stack (Installing)");

# Creating database and user account
mysql_name = environment.get("MYSQL_ROOT_PASSWORD", True);

## Checking external networks
docker.network.exists("web");

## Creating the volumes, networks and containers
docker.compose.up("--build --no-start");