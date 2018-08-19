import subprocess

#subprocess.check_output("pip install -r requirements.txt --ignore-installed", shell=True).decode()
subprocess.check_output("set FLASK_APP=main.py && flask run --host \"localhost\" --port 8080", shell=True).decode()
