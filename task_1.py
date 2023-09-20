from random import randint

class SchoolJournal:
    def __init__(self, subject, name_surname):
        self.grade_list = []
        self.subject = subject
        self.student = name_surname
    

    def grade(self, n=''):
        self.grade_list.append(n)
    
    
    def printer(self):
        print("Предмет:", self.subject)
        print("Студент:", self.student)
        print("Оценки:", ', '.join(map(str, self.grade_list)))
    

    def final_grade(self):
        print("Средний балл:", sum(self.grade_list) / len(self.grade_list))


schooljournal = SchoolJournal('Rus', 'Maxim Goydin')

for _ in range(20):
    schooljournal.grade(randint(2, 5))

schooljournal.printer()
schooljournal.final_grade()
