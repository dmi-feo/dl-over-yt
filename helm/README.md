The way to success:
```
helm upgrade --install ingress-nginx ingress-nginx \
  --repo https://kubernetes.github.io/ingress-nginx \
  --namespace ingress-nginx --create-namespace
  
helm upgrade --install \
 --set yt_settings.host=<YTHOST> \
 --set yt_settings.root_collection_node_id=<NODE_ID> \
 --namespace dl-over-yt --create-namespace \
 dl-over-yt ./dl-over-yt

```