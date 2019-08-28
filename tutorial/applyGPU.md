# 申請一顆Google GPU

## 在配額頁面申請

1. 進入[VM執行個體](https://console.cloud.google.com/compute/instances)頁面 已啟用虛擬機
![](https://i.imgur.com/hhAEaLh.png)
2. 進入[配額頁面](https://console.cloud.google.com/iam-admin/quotas) 點選`升級帳戶` 已啟用申請GPU功能 如果對升級帳戶有疑慮可以點選[此連結](https://github.com/superj80820/cloud-gaming/blob/master/tutorial/applyGPU.md#%E4%BD%A0%E5%8F%AF%E8%83%BD%E6%9C%83%E6%9C%89%E7%9A%84%E7%96%91%E5%95%8F)
![](https://i.imgur.com/0T7v0Cr.png)
![](https://i.imgur.com/pkndHiF.png)
3. 重新整理 點選下拉`指標`>選擇`無`取消所有指標
![](https://i.imgur.com/kenXrho.png)
4. 輸入`GPU`>選擇`GPUs(all regions)`
![](https://i.imgur.com/z3aHZYY.png)
5. 對`Compute Engine API`打勾>點選`編輯配額`>在右方頁面分別輸入名稱\email\電話號碼
![](https://i.imgur.com/7qmLwFI.png)
6. 新增配額限制填寫`1`>要求說明填寫`Need to training code` 或者你想要說的其他理由>點選`完成`>點選`提交要求`
![](https://i.imgur.com/NRywiAu.png)
7. 幾分鐘後 就會收到Google寄過來的審核信
![](https://i.imgur.com/G9LFquO.png)
8. 通才在兩三天內 就會獲得GPU審核通過的通知信 我是一天內收到
![](https://i.imgur.com/uelFmkK.png)
![](https://i.imgur.com/FGVNxdN.png)

## 你可能會有的疑問

1. 升級**付費帳戶**會需要錢嗎?

    依照Google對升級付費帳戶的[說明頁面](https://cloud.google.com/free/docs/gcp-free-tier?hl=zh_TW&_ga=2.217959766.-1906969446.1566836275#how-to-upgrade) 升級成付費帳戶可以保留300塊美金在你的帳戶中 也就是說升級之後以樣可以使用免費額度 **但是**

    > 在超過300塊免費額度後會自動向您收費

    所以您必須留意這點