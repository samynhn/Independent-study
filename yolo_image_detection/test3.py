import matplotlib.pyplot as plt
temper1 = [32.1, 33.5, 33.6, 33.7, 34.9, 34.9, 35, 35.1, 35.5, 36.3, 36.4, 36.5, 36.5, 36.4, 36.3]
temper2 = [25.1, 25.5, 25.6, 25.6, 26.2, 26.3, 26, 26.1, 25.5, 25.3, 25.4, 25.2, 25.1, 25, 24.5]
plt.plot(range(len(scores)), temper1)
plt.plot(range(len(scores)), temper2)
plt.show()