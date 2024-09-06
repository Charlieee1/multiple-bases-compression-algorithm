INFORMATION_STATES = [3, 4, 5]
# Assume information entered is valid
data = [int(input()) for i in range(len(INFORMATION_STATES))]

encoded_number = 0
multiplier = 1

for i in range(len(INFORMATION_STATES)):
    encoded_number += data[i] * multiplier
    multiplier *= INFORMATION_STATES[i]
print(encoded_number)
