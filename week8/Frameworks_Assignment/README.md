# Frameworks_Assignment — CORD-19 Data Explorer
```


## How to get the data (Kaggle)
1. Go to: https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge
2. Download only `metadata.csv` from the Data tab.
3. Place the CSV in the `data/` folder.

Alternatively, use Kaggle API (after placing `~/.kaggle/kaggle.json`):
```bash
kaggle datasets download -d allen-institute-for-ai/cord-19-research-challenge --unzip -p data
```
## Setup
1. Create & activate a virtual environment:
```bash
python -m venv venv
# mac/linux
source venv/bin/activate
# windows
venv\Scripts\activate
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
## Notebook (analysis)
Open `notebooks/analysis.ipynb` and run the cells. The notebook walks through:
- Loading the dataset
- Basic exploration (shape, dtypes, missing values)
- Cleaning decisions (dropping columns with many missingness, parsing dates)
- Feature engineering (publication year, abstract word count)
- Basic analysis (papers per year, top journals, frequent title words)
- Visualizations saved to `outputs/` (publications_by_year.png, top_journals.png, wordcloud_titles.png)
## Streamlit app
Run locally with:
```bash
streamlit run app.py
```
The app will let you filter by year range, view top journals, and download filtered CSVs.
## Expected outputs
After running the notebook you will find:
- `outputs/publications_by_year.png`
- `outputs/top_journals.png`
- `outputs/wordcloud_titles.png`
## Notes and reflection (suggested items to include in your deliverable)
- Document which columns you dropped and why (e.g., >80% missing)
- Note how many rows had missing `publish_time` and how you handled them
- Describe the main findings (years with highest publication counts, top journals, common title words, share of preprints)