from sqlalchemy import VARCHAR, Column, Integer

from database import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(VARCHAR(255), nullable=False)
    author = Column(VARCHAR(255), nullable=False)
    publish_date = Column(VARCHAR(255), nullable=False)
