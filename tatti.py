class Point2:
    def __init_(self,x,y):
        self.x = x
        self.y =y 
        

nested_lst = [1,2,[4,5,[8,[0,Point2(12,13)]]]]

z = nested_lst[2][2][1][1]
print(z)
