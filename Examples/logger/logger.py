import logging

formatter = logging.Formatter('%(asctime)s.%(msecs)03d %(levelname)s: %(message)s', 
                               datefmt='%Y%m%d %H:%M:%S')

# File handler
handler_1 = logging.FileHandler('logs/myLog.log')
handler_1.setFormatter(formatter)

# Screen handler
handler_2 = logging.StreamHandler()
handler_2.setFormatter(formatter)

# Get logger
logger = logging.getLogger('myLogger')
logger.setLevel(logging.DEBUG)
logger.addHandler(handler_fusion_1)
logger.addHandler(handler_fusion_2)