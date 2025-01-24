from loguru import logger
from time import sleep

logger.add('logging.log', format="{time} - {message}", level= "INFO", rotation= "1 day")

def primeira_atividade():
    logger.info("1")
    sleep(2)

def segunda_atividade():
    logger.info("Atividade 2")
    sleep(2)

def terceira_atividade():
    logger.info("Atividade 3")
    sleep(2)


def pipeline():
    primeira_atividade()
    segunda_atividade()
    terceira_atividade()
    logger.info("Pipeline Finalizou")
pipeline()