import logging

logger = logging.getLogger('TEST-LOG')  # create an instance
                                        # 'logger' by logging.getlogger method
logger.setLevel(logging.DEBUG) #set  level to DEBUG

#below create a console handler
ch = logging.StreamHandler()#create a StreamHandler instance
ch.setLevel(logging.DEBUG)#set  level to DEBUG

#below create a file handler
fh = logging.FileHandler('access.log') #create a FileHandler instance
fh.setLevel(logging.WARNING) #set  level to WARNING
formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')


#below add formatter to ch and fh
ch.setFormatter(formatter)
fh.setFormatter(formatter)


#below add ch and fh to logger
logger.addHandler(ch)
logger.addHandler(fh)

#below are outputs
logger.debug('debug msg')
logger.info('info msg')
logger.warn('warn msg')
logger.error('error msg')
logger.critical('critical msg')