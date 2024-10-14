#!/bin/bash

POSTGRES_USER="tech"
POSTGRES_PASSWORD="tech"
POSGRES_DB="sample_message_db"

# Start the Postgres service
brew services start postgresql
echo "Creating User ..."
psql postgres -c "CREATE USER $POSTGRES_USER WITH PASSWORD '$POSTGRES_PASSWORD';" 2> /dev/null
echo "Creating Database ..."
psql postgres -c "CREATE DATABASE $POSGRES_DB WITH OWNER $POSTGRES_USER;" 2> /dev/null
echo "completed creating user and database"
