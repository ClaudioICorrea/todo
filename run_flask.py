import subprocess
import os

def run_flask():
    print('start APP in Flask..')
    os.environ['FLASK_APP'] = 'todo'

    print('start database')
    os.environ['FLASK_DATABASE_HOST'] = 'localhost'
    os.environ['FLASK_DATABASE_PASSWORD'] = 'comoqueso123'
    os.environ['FLASK_DATABASE_USER'] = 'lukeroot'
    os.environ['FLASK_DATABASE'] = 'prueba'

    subprocess.call(["flask","init-db"])

    
    print('start APP as development..')
    os.environ['FLASK_VPN'] = 'development'
    print('flask run..')
    subprocess.call(["flask","run"])
    
    #subprocess.call(["set"])
    print('Done')
run_flask()