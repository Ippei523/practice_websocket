#!/bin/bash

if [ -f ./scripts/.env ]; then
  source ./scripts/.env
else
  echo "No .env file found"
  exit 1
fi

# show the variables
echo "POSTGRES_USER: $POSTGRES_USER"
echo "POSTGRES_PASSWORD: $POSTGRES_PASSWORD"
echo "POSGRES_DB: $POSGRES_DB"

# Start the Postgres service
brew services start postgresql
echo "Creating User ..."
psql postgres -c "CREATE USER $POSTGRES_USER WITH PASSWORD '$POSTGRES_PASSWORD';" 2> /dev/null
echo "Creating Database ..."
psql postgres -c "CREATE DATABASE $POSGRES_DB WITH OWNER $POSTGRES_USER;" 2> /dev/null
echo "completed creating user and database"
