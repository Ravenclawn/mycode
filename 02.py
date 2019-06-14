#!/usr/bin/python3

"""
对象的域（实例变量）代表了对象的状态，修改变量，就修改了实例的状态。当把
一个对象作为参数传给其他函数时，其他函数可能会错误的修改实例变量，需要控
制访问（封装）--数据隐藏

以双下划线"__" 开头的变量是私有变量，类外部不能直接访问

以下划线“_" 开头的变量是保护变量，子类可以访问，但是非子类的类外部不能直接访问

以双下划线开头和结尾的变量是系统变量
"""

class People:

    def __init__(self, n="", g="x"):
        self.__name = n
        self.__gender = g

    def info(self):
        print("%s's gender is %s" %(self.__name, self.__gender))
    
    def getGender(self,a):
        return self.__name
    def setGender(self,a):
        if len(a)<=5:
            self.__gender=a
    def getName(self):
      return self.__name

class Student(People):
  def __init__(self,n='',g='x',stuID=0):
    super(Student,self).__init__(n,g)
    self.__stuID=stuID

s1=Student("ling","female",13)
print(s1.getName())
s1.info()