class clockTime: 
    def __init__(self):
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
    
    def setHours(self,hours):
        self.hours = hours

    def setMinutes(self,minutes):
        self.minutes = minutes

    def setSeconds(self,seconds):
        self.seconds = seconds

    def setTime(self,hours,minutes,seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        
    def showTime(self):
        return ('{}:{}:{}'.format(self.hours, self.minutes, self.seconds)) 
        
result = 0
hours = int(input('Enter hours’ value: '))
minutes = int(input('Enter minutes’ value: '))
seconds = int(input('Enter seconds’ value: '))

object_clockTime=clockTime()
object_clockTime.setTime(hours,minutes,seconds)
print(object_clockTime.showTime())