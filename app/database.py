import os
import urllib.parse
from azure.identity import DefaultAzureCredential
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")
if not SQLALCHEMY_DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is required")

if SQLALCHEMY_DATABASE_URL.startswith("postgres://"):
    SQLALCHEMY_DATABASE_URL = SQLALCHEMY_DATABASE_URL.replace("postgres://", "postgresql://", 1)

# Logic to handle Managed Identity (Passwordless)
parsed = urllib.parse.urlparse(SQLALCHEMY_DATABASE_URL)
# If there's no password in the URL, we assume Managed Identity should be used
use_managed_identity = parsed.password is None and "localhost" not in SQLALCHEMY_DATABASE_URL

if use_managed_identity:
    def connector():
        credential = DefaultAzureCredential()
        token = credential.get_token("https://ossrdbms-aad.database.windows.net/.default")
        
        # Inject the token as the password
        host_port = f"{parsed.hostname}:{parsed.port}" if parsed.port else parsed.hostname
        conn_str = f"dbname={parsed.path[1:]} user={parsed.username} password={token.token} host={parsed.hostname} port={parsed.port or 5432} sslmode=require"
        
        import psycopg2
        return psycopg2.connect(conn_str)

    engine = create_engine("postgresql://", creator=connector)
else:
    engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
