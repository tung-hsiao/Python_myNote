
import logging

class myClass(object):
    def __init__(self, logger):
        self.event_queue = []
        self.logger = logger
        self.running = True

    def run(self):
      t = threading.Thread(target=self.process, args=())
      t.setDaemon(True)
      t.start()
    
    def stop(self):
        self.running = False
    
    def process(self):
        self.logger.info(f"[ process ] Start! ")
        while self.running:
            print("Zz..")
            time.sleep(1)

logger = logging.getLogger(__name__)
my_class = myClass(logger)
my_class.run()
