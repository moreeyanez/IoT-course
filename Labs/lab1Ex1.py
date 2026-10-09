import json

class devicesManagement:
    def __init__(self, fileName):
        self.fileName = fileName
        self.data = json.load(open(fileName))

    def searchByName(self):
        '''print all the information about the devices for the given name'''
        name = input("Enter the device name: ")
        flag = False
        for device in self.data["devicesList"]:
            if device["deviceName"] == name:
                print(json.dumps(device, indent=4))
                flag = True
        if flag == False:
            print(f"No device found with the name: {name}")
    

    def searchByID(self):
        '''print all the information about the devices for the given ID'''
        id = int(input("Enter the device ID: "))
        flag = False
        for device in self.data["devicesList"]:
            if device["deviceID"] == id:
                print(json.dumps(device, indent=4))
                flag = True
        if flag == False:
            print(f"No device found with the ID: {id}")    

    def searchByService(self):
        '''print all the information about the devices that provides the given service'''
        service = input("Enter the service name: ")
        flag = False
        for device in self.data["devicesList"]:
            if device["availableServices"] == service:
                print(json.dumps(device, indent=4))
                flag = True
        if flag == False:
            print(f"No device found with the service: {service}")  

    def searchByMeasureType(self):
        '''print all the information about the device that provides such measure type'''
        measureType = input("Enter the measure type: ")
        flag = False
        for device in self.data["devicesList"]:
            if device["measureType"] == measureType:
                print(json.dumps(device, indent=4))
                flag = True
        if flag == False:
            print(f"No device found with the measure type: {measureType}")

    def insertDevice(self):
        '''insert a new device it that is not already present on the list (the
        ID is checked). Otherwise ask the end-user to update the information about the
        existing device with the new parameters. Every time that this operation is
        performed the “last_update” field needs to be updated with the current date and
        time in the format “yyyy-mm-dd hh:mm”. The structure of the parameters of
        the file must follow the one of the ones that are already present in the file.'''

    def printAll(self):
        '''print the full catalog'''
        print(json.dumps(self.data['devicesList'], indent=4))

    def exit(self):
        '''save the catalog (if changed) in the same JSON file provided as input.'''


if __name__=='__main__':
    manager = devicesManagement("catalog.json")
    manager.searchByName()
    manager.searchByID()
    manager.searchByService()
    manager.searchByMeasureType()
    manager.insertDevice()
    manager.printAll()
    manager.exit()



    '''"devicesList":[
        {"deviceID":1,
        "deviceName":"DHT11",
        "measureType":
            ["Temperature","Humidity"],
        "availableServices":
            ["MQTT","REST"],
        "servicesDetails":
            [{"serviceType":"MQTT",
            "topic":["MySmartThingy/1/temp","MySmartThingy/1/hum"]},
            {"serviceType":"REST",
            "serviceIP":"dht11.org:8080"}],
        "lastUpdate":"2020-03-30"}'''

