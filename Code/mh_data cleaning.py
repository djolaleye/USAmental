#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 10:34:54 2023

@author: deji
"""
import pandas as pd

pd.options.display.max_columns = None

main = pd.read_csv('MentalhealthDepressiondisorderData.csv')
# consists of 4 distinct tables, need to separate

mh_disorder_shares = main.iloc[:6468].copy() # Mental Health Disorder Shares in %.

mh_disorder_mf = main.iloc[6469:54276].copy() # Mental Health Disorder Share per Sex in %.

mh_sui_dep = main.iloc[54277:102084].copy() # Suicide and Depression per 100k inhabitants.

mh_depdisorders = main.iloc[102085:].copy() # Prevalence - Depressive disorders per 100k inhabitants.


# Remove unnecessary columns
mh_disorder_shares = mh_disorder_shares.iloc[:,1:]
mh_disorder_mf = mh_disorder_mf.iloc[:,1:7]
mh_sui_dep = mh_sui_dep.iloc[:,1:7]
mh_depdisorders = mh_depdisorders.iloc[:,1:5]



# Change column names to represent data
mh_disorder_shares.rename(columns={'Schizophrenia (%)':'Schizophrenia(%)',
                               'Bipolar disorder (%)':'Bipolar_disorder(%)',
                               'Eating disorders (%)':'Eating_disorders(%)',
                               'Anxiety disorders (%)':'Anxiety_disorders(%)',
                               'Drug use disorders (%)':'Drug_use_disorders(%)',
                               'Depression (%)':'Depression(%)',
                               'Alcohol use disorders (%)':'Alcohol_use_disorders(%)'}, inplace = True)

mh_disorder_mf.rename(columns={'Schizophrenia (%)':'Prevalence_in_males(%)',
                               'Bipolar disorder (%)':'Prevalence_in_females(%)',
                               'Eating disorders (%)':'Population'}, inplace = True)

mh_sui_dep.rename(columns={'Schizophrenia (%)':'Suicide_rate(per100.000)',
                           'Bipolar disorder (%)':'Depression_rate(per100.000)',
                           'Eating disorders (%)':'Population'}, inplace = True)

mh_depdisorders.rename(columns={'Schizophrenia (%)':'Depression_prevalence'}, inplace = True)


# Remove missing values - NA country codes remain (denotes group of countries rather than individual)
mh_disorder_mf.dropna(inplace = True)
mh_sui_dep.drop_na(inplace = True)


# Change data types from object to numeric (Year in numeric rather than date)
mh_disorder_shares.iloc[:, 2:] = mh_disorder_shares.iloc[:, 2:].apply(pd.to_numeric)
mh_disorder_mf[['Year', 'Prevalence_in_males(%)','Prevalence_in_females(%)', 'Population']] = mh_disorder_mf[['Year', 'Prevalence_in_males(%)','Prevalence_in_females(%)', 'Population']].apply(pd.to_numeric)
mh_sui_dep[['Year', 'Suicide_rate(per100.000)','Depression_rate(per100.000)', 'Population']] = mh_sui_dep[['Year', 'Suicide_rate(per100.000)','Depression_rate(per100.000)', 'Population']].apply(pd.to_numeric)
mh_depdisorders[['Year', 'Depression_prevalence']] = mh_depdisorders[['Year', 'Depression_prevalence']].apply(pd.to_numeric)




# Export cleaned data
mh_disorder_shares.to_csv('mh_disorders.csv')
mh_disorder_mf.to_csv('mh_by_sex.csv')
mh_sui_dep.to_csv('mh_suicide_and_depression.csv')
mh_depdisorders.to_csv('mh_depression.csv')






