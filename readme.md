- # 使用前置

  需安裝套件皆於 requirement.txt 中 可使用指令 `pip install -r requirements.txt` 安裝

- # 使用方式

  僅須執行 start_server.py 即可

  若要用 commend line 執行可以使用 uvicorn FastApi.user_management:app --reload

---

- # 個人化設定

  設定位置:setting 資料夾中的 setup.py

  可以調整啟動所需的 ip 與 port 號、或是 log 設定等功能。

---

- # API 測試

進行 api 相關測試可以使用以下方法進行:

1.  若已開啟 server，可以於首頁 _[點我](/docs#)_ 將引導至 FastAPI 內建測試頁，裡面也有詳細介紹

2.  若不使用 fastapi 內建測試頁，也可以使用 postman 進行測試。

---

- # 單元測試

  於 user_info/tests 中的 test_user_info 中有相關的測試案例，可以使用指令 pytest [测试文件] -s –q 執行

  若有安裝 allure 還可以產生好看的 allure 報告 [官方安裝教學](https://github.com/allure-framework/allure2?tab=readme-ov-file)

  安裝完後可以至 allure-report 中的 complete.html 查看測試結果

  若未安裝也可以正常執行 pytest 並查看 pytest 結果
