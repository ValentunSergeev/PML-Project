from pydantic import BaseModel
from typing import Optional, List
import json


class Detection(BaseModel):
    startX: float
    startY: float
    endX: float
    endY: float

    category: str
    confidence: float


class Frame(BaseModel):
    deviceId: str
    detections: List[Detection]

    @classmethod
    def __get_validators__(cls):
        yield cls.validate_to_json

    @classmethod
    def validate_to_json(cls, value):
        if isinstance(value, str):
            return cls(**json.loads(value))
        return value


