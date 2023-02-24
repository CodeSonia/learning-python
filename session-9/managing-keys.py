import os
from dotenv import load_dotenv

load_dotenv()

print(os.getenv('ONE'))
print(os.getenv('TWO'))
