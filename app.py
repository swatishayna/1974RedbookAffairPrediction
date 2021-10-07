import streamlit as st
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()



input_required =['occ_2', 'occ_3', 'occ_4', 'occ_5', 'occ_6', 'occ_husb_2', 'occ_husb_3',
       'occ_husb_4', 'occ_husb_5', 'occ_husb_6', 'rate_marriage', 'age',
       'yrs_married', 'children', 'religious', 'educ']


occ_woman = st.radio('Occupation of Lady',  ('farming/semi-skilled/unskilled', '"white collar', 'teacher/nurse/writer/technician/skilled', 'managerial/business','professional with advanced degree','others'))
occ_man   = st.radio('Occupation of Man',  ('farming/semi-skilled/unskilled', '"white collar', 'teacher/nurse/writer/technician/skilled', 'managerial/business','professional with advanced degree','others'))

