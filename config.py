import os

from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv('BSTACK_USERNAME')
PASSWORD = os.getenv('BSTACK_ACCESSKEY')
context = os.getenv('context', 'bstack')
