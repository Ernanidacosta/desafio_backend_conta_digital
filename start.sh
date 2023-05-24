#!/bin/bash

set -e

# Function to install PostgreSQL
install_postgresql() {
  echo "Installing PostgreSQL..."
  # Add commands here to install PostgreSQL on your specific system
  # For example, on Ubuntu or Debian-based systems:
  apt-get update
  apt-get install -y postgresql
}

# Check if psql command is available
if ! command -v psql &> /dev/null; then
  echo "psql command not found. Installing PostgreSQL..."
  install_postgresql
fi

# Verifica se o banco de dados já existe
if psql -h localhost -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c '\q' 2>/dev/null; then
  echo "Banco de dados já existe."
else
  echo "Criando banco de dados..."
  psql -h localhost -U "$POSTGRES_USER" -c "CREATE DATABASE $POSTGRES_DB"
fi

# Continue with the rest of the script
echo "Carrying on with the remaining script..."
# Add your remaining commands here
