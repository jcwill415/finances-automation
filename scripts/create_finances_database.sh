#!/usr/bin/env bash

# Create a new PostgreSQL database storage cluster, start up a server for it and create a database there.

database="finances"
database_storage_area="../data/database_cluster"
user="Marcus1"


overwrite_cluster() {
    # If the cluster exists already, ask the user if they want to overwrite it
    if [ -d $database_storage_area ]; then
        while true; do
            read -p "Database cluster already exists: would you like to overwrite it? " choice

            case $choice in
                [Yy]* )
                    pg_ctl -D $database_storage_area stop
                    rm -r $database_storage_area
                    break;;

                [Nn]* )
                    exit;;

                * )
                    echo "Please answer yes or no:";;

            esac
        done
    fi
}


create_database() {
    # Create database cluster
    initdb -D $database_storage_area

    # Start database server
    pg_ctl -D $database_storage_area start

    # Create user database so future psql commands can be executed by them
    createdb $user

    # Create the required database
    createdb $database

    # Stop server
    pg_ctl -D $database_storage_area stop
}


overwrite_cluster
create_database
