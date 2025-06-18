import pandas as pd
import streamlit as st
import plotly.express as px

cars = pd.read_csv('vehicles_us.csv')


# App header
st.header("US Vehicle Advertisements Data Dashboard")

# Checkbox to filter cars by year
if st.checkbox("Show only cars from 2015 and newer"):
    cars_filtered = cars[cars['model_year'] >= 2015]
else:
    cars_filtered = cars

# Bar chart: Average price by model year
mean_price = cars_filtered.groupby('model_year')['price'].mean().reset_index()

fig_bar = px.bar(mean_price, x='model_year', y='price',
                 title='Average Vehicle Price by Model Year')
st.plotly_chart(fig_bar)

# Histogram: Number of listings by model
fig_hist_model = px.histogram(cars_filtered, x='model',
                              title='Number of Listings by Vehicle Model',
                              nbins=30)
st.plotly_chart(fig_hist_model)

# Histogram: Odometer readings by model
fig_hist_odometer = px.histogram(cars_filtered, x='model', y='odometer',
                                 title='Odometer Readings by Model',
                                 nbins=30)
st.plotly_chart(fig_hist_odometer)

# Scatter plot: Odometer vs. Model Year
fig_scatter = px.scatter(cars_filtered, x='model_year', y='odometer',
                         title='Odometer vs. Model Year')
st.plotly_chart(fig_scatter)
