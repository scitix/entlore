# Acceptance document for 20251127-Bexlink cluster with 256 H20X machines
- Scope is acceptance for 20251127-Bexlink cluster with 256 H20X machines.
- First acceptance date: 2025-11-27.
- First round counted 231 cluster nodes.
- The first round also captured the issue-node list.
- Bexlink-yzaloom67-206: management IP 10.162.218.39.
- Bexlink-yzaloom67-206: NotReady, progress 1127:supplier investigating.
- Bexlink-yzaloom67-169 appeared in the first acceptance table.

- Bexlink-yzaloom67-169: management IP 10.126.71.219.
- Bexlink-yzaloom67-169: NotReady, progress 1127:supplier investigating.
- Bexlink-yzaloom67-088: 400G adapter could not enter roce mode.
- Bexlink-yzaloom67-2-022: management IP 10.96.235.108.
- Bexlink-yzaloom67-2-022: boot behavior was abnormal.
- Bexlink-yzaloom67-092: management IP 10.239.134.132, NotReady.

- Bexlink-yzaloom67-159: management IP 10.132.50.183, NotReady.
- Bexlink-yzaloom67-199: management IP 10.67.110.59.
- Bexlink-yzaloom67-199: out-of-band error noted.
- A Gpu drop-card section is part of the document.
- Second acceptance date: 2025-12-04.
- The second fault table used node ID, management address, fault, and sn.
- Bexlink-yzaloom67-213 was included in the second acceptance table.
Roce down
  10.175.141.189 (Serial: 4DEJK21)    475-Q59
  10.203.38.31 (Serial: 9YHSLW0)    239-Q42
  10.145.172.26 (Serial: 2DQMLU1)    891-U98
  10.38.108.95 (Serial: 2EWRF04)    784-F76
  10.149.136.82 (Serial: 9RRHM68)    230-A18
  10.193.164.133 (Serial: K547967Q7950056)    201-U12
  10.216.122.104 (Serial: GG97T42)    224-L94
  10.207.45.69 (Serial: D542865I3583010)    873-Z25
  10.85.207.69 (Serial: DR73Q94)    722-E04
25g down
  10.24.68.67 (Serial: 4RLCII6)    222-B24
  10.214.85.81 (Serial: I5NCFG2)    468-K61
  10.162.214.90 (Serial: 0EIBQ48)    642-F49
  10.96.175.19 (Serial: 1XIGA34)    756-S30

- Bexlink-yzaloom67-213: management address 10.38.108.95.
- Bexlink-yzaloom67-213: eth4 needs onsite repair, sn 2EWRF04.
- Bexlink-yzaloom67-028: management address 10.193.164.133.
- Bexlink-yzaloom67-028: enp155s0np0 needs onsite repair.
- Bexlink-yzaloom67-028: sn K547967Q7950056.
- Bexlink-yzaloom67-199: management address 10.203.38.31.
- Bexlink-yzaloom67-199: eth2 needs onsite repair, sn 9YHSLW0.

- Bexlink-yzaloom67-2-117: management address 10.211.222.203.
- Bexlink-yzaloom67-2-117: eth0 needs onsite repair, sn VDBVV73.
- Bexlink-yzaloom67-071: management address 10.44.166.145.
- Bexlink-yzaloom67-071: dropped-card needs onsite repair.
- Bexlink-yzaloom67-071: sn Q778387L0815866.
- Bexlink-yzaloom67-009: management address 10.207.45.69.
- Bexlink-yzaloom67-009: dropped-card rebooting--recovered.

- Bexlink-yzaloom67-009: sn L950130U5022167.
- Bexlink-yzaloom67-038: management address 10.80.90.25.
- Bexlink-yzaloom67-038: dropped-card rebooting--recovered.
- Bexlink-yzaloom67-038: sn xxx.
- First xxx placeholder row: success.
- Second xxx placeholder row: success.
- Bexlink-yzaloom67-247 was duplicated and had no configuration.

# Remarks
- Bexlink-yzaloom67-2-148: status ok, repeated configuration.
- Bexlink-yzaloom67-2-116: status ok, repeated configuration.
- Bexlink-yzaloom67-2-118: repeated configuration.
- Bexlink-yzaloom67-233: repeated configuration.
- Bexlink-yzaloom67-2-148 / 116 / 118 was the grouped repeated-configuration line.
- Remark 1 pointed to the lldp table.

- lldp table file: lldp_vyrwave.xlsx.
- roce tenant configuration mapping used vlan 52.
- The mapping table covered all leaf vlan52 subnets for IP allocation.
- ROCE Manual Tenant Configuration Mapping Table 20250603-v2.xlsx supplied the manual ROCE mapping.
- 6-11-1 Shanghai RoCE automatic IP allocation and vlan change was an @Sophie Walsh tool link.
- The tool runs only from jump host Erlwick at 117.146.214.105.
- Working directory: /root/devnet/roce-tools.
- Send any process error to @Sophie Walsh, since legacy tenants may need DB removal and switch config refresh.

# Script execution process
- Step 3.1 updated machine lldp details through yaml file test.json.
- Step 3.2 ran IP allocation with `python3 roce_tool.py alloc-ip test.json --save`.
- The script produced test_output_20251205_1136.json.
- Step 3.3 applied the switch-side configuration.
- Step 3.4 ran the assigned ethx IP addresses on the service side.
[
    {
        "server_name": "Bexlink-yzaloom67-001",
        "site": "EW",
        "vlan_id": 52,
        "interfaces": [
            {
                "interface_name": "eth0",
                "switch_name": "EW-RLF317",
                "switch_port": "400GE1/0/128"
            },
            {
                "interface_name": "eth1",
                "switch_name": "EW-RLF318",
                "switch_port": "400GE1/0/128"
            },
            {
                "interface_name": "eth2",
                "switch_name": "EW-RLF319",
                "switch_port": "400GE1/0/128"
            },
            {
                "interface_name": "eth3",
                "switch_name": "EW-RLF320",
                "switch_port": "400GE1/0/128"
            },
            {
                "interface_name": "eth4",
                "switch_name": "EW-RLF321",
                "switch_port": "400GE1/0/128"
            },
            {
                "interface_name": "eth5",
                "switch_name": "EW-RLF322",
                "switch_port": "400GE1/0/128"
            },
            {
                "interface_name": "eth6",
                "switch_name": "EW-RLF323",
                "switch_port": "400GE1/0/128"
            },
            {
                "interface_name": "eth7",
                "switch_name": "EW-RLF324",
                "switch_port": "400GE1/0/128"
            }
        ]
    }
]
image.png
image.png