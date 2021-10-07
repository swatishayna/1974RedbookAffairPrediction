import streamlit as st
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()






occ_woman = st.radio('Occupation of Lady',  ('farming/semi-skilled/unskilled', '"white collar', 'teacher/nurse/writer/technician/skilled', 'managerial/business','professional with advanced degree','others'))
occ_man   = st.radio('Occupation of Man',  ('farming/semi-skilled/unskilled', '"white collar', 'teacher/nurse/writer/technician/skilled', 'managerial/business','professional with advanced degree','others'))
rate_marriage = st.radio('Rating Input of Marriage Life', ('VeryPoor','Poor','Good','VeryGood','Excellent'))
age = st.slider('Age of lady', min_value = 17, max_value=42)
yrs_married = st.slider('Number of Married Years', min_value = 0, max_value=23)
children = st.number_input('ChildrenCount', min_value =0, max_value =5)
religious = st.radio('Are You religious?',('Not at all', 'Yes but not much', 'Yes', 'Highly Religious'))
educ= st.radio('level of education', ('grade school','high school', 'some college', 'college graduate','some graduate school','advanced degree'))

print(occ_woman,occ_man,rate_marriage,age,yrs_married,children,religious,educ)