#main() contains a test case for the order_id log API
#I just used an array. record() appends the order_id to the array
#get_last() returns the element at the specified location

def main():
    log = Log()
    log.record(1234)
    log.record(5432)
    log.record(6241)
    log.record(2596)
    log.record(5242)
    print(log.get_last(1))
    print(log.get_last(3))

class Log:
    logStorage = []
    
    def __init__(self):
        self.logStorage = []
    
    #adds the order_id to the log
    def record(self, order_id):
        self.logStorage.append(order_id)

    #gets the ith last element from the log
    def get_last(self, i):
        return self.logStorage[len(self.logStorage)-i]
    
main()
