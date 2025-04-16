# API HW Project - Timezone API

## How to Use

1. open up your terminal or shell.
2. run the following command.

```bash
curl -H "Authorization: Bearer supersecrettoken123" http://34.135.182.0:5000/api/time/CAPITALCITYHERE
```
## Explanation of command
- curl: cmd line tool to make http request from terminal
- -H: includes authorization key header
- "Authorization: Bearer supersecrettoken123": the header (Authorization Token)
- http://34.135.182.0:5000/api/time: base url, including public IP address
- CAPITALCITYHERE: the city paramater you want to check


make sure to replace CAPITALCITYHERE with one from this list: 

    Beijing
    Tokyo
    Moscow
    Kinshasa
    Jakarta
    Lima
    Cairo
    Seoul
    Mexico City
    London
    Dhaka
    Tehran
    Bangkok
    Hanoi
    Baghdad
    Riyadh
    Hong Kong
    Bogotá
    Santiago
    Ankara
    Singapore
    Kabul
    Nairobi
    Amman
    Algiers
    Berlin
    Madrid
    Buenos Aires
    Addis Ababa
    Kuwait City
    Brasília
    Guatemala City
    Pretoria
    Kyiv
    Pyongyang
    Tashkent
    Rome
    Quito
    Yaoundé
    Lusaka
    Khartoum
    Taipei
    Sanaa
    Luanda
    Ouagadougou
    Accra
    Mogadishu
    Baku
    Phnom Penh
    Caracas
