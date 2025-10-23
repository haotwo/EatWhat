from sqlalchemy import Integer,String,Text
from sqlalchemy.orm import Mapped,mapped_column

from src.core.base_model import Base,DateTimeMixin

class Dish(Base,DateTimeMixin):
    __tablename__ = "dishes"
    id: Mapped[int] = mapped_column(Integer,primary_key=True,comment="用户id")
    name: Mapped[str] = mapped_column(String,unique=True,nullable=False,comment="用户名")
    description: Mapped[str | None] = mapped_column(Text)
    