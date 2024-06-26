import logging
LOG_FORMAT = "%(levelname)s %(asctime)s %(message)s"
logging.basicConfig(filename="C:\\Users\\ggashaw\\Documents\\excercises python\\ul.log",
                    level=logging.DEBUG,filemode='w', format=LOG_FORMAT)
logger = logging.getLogger()
logger.debug("Message from debug ")
logger.info("Servers are running info")
logger.warning("Message from warning")
logger.error("Servers are running error")
logger.critical("Message from critical")