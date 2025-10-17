#!/bin/bash
# Database connection check script
# SECURE VERSION - Uses environment variables only

if [ -z "$DATABASE_URL" ]; then
    echo "❌ Error: DATABASE_URL environment variable not set"
    echo "Please set DATABASE_URL in your environment or .env file"
    exit 1
fi

echo "🔍 Checking database connection..."
echo "Using DATABASE_URL from environment variables"

# Test connection using environment variable
psql "$DATABASE_URL" -c "SELECT version();" > /dev/null 2>&1

if [ $? -eq 0 ]; then
    echo "✅ Database connection successful"
else
    echo "❌ Database connection failed"
    echo "Please check your DATABASE_URL environment variable"
    exit 1
fi
