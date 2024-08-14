"""
run.py
Script de inicio Vision
"""
import os
import asyncio
from main import run_server

if __name__ == '__main__':
    os.system('cls')
    WEB_DIR = '.'
    os.chdir(WEB_DIR)
    asyncio.run(run_server())
