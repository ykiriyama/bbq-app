import streamlit as st

st.set_page_config(page_title="Zero Fuss BBQ", layout="centered")

# スマホ対応CSS追加
st.markdown("""
<style>
    @media screen and (max-width: 768px) {
        h1 {
            font-size: 7vw !important;
        }
        p {
            font-size: 4vw !important;
        }
        h2 {
            font-size: 5vw !important;
        }
        h3 {
            font-size: 4vw !important;
        }
        div[data-testid="stNumberInput"] input {
            font-size: 16px !important;
        }
        div[data-testid="stRadio"] label {
            font-size: 16px !important;
        }
    }
</style>
""", unsafe_allow_html=True)

# 言語選択（サイドバーに移動）
with st.sidebar:
    lang = st.radio("🌐 言語を選んでください / Select language", ["日本語", "English"])
lang_key = "ja" if lang == "日本語" else "en"

# テキスト辞書
t_texts = {
    "ja": {
        "title": "楽々BBQ!",
        "desc": "以下の質問に答えると、サービス料金を自動で見積もります。",
        "people": "1️⃣ 当日は何名様の予定ですか？",
        "shopping": "2️⃣ ショッピング〜お届けサービスをご希望ですか？",
        "shopping_options": ["希望しない（シェフ派遣のみ）", "シェフ派遣＋食材のみのショッピング〜お届け", "シェフ派遣＋（食材＋ドリンク）のショッピング〜お届け"],
        "result": "📄 お見積もり結果",
        "total": "合計金額",
        "note": "（※食材費は含まれていません）",
        "form_title": "✅ 予約をご希望の方はこちらから",
        "form_link": "📋 Googleフォームで予約する",
        "currency": "SGD"
    },
    "en": {
        "title": "Zero Fuss BBQ!",
        "desc": "Answer the following questions to get an instant service quote.",
        "people": "1️⃣ How many people will you be serving?",
        "shopping": "2️⃣ Do you want shopping & delivery service?",
        "shopping_options": ["No (Chef hire only)", "chef hire + shopping and deliver food only", "chef hire + shopping and delivery (Food + Drinks)"],
        "result": "📄 Estimate Result",
        "total": "Total Amount",
        "note": "(Food cost not included)",
        "form_title": "✅ Click below to proceed with reservation",
        "form_link": "📋 Reserve via Google Form",
        "currency": "SGD"
    }
}
t = t_texts[lang_key]

# タイトルと説明文
st.markdown(f"""
<div style='background-color:#cc0000;padding:20px;border-radius:10px;text-align:center;'>
    <h1 style='color:white;font-size:48px;font-weight:bold;margin-bottom:10px;'>{t['title']}</h1>
    <p style='color:#fff;font-size:18px;margin:0;'>{t['desc']}</p>
</div>
""", unsafe_allow_html=True)

# 入力セクション
people = st.number_input(t["people"], min_value=1, step=1)
option = st.radio(t["shopping"], t["shopping_options"])

# 金額計算
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

# 見積もり結果表示
st.markdown("""
<div style='background-color:#000;padding:25px;margin-top:20px;border-radius:12px;'>
    <h2 style='color:#ffffff;text-align:center;margin-bottom:15px;'>📄 {}</h2>
    <div style='background-color:#cc0000;color:#ffffff;padding:25px;border-radius:12px;text-align:center;'>
        <h3 style='margin:0;font-size:20px;'>💰 {}</h3>
        <div style='font-size:36px;font-weight:bold;margin:5px 0;'>{} {}</div>
        <p style='font-size:13px;color:#ffeeee;'>{}</p>
    </div>
</div>
""".format(t["result"], t["total"], total, t['currency'], t['note']), unsafe_allow_html=True)

# フォームリンク表示
st.markdown(f"""
<div style='text-align:center;margin-top:30px;'>
    <h3>{t['form_title']}</h3>
    <a href="https://docs.google.com/forms/d/e/1FAIpQLSejyTYZKzsIrtO5as3DVHTMVEGWRVfAj-fcbi2ONhq9Oan0dg/viewform?usp=header" 
       target="_blank" 
       style="font-size:18px;color:#cc0000;font-weight:bold;">
        {t['form_link']}
    </a>
</div>
""", unsafe_allow_html=True)