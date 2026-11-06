#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Actual reference distances (cm)
actual = np.array([10, 20, 30, 40, 50, 60, 70, 80])

# Ultrasonic sensor measured distances (cm)
sensor = np.array([10.5, 20.8, 30.4, 41.2, 50.8, 61.5, 70.9, 81.7])

# Reshape sensor data for Linear Regression
X = sensor.reshape(-1, 1)
y = actual

# Create and train the regression model
model = LinearRegression()
model.fit(X, y)

# Calculate calibration slope and offset
a = model.coef_[0]
b = model.intercept_

# Display calibration equation
print("ULTRASONIC SENSOR CALIBRATION")
print("--------------------------------")
print("Calibration Slope (a):", round(a, 4))
print("Calibration Offset (b):", round(b, 4))
print("\nCalibration Equation:")
print("Actual Distance =", round(a, 4), "* Sensor Reading +", round(b, 4))

# Calculate corrected distances
corrected = model.predict(X)

# Calculate errors
error = sensor - actual
percentage_error = (np.abs(error) / actual) * 100

# Display observation table
print("\nCALIBRATION OBSERVATION TABLE")
print("--------------------------------")
print("Actual(cm)  Sensor(cm)  Corrected(cm)  Error(%)")

for i in range(len(actual)):
    print(f"{actual[i]:8.2f}  {sensor[i]:10.2f}  {corrected[i]:13.2f}  {percentage_error[i]:8.2f}")

# Plot calibration graph
plt.figure(figsize=(9, 6))

plt.scatter(sensor, actual, color='blue', label='Experimental Data')

plt.plot(sensor, corrected, color='red', label='Calibration Line')

plt.xlabel("Sensor Reading (cm)")
plt.ylabel("Actual Reference Distance (cm)")
plt.title("Ultrasonic Sensor Calibration Using Linear Regression")

plt.legend()
plt.grid(True)
plt.show()

# Test with a new sensor reading
new_reading = 50

corrected_distance = model.predict([[new_reading]])[0]

print("\nCALIBRATION TEST")
print("--------------------------------")
print("New Sensor Reading:", new_reading, "cm")
print("Corrected Distance:", round(corrected_distance, 2), "cm")


# In[ ]:




