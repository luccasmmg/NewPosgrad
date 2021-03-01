#!/bin/bash

echo "Building containers"
docker-compose -f docker-compose-e2e.yml up -d

# Hack to wait for postgres container to be up before running alembic migrations
sleep 5;

echo "Running migrations"
docker-compose -f docker-compose-e2e.yml run --rm backend alembic upgrade head

echo "Creating initial data"
docker-compose -f docker-compose-e2e.yml run --rm backend python3 app/initial_data.py

echo "Running tests"
docker-compose -f docker-compose-e2e.yml run --rm backend pytest

echo "Running Cypress Tests"
cd frontend
yarn run test:e2e

