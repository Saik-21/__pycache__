class practice:
    def __init__(self,n):
        self.n = n
    
    def char_traverse(self):
        for i in self.n:
            print(i)
    def index(self,t):
        return f"The character of the String is {self.n[t]} having index {t}"
    def make_it_list(self):
        return list(self.n)
    def make_it_dictionary(self):
        d = {}
        for i,v in enumerate(self.n):
            d[i] = v
        return d
            
p1 = practice('Python')
print(p1.make_it_dictionary())


