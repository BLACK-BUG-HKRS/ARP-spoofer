import win32serviceutil
import time

class Wservice:
    
    def __init__(self, service, machine=None, verbose=False):
        self.service = service
        self.machine = machine
        self.verbose = verbose

    @property
    def running(self):
        return win32serviceutil.QueryServiceStatus(self.service)[1] == 4
    
    def 