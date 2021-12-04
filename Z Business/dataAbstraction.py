
import pandas as pd
import numpy as np
import pandasql as psql
import re
import matplotlib.pyplot as plt
import seaborn as sns

# User Input: 
nyc_zipcode = input("Enter NYC zip code: ")
Business_type = input("Enter Business type: ")

# Data Used: 
income_csv = pd.read_csv("Z Business/csv/ACSST5Y2019.S1901_data_with_overlays_2021-11-17T013226.csv", skiprows=1)
business_data = pd.read_csv("Z Business/csv/Legally_Operating_Businesses.csv")

# data cleaning  | Income data:

clean_income_data = pd.DataFrame()

zipcodes = []
for z in income_csv["Geographic Area Name"]:
    zipcodes.append(z.split()[1])
clean_income_data["zipcode"] = zipcodes

clean_income_data["Total Households"] = income_csv["Estimate!!Households!!Total"]
clean_income_data["MOE Total Households"] = income_csv["Margin of Error!!Households!!Total"]
clean_income_data["Less than $10,000"] = income_csv["Estimate!!Households!!Total!!Less than $10,000"]
clean_income_data["MOE Less than $10,000"] = income_csv["Margin of Error!!Households!!Total!!Less than $10,000"]
clean_income_data["$10,000 to $14,999"] = income_csv["Estimate!!Households!!Total!!$10,000 to $14,999"]
clean_income_data["MOE $10,000 to $14,999"] = income_csv["Margin of Error!!Households!!Total!!$10,000 to $14,999"]
clean_income_data["$15,000 to $24,999"] = income_csv["Estimate!!Households!!Total!!$15,000 to $24,999"]
clean_income_data["MOE $15,000 to $24,999"] = income_csv["Margin of Error!!Households!!Total!!$15,000 to $24,999"]
clean_income_data["$25,000 to $34,999"] = income_csv["Estimate!!Households!!Total!!$25,000 to $34,999"]
clean_income_data["MOE $25,000 to $34,999"] = income_csv["Margin of Error!!Households!!Total!!$25,000 to $34,999"]
clean_income_data["$35,000 to $49,999"] = income_csv["Estimate!!Households!!Total!!$35,000 to $49,999"]
clean_income_data["MOE $35,000 to $49,999"] = income_csv["Margin of Error!!Households!!Total!!$35,000 to $49,999"]
clean_income_data["$50,000 to $74,999"] = income_csv["Estimate!!Households!!Total!!$50,000 to $74,999"]
clean_income_data["MOE $50,000 to $74,999"] = income_csv["Margin of Error!!Households!!Total!!$50,000 to $74,999"]
clean_income_data["$75,000 to $99,999"] = income_csv["Estimate!!Households!!Total!!$75,000 to $99,999"]
clean_income_data["MOE $75,000 to $99,999"] = income_csv["Margin of Error!!Households!!Total!!$75,000 to $99,999"]
clean_income_data["$100,000 to $149,999"] = income_csv["Estimate!!Households!!Total!!$100,000 to $149,999"]
clean_income_data["MOE $100,000 to $149,999"] = income_csv["Margin of Error!!Households!!Total!!$100,000 to $149,999"]
clean_income_data["$150,000 to $199,999"] = income_csv["Estimate!!Households!!Total!!$150,000 to $199,999"]
clean_income_data["MOE $150,000 to $199,999"] = income_csv["Margin of Error!!Households!!Total!!$150,000 to $199,999"]
clean_income_data["$200,000 or more"] = income_csv["Estimate!!Households!!Total!!$200,000 or more"]
clean_income_data["MOE $200,000 or more"] = income_csv["Margin of Error!!Households!!Total!!$200,000 or more"]
clean_income_data["Households Median Income"] = income_csv["Estimate!!Households!!Median income (dollars)"]
clean_income_data["MOE Households Median Income"] = income_csv["Margin of Error!!Households!!Median income (dollars)"]
clean_income_data["Households Mean Income"] = income_csv["Estimate!!Households!!Mean income (dollars)"]
clean_income_data["MOE Households Mean Income"] = income_csv["Margin of Error!!Households!!Mean income (dollars)"]



clean_business_data = pd.DataFrame()
clean_business_data["Industry"] = business_data["Industry"]
clean_business_data["Address ZIP"] = business_data["Address ZIP"]

clean_income_data.to_csv("clean_income_data.csv")
clean_business_data.to_csv("clean_business_data.csv")


def getBusinessCount(zipcode,industry):
    numBusiness = clean_business_data[clean_business_data["Address ZIP"] == zipcode and clean_business_data["Industry"] == industry]
    return numBusiness

# print(clean_business_data) 271668