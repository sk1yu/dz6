import logging
from datetime import datetime

logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d'
)

logging.info('Це інформаційне повідомлення.')

print("Повідомлення записано у файл app.log")
