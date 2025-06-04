# Database configuration
DATABASE_URL = "postgresql://user:password@localhost/mydb"

# AWS Configuration  
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYzEXAMPLEKEY"
AWS_REGION = "us-west-2"

# Third party APIs
OPENAI_API_KEY = "sk-1234567890abcdefghijklmnopqrstuvwxyz123456"

# Google Services
GOOGLE_API_KEY = "AIzaSyDaGmWKa4JsXZ-HjGw7ISLn_3namBGewQe"

def get_database_connection():
    return f"Connected to {DATABASE_URL}"