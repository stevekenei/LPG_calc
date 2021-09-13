#!/usr/bin/env python
# coding: utf-8

# In[49]:


import streamlit as st
import plotly.graph_objects as go
import numpy as np
from time import sleep
import altair as alt


# In[7]:


st.set_page_config(page_title="LPG vs other fuel Calculator")


# In[8]:


st.title("LPG vs other fuel Calculator")


# In[9]:


st.header("**Monthly consumption**")


# In[10]:


st.subheader("Fuel comparison")


# In[41]:


colFueltype, colPermonth, colCost = st.columns(3)


# In[46]:


with colFueltype:
    fuel_type = option = st.selectbox('Which fuel type do you use?', ('LPG', 'Firewood', 'Charcoal', 'Electricity', 'Kerosene'))
with colPermonth:
    fuel_amount = st.number_input("Enter consumption per month in kilos/litres: ", min_value=0.0)
with colCost:
    cost_client = st.number_input("How much do you spend on fuel per unit each month(kg/l): ", min_value=1)


# In[51]:


energy_density = []
cost = []
for fuel in fuel_type:
    if fuel == 'LPG':
        energy_density = 25
        cost = 212
    elif fuel == 'Firewood':
        energy_density = 16
        
    elif fuel == 'Charcoal':
        energy_density = 30
       
    elif fuel == 'Electricity':
        energy_density = 14.4
        
    else:
        energy_density = 42.8
       
st.write('The Energy density of {} is {} per kg/l'.format(fuel_type, energy_density))
st.write('Your monthly energy cost is {} KES'.format(cost_client))
st.write('Your equivalent monthly cost using LPG is xxxx KES')


# In[48]:


st.header("**Forecast Savings**")


# In[59]:


st.subheader("Forecast Month")
forecast_months = st.number_input("Enter your forecast months (Min 1 month): ", min_value=0, format='%d')
    
st.write('Your equivalent savings forecasted by {} month is {} KES'.format(forecast_months, cost_client*forecast_months - 2760*forecast_months)) 


# colForecast1, colForecast2 = st.beta_columns(2)
# with colForecast1:
#     st.subheader("Forecast Year")
#     forecast_year = st.number_input("Enter your forecast year (Min 1 year): ", min_value=0,format='%d')
#     forecast_months = 12 * forecast_year 
    
#     st.subheader("Annual Inflation Rate")
#     annual_inflation = st.number_input("Enter annual inflation rate (%): ", min_value=0.0,format='%f')
#     monthly_inflation = (1+annual_inflation)**(1/12) - 1
#     cumulative_inflation_forecast = np.cumprod(np.repeat(1 + monthly_inflation, forecast_months))
#     forecast_expenses = monthly_expenses*cumulative_inflation_forecast
# with colForecast2:
#     st.subheader("Annual Salary Growth Rate")
#     annual_growth = st.number_input("Enter your expected annual salary growth (%): ", min_value=0.0,format='%f')
#     monthly_growth = (1 + annual_growth) ** (1/12) - 1
#     cumulative_salary_growth = np.cumprod(np.repeat(1 + monthly_growth, forecast_months))
#     forecast_salary = monthly_takehome_salary * cumulative_salary_growth 
    
# forecast_savings = forecast_salary - forecast_expenses 
# cumulative_savings = np.cumsum(forecast_savings)

# x_values = np.arange(forecast_year + 1)

# fig = go.Figure()
# fig.add_trace(
#         go.Scatter(
#             x=x_values, 
#             y=forecast_salary,
#             name="Forecast Salary"
#         )
#     )

# fig.add_trace(
#         go.Scatter(
#             x=x_values,
#             y=forecast_expenses,
#             name= "Forecast Expenses"
#         )
#     )

# fig.add_trace(
#         go.Scatter(
#                 x=x_values, 
#                 y=cumulative_savings,
#                 name= "Forecast Savings"
#             )
#     )
# fig.update_layout(title='Forecast Salary, Expenses & Savings Over the Years',
#                    xaxis_title='Year',
#                    yaxis_title='Amount($)')

# st.plotly_chart(fig, use_container_width=True)


# In[ ]:




