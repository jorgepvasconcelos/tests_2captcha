from dotenv import load_dotenv
from decouple import config

load_dotenv('env.env')


API_KEY = config("API_KEY")
