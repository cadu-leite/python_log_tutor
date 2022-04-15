from logging.handlers import TimedRotatingFileHandler
import logging
import sys

logger = logging.getLogger(__name__)
logger.setLevel(10)

def print_log():

    print(f'\n\tSobre os `loggers` em `{__name__}` ... \n')
    print(f'\t|{"Logger Name"  :<14}|{"Parent Name"    :<30}|{"Eff. Level"            :<10}|{"Level"  :<5}|{"Handlers" :<30}|')
    print(f'\t|{"-"    :-<14}|{"-"             :-<30}|{"-"                    :-<10}|{"-"      :-<5}|{"-"       :-<30}|')
    l = [f'\t|{name    :.<14}|{obj.parent.name  :<30}|{obj.getEffectiveLevel() :<10}|{obj.level:<5}|{obj.handlers}' for name, obj in  logger_root.manager.loggerDict.items()]
    #l = f'\t|{logger_root    :.<14}|{logger_root.parent.name  :<30}|{logger_root.getEffectiveLevel() :<10}|{logger_root.level:<5}|{logger_root.handlers}'
    print('\n'.join(l)+'\n')


def main():

    logger.warning('WOW Main started')

    logger.debug(' [debug] esta me vendo?')       #logging.DEBUG    = 10
    logger.info(' [info] esta me vendo?')         #logging.INFO     = 20
    logger.warning(' [warning] esta me vendo?')   #logging.WARNING  = 30
    logger.critical(' [critical] esta me vendo?') #logging.CRITICAL = 50
    logger.error(' [error] esta me vendo?')       #logging.ERROR    = 40

    logger.warning('OOOPS Main finished')


if __name__ == '__main__':


    handler_stream = logging.StreamHandler(stream=sys.stdout)
    handler_file = TimedRotatingFileHandler(filename='pyton_log.log.txt', when='M', interval=1, backupCount=2)


    formatter_stream_ = logging.Formatter('%(asctime)s %(levelname)09s LOGr:%(name)-10s f:%(funcName)-8s:%(lineno)-2d msg:%(message)s')
    formatter_file = logging.Formatter('%(asctime)s %(levelname)s LOGr:%(name)s f:%(funcName)s:%(lineno)d>%(message)s')

    handler_stream.setFormatter(formatter_stream_)
    handler_file.setFormatter(formatter_file)
    handler_file.setLevel(10)

    logger_root = logging.getLogger()
    logger_root.addHandler(handler_stream)
    logger_root.addHandler(handler_file)
    logger_root.setLevel(30)

    main()
    print_log()

    logger_root.debug(' [debug] esta me vendo?')       #logging.DEBUG    = 10
    logger_root.info(' [info] esta me vendo?')         #logging.INFO     = 20
    logger_root.warning(' [warning] esta me vendo?')   #logging.WARNING  = 30
    logger_root.critical(' [critical] esta me vendo?') #logging.CRITICAL = 50
    logger_root.error(' [error] esta me vendo?')       #logging.ERROR    = 40



