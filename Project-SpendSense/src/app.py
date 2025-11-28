import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="SpendSense - 生活消費 Dashboard", layout="wide")

st.header("💸 SpendSense - 生活消費 Dashboard", divider="rainbow")
st.markdown("請上傳一個包含 `date, category, item, amount` 欄位的 CSV，讓我幫你分析吧！\n")

# 檔案上傳區
uploaded_file = st.file_uploader("範例檔案：[sample_expenses.csv](https://github.com/darri/python-course-materials/blob/main/Project-SpendSense/data/sample_expenses.csv)", type=["csv"])

# 如果沒有上傳，就提醒使用者
if uploaded_file is None:
    st.info("還沒有上傳檔案，請先上傳 sample_expenses.csv 試試看")
else:
    # 讀取資料
    df = pd.read_csv(uploaded_file)

    # 基本檢查
    required_cols = {"date", "category", "item", "amount"}
    if not required_cols.issubset(df.columns):
        st.error(f"CSV 欄位需要至少包含：{required_cols}")
    else:
        st.success("成功讀取資料！")

        # 總花費（根據類別）
        category_summary = df.groupby(by="category", as_index=False)["amount"].sum()
        category_summary = category_summary.sort_values(by="amount", ascending=False)

        # 總花費（根據日期）
        date_summary = df.groupby(by="date", as_index=False)["amount"].sum()
        date_summary = date_summary.sort_values(by="date", ascending=False)

        # 左右兩欄排版
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("📄 原始資料")
            n = st.number_input("查看前幾筆資料：", value=10, min_value=1, max_value=len(df), step=1, key="n")
            if n > 0:
                st.dataframe(df.head(n=st.session_state.n), use_container_width=True)

        with col2:

            # 互動：選擇一個類別，顯示明細
            st.subheader("🔎 查看明細")

            # 左右兩欄排版 (for 下拉選單 - 選擇類別和日期)
            sub_col1, sub_col2 = st.columns(2)
            with sub_col1:
                category_options = df["category"].unique().tolist()
                category_options.insert(0, "所有類別")
                selected_cat = st.selectbox("選擇一個類別：", category_options)
            with sub_col2:
                date_options = df["date"].unique().tolist()
                date_options.insert(0, "所有日期")
                selected_date = st.selectbox("選擇一個日期：", date_options)
            
            # 過濾資料
            if selected_cat != "所有類別" and selected_date != "所有日期":
                filtered = df[(df["date"] == selected_date) & (df["category"] == selected_cat)]
            elif selected_cat != "所有類別":
                filtered = df[df["category"] == selected_cat]
            elif selected_date != "所有日期":
                filtered = df[df["date"] == selected_date]
            else:
                filtered = df

            st.write(f"共 {len(filtered)} 筆消費，總金額：{filtered['amount'].sum()} 元")
            st.dataframe(filtered, use_container_width=True)

        st.subheader("📊 類別花費長條圖")
        st.bar_chart(category_summary.set_index("category")["amount"],
                     sort=False,
                     horizontal=True)
        st.subheader("📊 日期花費長條圖")
        fig = px.line(date_summary, x="date", y="amount",
                     labels={"date": "日期", "amount": "金額"})
        fig.update_xaxes(tickangle=0)  # 調整 x 軸標籤角度為 -45 度（可改為 0, 45, -45 等）
        st.plotly_chart(fig, use_container_width=True)
