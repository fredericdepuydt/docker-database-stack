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
sys.path.insert(1, '/usr/local/lib/depuydt/python/')

from echo import echo
from docker import docker
from environment import environment

## TITLE
echo.section("DOCKER DEPLOYING","Database Stack (Starting)");

## Gathering required variables
environment.get("DOMAINNAME");
environment.get("MYSQL_ROOT_PASSWORD", True);

## Starting All Containers
docker.compose.up("-d");

