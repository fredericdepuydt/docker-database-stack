#!/bin/sh

############################################################################
## Raspberry-Pi installation script                                       ##
## Author: Frederic Depuydt                                               ##
## Mail: frederic.depuydt@outlook.com                                     ##
##                                                                        ##
## Executing this script requires the 'depuydt' shell libraries           ##
############################################################################

## INCLUDES
. /usr/local/lib/depuydt/sh/echoes.sh
. /usr/local/lib/depuydt/sh/files.sh

## TITLE
echo_section "DOCKER DEPLOYING:" "Database Stack (Installing)"

# Creating external networks
if [ -z "$(docker network list -f name=^web$ -q)" ]; then docker network create web; fi

## Setting database root password
printf " Database root password: "
read var_read
# adding domainname to /etc/environment file as DOMAINNAME
file_set_line "/etc/environment" "^DATABASE_ROOT_PW=\".*\"" "DATABASE_ROOT_PW=\"$var_read\""

## Creating containers
docker-compose up -d --build
