# Engage-Final-Project
Reproducing this web app
To recreate this web app on your system, do the following.

Create conda environment
Firstly, we will create a conda environment called eda

conda create -n eda python=3.7.9
Secondly, we will login to the eda environment

conda activate eda
Install prerequisite libraries

Download requirements.txt file

wget https://raw.githubusercontent.com/dataprofessor/eda-app/main/requirements.txt

Pip install libraries

pip install -r requirements.txt
Download and unzip contents from GitHub repo
Download and unzip contents from https://github.com/dataprofessor/eda-app/archive/main.zip

Launch the app
streamlit run app.py
