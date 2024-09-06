INFORMATION_STATES = [15, 16, 17]
encoded_number = int(input())

multipliers = [1]
for i in range(len(INFORMATION_STATES) - 1):
    multipliers.append(multipliers[-1] * INFORMATION_STATES[i])
multipliers.reverse()

output = []
for i in range(len(INFORMATION_STATES)):
    for j in range(INFORMATION_STATES[-1-i], -1, -1):
        if encoded_number >= j * multipliers[i]:
            output.append(j)
            encoded_number -= j * multipliers[i]
            break
output.reverse()

print(output)
