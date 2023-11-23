python3.10 -m venv ./venv
. ./venv/bin/activate
pip install -r requirements.txt
export APP_SETTINGS="config.Config"
/bin/python3 manage.py