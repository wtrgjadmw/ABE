
class formulaData:
    def __init__(self, operands, result, type) -> None:
        self.operands = operands
        self.result = result
        self.type = type
        self.limit_time = -1
    
    def set_limit_time(self, limit_time):
        self.limit_time = limit_time
        
    def print(self, file = None):
        print("[{}, {}, {}]".format(self.result, self.operands, self.type), end=", ", file=file)