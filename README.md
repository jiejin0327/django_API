# 人臉識別和明星臉偵測Web應用程式

這是一個使用django撰寫API，可以辨識人臉和明星臉偵測等功能

## 使用技術

- Python 3.8
- Django 3.2
- face_recognition 1.3.0
- pypinyin 0.42.0

## 使用方法

- 下載或克隆本專案到本地端
- 安裝所需套件
- 執行django伺服器
- 透過以下URL呼叫API：
  - /training/<str:UserId>/<path:ImgPath>
  - /recognition/<path:ImgPath>
  - /DetectStar/<path:ImgPath>

## 功能與特色

- 訓練：將使用者提供的UserId和ImgPath作為參數，將圖片中的人臉特徵存入資料庫。
- 識別：將使用者提供的ImgPath作為參數，比對資料庫中的人臉特徵，返回最相似的UserId。
- 明星臉偵測：將使用者提供的ImgPath作為參數，比對明星資料庫中的人臉特徵，返回最相似的明星名字。
- 使用OpenCV和face_recognition等技術進行人臉辨識和偵測
- 支援中文輸入
