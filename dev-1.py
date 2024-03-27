class practice:
    def __init__(self,n):
        self.n = n
    
    def char_traverse(self):
        for i in self.n:
            print(i)
    def index(self,t):
        return f"The character of the String is {self.n[t]} having index {t}"

p1 = practice('Hello')
p1.char_traverse()
print(p1.index(2))