'''
Exercise 4
Modify the class you wrote for previous exercise by adding a method to read a file that contains the
measurements of the sensor. If the file is written as follows:
    sensor1Measurements.txt
    21,25,30,22
you will be able to obtain the separated list of measurements by splitting the content in this way:
    fileContent= open(‘sensor1Measurements.txt’).read()
    sensor1MeasurementList=fileContent.split(‘,’)
However, in this way sensor1MeasurementList will be a list of string. How can we convert it into a list of numbers
(int or float) ?
After you find a way to do that, add a method to the class to find the average, the maximum and the minimum of
the measurements
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
