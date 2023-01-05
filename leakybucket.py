import random

packetCount = 0
buffer = 0
maxValue = random.choice([10, 20, 40, 80, 160])
packetSize = random.choice([10, 20, 40, 80, 160])

while buffer <= maxValue:
    buffer += packetSize
    packetCount += 1
    if buffer > maxValue:
        break
    
print("maxValue:",maxValue)
print("packetSize:",packetSize)    
print("packetCount:",packetCount-1)