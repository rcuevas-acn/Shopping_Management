import subprocess


def run_app():
    # install = "pip install -r requirements.txt --ignore-installed"
    # print("Command to install requirements...." + install)
    # try:
    #     print("Command start service {}".format(subprocess.check_output(install, shell=True)))
    # except Exception as e:
    #     print("Error: {}".format(e.output))
    run = "set FLASK_APP=main.py && set FLASK_ENV=\"development\" && flask run --host \"localhost\" --port 8080"
    print("Command to run app...." + run)
    try:
        print("Command start service {}".format(subprocess.check_output(run, shell=True)))
    except Exception as e:
        print("Error: {}".format(e.output))


run_app()
