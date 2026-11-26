import streamlit as st

st.set_page_config(
    page_title="Myanmar Speech-to-Text",
    page_icon="🎙️",
    layout="wide",
)

# Custom CSS for clean header & spacing
st.markdown(
    """
    <style>
        .main-header {
            background: linear-gradient(90deg, #1E3A8A 0%, #2563EB 100%);
            padding: 1.5rem;
            border-radius: 12px;
            color: white;
            margin-bottom: 1.5rem;
        }
        .main-header h1 {
            color: white !important;
            margin: 0;
            font-size: 1.8rem;
        }
        .main-header p {
            color: #DBEAFE;
            margin: 0.4rem 0 0 0;
        }
    </style>
    <div class="main-header">
        <h1>🎙️ Myanmar Speech-to-Text</h1>
        <p>မြန်မာအသံကို စာသားအဖြစ် လွယ်ကူမြန်ဆန်စွာ ပြောင်းလဲခြင်း</p>
    </div>
""",
    unsafe_allow_html=True,
)

with st.sidebar:
  st.header("ℹ️ အချက်အလက်")
  st.info("WAV, MP3, M4A, OGG ဖိုင်များကို Upload တင်နိုင်သလို တိုက်ရိုက်လည်း အသံသွင်းနိုင်ပါတယ်။")
  st.caption("Output: Myanmar Unicode")

col1, col2 = st.columns(2, gap="large")

with col1:
  with st.container(border=True):
    st.subheader("🎤 1. တိုက်ရိုက်အသံသွင်းရန်")
    st.write("မိုက်ခရိုဖုန်းမှတစ်ဆင့် စကားပြောပြီး စာသားပြောင်းပါ။")

with col2:
  with st.container(border=True):
    st.subheader("📁 2. Audio File တင်ရန်")
    st.write("ကွန်ပျူတာ (သို့) ဖုန်းထဲရှိ ဖိုင်ကို ရွေးချယ်တင်ပါ။")
