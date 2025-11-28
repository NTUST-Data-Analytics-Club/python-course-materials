# SpendSense

## 介紹

SpendSense 是一個生活消費 Dashboard，可以幫助你分析你的生活消費情況，並提供視覺化圖表。

## 使用方式

1. 上傳一個包含 `date, category, item, amount` 欄位的 CSV 檔案
2. 查看原始資料
3. 選擇一個類別或日期，查看明細
4. 查看類別花費長條圖
5. 查看日期花費折線圖

範例檔案：[sample_expenses.csv](https://github.com/darri/python-course-materials/blob/main/Project-SpendSense/data/sample_expenses.csv)

## 使用技術

- Streamlit：用於建立生活消費 Dashboard
- Pandas：用於處理 CSV 檔案
- Plotly：用於繪製視覺化圖表

## 安裝

```bash
pip install -r requirements.txt
```

## 執行

```bash
streamlit run src/app.py
```

## 備註

- **建議使用 VSCode 開啟此專案**
- **建議使用 Python 3.12 或 3.13 版本**
- **建議使用虛擬環境，啟動之後並安裝 requirements.txt 中的套件**

#### 虛擬環境使用方式 (Mac/Linux)
- 建立虛擬環境
```bash
python -m venv .venv

# 建立虛擬環境 (Windows建議不要用 "."作為虛擬環境名稱開頭，避免路徑問題)
python -m venv venv
```
- 啟動虛擬環境
```bash
# 啟動虛擬環境 (Mac/Linux)
source .venv/bin/activate

# 啟動虛擬環境 (Windows)
venv/Scripts/activate.bat
```
- 安裝 requirements.txt 中的套件
```bash
pip install -r requirements.txt
```
- 執行 Streamlit 應用程式
```bash
# 執行 Streamlit 應用程式 (Mac/Linux)
.venv/bin/streamlit run src/app.py

# 執行 Streamlit 應用程式 (Windows)
venv/Scripts/streamlit run src/app.py
```
- 退出虛擬環境
```bash
# 退出虛擬環境 (Mac/Linux)
deactivate

# 退出虛擬環境 (Windows)
venv/Scripts/deactivate.bat
```