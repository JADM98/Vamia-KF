import numpy as np
import matplotlib.pyplot as plt

from filters import kalman

kf = kalman.KalmanFilter()
# kf.update((1,2))
kf.setStdDeviation(15)
kf.setNewMeasureTime(25)

x = np.linspace(-10, 10, 100)
measurements = - (x**2 + 2*x - 2)  + np.random.normal(0, 15, 100)
predictions = []
updates = []

for z in measurements:
    updates.append(kf.update((z)))
    predictions.append(kf.predict())

# predictions.append(kf.predict())

import matplotlib.pyplot as plt
plt.plot(range(len(measurements)), measurements, label = 'Measurements')
plt.plot(range(len(predictions)), np.array(predictions), label = 'Kalman Filter Prediction')
plt.plot(range(len(updates)), np.array(updates), label = 'Kalman Filter Updates')
plt.legend()
plt.show()