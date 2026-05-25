### ALOK SHRESTHA


import math
class CalculatorLogic:
    def __init__(self):
        self.first_num=None
        self.second_num=None
        self.math=None
        # self.fact = 1.0
    
    def get_first_val_and_operator(self,first_num,operator):# suru ko value liney ani operator store garney just that much
        self.first_value = float(first_num)
        self.operation = operator

    def get_second_val_and_calculate(self,second_num):
        self.second_value = float(second_num)
        if(self.operation=="add"):
            return self.first_value+self.second_value
        if(self.operation=="subtract"):
            return self.first_value-self.second_value
        if(self.operation=="multiplication"):
            return self.first_value*self.second_value
        if(self.operation=="division"):
            return self.first_value/self.second_value
        if(self.operation=="power"):
            return self.first_value**self.second_value
        
        
    def get_val_and_square(self,first_num):
        self.first_value = float(first_num)*float(first_num)
        return self.first_value
    
    def get_val_and_square_root(self,first_num):
        self.calculated_value = float(first_num)**(1/2)  # 5^(1/2)= rootunder(5)
        return self.calculated_value

    def get_val_and_find_sin(self,first_num):
        self.value = math.sin(first_num)
        return self.value
    def get_val_and_find_cos(self,first_num):
        self.value = math.cos(first_num)
        return self.value
    def get_val_and_find_tan(self,first_num):
        self.value = math.tan(first_num)
        return self.value
    def get_val_and_find_e(self,first_num):
        self.value = math.exp(first_num)
        return self.value
    def get_val_and_find_log(self,first_num):
        self.value = math.log10(first_num)
        return self.value
    def get_val_and_find_ln(self,first_num):
        self.value = math.log(first_num)
        return self.value
    def get_val_and_find_fact(self,first_num):# factorial integer rw non negative number ko lagi matra ho so be ready for error
        self.fact=1
        for i in range(1,int(first_num)+1):
            self.fact = self.fact*i
        return self.fact 

    # def button_click(self,number):
    #     self.current = self.e.get()
    #     self.e.delete(0,END)
    #     self.e.insert(0,str(self.current)+str(number))
    
    # def button_del(self):

    #     self.e.delete(len(self.e.get())-1,END)   # This line is copied from Chatgpt Couldnot understand how to skip the index and get the second last value Note;;;;; have to search for another method
    
    # def button_clear(self):
    #     self.e.delete(0,END)
    
    # def button_Paranthesis(self):
    #     return
    
    # def button_divide(self):
    #     self.first_num
    #     self.math
    #     self.math="division"
    #     self.first_num=float(self.e.get())
    #     self.e.delete(0,END)
    
    # def button_multiply(self):
    #     self.first_num
    #     self.math
    #     self.math="multiplication"
    #     self.first_num=float(self.e.get())
    #     self.e.delete(0,END)
    
    # def button_subtract(self):
    #     self.first_num
    #     self.math
    #     self.math="subtraction"
    #     self.first_num=float(self.e.get())
    #     self.e.delete(0,END)

    # def button_sqrt(self):
    #     self.first_num
    #     self.math
    #     self.math="sqrt"
    #     self.first_num=float(self.e.get())
    #     self.e.delete(0,END)

    # def button_add(self):
    #     self.first_num
    #     self.math
    #     self.math="addition"
    #     self.first_num=float(self.e.get())
    #     self.e.delete(0,END)

    # def button_square(self):
    #     self.current = self.e.get()
    #     self.e.delete(0,END)
    #     self.e.insert(0,float(self.current)*float(self.current))
    
    # def button_equals(self):
    #     self.second_num
    #     self.second_num=float(self.e.get())
    #     self.e.delete(0,END)

    #     if(self.math == "addition"):
    #         self.e.insert(0,self.first_num + self.second_num)
    #     if(self.math == "subtraction"):
    #         self.e.insert(0,self.first_num - self.second_num)
    #     if(self.math == "multiplication"):
    #         self.e.insert(0,self.first_num * self.second_num)
    #     if(self.math == "division"):
    #         self.e.insert(0,self.first_num / self.second_num)
    
    # def button_power(self):
    #     return
    
    # def button_dot(self):
    #     return
    
    # def button_pie(self):
    #     return
    
    # def button_exp(self):
    #     return
    
    # def button_ans(self):
    #     return   
     
    # def button_log(self):
    #     return
    
    # def button_ln(self):
    #     return
    
    # def button_sin(self):
    #     return
    
    # def button_cos(self):
    #     return
    
    # def button_tan(self):
    #     return
    
    # def button_python(self):
    #     return
    
    # def button_asm(self):
    #     return
    
    # def button_auto(self):
    #     return
    
    # def button_history(self):
    #     return
    
    # def button_factorial(self):
    #     return
