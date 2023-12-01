#! /bin/bash

apt install -y golang
go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
apt install -y wordlists
apt install -y arjun
apt install -y gobuster
apt install -y dirb
apt install -y dirbuster
apt install -y john
apt install -y hashcat
apt install -y nmap
curl "https://raw.githubusercontent.com/ngductung/abcxyz/main/.banner1" -o /.banner1 && echo "cat /.banner1" >> /home/ngductung/.bashrc
curl "https://raw.githubusercontent.com/ngductung/abcxyz/main/.banner2" -o /.banner2 && echo "cat /.banner2" >> /root/.bashrc
