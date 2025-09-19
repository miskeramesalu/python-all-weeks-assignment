# app.py - Streamlit app for CORD-19 metadata

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.set_page_config(page_title='CORD-19 Data Explorer', layout='wide')
@st.cache_data
def load_data(path='data/metadata.csv', nrows=None):
return pd.read_csv(path, nrows=nrows, low_memory=False)

st.title('CORD-19 Data Explorer')
st.write('Simple exploration of the CORD-19 metadata (titles, abstracts, journals, dates).')
# Sidebar
use_sample = st.sidebar.checkbox('Load sample (faster)', value=True)
if use_sample:
nrows = 50000
else:
nrows = None
path = st.sidebar.text_input('Path to metadata.csv', value='data/metadata.csv')
try:
df = load_data(path, nrows=nrows)
except FileNotFoundError:
st.error(f"File not found: {path}. Please download metadata.csv from Kaggle and place it in the data/ folder.")
st.stop()
# Prepare data
if 'publish_time' in df.columns:
df['publish_time_parsed'] = pd.to_datetime(df['publish_time'], errors='coerce', infer_datetime_format=True)
df['year'] = df['publish_time_parsed'].dt.year
else:
df['year'] = None
# Basic filters
min_year = int(df['year'].dropna().min()) if df['year'].dropna().size>0 else 2015
max_year = int(df['year'].dropna().max()) if df['year'].dropna().size>0 else 2023
year_range = st.sidebar.slider('Select year range', min_year, max_year, (min_year, max_year))
# Filtered dataframe
if df['year'].notna().any():
mask = df['year'].between(year_range[0], year_range[1])
df_filt = df[mask]
else:
df_filt = df.copy()
st.subheader(f'Showing {len(df_filt):,} papers')
# Publications by year plot
if 'year' in df.columns:
year_counts = df_filt['year'].value_counts().sort_index()
fig1, ax1 = plt.subplots()
year_counts.plot(kind='bar', ax=ax1)
ax1.set_xlabel('Year')
ax1.set_ylabel('Count')
ax1.set_title('Publications by Year')
st.pyplot(fig1)
# Top journals
st.subheader('Top journals')
if 'journal' in df.columns:
top_n = st.sidebar.slider('Top N journals', 5, 50, 15)
top_j = df_filt['journal'].fillna('Unknown').value_counts().head(top_n)
fig2, ax2 = plt.subplots()
top_j.sort_values().plot(kind='barh', ax=ax2)
ax2.set_xlabel('Count')
ax2.set_title('Top journals')
st.pyplot(fig2)
# Show sample rows
st.subheader('Sample records')
show_cols = ['title', 'authors', 'journal', 'publish_time']
available_cols = [c for c in show_cols if c in df_filt.columns]
st.dataframe(df_filt[available_cols].head(200))

# Download filtered CSV
csv = df_filt.to_csv(index=False)
st.download_button('Download filtered CSV', csv, file_name='cord19_filtered.csv', mime='text/csv')

st.markdown('---')
st.markdown('**Notes:** For full analysis, run the Jupyter notebook `notebooks/analysis.ipynb` which saves figures to `outputs/`.')