#!/bin/bash
# Database migration script
# SECURE VERSION - Uses environment variables only

if [ -z "$DATABASE_URL" ]; then
    echo "❌ Error: DATABASE_URL environment variable not set"
    echo "Please set DATABASE_URL in your environment or .env file"
    exit 1
fi

if [ -z "$DIRECT_URL" ]; then
    echo "❌ Error: DIRECT_URL environment variable not set"
    echo "Please set DIRECT_URL in your environment or .env file"
    exit 1
fi

echo "🔄 Running database migrations..."
echo "Using environment variables for database connection"

# Set environment variables for Prisma
export DATABASE_URL
export DIRECT_URL

# Run migrations
cd autogpt_platform/backend
poetry run prisma generate
poetry run prisma migrate deploy

if [ $? -eq 0 ]; then
    echo "✅ Database migrations completed successfully"
else
    echo "❌ Database migrations failed"
    exit 1
fi
