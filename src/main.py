# src/main.py
import os
import asyncio   #agregado
import schedule  #agregado
import time
from views.http_server import HTTPServer, MyHTTPRequestHandler
from views.websocket_server import WebSocketServer, WebSocketHandler, HTTPRequestHandler, MessageHandler
from utils.server_utility import ServerUtility
from services.http_service import HTTPService
from services.ssl_service import SSLService
from src.logs.config_logger import LoggerConfigurator

async def run_server():
    local_ip = ServerUtility.get_local_ip()
    ssl_service = SSLService()
    logger = LoggerConfigurator().configure()
    http_service = HTTPService(logger)
    http_request_handler = HTTPRequestHandler(http_service)
    message_handler = MessageHandler(http_request_handler)
    websocket_handler = WebSocketHandler(message_handler)

    http_server = HTTPServer((local_ip, 4443), MyHTTPRequestHandler, ssl_service)
    http_server.start()

    websocket_server = WebSocketServer(ssl_service, websocket_handler)
    await websocket_server.start()  # Await the coroutine

async def run_store_data():
    while True:
        print("")
        print('Storing data...')
        print("")
        #os.system('python src/store_data.py')
        #await asyncio.sleep(300)  # Espera de 300 segundos     
    
###################################################################
#async def run_main():
#    await asyncio.gather(
#        run_server(),
#        run_store_data()
#    )
####################################################################

def schedule_task():
    # Definir los minutos específicos en los que deseas ejecutar la tarea
    #minutes = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55]
    minutes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]
    
    for minute in minutes:
        schedule.every().hour.at(f":{minute:02d}").do(lambda: asyncio.run(run_store_data()))

    while True:
        schedule.run_pending()
        time.sleep(1)

async def run_main():
    # Aquí puedes agregar otras tareas que necesites ejecutar
    loop = asyncio.get_event_loop()
    loop.run_in_executor(None, schedule_task)

if __name__ == '__main__':
    asyncio.run(run_main())