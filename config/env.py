import os
from dotenv import load_dotenv


load_dotenv()

NAME=os.getenv('communication_database_name')
USERNAME=os.getenv('communication_database_username')
HOST=os.getenv('communication_database_host')
PORT=os.getenv('communication_database_port')
PASSWORD=os.getenv('communication_database_password')