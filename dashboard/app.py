import streamlit as st
import redis
import json
import pandas as pd
import time

st.set_page_config(layout="wide")
st.title("Siber Saldiri Paneli")

r = redis.Redis(host='redis_db', port=6379, db=0, decode_responses=True)
placeholder = st.empty()

while True:
    with placeholder.container():
        attacks = r.lrange('attacks', 0, 99)
        
        if attacks:
            data = [json.loads(a) for a in attacks]
            df = pd.read_json(json.dumps(data))
            st.dataframe(df, use_container_width=True)
        else:
            st.write("Sistem temiz, saldiri bekleniyor...")
            
        time.sleep(2)