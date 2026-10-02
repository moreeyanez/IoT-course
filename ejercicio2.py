'''
Exercise 2
Modify the class you wrote for the previous exercise by adding a method that writes the Sensor
information on a .txt file
'''

#This is the class
class TemperatureSensor:
    def __init__(self,sensorName,sensorID,yearFabrication):
        self.sensorName=sensorName
        self.sensorID=sensorID
        self.yearFabrication=yearFabrication
    
    def show_sensorInfo(self):
        print(f"Sensor ID: {self.sensorID}, Sensor Name: {self.sensorName}, Year of Fabrication: {self.yearFabrication}, The age of the sensor is: {self.age()} years")

    def age(self):
        currentYear = 2026
        sensorAge = currentYear - self.yearFabrication
        return sensorAge

    def save_sensorInfo(self):
        f = open('sensorInfo.txt','w')
        f.write(f'Sensor ID: {self.sensorID}\nSensor Name: {self.sensorName}\nYear of Fabrication: {self.yearFabrication}\nAge of the sensor: {self.age()} years')
        f.close()


#This is the main of our program
if __name__=='__main__':
    sensorName= input("Enter the sensor name: ")
    sensorID= input("Enter the sensor ID: ")
    yearFabrication= int(input("Enter the year of fabrication: "))
    sensor1= TemperatureSensor(sensorName,sensorID,yearFabrication)
    sensor1.show_sensorInfo()
    sensor1.age()
    sensor1.save_sensorInfo()
