import numpy as np

temperature = np.arange(0, 41, 1)
fan_speed = np.arange(0, 11, 1)

def trimf(x, a, b, c):
    left = 0 if b == a else (x - a) / (b - a)
    right = 0 if c == b else (c - x) / (c - b)
    return max(min(left, right), 0)

temperature_input = 28

temp_low_level = trimf(temperature_input, 0, 0, 20)
temp_medium_level = trimf(temperature_input, 10, 20, 30)
temp_high_level = trimf(temperature_input, 20, 30, 40)

fan_low = np.array([trimf(x, 0, 0, 5) for x in fan_speed])
fan_medium = np.array([trimf(x, 2, 5, 8) for x in fan_speed])
fan_high = np.array([trimf(x, 5, 10, 10) for x in fan_speed])

activation_low = np.fmin(temp_low_level, fan_low)
activation_medium = np.fmin(temp_medium_level, fan_medium)
activation_high = np.fmin(temp_high_level, fan_high)

aggregated = np.maximum(np.maximum(activation_low, activation_medium), activation_high)

if np.sum(aggregated) == 0:
    fan_output = 0
else:
    fan_output = np.sum(fan_speed * aggregated) / np.sum(aggregated)

print(f"Temperature input: {temperature_input}°C")
print(f"Calculated fan speed: {fan_output:.2f}")
