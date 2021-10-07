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

predict =  st.button('Predict')

print(occ_woman,occ_man,rate_marriage,age,yrs_married,children,religious,educ)

d_occupation_women = {
    'occ_2' : 0,
    'occ_3' : 0, 
    'occ_4' : 0, 
    'occ_5' : 0, 
    'occ_6' : 0
}
d_occupation_man = {
    'occ_husb_2' : 0,
    'occ_husb_3' : 0, 
    'occ_husb_4' : 0, 
    'occ_husb_5' : 0, 
    'occ_husb_6' : 0
}


if predict:
    if occ_woman == 'farming/semi-skilled/unskilled':
        d_occupation_women['occ_2'] = 1
    elif occ_woman == 'white collar':
        d_occupation_women['occ_3'] = 1
    elif occ_woman == 'teacher/nurse/writer/technician/skilled':
        d_occupation_women['occ_4'] = 1
    elif occ_woman == 'managerial/business':
        d_occupation_women['occ_5'] = 1
    elif occ_woman == 'professional with advanced degree':
        d_occupation_women['occ_6'] = 1
   
    if occ_man == 'farming/semi-skilled/unskilled':
        d_occupation_man['occ_husb_2'] = 1
    elif occ_man == 'white collar':
        d_occupation_man['occ_husb_3'] = 1
    elif occ_man == 'teacher/nurse/writer/technician/skilled':
        d_occupation_man['occ_husb_4'] = 1
    elif occ_man == 'managerial/business':
        d_occupation_man['occ_husb_5'] = 1
    elif occ_man == 'professional with advanced degree':
        d_occupation_man['occ_husb_6'] = 1
    
    inputs =[]
    inputs.append(d_occupation_women.values())
    inputs.append(d_occupation_man.values())
    inputs.append(rate_marriage)
    inputs.append(age)
    inputs.append(yrs_married)
    inputs.append(children)
    inputs.append(religious)
    inputs.append(educ)
    
    st.write(inputs)
