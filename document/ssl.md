## 前提

```bash
dig <domain name>
# ipアドレスを確認
# curl ifconfig.me
ipアドレスが同じことを確認
```

```
apt-get install openssl
```

## install certbot

```
apt-get update
apt-get install -y certbot python3-certbot-apache
certbot --version
```

## 初回作成

```bash
certbot --apache certonly
```

```bash
cd /etc/apache2/sites-enabled/
ln -s /etc/apache2/sites-available/default-ssl.conf default-ssl.conf
vim default-ssl.conf
```

```
<VirtualHost *:443>
SSLCertificateFile      /etc/letsencrypt/live/thinkstream.tk/cert.pem
SSLCertificateKeyFile   /etc/letsencrypt/live/thinkstream.tk/privkey.pem
SSLCertificateChainFile /etc/letsencrypt/live/thinkstream.tk/chain.pem
```

```bash
a2enmod rewrite
a2enmod ssl
apache2ctl -M | grep -i ssl
# ssl_module (shared)
apache2ctl restart
```

```bash
vim /etc/apache2/sites-enabled/000-default.conf
```
```
<IfModule rewrite_module>
    RewriteEngine On
    LogLevel alert rewrite:trace3
    RewriteCond %{HTTPS} off
    RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [R=301,L]
</IfModule>
```
