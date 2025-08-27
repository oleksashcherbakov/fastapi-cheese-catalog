from enum import StrEnum, auto

from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship

from db.engine import Base


class PackagingType(StrEnum):
    IN_PACKAGE = "in_package"
    WEIGHT = "weight"


class DBCheeseType(Base):
    __tablename__ = "cheese_type"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(511), nullable=False, unique=True)


class DBCheese(Base):
    __tablename__ = "cheese"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False, unique=True)
    price = Column(Integer, nullable=False)
    packaging_type = Column(Enum(PackagingType), nullable=False)
    cheese_type_id = Column(Integer, ForeignKey("cheese_type.id"))

    cheese_type = relationship(DBCheeseType)