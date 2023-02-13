
# Linux command
```
shutdown -h now     立即關機 
reboot

sudo su                切換成root帳號
su OTHER_ACCOUNT    切換成其他帳號



swapoff -a          #關閉swap (記憶體置換)


# 把命令放到背景執行
CMD &    (add a '&' in the end)

# 查詢現行的背景工作可使用
jobs -l

# 把工作帶回前景
fg [PID]

```


# Vim
```
i：插入模式，可以輸入字串文字內容
:：底線命令模式，可以在最底一行輸入操作指令
v：切換到視覺模式，可以使用選擇文字，方便閱讀和強調

鍵盤輸入 Esc 會回到命令模式
```
```
:q：不儲存直接離開
:q!：不儲存，強制直接離開
:w：儲存文檔但不離開
:wq：儲存並離開
:!wq：強制儲存並離開
```

