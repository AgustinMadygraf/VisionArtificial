"""
run.py
Script de ejecución del servidor de mensajería.
"""
import asyncio
import os
from src.main import run_server

if __name__ == '__main__':
    os.system("cls" if os.name == "nt" else "clear")
    asyncio.run(run_server())
