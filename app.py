import pandas as pd
import streamlit as st
from PIL import Image

st.title('Информация по заказам еды с онлайн сервиса')
df = pd.read_csv('onlinefoods.csv')

# Displaying an image
image = Image.open('dataset-cover.png')
st.image(image)

# Slider to chose age
#show_age = st.sidebar.checkbox("Указать возраст клиентов")
show_age = st.checkbox("Указать возраст клиентов")
if show_age == True:

    min_age = min(df['Age'])
    max_age = max(df['Age'])
    age = st.slider("Выберите возраст",
                                                min_value=min_age,
                                                max_value=max_age,
                                                value=(min_age,max_age)
                                                )

    df = df[(df['Age']>= age[0]) & (df['Age'] <= age[1])]

show_gender = st.checkbox("Указать пол клиентов")
if show_gender == True:
    gender = st.multiselect(
        'Выберите пол',
        df['Gender'].unique()
    )
    df = df[df['Gender'].isin(gender)]

if st.button('Получить данные'):
    st.success('Данные по вашему запросу')
    st.dataframe(df)