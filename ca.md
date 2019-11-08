```sh
> export INSTALL_ROOT=/opt/oss
> export SUBJECT_ALT_NAME=IP:10.57.76.77
```

```sh 
> openssl genrsa -aes128 -out accampus.key 4096  --- 输入私钥的密码
> openssl req -new -days 3650 -key accampus.key -out accampus.csr -config /opt/oss/openssl/etc/openssl.conf   -- 输入私钥的密码
> openssl ca -extensions usr_cert -in accampus.csr -out accampus.crt -keyfile /opt/oss/manager/var/ca/ca_key.pem -cert /opt/oss/openssl/etc/openssl.conf  -- 根CA私钥的密码
```
 
```sh
> openssl pkcs12 -export -in accampus.crt -inkey accampus.key -out accampus.p12
```

备注：  
- *.key 是服务证书私钥文件
- *.csr 是证书请求文件
- *.crt 是服务证书
- *.p12 这个私钥与服务证书合并后的文件
