# run.py
import sys
import os
import asyncio

# Asegúrate de que el directorio `src` esté en el `PYTHONPATH`
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from src.main import run_server
#from src.models.update_repo import RepoUpdater

if __name__ == '__main__':
    repo_path = 'C:\AppServ\www\IOTIMAGEPROC'
    #updater = RepoUpdater(repo_path)
    #updater.run()
    web_dir = '.'
    os.chdir(web_dir)
    asyncio.run(run_server())  # Use asyncio.run to execute the async function
