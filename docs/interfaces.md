# Interfaces de rede

Comandos para:
1. Listá-las: `ip link`; `lshw -class network`
2. Verificar endereços IPv4 delas: `ip address`
3. Desativar uma: `ip link set INTERFACE down` (Verificar!)
4. Ativar uma: `ip link set INTERFACE up` (Verificar!)


## Configuração no Ubuntu servidor

- Sistema: netplan[^1]
- Arquivo de configuração: `/etc/netplan/*.yaml`
- Comandos para ativar configuração:
  - `netplan try`
  - `netplan apply`


## Configuração no Debian

- Sistema: ifupdown
- Arquivos de configuração: 
  - `/etc/network/interfaces`
  - `/etc/network/interfaces.d/*`
  - `/etc/resolv.conf` (Para o DNS, às vezes)


- Comandos para ativar/desativar interfaces de rede:
  - Desativar: `ifdown INTERFACE`
  - Ativar: `ifup INTERFACE`

## Configuração com `systemd-networkd`

- Sistema: systemd-networkd
- Arquivo de configuração: `/etc/systemd/network/*.network`
- Comandos para ativar as novas configurações:
  - `systemctl reload systemd-networkd.service`

## Referências

- []()


[^1]: Netplan: https://netplan.io/