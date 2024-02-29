from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from fastapi.responses import FileResponse
from leetscrape import GenerateCodeStub
import shutil
from pathlib import Path
import os

version = "1.0.0"


app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health():
    # today = date.today()
    now = datetime.now()
    today = now.strftime("%b %d, %Y")
    time = now.strftime("%I:%M:%S %p")
    return {"version": version, "date": today, "time": time}


@app.get("/generate-files/{qName}")
async def prepFiles(qName: str):
    print("endpoint /lc-test-files called")
    print(qName)
    directory = "./generated-code-stubs"
    try:
        shutil.rmtree(directory)

    except:
        print("No directory named code")

    path = Path(directory)
    path.mkdir(parents=True, exist_ok=True)

    try:
        fcs = GenerateCodeStub(titleSlug=qName)
        fcs.generate(directory=directory)

    except:
        print(f"Unable to generate code stubs for {qName}")
        return {
            "status": "error",
            "message": f"Unable to generate code stubs for {qName}",
        }

    arr = os.listdir("./generated-code-stubs")

    if len(arr) != 2:
        return {
            "status": "error",
            "message": f"Incorrect number of files generated",
        }

    return {"status": "success"}


@app.get("/getFileTest")
async def getTestFile():
    file_path = "./test.txt"

    return FileResponse(path=file_path, filename=file_path, media_type="text")


@app.get("/getSolutionFile")
async def getSolutionFile():
    file_path = "./generated-code-stubs"
    arr = os.listdir(file_path)
    fileName = arr[0] if "test" in arr[0] else arr[1]
    print(fileName)
    file_path += f"/{fileName}"

    # return {"Status": "success"}
    return FileResponse(path=file_path, filename=fileName, media_type="text")


@app.get("/getTestFile")
async def getSolutionFile():
    file_path = "./generated-code-stubs"
    arr = os.listdir(file_path)
    fileName = arr[0] if "test" not in arr[0] else arr[1]
    print(fileName)

    file_path += f"/{fileName}"

    # return {"Status": "success"}
    return FileResponse(path=file_path, filename=fileName, media_type="text")
