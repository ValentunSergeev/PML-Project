from typing import Optional
from fastapi import FastAPI, Form, File, UploadFile, Body
from pydantic import parse_obj_as

import uvicorn

from warehouse.models import Frame
from warehouse.file_storage import save_image

app = FastAPI()


@app.post("/detections/")
async def read_item(
        image: UploadFile = File(...),
        frame: Frame = Form(...),
):
    filename = await save_image(frame.deviceId, image)
    return {"file_path": filename}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
