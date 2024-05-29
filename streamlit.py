import streamlit as st

#Streamlitinterface
st.title('Bank Client Term Deposit Subscription Predict')

# Input fields
age = st.number_input('Age', min_value=18, max_value=95, step=1)
job = st.number_input('job', min_value=1, max_value=12)
marital = st.number_input('marital', min_value=1, max_value=3)
education = st.number_input('education', min_value=0, max_value=3)
default = st.number_input('default', min_value=1, max_value=2)
balance = st.number_input('balance (in $)', min_value=-8000, max_value=105000)
housing = st.number_input('housing', min_value=1, max_value=2)
loan = st.number_input('loan', min_value=1, max_value=2)
contact = st.number_input('contact', min_value=1, max_value=3)
day = st.number_input('day', min_value=1, max_value=31)
month = st.number_input('month', min_value=1, max_value=12)
duration = st.number_input('duration', min_value=0, max_value=4918)
campaign = st.number_input('campaign', min_value=1, max_value=63)
pdays = st.number_input('pdays', min_value=-1, max_value=63)
previous = st.number_input('previous', min_value=0, max_value=275)
poutcome = st.number_input('poutcome', min_value=0, max_value=3)

features = [age, job, marital, education, default, balance, housing, loan, contact, day, month, duration, campaign,
            pdays, previous, poutcome]

if st.button('Calculate Deposit Subscription Predict'):
    # adicionar o modelo aqui
    predicted_subscription = 1  # Trocar pro modelo

    if predicted_subscription == 1:
        st.success('The customer is likely to subscribe to a term deposit.')
    else:
        st.error('The customer is not likely to subscribe to a term deposit.')
