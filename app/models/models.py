from datetime import datetime
from sqlalchemy import Column, String, Integer, Float, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BankAccount(Base):
    __tablename__  = 'bank_accounts'
    bank_account_id = Column(Integer, primary_key=True)
    currency = Column(String(3))
    balance = Column(Float, default=0.0)
    user_id = Column(Integer, ForeignKey('users.user_id'))


class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    fullname = Column(String)
    login = Column(String, unique=True, nullable=False)
    password = Column(String)


class Transaction(Base):
    __tablename__ = 'transactions'
    transaction_id = Column(Integer, primary_key=True)
    amount = Column(Float)
    currency = Column(String(3))
    type = Column(String(3))
    from_account_id = Column(Integer, ForeignKey('bank_accounts.bank_account_id'))
    to_account_id = Column(Integer, ForeignKey('bank_accounts.bank_account_id'))
    transaction_type_id = Column(Integer, ForeignKey('transaction_types.transaction_type_id'))
    timestamp = Column(DateTime, default=datetime)


class TransactionType(Base):
    __tablename__ = 'transaction_types'
    transaction_type_id = Column(Integer, primary_key=True)
    transaction_name = Column(String)
    transaction_code = Column(String)