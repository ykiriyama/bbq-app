import streamlit as st
from datetime import datetime, time
import time as time_mod

st.set_page_config(page_title="BBQ App", layout="centered")

# 言語辞書
texts = {
    "ja": {
        "title": "🍖 BBQ シェフ派遣サービス",
        "desc": "以下の質問に答えると、サービス料金を自動で見積もります。",
        "people": "1️⃣ 当日は何名様の予定ですか？",
        "shopping": "2️⃣ ショッピング〜お届けサービスをご希望ですか？",
        "shopping_options": ["希望しない（シェフ派遣のみ）", "シェフ派遣＋食材のみのショッピング〜お届け", "シェフ派遣＋（食材＋ドリンク）のショッピング〜お届け"],
        "result": "📄 お見積もり結果",
        "total": "合計金額：",
        "note": "（※食材費は含まれていません）",
        "form_title": "✅ 予約をご希望の方はこちらから",
        "form_link": "📋 Googleフォームで予約する",
        "currency": "SGD"
    },
    "en": {
        "title": "🍖 BBQ Chef Hire Service",
        "desc": "Answer the following questions to get an instant service quote.",
        "people": "1️⃣ How many people will you be serving?",
        "shopping": "2️⃣ Do you want shopping & delivery service?",
        "shopping_options": ["No (Chef hire only)", "chef hire + shopping and deliver food only", "chef hire + shopping and delivery(Food + Drinks)"],
        "result": "📄 Estimate Result",
        "total": "Total Amount:",
        "note": "(Food cost not included)",
        "form_title": "✅ Click below to proceed with reservation",
        "form_link": "📋 Reserve via Google Form",
        "currency": "SGD"
    }
}

lang = st.radio("🌐 Select Language / 言語を選んでください", ["日本語", "English"])
lang_key = "ja" if lang == "日本語" else "en"
t = texts[lang_key]

st.title(t["title"])
st.write(t["desc"])

people = st.number_input(t["people"], min_value=1, step=1)
option = st.radio(t["shopping"], t["shopping_options"])

if people < 10:
    chef_fee = 200
    shopping_fee = {
        t["shopping_options"][0]: 0,
        t["shopping_options"][1]: 50,
        t["shopping_options"][2]: 100
    }
else:
    chef_fee = 300
    shopping_fee = {
        t["shopping_options"][0]: 0,
        t["shopping_options"][1]: 100,
        t["shopping_options"][2]: 200
    }

total = chef_fee + shopping_fee[option]

if people > 0:
    st.markdown("---")
    st.subheader(t["result"])

    with st.spinner("計算中..."):
        time_mod.sleep(0.7)
        st.markdown(
            f"""
            <div style="background-color:#f0f8ff;padding:20px;border-radius:12px;border:2px solid #00aaff">
                <h2 style="color:#00aaff;margin-top:10px;">💰 {t['total']} <span style=\"color:#000;\">{total} {t['currency']}</span></h2>
                <p style="margin-top:10px;font-size:13px;color:#777;">{t['note']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(f"### {t['form_title']}")
    st.markdown(
        f"[{t['form_link']}](https://docs.google.com/forms/d/e/1FAIpQLSejyTYZKzsIrtO5as3DVHTMVEGWRVfAj-fcbi2ONhq9Oan0dg/viewform?usp=header)",
        unsafe_allow_html=True
    )