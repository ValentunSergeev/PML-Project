from sqlalchemy.orm import Session, subqueryload

from .. import models
from .db import schemas


def get_frames(db: Session, device_id: str):
    return db.query(schemas.FrameDb)\
        .filter(schemas.FrameDb.deviceId == device_id)\
        .options(subqueryload("detections"))\
        .all()


def insert_frame(db: Session, frame: models.Frame, file_name: str):
    db_detections = [schemas.DetectionDb(**detection.dict()) for detection in frame.detections]

    frame_dict = frame.dict()
    frame_dict["detections"] = db_detections

    db_frame = schemas.FrameDb(**frame_dict, fileName=file_name)

    db.add(db_frame)

    db.commit()
