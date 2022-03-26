from operatores import Subtract , Add, Multible, Divide, BaseOperator
from Range import  Range
from random import randint


class Question:
  """this class will genrate random maths questions """
  
  ALLOWED_OPERATORES = ['+' , '-' , '*' , '/']
  DIVIDE_ROUND = 2
  
  def __init__(self,question_text,right_answer,marks=1):
    self.question_text = question_text
    self.right_answer  = right_answer  
    self.marks = marks 
    Range.CheckInt(marks)
  
  @classmethod
  def CheckOperator(cls,oper:str):  
  
    if not oper in cls.ALLOWED_OPERATORES:
      raise ValueError(f"Please Enter an Operator in the allowed List {cls.ALLOWED_OPERATORES}")
  
  
  def WhichOperator(oper:BaseOperator):
    """this function will take an operator then will return a function that work for each operator for X Y  
    return None if not found 
    ####### todo I think we can make a more dinamic way to check which operator and make it daynamic to add any one 
    """
    return oper
  
  
  
  @classmethod
  def CreateQuestion(cls,X:int,Y:int,operator:str):
    """give it the X and Y and it will generate the question and
    store the right answer it return Question Object
    X oper Y = right_answer
    """
    Range.CheckInt(X,Y)
    cls.CheckOperator(operator)
    func  = cls.WhichOperator(operator)
    
    right_answer = round(func(X,Y),cls.DIVIDE_ROUND)
    question_text = cls.CreateQuestionText(X,Y,operator)
    
    return cls(question_text,right_answer)
  
  
  @staticmethod
  def CreateQuestionText(x,y,oper):
    return f'{x} {oper} {y}' 
  
  
  @classmethod
  def GenerateRandomQuestoin(cls,X:Range,Y:Range):
    """this function will take the 
    range for making the questions then will return an object for it
    as X [+ / - * ] Y = answer
    """
    
    x = randint(X.start,X.end)
    y = randint(Y.start,Y.end)
    oper = cls.ALLOWED_OPERATORES[randint(0,len(cls.ALLOWED_OPERATORES)-1 )  ]
    return cls.CreateQuestion(x,y,oper)
  
  
  def Answer(self,answer):
    if self.right_answer == answer :
      return self.marks
    return 0
    
    

  
  def json(self,indent:int = 4 ):
    """this function will convert the question to json object"""
    import json
    Range.CheckInt(indent)
    return json.dumps(self.__dict__,indent=indent)

  def __str__(self) -> str:
      return f'{self.question_text}' 


if __name__ == "__main__":
  q = Question.GenerateRandomQuestoin(Range(1,10),Range(2,5))
  print(q.json())