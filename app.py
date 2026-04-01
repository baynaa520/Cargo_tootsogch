import streamlit as st
import backend as be
import pandas as pd
import json
import requests
from datetime import datetime, timedelta

st.header("Hello")

st.subheader("Sub_header_shu")

st.write("Baynaa")

st.divider()

name = st.text_input("Ner")

st.write("Tanii ner:" , name)

nas = st.number_input("Tanii_nas")

st.write("Ta heden nastai we?" ,nas)

pwd = st.text_input("password" , type = "password")

Color = st.selectbox("Ungu songoh" , ["Tsagaan", "Har" , "Ulaan"])

Colors = st.multiselect("Ungu songoh" , ["Tsagaan", "Har" , "Ulaan"])

st.divider()


import streamlit as st
import backend as be # backend хавтас доторх __init__.py-г дуудаж байна


st.divider()

# --- 2. Алтны ханш хэсэг ---
st.header("📈 Алтны ханш хайх")

col_s, col_e = st.columns(2)
with col_s:
    start_date = st.selectbox("Эхлэх огноо", ["2026-03-01", "2026-01-01"])
with col_e:
    end_date = st.selectbox("Дуусах огноо", ["2026-03-15", "2026-03-30"])

if st.button("Ханш хайх"):
    with st.spinner("Мэдээллийг татаж байна..."):
        result = be.currency_data(start_date, end_date)
        
        # Хэрэв ирсэн дата нь DataFrame бол (амжилттай)
        import pandas as pd
        if isinstance(result, pd.DataFrame):
            st.success("✅ Мэдээллийг амжилттай татлаа!")
            
            # Статистик харуулах
            m1, m2, m3 = st.columns(3)
            m1.metric("Дундаж", f"{result['GOLD_BUY'].mean():,.2f} ₮")
            m2.metric("Хамгийн их", f"{result['GOLD_BUY'].max():,.0f} ₮")
            m3.metric("Хамгийн бага", f"{result['GOLD_BUY'].min():,.0f} ₮")
            
            # Хүснэгт харуулах
            st.dataframe(result, use_container_width=True)
        else:
            # Хэрэв алдааны мессеж (String) ирсэн бол
            st.error(result)


st.divider()
st.header("📈excel filr tsewerlegee ")

files = st.file_uploader("file-aan oruulna uu", type = ["xlsx",'xls'] , accept_multiple_files = True)

for file in files:
    st.dataframe(be. dp_as.xls(file))




st.header("📦 Карго тооцоолуур")

# 1. Хэмжээний нэгж сонгох (см эсвэл метр)
unit_size = st.radio("Хэмжээний нэгж:", ("см", "метр"), horizontal=True, key="size")

# 2. Жингийн нэгж сонгох (кг эсвэл грамм)
unit_weight = st.radio("Жингийн нэгж:", ("кг", "грамм"), horizontal=True, key="weight")

col1, col2, col3, col4 = st.columns(4)

with col1:
    h = st.number_input(f"Өндөр ({unit_size})", value=10.0)
with col2:
    d = st.number_input(f"Гүн ({unit_size})", value=10.0)
with col3:
    l = st.number_input(f"Урт ({unit_size})", value=10.0)
with col4:
    w = st.number_input(f"Жин ({unit_weight})", value=1.0)

# --- ХӨРВҮҮЛЭХ ЛОГИК ---

# Хэмжээг см рүү хөрвүүлэх
if unit_size == "метр":
    h_cm, d_cm, l_cm = h * 100, d * 100, l * 100
else:
    h_cm, d_cm, l_cm = h, d, l

# Жинг кг рүү хөрвүүлэх
if unit_weight == "грамм":
    w_kg = w / 1000
else:
    w_kg = w

# --- БОДОХ ХЭСЭГ ---
if st.button("Карго бодох"):
    # Backend-рүүгээ СМ болон КГ-аар хөрвүүлсэн утгаа явуулна
    price = be.cargo_price_calculator(h_cm, d_cm, l_cm, w_kg)
    st.success(f"Таны каргоны үнэ: {price:,.0f} ₮")
    st.info(f"Тооцоолсон жин: {w_kg} кг") # Хэрэглэгчид баталгаажуулж харуулбал гоё

    