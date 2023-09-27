#Name: Andreas Constantinou
#Email: Andreas.Constantinou64@myhunter.cuny.edu

#Title: Growth of Death in NYC

#URL: https://andreasconstantino26.wixsite.com/website

#Resources: https://data.cityofnewyork.us/Health/New-York-City-Leading-Causes-of-Death/jb7j-dtam , https://gun-control.procon.org/, 
#https://apps.health.ny.gov/public/tabvis/PHIG_Public/lcd/reports/#lifeexp

##Abstract: This project talks about all the deaths happening in NYC and what we can do in order to decrease it. I mention many different variables such as
##race, gender, year, and cause and talk about the relevance each of these variables have.

#IMPORTANT: In the data I used, whenever they wanted to put 0 they put a (.) instead so I manually changed all the . to 0


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Import csv file
data = pd.read_csv (r'New_York_City_Leading_Causes_of_Death.csv')
df = pd.DataFrame(data)
#The death column was written as a string instead of integers so I used this in order to be able to add
df['Deaths']  = df['Deaths'].astype(int)

#Gender death
copy_frame= pd.DataFrame() # Extracts all the male and female values and puts them into two seperate variables
Male = df[df['Sex'] == 'M'] # Makes a variable that takes in all male values
Female = df[df['Sex'] == 'F']# Makes a variable that takes in all female values

male_total = Male['Deaths'].sum() # Adds up the total amount of death for men
female_total = Female['Deaths'].sum() # Adds up the total amount of death for women
#Makes the appropraite label names and puts in the information for each label. Then names each axis and shows the bar graph
copy_frame['Gender'] = 'Male', 'Female' # Makes the column names
copy_frame['Total'] = male_total, female_total #puts data in column names
print(copy_frame)
bar = copy_frame.plot.bar(x = 'Gender', y = 'Total', rot = 0) #Provides x and y axis, and puts in the info
plt.ylabel('Deaths') #Titles y label
plt.title('Gender Deaths') #Titles x label
plt.show()

#Race death
temp0 = pd.DataFrame() #Seperates all the information based on race
His = df[df['Race Ethnicity'] == 'Hispanic']
Asap = df[df['Race Ethnicity'] == 'Asian and Pacific Islander']
BNH = df[df['Race Ethnicity'] == 'Black Non-Hispanic']
NSU = df[df['Race Ethnicity'] == 'Not Stated/Unknown']
ORE = df[df['Race Ethnicity'] == 'Other Race/ Ethnicity']
WNH = df[df['Race Ethnicity'] == 'White Non-Hispanic']

His_total = His['Deaths'].sum() #Adds up each total of the amount of deaths from each race
Asap_total = Asap['Deaths'].sum()
BNH_total = BNH['Deaths'].sum()
NSU_total = NSU['Deaths'].sum()
ORE_total = ORE['Deaths'].sum()
WNH_total = WNH['Deaths'].sum()

#Makes the appropraite label names and puts in the information for each label. Then names each axis and shows the bar graph, also prints a chart to show exact numbers
temp0['Race'] = 'Hispanic', 'Asian and Pacific Islander', 'Black Non-Hispanic', 'Not Stated/Unknown', 'Other Race/ Ethnicity', 'White Non-Hispanic' 
temp0['Total'] = His_total, Asap_total, BNH_total, NSU_total, ORE_total, WNH_total 
print(temp0)
bar = temp0.plot.bar(x = 'Race', y = 'Total', rot = 0)
plt.ylabel('Deaths')
plt.title('Race Deaths')
plt.show()

#Year Death
year00 = pd.DataFrame()#Seperates all the information based on year
two7 = df[df['Year'] == 2007]
two8 = df[df['Year'] == 2008]
two9 = df[df['Year'] == 2009]
two10 = df[df['Year'] == 2010]
two11 = df[df['Year'] == 2011]
two12 = df[df['Year'] == 2012]
two13 = df[df['Year'] == 2013]
two14 = df[df['Year'] == 2014]
two15 = df[df['Year'] == 2015]
two16 = df[df['Year'] == 2016]
two17 = df[df['Year'] == 2017]

two7_total = two7['Deaths'].sum() #Adds up each total of the amount of deaths from each year
two8_total = two8['Deaths'].sum()
two9_total = two9['Deaths'].sum()
two10_total = two10['Deaths'].sum()
two11_total = two11['Deaths'].sum()
two12_total = two12['Deaths'].sum()
two13_total = two13['Deaths'].sum()
two14_total = two14['Deaths'].sum()
two15_total = two15['Deaths'].sum()
two16_total = two16['Deaths'].sum()
two17_total = two17['Deaths'].sum()

#Makes the appropraite label names and puts in the information for each label. Then names each axis and shows the bar graph, also prints a chart to show exact numbers
year00['Years'] = '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017' 
year00['Total'] = two7_total, two8_total, two9_total, two10_total, two11_total, two12_total, two13_total, two14_total, two15_total, two16_total, two17_total
print(year00)
bar = year00.plot.bar(x = 'Years', y = 'Total', rot = 0)
plt.ylabel('Deaths')
plt.title('Yearly Deaths')
plt.show()

#Cause of Death
Cause00 = pd.DataFrame() #Seperates all the information based on cause of death
DOH = df[df['Leading Cause'] == 'Diseases of Heart (I00-I09, I11, I13, I20-I51)']
CLR = df[df['Leading Cause'] == 'Chronic Lower Respiratory Diseases (J40-J47)']
MDA = df[df['Leading Cause'] == 'Mental and Behavioral Disorders due to Accidental Poisoning and Other Psychoactive Substance Use (F11-F16, F18-F19, X40-X42, X44)']
CLC = df[df['Leading Cause'] == 'Chronic Liver Disease and Cirrhosis (K70, K73)']
DMM = df[df['Leading Cause'] == 'Diabetes Mellitus (E10-E14)']
CDD = df[df['Leading Cause'] == 'Cerebrovascular Disease (Stroke: I60-I69)']
MNN = df[df['Leading Cause'] == 'Malignant Neoplasms (Cancer: C00-C97)']
IFP = df[df['Leading Cause'] == 'Influenza (Flu) and Pneumonia (J09-J18)']
ADP = df[df['Leading Cause'] == 'Accidents Except Drug Posioning (V01-X39, X43, X45-X59, Y85-Y86)']
EHD = df[df['Leading Cause'] == 'Essential Hypertension and Renal Diseases (I10, I12)']
AOC = df[df['Leading Cause'] == 'All Other Causes']

DOH_total = DOH['Deaths'].sum() #Adds up each total of the amount of deaths from each year
CLR_total = CLR['Deaths'].sum()
MDA_total = MDA['Deaths'].sum()
CLC_total = CLC['Deaths'].sum()
DMM_total = DMM['Deaths'].sum()
CDD_total = CDD['Deaths'].sum()
MNN_total = MNN['Deaths'].sum()
IFP_total = IFP['Deaths'].sum()
ADP_total = ADP['Deaths'].sum()
EHD_total = EHD['Deaths'].sum()
AOC_total = AOC['Deaths'].sum()

#Makes the appropraite label names and puts in the information for each label. Then names each axis and shows the bar graph, also prints a chart to show exact numbers
Cause00['Leading Cause'] = 'Heart Desease', 'Respiratory Desease', 'Behavior disorder', 'Cirrhosis', 'Diabetes Mellitus', 'Stroke', 'Cancer', 'Flu/Pneumonia', 'Accidents', 'Hypertention/Renal desease', 'Other' 
Cause00['Total'] = DOH_total, CLR_total, MDA_total, CLC_total, DMM_total, CDD_total, MNN_total, IFP_total, ADP_total, EHD_total, AOC_total
print(Cause00)
bar = Cause00.plot.bar(x = 'Leading Cause', y = 'Total', rot = 0)
plt.ylabel('Deaths')
plt.title('Cause of Death')
plt.show()




