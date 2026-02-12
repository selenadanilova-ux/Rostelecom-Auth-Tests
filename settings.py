import os

from dotenv import load_dotenv

load_dotenv()

valid_email = os.getenv('valid_email')
valid_password = os.getenv('valid_password')
valid_phone = os.getenv('valid_phone')
valid_login = os.getenv('valid_login')

nonvalid_email = os.getenv('nonvalid_email')
nonvalid_phone = os.getenv('nonvalid_phone')
nonvalid_password = os.getenv('nonvalid_password')
nonvalid_login = os.getenv('nonvalid_login')

empty_email = os.getenv('empty_email')
empty_password = os.getenv('empty_password')
empty_phone = os.getenv('empty_phone')
empty_login = os.getenv('empty_login')