#!/bin/bash

#If one command fails, it stops the script
set -e

### Current Tools: subfinder, assetfinder, amass, waybackurls,
### shuffledns, naabu, katana, httpx, ffuf, wafw00f, sqlmap

sudo apt update
sudo apt upgrade -y
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
go install -v github.com/tomnomnom/assetfinder@latest
CGO_ENABLED=0 go install -v github.com/owasp-amass/amass/v5/cmd/amass@main
go install github.com/tomnomnom/waybackurls@latest
go install -v github.com/projectdiscovery/shuffledns/cmd/shuffledns@latest
sudo apt install -y libpcap-dev
go install -v github.com/projectdiscovery/naabu/v2/cmd/naabu@latest
CGO_ENABLED=1 go install github.com/projectdiscovery/katana/cmd/katana@latest
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
go install github.com/ffuf/ffuf/v2@latest
sudo apt install sqlmap wafw00f

