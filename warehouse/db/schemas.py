from sqlalchemy import Float, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class DetectionDb(Base):
    __tablename__ = "detections"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    startX = Column(Float)
    startY = Column(Float)
    endX = Column(Float)
    endY = Column(Float)

    category = Column(String)
    confidence = Column(Float)

    frame_id = Column(Integer, ForeignKey("frames.id"))

    frame = relationship("FrameDb", back_populates="detections")


class FrameDb(Base):

    __tablename__ = "frames"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    deviceId = Column(String, index=True)

    fileName = Column(String)

    detections = relationship("DetectionDb", back_populates="frame")
