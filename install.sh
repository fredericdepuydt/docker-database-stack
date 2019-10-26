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
echo_section "DOCKER DEPLOYING:" "Database Stack"

## Setting database root password
printf " Database root password: "
read var_read
# adding domainname to /etc/environment file as DOMAINNAME
sudo file_set_line "/etc/environment" "^DATABASE_ROOT_PW=\".*\"" "DATABASE_ROOT_PW=\"$var_read\""

## Creating containers
docker-compose up -d --build
