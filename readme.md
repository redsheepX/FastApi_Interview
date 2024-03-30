- # 使用方式

  僅須執行 start_server.py 即可

---

- # 個人化設定

  設定位置:setting 資料夾中的 setup.py

  可以調整啟動所需的 ip 與 port 號、或是 log 設定等功能。

---

- # API 測試

進行 api 相關測試可以使用以下方法進行:

1.  若已開啟 server，可以於首頁 _[點我](/docs#)_ 將引導至 FastAPI 內建測試頁

2.  若未開啟 server，可以使用 postman 進行測試。

---

- # 單元測試

  於 user_info/tests 中的 test_user_info 中有相關的測試案例，可以使用指令 pytest [测试文件] -s –q 執行

  若有安裝 allure 還可以產生好看的 allure 報告 [官方安裝教學](https://github.com/allure-framework/allure2?tab=readme-ov-file)
