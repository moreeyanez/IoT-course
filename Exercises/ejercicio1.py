'''
Exercise 1
Develop a Sensor class similar to the one in the previous example. The class should be able to receive as
input the sensor name, the sensor ID and the year of fabrication of the sensor. In addition, it must have
a method to return the current “age” of the sensor. The input should be provided by the user (NOT
hardcoded in the script).
'''

#This is the class
class TemperatureSensor:
    def __init__(self,sensorName,sensorID,yearFabrication):
        self.sensorName=sensorName
        self.sensorID=sensorID
        self.yearFabrication=yearFabrication
    
    def show_sensorInfo(self):
        print(f"Sensor ID: {self.sensorID}, Sensor Name: {self.sensorName}, Year of Fabrication: {self.yearFabrication}")

    def age(self):
        currentYear = 2026
        sensorAge = currentYear - self.yearFabrication
        print(f"The age of the sensor is: {sensorAge} years")

#This is the main of our program
if __name__=='__main__':
    sensorName= input("Enter the sensor name: ")
    sensorID= input("Enter the sensor ID: ")
    yearFabrication= int(input("Enter the year of fabrication: "))
    sensor1= TemperatureSensor(sensorName,sensorID,yearFabrication)
    sensor1.show_sensorInfo()
    sensor1.age()
