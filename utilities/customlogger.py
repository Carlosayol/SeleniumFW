import inspect
import logging

def customLogger(logLevel=logging.DEBUG):
    #Inspect.stack obtiene el nombre de la clase / metodo de donde este metodo es ejecutado
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    #Logeemos todos los mensajes
    logger.setLevel(logging.DEBUG)

    fileHandler = logging.FileHandler("automationFramework.log", mode="a")
    fileHandler.setLevel(logLevel)

    formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s at Line %(lineno)d',
                    datefmt='%m/%d/%Y %H:%M:%S')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger

