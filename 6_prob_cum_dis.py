from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
#Probability functions
np.set_printoptions(precision=8)
t_dist=stats.t(20)
#Plot the PDF
t_values =np.linspace(-4,6,1000)
plt.plot(t_values,t_dist.pdf(t_values))
plt.xlabel('t value')
plt.ylabel('probability for 1 value')
plt.title('PDF for t distribution with df=20')
plt.show()
#Plot the CDF
plt.plot(t_values,t_dist.cdf(t_values))
plt.xlabel('t value')
plt.ylabel('probability for t value<=t')
plt.title('CDE for t distribution with df=20')
plt.show()