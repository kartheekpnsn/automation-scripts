import logging
logging.basicConfig(filename='example.log', format='[%(asctime)s]:(# %(lineno)d) - %(levelname)s: %(message)s', level=logging.DEBUG)
logging.debug('This message should appear on the console')
logging.info('So should this')
logging.warning('And this, too')
logging.error('This is error')
