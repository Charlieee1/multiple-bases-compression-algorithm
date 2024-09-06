INFORMATION_STATES = [15, 16, 17]
# Assume information entered is valid
data = [int(input()) for i in range(len(INFORMATION_STATES))]

encoded_number = 0
multiplier = 1

for i in range(len(INFORMATION_STATES)):
    encoded_number += data[i] * multiplier
    multiplier *= INFORMATION_STATES[i]
print(encoded_number)
