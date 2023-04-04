# Access
Level: Medium

Description:
```
There is a log file containing HTTP requests sent to a webserver. Can you answer all the questions to determine what malicious actors tried to do?


1. How many unique IP addresses have sent HTTP requests to the web server? (flag format `byuctf{0000}`)
2. How many attempts were made to grab a `.env` file? (flag format `byuctf{0000}`)
3. What IPs attempted to exploit log4j? (flag format `byuctf{100.100.100.100_200.200.200.200}`)
4. What is the name of the exploit file that would be run in the obfuscated log4j attempt? (flag format `byuctf{filename}`)
5. What IP addresses attempted to exploit CVE-2021-3129? (flag format `byuctf{100.100.100.100_200.200.200.200}`)
6. What is the name of the ISP that hosts the Russian IP attempting to exploit CVE-2021-3129? (flag format `byuctf{ispname}`)
```

## Writeup
1. How many unique IP addresses have sent HTTP requests to the web server?
    - `byuctf{98}`
    - (`cat forensics-steganography/access/access.log | awk '{print $1}' | sort | uniq | wc -l`)
1. How many attempts were made to grab a `.env` file?
    - `byuctf{95}`
    - (`cat forensics-steganography/access/access.log | grep \.env | wc -l`)
1. What IPs attempted to exploit log4j?
    - `byuctf{98.0.242.10_198.98.61.124}` or `byuctf{198.98.61.124_98.0.242.10}`
    - (`cat forensics-steganography/access/access.log | grep \$\{ | awk '{print $1}'`)
1. What is the name of the exploit file that would be run in the obfuscated log4j attempt?
    - `byuctf{dev_sshd}`
1. What IP addresses attempted to exploit CVE-2021-3129?
    - `byuctf{20.24.24.111_45.146.165.37}` or `byuctf{45.146.165.37_20.24.24.111}`
    - (`cat forensics-steganography/access/access.log | grep _ignition | awk '{print $1}' | sort | uniq`)
1. What is the name of the ISP that hosts the Russian IP attempting to exploit CVE-2021-3129?
    - `byuctf{Selectel}`
    - (https://www.virustotal.com/gui/ip-address/45.146.165.37/community)