
import serial

class serialClass():
    #variables used for recieving and transimitting over serial
    baudRateTx=1
    baudRateRx=0
    comPortTx=""
    comPortRx=""
    
    #variables used for main battery status
    voltage=0.0
    current=0
    current3_3=0
    current_5=0

    #varaibles used for Subsystem status
    OBC=0
    ADCS=0
    Payload=0
    comm_antennas=0
    #External system status variables
    Temp=0
    solar1=0
    solar2=0
    solar3=0
    solar4=0

    #EPS Motors status
    MotorX=0
    MotorY=0
    MotorZ=0
    
    #Temprature  Sensors in EPS
    EPSTemp=0
    BatHeater =0

    #Time
    Time=0

    serial_data=""


    def recieve_serial(self):
        try:
            # Replace 'COMx' with your actual serial port (e.g., COM3 on Windows, /dev/ttyUSB0 on Linux)
            with serial.Serial(self.comPortRx, self.baudRateRx, timeout=10) as serial_port:
                # Read one line from the serial port
                self.serial_data = serial_port.readline().decode('utf-8').strip()
                # Print the received data
                print("Received: {}".format(self.serial_data))
        except serial.SerialException as e:
            print(f"Error: {e}")


    def Manager_ofRecievedData(self):
        # Assuming self.serial_data is a string containing comma-separated values
        self.received_data = self.serial_data.split(',')
        
        #Recieved Data squence 
          #0)Time
          #1)Voltage
          #2)Current
          #3)Current3.3
          #4)Current5
          #5)Payload
          #6)OBCS
          #7)ADCS
          #8)Temp
          #9)Solar1
          #10)Solar2
          #11)Solar3
          #12)Solar4
          #13)COMM
          #14)EPSTemp
          #15)BatHeater
          #16)MotorX
          #17)MotorY
          #18)MotorZ

        # Assigning values to variables
        Time = int(self.received_data[0])
        voltage = float(self.received_data[1])
        current = int(self.received_data[2])
        current3_3 = int(self.received_data[3])
        current_5 = int(self.received_data[4])
        Payload = int(self.received_data[5])
        OBC = int(self.received_data[6])
        ADCS = int(self.received_data[7])
        Temp = int(self.received_data[8])
        solar1 = int(self.received_data[9])
        solar2 = int(self.received_data[10])
        solar3 = int(self.received_data[11])
        solar4 = int(self.received_data[12])
        comm_antennas = int(self.received_data[13])
        EPSTemp = float(self.received_data[14])
        BatHeater = int(self.received_data[15])
        MotorX = int(self.received_data[16])
        MotorY = int(self.received_data[17])
        MotorZ = int(self.received_data[18])

        # Assigning values to instance variables
        self.Time = Time
        self.voltage = voltage
        self.current = current
        self.current3_3 = current3_3
        self.current_5 = current_5
        self.Payload = Payload
        self.OBC = OBC
        self.ADCS = ADCS
        self.Temp = Temp
        self.solar1 = solar1
        self.solar2 = solar2
        self.solar3 = solar3
        self.solar4 = solar4
        self.comm_antennas = comm_antennas
        self.BatHeater =BatHeater
        self.EPSTemp = EPSTemp
        self.MotorX = MotorX
        self.MotorY = MotorY
        self.MotorZ= MotorZ









       