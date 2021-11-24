from typing import List

import uvicorn
from fastapi import FastAPI, Form, File, UploadFile, Depends
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from warehouse import crud, models
from warehouse.db.database import SessionLocal, engine, Base
from warehouse.file_storage import save_image
from warehouse.models import Frame

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/frames/")
async def insert_frame(
        image: UploadFile = File(...),
        frame: Frame = Form(...),
        db: Session = Depends(get_db)
):
    filename = await save_image(frame.deviceId, image)
    crud.insert_frame(db, frame, filename)
    return {"file_path": filename}


@app.get("/detections/{deviceId}", response_model=List[models.Frame])
async def get_frames(
        deviceId: str,
        db: Session = Depends(get_db)
):
    frames = crud.get_frames(db, deviceId)

    return frames


# TODO better to use nginx to serve static data
@app.get("/images")
async def main(file_name: str):
    # Not secure to allow to read any file, but anyways...
    return FileResponse(file_name)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
