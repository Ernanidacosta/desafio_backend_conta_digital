#!/bin/bash

set -e

# Verifica se o banco de dados já existe
if psql -h localhost -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c '\q' 2>/dev/null; then
  echo "Banco de dados já existe."
else
  echo "Criando banco de dados..."
  psql -h localhost -U "$POSTGRES_USER" -c "CREATE DATABASE $POSTGRES_DB"
fi
