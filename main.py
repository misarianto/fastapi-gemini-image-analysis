from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import JSONResponse
from typing import Annotated
from PIL import Image
from gemini import send_propmt_flash

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/upload-file")
async def upload_file_to_text(
    upload_file: UploadFile, 
    prompt_text: Annotated[str, Form()]
):
    try:
        fileimage = Image.open(upload_file.file)
        response = send_propmt_flash(fileimage, prompt_text)
        print(response.text)
        return {"message": response.text}
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)