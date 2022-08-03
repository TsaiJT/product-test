# Table schema
* Each attribute is not nullable

![image](https://user-images.githubusercontent.com/15087421/182535663-ab361591-5d54-4356-89a2-948733b89b23.png)


# ENV
ENV: linux-base env
localhost package: docker, docker-compose


# start service
1. `$mkdir -p /opt/product`
2. copy the package to `/opt/product`
3. `$cd /opt/product`
3. `$docker-compose up -d`
4. the service would start up


# test api

use curl method from localhost to trigger api

## create
```
curl -XPOST -H "Content-Type:application/json" 192.168.180.112:8899/products -d '{
    "name": "LCD", "code": "V-082", "category": "3C", "unit_price": 20, "inventory": 25, "color": "Red", "size": "S、L"
}'
```


## update
```
curl -XPUT -H "Content-Type:application/json" 192.168.180.112:8899/products/9231370afd44460eba5922687b4f8940 -d '{
    "inventory": 30, "color": "Red", "size": "S、L"
}'
```


## read
```
curl -XGET 192.168.180.112:8899/products/9231370afd44460eba5922687b4f8940
```


## delete
```
curl -XDELETE 192.168.180.112:8899/products/f47d5b70fc514ba8a41ff1492dab4b84
```
