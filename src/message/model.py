from src.config.settings import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey
from src.user.model import Users
from src.dialog.model import Dialog

class Message(Base):
    __tablename__ = "message"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    sender_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    dialog_id: Mapped[int] = mapped_column(ForeignKey("dialog.id"), nullable=False)
    content: Mapped[str] = mapped_column(nullable=False)
    users: Mapped["Users"] = relationship(Users,backref="users",lazy="joined")
    dialogs: Mapped["Dialog"] = relationship(Dialog, backref="dialog", lazy="joined")