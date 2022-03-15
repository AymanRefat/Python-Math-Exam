
class Range:
  """this class will make some thing like that (1,5)
  but the [0] < [1]
  """
  
  def __init__(self,start:int,end:int):
    self.CheckInt(start,end)
    self.start = int(start)
    self.end = int(end)
    self.CheckRange()
    
  @staticmethod
  def CheckInt(*nums):
    """this function will check if the given numbers are intgers or no and raise error if not"""
    try: 
      map(int,nums)
    except ValueError:
        print("Please Enter an Intger")
  
  def CheckRange(self):
    """this function will make sure that the start < end it raise error if not  """
    if self.start >= self.end:
      raise ValueError("please Make Sure that the START of the range smaller than the END")
