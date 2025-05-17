### alt_ch_e7 ###

## Local testing ##

# Environment setting
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload

# Available at:
http://127.0.0.1:8000/status
http://127.0.0.1:8000/repair-bay
curl -i http://127.0.0.1:8000/teapot
