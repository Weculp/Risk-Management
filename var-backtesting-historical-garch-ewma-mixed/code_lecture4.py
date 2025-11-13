#########################
####### LECTURE 4 #######
#########################

# Import standard libraries
import numpy as np
import pandas as pd
from scipy.optimize import fmin
import matplotlib
import matplotlib.pyplot as plt
import os
from arch import arch_model

# Read in data
os.chdir('PATH_TO_YOUR_DROPBOX/Dropbox/spring2022/lecture4_ModelBasedApproach/code')
dta = pd.read_csv('./SP500VIX.csv', parse_dates=['date'])

dta['ret'] = dta['SP500'].pct_change(1)
dta['ret2'] = dta['ret']**2
dta = dta.dropna() # drops all rows with missing data (here only first row)

### EWMA variance

# initialize by starting only as of 2008
# technically we are ignoring V_L, but since it enters with lambda^174 ~ 0 it can be ignored

Lambda = 0.94

dta_early = dta[dta['date'] < "2008-01-01"]
sigma0 = sum(np.array(dta_early['ret2']) * (1-Lambda)*Lambda**(np.linspace(len(dta_early.index), 1, len(dta_early.index))))

# then use the simple volatility updating
dta_post = dta[dta['date'] >= "2008-01-01"]
Ret2 = np.array(dta_post['ret2'])

sigma2 = np.concatenate((np.array([sigma0]), np.zeros(len(Ret2))), axis = None)

for j in range(1, len(sigma2)):
    sigma2[j] = sigma2[j-1]*Lambda + Ret2[j-1]*(1-Lambda)

# visualize
dates = matplotlib.dates.date2num(dta_post['date'])
plt.plot_date(dates, np.sqrt(sigma2[1:]),'b-')
plt.show()


### ARCH(1) max likelihood

def logL(omega, alpha, data):
    ret2 = data**2
    sigma0 = omega/(1-alpha)
    sigma2 = np.concatenate((np.array([sigma0]), np.zeros(len(data))), axis = None)
    loglik = 0
    for t in range(0, len(data)):
        sigma2[t+1] = omega + alpha*ret2[t]
        loglik = loglik - np.log(sigma2[t]) - ret2[t]/sigma2[t]
    return(loglik)

def tobeoptimized(param):
    return(-logL(param[0], param[1], np.array(dta['ret'])))  # maximize f() is equivalent to minimize -f()

fmin(tobeoptimized,[1e-06, 1e-01])
# this is for exposition, import libraries otherwise, e.g. arch below 

model = arch_model(np.array(100*dta['ret']), mean='zero', vol='ARCH', p=1)
model_fit = model.fit()
model_fit