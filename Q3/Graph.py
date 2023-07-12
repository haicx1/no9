import math
from Stack import *
class Graph:
    def __init__(self,data):
        self.a = data
    def display(self):
        for i in range(len(self.a)):
            for j in range(len(self.a[i])):
                print(self.a[i][j], end =" ")
            print("")
        print("")
    def deg(self, x):
        count =0
        for i in range(len(self.a)):
            count += self.a[x][i]
        return count    
    def breadth_first(self,x):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 1 ========






        #-------------------------
        pass                     
    def f1(self,start):
        self.breadth_first(start)
        # print("")
        
        pass
    
    
    #---------------------------------    
    
    #------------------------------
    def f2(self,start, end):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 1 ========





        #-------------------------------------
        pass
      