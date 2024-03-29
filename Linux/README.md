
# Linux command
```
shutdown -h now     立即關機 
reboot

sudo su                切換成root帳號
su OTHER_ACCOUNT    切換成其他帳號

swapoff -a          #關閉swap (記憶體置換)

# tmux
tmux ls              # list all Sessions
tmux attach -t 0     # attach to [session#]

Ctrl+b 再輸入 d	detach current session，exit tmux environment。
Ctrl+b 再輸入 s	select session with UI

tmux list-session
tmux kill-session -t

# 把命令放到背景執行
CMD &    (add a '&' in the end)

# 查詢現行的背景工作可使用
jobs -l

# 把工作帶回前景
fg [PID]

# 將該資料夾下所有檔案之權限改成777
sudo chmod 777 -R .

# How to download a file from server using SSH?
scp username@remotehost.ip:file.txt /local/dir

```

# Network
```
# 顯示網路介面的現行配置
ifconfig

# IP routing table
route
```

# 即時監控網路流量
```
sudo apt install iftop
sudo iftop
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

# ssh
在linux環境中，開啟terminal，type以下指令。安裝完成後，服務默認開啟。
```
sudo apt-get install openssh-server
```



