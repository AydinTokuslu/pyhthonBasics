# question

class Question:
    def __init__(self,text,choices,answer) -> None:
        self.text=text
        self.choices=choices
        self.answer=answer
    def checkAnswer(self,answer):
        return self.answer==answer


q1=Question('en iyi programlama dili hangisidir?', ['C#', 'PYTHON','JAVASCRİPT','JAVA'], 'PYTHON')
q2=Question('en popüler programlama dili hangisidir?', ['PYTHON','JAVASCRİPT','C#', 'JAVA'], 'PYTHON')
q3=Question('en çok kazandıran programlama dili hangisidir?', ['C#', 'JAVASCRİPT','JAVA','PYTHON'], 'PYTHON')

liste=[q1,q2,q3]

# print(q1.checkAnswer('PYTHON'))
# print(q2.checkAnswer('C#'))

# quiz
class Quiz:
    def __init__(self,questions) -> None:
        self.questions=questions
        self.score=0
        self.questionIndex=0

    def getQuestion(self):
        return quiz.questions[self.questionIndex]

    def displayQuestion(self):
        question=self.getQuestion()
        print(f'soru {self.questionIndex+1}: {question.text}')

        for q in question.choices:
            print('-'+q)

        answer=input('cevap : ')
        self.guess(answer)
        self.loadQuestion()
        #print(question.checkAnswer(answer))

    def guess(self,answer):
        question=self.getQuestion()

        if question.checkAnswer(answer):
            self.score+=1
        self.questionIndex+=1

       # self.displayQuestion()

    def loadQuestion(self):
        if len(self.questions)== self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()

    def showScore(self):
        print('score: ', self.score)

    def displayProgress(self):
        totalQuestion=len(self.questions)
        questionNumber=self.questionIndex+1

        if questionNumber> totalQuestion:
            print('quiz bitti')
        else:
            print(f'Question {questionNumber} of {totalQuestion}'.center(100,'*'))


q1=Question('en iyi programlama dili hangisidir?', ['C#', 'PYTHON','JAVASCRİPT','JAVA'], 'PYTHON')
q2=Question('en popüler programlama dili hangisidir?', ['PYTHON','JAVASCRİPT','C#', 'JAVA'], 'PYTHON')
q3=Question('en çok kazandıran programlama dili hangisidir?', ['C#', 'JAVASCRİPT','JAVA','PYTHON'], 'PYTHON')
q4=Question('en çok sevilen programlama dili hangisidir?', ['C#', 'JAVASCRİPT','JAVA','PYTHON'], 'PYTHON')
q5=Question('en kolay programlama dili hangisidir?', ['C#', 'JAVASCRİPT','JAVA','PYTHON'], 'PYTHON')


questions=[q1,q2,q3,q4,q5]

quiz=Quiz(questions)
#question=quiz.getQuestion()
#print(question.text)

quiz.loadQuestion()
