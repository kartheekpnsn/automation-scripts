class Logger:

    def __init__(self, log_flag = True):
        self.log_flag = log_flag
        if self.log_flag:
            self.log_file = 'file_process_'
            self.init_logger()

    def init_logger(self):
        """
        Initiates the logging object
        :return: None
        """
        try:
            os.makedirs('logs')
        except:
            pass
        timestamp = datetime.datetime.now().strftime("%d-%m-%Y %H-%M-%S")
        logging.basicConfig(filename = 'logs/' + self.log_file + timestamp + '.log',
                            format = '[%(asctime)s]:(# %(lineno)d) - %(levelname)s: %(message)s',
                            level = logging.DEBUG)
        self.write_logger('Initiated the logger')

    def write_logger(self, message = "", error = False):
        """
        To write the logs and print them on console simultaneously
        :param message: string, message that needs to be printed in the logs
        :param error: bool, tells us whether the message is an error message
        :return: None
        """
        if error:
            if self.log_flag:
                logging.error(message)
            print('>> ERROR: ' + message + ' <<')
        else:
            if self.log_flag:
                logging.info(message)
            print('>> ' + message + ' <<')
