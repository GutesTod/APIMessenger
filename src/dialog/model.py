from src.config.settings import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey
from src.user.model import Users

class Dialog(Base):
    __tablename__ = "dialog"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id1: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    user_id2: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    users: Mapped["Users"] = relationship(Users,backref="users",lazy="joined")