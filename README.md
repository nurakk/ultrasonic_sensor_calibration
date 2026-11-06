# Ultrasonic Sensor Calibration Using Linear Regression

## 1. Project Overview

This project demonstrates the calibration of an ultrasonic distance sensor using Python and Linear Regression.

The experiment compares the distance measured by an ultrasonic sensor with known reference distances. A Linear Regression model is developed to calculate the calibration slope and offset. The resulting calibration equation is used to correct sensor measurements.

The experiment is implemented using Jupyter Notebook and is suitable for engineering students studying Robotics, Automation, Instrumentation and Sensor Technology.

## 2. Objectives

- Understand the concept of ultrasonic sensor calibration.
- Compare sensor measurements with actual reference distances.
- Calculate measurement errors and percentage errors.
- Develop a calibration equation using Linear Regression.
- Visualize experimental data using a calibration graph.
- Estimate corrected distances using the calibration model.

## 3. Algorithm Used

**Linear Regression**

Linear Regression is a supervised machine learning algorithm used to establish a mathematical relationship between sensor measurements and actual reference distances.

The calibration equation is:

\[
d_{actual}=a \times d_{sensor}+b
\]

Where:

- `d_actual` – Actual reference distance (cm)
- `d_sensor` – Ultrasonic sensor reading (cm)
- `a` – Calibration slope
- `b` – Calibration offset

## 4. Technologies Used

- Python 3
- Jupyter Notebook
- NumPy
- Matplotlib
- Scikit-learn
- Linear Regression

## 5. Experimental Setup

The experiment uses:

- HC-SR04 ultrasonic sensor (for physical implementation)
- Arduino Uno or ESP32 (optional hardware interface)
- Flat target surface
- Measuring scale or measuring tape
- Computer with Python and Jupyter Notebook

**Note:** The current Python program uses illustrative sample measurements. Actual sensor readings should be collected experimentally for real calibration.

## 6. Software Requirements

Install the required libraries:

```python
%pip install numpy matplotlib scikit-learn
```

## 7. How to Run the Project

### Step 1: Clone the repository

```bash
git clone https://github.com/nurakk/ultrasonic_sensor_calibration.git
```

### Step 2: Navigate to the repository

```bash
cd ultrasonic_sensor_calibration
```

### Step 3: Open Jupyter Notebook

```bash
jupyter notebook
```

### Step 4: Execute the notebook

Open the Jupyter Notebook file and execute the cells sequentially.

## 8. Expected Outputs

The program generates:

1. Calibration slope and offset.
2. Linear calibration equation.
3. Calibration observation table.
4. Experimental data scatter plot.
5. Linear regression calibration curve.
6. Corrected distance prediction for a new sensor reading.

## 9. Applications

- Distance measurement systems
- Mobile robot navigation
- Obstacle detection
- Autonomous robotic systems
- Sensor accuracy improvement
- Robotics and automation laboratory experiments

## 10. Repository Structure

```text
ultrasonic_sensor_calibration/
│
├── ultrasonic_sensor_calibration.ipynb
├── README.md
└── .gitignore
```

## 11. Author

**Arun Kumar K**  
Department of Robotics and Automation

GitHub: [@nurakk](https://github.com/nurakk)

## 12. References

- [Scikit-learn – Linear Regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)
- [NumPy Documentation](https://numpy.org/doc/)
- [Matplotlib Documentation](https://matplotlib.org/stable/)
- [HC-SR04 Ultrasonic Sensor Datasheet](https://cdn.sparkfun.com/datasheets/Sensors/Proximity/HCSR04.pdf)

---

**Educational Project | Robotics and Automation Laboratory**
