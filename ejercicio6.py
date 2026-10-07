'''
Exercise 6
Modify the code of exercise 4 and 5 to be able to work with a json file similar 
to the one below.
'''

import json

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

    def isCalibrated(self):
        calibrationStatus = input("Is the sensor calibrated? (True/False): ")
        if calibrationStatus.lower() == 'true':
            print("The sensor is calibrated.")
            return True
        elif calibrationStatus.lower() == 'false':
            print("The sensor is not calibrated.")
            return False
        else:
            print("Invalid input. Please enter True or False.")

    def read_measurements(self, filename):
        fileContent = open(filename).read()
        sensorMeasurementList = fileContent.split(',')
        sensorMeasurementList = [float(i) for i in sensorMeasurementList]
        return sensorMeasurementList

    def find_average(self, sensorMeasurementList):
        average = sum(sensorMeasurementList) / len(sensorMeasurementList)
        return average

    def find_maximum(self, sensorMeasurementList):
        maximum = max(sensorMeasurementList)
        return maximum

    def find_minimum(self, sensorMeasurementList):
        minimum = min(sensorMeasurementList)
        return minimum

    def asDictionary(self):
        sensorDict = {
            "Sensor Name": self.sensorName,
            "Sensor ID": self.sensorID,
            "Year of Fabrication": self.yearFabrication,
            "Measurements": self.read_measurements("sensor1Measurements.txt"),
        }
        return sensorDict

    def printDictionary(self):
        sensorDict = self.asDictionary()
        for key, value in sensorDict.items():
            print(f"{key}: {value}")

    def save_as_json(self):
        '''
        sensorDict = self.asDictionary()
        with open('sensorInfo.json', 'w') as json_file:
            json.dump(sensorDict, json_file, indent=4)
        print("Sensor information saved as JSON.")
        '''
        sensorDict = self.asDictionary()
        json.dump(sensorDict,open("infoSensor.json","w"))
        print("Sensor information saved as JSON.")

#This is the main of our program
if __name__=='__main__':
    sensorName= input("Enter the sensor name: ")
    sensorID= input("Enter the sensor ID: ")
    yearFabrication= int(input("Enter the year of fabrication: "))
    sensor1= TemperatureSensor(sensorName,sensorID,yearFabrication)
    sensor1.show_sensorInfo()
    sensor1.age()
    sensor1.save_sensorInfo()
    sensor1.isCalibrated()
    sensor1Measurements = sensor1.read_measurements("sensor1Measurements.txt")
    print(f"The average of the measurements is: {sensor1.find_average(sensor1Measurements)}")
    print(f"The maximum of the measurements is: {sensor1.find_maximum(sensor1Measurements)}")
    print(f"The minimum of the measurements is: {sensor1.find_minimum(sensor1Measurements)}")
    sensor1.asDictionary()
    sensor1.printDictionary()
    sensor1.save_as_json()