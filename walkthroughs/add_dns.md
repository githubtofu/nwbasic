* Install the resolvconf package.
    `sudo apt install resolvconf`

* Edit /etc/resolvconf/resolv.conf.d/head and add the following:
```
    nameserver 8.8.4.4
    nameserver 8.8.8.8
```
* Restart the resolvconf service.
`sudo service resolvconf restart`

