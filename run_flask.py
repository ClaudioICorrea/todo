import subprocess
import os

def run_flask():
    print('start database')
    os.environ['FLASK_DATABASE_HOST'] = 'localhost'
    os.environ['FLASK_DATABASE_PASSWORD'] = 'comoqueso123'
    os.environ['FLASK_DATABASE_USER'] = 'lukeroot'
    os.environ['FLASK_DATABASE'] = 'prueba'

    subprocess.call(["flask","init-db"])

    print('start APP in Flask..')
    os.environ['FLASK_APP'] = 'todo'
    print('start APP as development..')
    os.environ['FLASK_VPN'] = 'development'
    print('flask run..')
    subprocess.call(["flask","run"])
    
    #subprocess.call(["set"])
    print('Done')
    #subprocess.run("export FLASK_VPN=development")
    return 

run_flask()