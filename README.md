# demo-vm-app

    python -m pip install -r requirements.txt

or

    python -m pip install fastapi uvicorn httpx Pillow transformers torch torchvision torchaudio

run

    uvicorn main:app --workers 4 --host 0.0.0.0 --port 8000
