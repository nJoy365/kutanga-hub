from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from common.database import Base


class GameServer(Base):
    __tablename__ = "game_servers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    game_type = Column(String, nullable=False, index=True)
    status = Column(String, default="stopped")
    created_at = Column(DateTime, default=datetime.now())
    last_updated = Column(DateTime, default=datetime.now(), onupdate=datetime.now())

    resource_logs = relationship("ResourceLog", back_populates="game_server")


class ResourceLog(Base):
    __tablename__ = "resource_logs"

    id = Column(Integer, primary_key=True, index=True)
    server_id = Column(Integer, ForeignKey("game_servers.id"), nullable=False)
    cpu_usage_percentage = Column(Integer, nullable=False)
    cpu_usage = Column(Float, nullable=False)
    memory_usage_percentage = Column(Integer, nullable=False)
    memory_usage = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.now())

    game_server = relationship("GameServer", back_populates="resource_logs")
