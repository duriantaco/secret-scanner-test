# Database configuration
DATABASE_URL = "postgresql://user:password@localhost/mydb"

# AWS Configuration  
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "[REDACTED_wJal...LEKE]Y"
AWS_REGION = "us-west-2"

# Third party APIs
OPENAI_API_KEY = "sk-[REDACTED_1234...1234]56"
STRIPE_SECRET_KEY = "[REDACTED_sk_l...klmn]"

# Google Services
GOOGLE_API_KEY = "[REDACTED_AIza...ewQe]"

def get_database_connection():
    return f"Connected to {DATABASE_URL}"