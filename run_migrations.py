#!/usr/bin/env python3
"""
Database migration script
SECURE VERSION - Uses environment variables only
"""

import os
import sys
import subprocess

def check_environment():
    """Check if required environment variables are set."""
    required_vars = ["DATABASE_URL", "DIRECT_URL"]
    missing_vars = []
    
    for var in required_vars:
        if not os.getenv(var):
            missing_vars.append(var)
    
    if missing_vars:
        print(f"❌ Error: Missing required environment variables: {', '.join(missing_vars)}")
        print("Please set these variables in your environment or .env file")
        return False
    
    return True

def run_migrations():
    """Run Prisma migrations."""
    print("🔄 Running database migrations...")
    print("Using environment variables for database connection")
    
    try:
        # Change to backend directory
        os.chdir("autogpt_platform/backend")
        
        # Run Prisma generate
        print("📦 Generating Prisma client...")
        result = subprocess.run(["poetry", "run", "prisma", "generate"], 
                              capture_output=True, text=True)
        if result.returncode != 0:
            print(f"❌ Prisma generate failed: {result.stderr}")
            return False
        
        # Run Prisma migrate deploy
        print("🚀 Deploying migrations...")
        result = subprocess.run(["poetry", "run", "prisma", "migrate", "deploy"], 
                              capture_output=True, text=True)
        if result.returncode != 0:
            print(f"❌ Migration deploy failed: {result.stderr}")
            return False
        
        print("✅ Database migrations completed successfully")
        return True
        
    except Exception as e:
        print(f"❌ Error running migrations: {e}")
        return False

if __name__ == "__main__":
    if not check_environment():
        sys.exit(1)
    
    if not run_migrations():
        sys.exit(1)
