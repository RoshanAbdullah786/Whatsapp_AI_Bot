from sqlalchemy import Table, Column, Integer, String, Text, DateTime, MetaData
from datetime import datetime

metadata = MetaData()

messages = Table(
    "messages",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("phone_number", String, nullable=False),
    Column("role", String, nullable=False),
    Column("content", Text, nullable=False),
    Column("timestamp", DateTime, default=datetime.utcnow()),
)
