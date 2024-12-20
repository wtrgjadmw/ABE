
class formulaData:
    def __init__(self, operands, result, type, csel_flag=0) -> None:
        self.operands = operands
        self.result = result
        self.type = type
        self.csel_flag = (1 if csel_flag == "one" else 0) if type == "CSEL" else csel_flag
        self.limit_time = -1
    
    def set_limit_time(self, limit_time):
        self.limit_time = limit_time
        
    def print(self, file = None, end=", "):
        print("['{}', {}, '{}', {}]".format(self.result, self.operands, self.type, self.csel_flag), end=end, file=file)
