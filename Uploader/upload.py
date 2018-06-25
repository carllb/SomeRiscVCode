import sys
import serial
import struct

header = int("FA",16)

if len(sys.argv) < 4:
    print ("Please specify: serial port, binary file, start location in hex")

port = sys.argv[1]
fileName = sys.argv[2]
start = int(sys.argv[3],16)

ser = serial.Serial(port)
print("Port: ")
print(ser.name)

bytes = []

with open(fileName, "r") as f:
    
    byte = f.read(1)    
    while byte != "":
        bytes.append( byte )        
        byte = f.read(1)

# send the header
rawHeader = struct.pack("B", header)
ser.write(rawHeader)

#send the start location
start = struct.pack("<I", start)
ser.write(start)

# send the size
size = len(bytes)
rawSize = struct.pack("<I",size)
for c in rawSize:
    ser.write(c)

#send the binary file
for b in bytes:
    ser.write(b)
