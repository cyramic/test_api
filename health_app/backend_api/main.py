import logging

from decouple import config
from fastapi import FastAPI, File, HTTPException, Security, UploadFile

from health_app.lib.file import get_temp_fs
from health_app.lib.security import get_api_key
from health_app.lib.tasks import process_file

log = logging.getLogger(__name__)

redis_url = config("REDIS_URL", "redis://localhost:6379")
upload_dir = config("UPLOAD_DIR", "osfs:///tmp/uploads")

app = FastAPI()


@app.post("/upload")
def upload(file: UploadFile = File(...), api_key: str = Security(get_api_key)):
    """
    Upload endpoint of the API to handle file uploads

    Parameters:
    file: File to be uploaded
    api_key: The key to ensure only authorised people can use this endpoint
    """
    if not file.filename.endswith(".json"):
        raise HTTPException(status_code=500, detail="Incorrect file format provided")

    file_fs = get_temp_fs(upload_dir)
    if not file_fs:
        raise HTTPException(status_code=500, detail="Failed to access upload directory")

    log.info(f"Have upload file...{file.filename}")
    try:
        contents = file.file.read()
        # Create a new file with the uploaded filename
        with file_fs.open(file.filename, "wb") as f:
            # Read the uploaded file content in chunks for efficiency
            f.write(contents)
            log.info(f"Processing File...{file.filename}")
    except Exception as err:
        raise HTTPException(status_code=500, detail="Error saving uploaded file")
    finally:
        file.file.close()
        # FastAPI automatically handles closing the uploaded file object

    result = process_file(file.filename)
    if result:
        return {"message": f"File {file.filename} uploaded successfully!"}
    else:
        raise HTTPException(status_code=400, detail="File could not be processed.")
