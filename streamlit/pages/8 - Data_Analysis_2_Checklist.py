# import pandas as pd
# import pandas_profiling
# from streamlit_pandas_profiling import st_profile_report
# run_data_pandas = run_data.profile_report()
# st_profile_report(run_data_pandas)
import streamlit as st
from Home import *

def main():
      st.set_page_config(page_title='RRGCC Running and Weather Data',
                         page_icon= ':runner:')
      
      header_path = 'images/rrgcc.png'
      
      st.image(header_path, use_column_width=True, width=100)
      
      centered_header('Running and Weather Data Analysis')
      centered_subheader('on RRGCC operated land')
      
      centered_header('Data Analysis 2 Project Requirement Checklist :')
      st.checkbox('Project plan for final project')
      st.checkbox('The project is uploaded to your GitHub repository and shows at minimum 5 separate commits')
      st.checkbox('The project includes a README with requirements met')
      st.checkbox('The project implements a data analysis program that uses pandas, matplotlib, and/or numpy to perform an analysis project of 2 or more pieces of data and implement a rich data visualization in Tableau / Jupyter/Plotly/Matplotlib, or something similar. At a minimum, the program should ingest, analyze, and display data. Any needed data cleaning should be clearly documented and repeatable.')

      centered_header('Features ( atleast one from each )')
      centered_header('Loading data:')
      st.checkbox('Read TWO data files (JSON, CSV, Excel, etc.).')
      st.checkbox('Read in TWO text data sources (in any format). For example, email chains or different pages from a book')
      st.checkbox('Read TWO data sets in with an API (or use two different APIs that have data you can combine to answer new questions).')
      st.checkbox('Scrape TWO pieces of data from anywhere on the internet and utilize it in your project.')
      st.checkbox('Set up a local database and read data in with SQLite or SQLAlchemy')

      centered_header('Clean and operate on the data while combining them :')
      st.checkbox('Clean your data and perform a pandas merge with your two data sets, then calculate some new values based on the new data set.')
      st.checkbox('Clean your data and perform a SQL join with your data sets using either plain sql or the pandasql Python library.')
      st.checkbox("If you’re using text data, get some information from your separate documents and summarize them in a DataFrame. This isn’t literally a join but accomplishes a similar idea. For example, getting the most frequent word distributions from both documents and then summarizing them in a table. ")

      centered_header('Visualize / present your data:')
      st.checkbox('Make 3 matplotlib or seaborn (or another plotting library) visualizations to display your data.')
      st.checkbox('Make a Tableau dashboard to display your data')
      st.checkbox('Make at least 1 Pandas pivot table and 1 matplotlib/seaborn plot. Pivot tables are a way to summarize your data and present it easily in a way that isn’t just a graph. They can be useful when combined with graphs.')
      st.checkbox('Make a visualization with Bokeh. You can create interactive online visualizations with this, but it is more involved than the other plotting libraries! Very cool though.')

      centered_header('Best Practices:')
      st.checkbox('Utilize a virtual environment and include instructions in your README on how the user should set one up')
      st.checkbox('Write 3 unit tests and include instructions on how the user can run them. This will mostly only apply if you’re building custom functions and classes.')
      st.checkbox('Build a custom data dictionary and include it either in your README or as a separate document. This will only apply if your data set does not already have a data dictionary or if you’re building a custom data set. For an example, see the resources to the right.')
      st.checkbox('Any other “best practices” your mentor can think of: this is open to interpretation, but if your mentor has a particular idea for a best practice about your specific project, that will meet the requirement for this table.')

      centered_header('Interpretation of your data:')
      st.checkbox('Annotate your code with markdown cells in Jupyter Notebook, write clear code comments, and have a well-written README.md. Tidy up your notebook, and make sure you don’t have any empty cells or incomplete cells that don’t do anything. Make sure it’s all functional before your final github commit.')
      st.checkbox('Annotate your .py files with well-written comments and a clear README.md (only applicable if you’re not using a jupyter notebook).')


if __name__ == '__main__':
    main()