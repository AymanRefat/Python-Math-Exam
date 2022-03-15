from Question import Question
from Range import Range


# TODO Change the range of numbers for each exam 

class Exam:
  """this calss will take the 
  level of it to make it defecalt 
  then generate exam with some random numbers 
  [ +  -   *  / ]
  from the question class and display the exam
  """
  QUESTION_CLASS = Question
  CreateMethod = Question.GenerateRandomQuestoin
  
  START_LEVEL , END_LEVEL = 1,3
  ALLOWED_LEVELS = tuple(range(START_LEVEL,END_LEVEL+ 1))
  
  def __init__(self,questions:list[Question] = None,level:int = 1) -> None:
      self.CheckLevel(level)
      
      self.level = int(level)
      if questions:
        self.questions = [] + questions 
      else: 
        self.questions = []
      

  def Requerments(self):
    # TODO make it change for each level 
      """return requerments as tuple  
      changes from each exam
      """
      
      start1 , end1 = 2 ,10 
      start2,end2 = 2 , 10 
      
      
      
      if self.level ==2 :
        end1 = end1**2
      elif self.level == 3: 
        end1 = end1**2
        end2 = end2**2
        
      
      return [Range(start1,end1), Range(start2,end2)]


  @classmethod
  def CheckLevel(cls,level):
    if not int(level) in cls.ALLOWED_LEVELS:
        raise ValueError(f"Please Enter a Level Between {cls.START_LEVEL} - {cls.END_LEVEL}")
        
  def AddQuestionsToExam(self ,questions_numbers:int):
    """take the createmethod from the class vars and use the requerments to get the ranges 
    and then create a list of questions """
    Range.CheckInt(questions_numbers)
    self.questions += [  self.__class__.CreateMethod(*self.Requerments()) for _ in range(questions_numbers)] 
    
  @property 
  def Questions(self):
    return self.questions

    
    
  def GetMarks(self):
    marks = 0 
    for ques in self.Questions:
      marks += ques.marks
    return marks
  
  def StartExam(self):
    marks = 0 
    total_marks = self.GetMarks()
    get_answer = lambda: float(input(f'{ques}: ')) 
    for ques in self.Questions : 
      try:
          answer = get_answer()
      except: 
        print('Please Enter a Number')
        get_answer()
      marks += ques.Answer(answer)

    print(f"you Got {marks} / {total_marks} ")

  def ShowRightAnswers(self):
    for ques in self.Questions:
      print(f'{ques} = {ques.right_answer}')


  def json_file(self,file_name='math_exam',path=None):
    import json
    data = [   ques.__dict__   for ques in self.questions ]
    if not path :
      with open(f'{file_name}.json','w') as f:
        json.dump(data,f,indent=4)

if __name__ == "__main__":
  exam = Exam()
  exam.level = 2
  exam.AddQuestionsToExam(100)
  exam.json_file()