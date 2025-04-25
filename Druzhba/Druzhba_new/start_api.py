import uvicorn

from fastapi.responses import FileResponse

from backend.api import app
from config import Config

# проверка ssl сертификата
@app.get("/.well-known/pki-validation/{file_path}")
async def download_file(file_path:str):
  return FileResponse(path=f'certificate/{file_path}', filename=file_path, media_type='multipart/form-data')


if __name__ == '__main__':
    config = Config()
    uvicorn.run(
        "start_api:app",
        host='0.0.0.0',
        port=8000,
        reload=True
    )
