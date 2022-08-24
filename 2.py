class Time():
    def __init__(self,time1,time2):
        self.ti1= time1
        self.ti2= time2

    def bigger(self):
        if self.ti1>self.ti2:
            print(f"{self.ti1} Bigger than {self.ti2}")
        else:
            print(f"{self.ti2} Bigger than {self.ti1}")

x=float(input("Please enter first time: "))
y=float(input("Please enter second time: "))
t1=Time(x,y)



t1.bigger()