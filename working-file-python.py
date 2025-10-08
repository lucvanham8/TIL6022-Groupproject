#Import relevant packages
import pandas as pd
import matplotlib.pyplot as plt

#Read the data
df_pres = pd.read_csv('data/transport_performance.csv', sep=';')
df_mob= pd.read_csv('data/mobiliteit.csv', sep=';')
df_pres.head()

#Initialise prestation data
df_pres['Periods'] = pd.to_numeric(df_pres['Periods'], errors='coerce')
df_pres['Transport performance (billion passenger kilometres )'] = pd.to_numeric(df_pres['Transport performance (billion passenger kilometres )'], errors='coerce')

#Rename columns
df_pres.rename({'Transport performance (billion passenger kilometres )': 'Total travel'}, axis=1, inplace=True)

#Drop unnesecary columns
df_pres.drop('Margins', axis=1, inplace=True)
df_pres.drop('Population', axis=1, inplace=True)

df_pres.head()

#Initialise mobility data
df_mob.head()

#Trying out some stuff

data_selected= df_pres[(df_pres['Region characteristics']=='The Netherlands') & (df_pres['Modes of travel']=='Total')]

plt.plot(data_selected['Periods'], data_selected['Total travel'])
print(plt.show())
