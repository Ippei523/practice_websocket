# Description: Makefile for the server

.PHONY: start
start:
	@echo "Starting server..."
	@sh ./scripts/frontend-start.sh &
	@sh ./scripts/backend-start.sh
	@echo "Server started!"

.PHONY: init-db
init-db:
	@echo "Initializing database..."
	@sh ./scripts/init-db.sh
	@echo "Database initialized!"
