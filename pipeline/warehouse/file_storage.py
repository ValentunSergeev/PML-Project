import aiofiles as aiofiles
from fastapi import UploadFile
import time
from os import path, makedirs

FILES_DIR = "detections"


async def save_image(device_id: str, file: UploadFile) -> str:
    extension = path.splitext(file.filename)[1]
    timestamp = time.time_ns()
    file_name = str(timestamp) + extension

    dir_path = path.join(FILES_DIR, device_id)
    file_path = path.join(dir_path, file_name)

    makedirs(dir_path, exist_ok=True)

    async with aiofiles.open(file_path, 'wb') as out_file:
        content = await file.read()
        await out_file.write(content)

    return file_path

