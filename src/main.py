import numpy as np
import matplotlib.pyplot as plt

from filters import kalman

kf = kalman.KalmanFilter()
# kf.update((1,2))
kf.setStdDeviation(2)
kf.setNewMeasureTime(25)

x = np.linspace(-10, 10, 100)
measurements = - (x**2 + 2*x - 2)  + np.random.normal(0, 2, 100)
predictions = []

for z in measurements:
    kf.update((z))
    predictions.append(kf.predict())

# predictions.append(kf.predict())

import matplotlib.pyplot as plt
plt.plot(range(len(measurements)), measurements, label = 'Measurements')
plt.plot(range(len(predictions)), np.array(predictions), label = 'Kalman Filter Prediction')
plt.legend()
plt.show()