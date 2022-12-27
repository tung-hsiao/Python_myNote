# Kubernetes

```
# 創建 pod
# 若restart=Always 則是deployment
# --dry-run=client 拿掉一些default參數，通常在output yaml時使用
# 若直接創建 pod (不輸出yaml) 就不需要加此參數
kubectl run <pod-name> --image=<image> --restart=Never --dry-run=client -o yaml > pod-def.yaml

kubectl apply -f

kubectl create
```

```
# 新增 Pod label
kubectl label pod <pod-name> <key>=<value>

# 刪除 Pod label
kubectl label pod <pod-name> <key>-

# 查看 Pod label
kubectl get pod --show-labels

# 查看特定 label 的 pod
kubectl get pod --selector <key>=<value>

# 新增 Node label
kubectl label nodes <node-name> <key>=<value>

# 刪除 Node label
kubectl label nodes <node-name> <key>=<value>-
```

```
# 對 Pod 內部下 command
kubectl exec <pod-name> -- <command>
```

```
# 創建 Service
kubectl expose pod 
```

```
# 創建 namespace
kubectl create ns <namespace-name>
kubectl apply -f xxx.yaml -n <namespace-name>
```

