from abc import ABC ,abstractmethod , abstractproperty
from Range import Range


class BaseOperator(ABC):
  operator = 'Oprator'


  def __init__(self):
      self.main()


  def main(self,*args):
    """this is the main function to check some things like int numbers and 
    if you want to run the it run it """
    self.check_int_args(args)
    self.function(*args)


  @abstractmethod
  def function(self,*args):
    """this Function do what the oprator do and it take args"""
    pass 
  

  @staticmethod
  def check_int_args(*args):

    for i in args:
      Range.CheckInt(i)

  
  def operator_text(self):
    """this is the oprator text look like [+,*,/....]"""
    return self.operator




class Subtract(BaseOperator):
    
    operator = '-'
    
    def function(self,x ,y ):

      return x -  y 

class Add(BaseOperator):
    
    operator = '+'
    
    def function(self,x ,y ):
      return x +  y 

class Multible(BaseOperator):
    
    operator = '*'
    
    def function(self,x ,y ):
      return x *  y 

class Divide(BaseOperator):
    
    operator = '/'
    
    def function(self,x ,y ):
      return x /  y 
