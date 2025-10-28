from fastapi_users.db import SQLAlchemyBaseUserTableUUID

from core.base_model import Base, DateTimeMixin


class User(SQLAlchemyBaseUserTableUUID,Base,DateTimeMixin):
    pass