import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#--------
#READ
#--------
df = pd.read_csv('analytical_py.csv').dropna()
print("START\n",df.columns)
#print(df); exit()

Y=(df.open_date.str[0:4].astype('float'))
M=((df.open_date.str[5:7].astype('float')))
D=(df.open_date.str[8:10].astype('float'))

#CONVERT YEAR TO CONTINOUS VARIABLE
YEAR=Y+(M-1.)/12.+(D-1)/365.

#--------
#PLOT
#--------
#https://www.statology.org/matplotlib-scatterplot-color-by-value/
fig, ax = plt.subplots()

im=ax.scatter(df['loan_payments'], df['loan_amount'], c=df['loan_term'])
# print(df['loan_payments']*df['loan_term']); print(df['loan_amount'])

ax.set(xlabel='loan_payments', ylabel='loan_amount',
       title='loan_payments vs loan_amount')

ax.grid()
fig.colorbar(im, orientation='vertical')

fig.savefig("base-visualization.png")
plt.show()



# print(Y.iloc[0],(M.iloc[0]-1)/12,(D.iloc[0]-1)/365)
# print(Y.iloc[1],(M.iloc[1]-1)/12,(D.iloc[1]-1)/365)
# print(Y+(M-1.)/12.+(D-1)/365.)
