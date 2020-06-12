# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


max_temp = np.array([39, 41, 43, 47, 49, 51, 45, 38, 37, 29, 27, 25])

min_temp = np.array([21, 23, 27, 28, 32, 35, 31, 28, 21, 19, 17, 18])

months = np.arange(12)

plt.plot(months, max_temp, 'go')
plt.plot(months, min_temp, 'co')

plt.xlabel('Months')
plt.ylabel('Max & Min Temperature')



from scipy import optimize
def yearly_temps(times, avg, ampl, time_offset):
    return (avg
            + ampl * np.cos((times + time_offset) * 1.8 * np.pi / times.max()))

res_max, cov_max = optimize.curve_fit(yearly_temps, months,
                                      max_temp, [40, 20, 0])
res_min, cov_min = optimize.curve_fit(yearly_temps, months,
                                      min_temp, [-40, 20, 0])






days = np.linspace(0, 12, num=365)

plt.figure()
plt.plot(months, max_temp, 'go')
plt.plot(days, yearly_temps(days, *res_max), 'm-')
plt.plot(months, min_temp, 'co')
plt.plot(days, yearly_temps(days, *res_min), 'y-')
plt.xlabel('Month')
plt.ylabel('Temperature ($^\circ$C)')

plt.show()













