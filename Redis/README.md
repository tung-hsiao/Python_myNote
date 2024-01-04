# Redis
## 安裝 Redis 資料庫
```
sudo apt update
sudo apt install redis-server    # 安裝 Redis server
```
透過vim開啟 /etc/redis/redis.conf 設定檔，(透過/)搜尋supervised，將 supervised 參數設定為 systemd，讓 Redis 資料庫伺服器可以與 Ubuntu Linux 的 systemd 溝通
```
supervised systemd
```
如此即完成 Redis 資料庫伺服器的安裝，接著可查看 Redis 資料庫服務的狀態
```
systemctl status redis.service
```
