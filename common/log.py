# import logging
import logging.handlers

FORMAT = '%(asctime)15s %(name)s-%(levelname)s  %(funcName)s:%(lineno)s %(message)s'
# logging.basicConfig(level=logging.DEBUG, format=FORMAT)
logger = logging.getLogger('tencent_speech.log')

rf_handler = logging.handlers.RotatingFileHandler(
    'tencent_speech.log', maxBytes=10 * 1024 * 1024,
    backupCount=5, encoding='utf-8')
rf_handler.setLevel(logging.DEBUG)
rf_handler.setFormatter(logging.Formatter(FORMAT))
logger.addHandler(rf_handler)
logger.setLevel('INFO')
