# Embeded_System_HW1

## (1) how to setup and run your program

### 1. Declaring and processing data

首先是將 csv 檔讀進來，存到 "data" 這個 list 中，再來我把作業指定要算 summation 的五個 ID 存到 "ID" 這個 list 中，並將他 sort 好，存到 "ID_sorted" 中，確保在 print 結果時是依照 lexicographical order，如下圖：

![](https://i.imgur.com/DpagbvX.png)

再來作業中要求我們做的事是把 "HUMD" 這欄的值為 "-99.000" 或 "-999.000" 的那一欄刪掉，我是反過來把 valid 的 data 放入 "new_data" 這個新的 list 中，並利用下面那個迴圈檢查 "new_data" 中是否還存在著 invalid data。

![](https://i.imgur.com/snKPBLA.png)

### 2. Calculate summation, append and print data

在這裡我依照 ID 的 lexicographical order 的順序（ID_sorted）去計算各個 station 的 "HUMD" summation value，並將資料 append 到 "result_list" 中，最後將結果 print 出來。

![](https://i.imgur.com/3mlUfUV.png)

---

## (2) what are the results

![](https://i.imgur.com/G2YEzV4.png)
