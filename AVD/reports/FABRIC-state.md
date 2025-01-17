
# Validate State Report

**Table of Contents:**

- [Validate State Report](validate-state-report)
  - [Test Results Summary](#test-results-summary)
  - [Failed Test Results Summary](#failed-test-results-summary)
  - [All Test Results](#all-test-results)

## Test Results Summary

### Summary Totals

| Total Tests | Total Tests Passed | Total Tests Failed |
| ----------- | ------------------ | ------------------ |
| 266 | 266 | 0 |

### Summary Totals Devices Under Tests

| DUT | Total Tests | Tests Passed | Tests Failed | Categories Failed |
| --- | ----------- | ------------ | ------------ | ----------------- |
| leaf1 |  52 | 52 | 0 | - |
| leaf2 |  52 | 52 | 0 | - |
| leaf3 |  51 | 51 | 0 | - |
| leaf4 |  51 | 51 | 0 | - |
| spine1 |  15 | 15 | 0 | - |
| spine2 |  15 | 15 | 0 | - |
| spine3 |  15 | 15 | 0 | - |
| spine4 |  15 | 15 | 0 | - |

### Summary Totals Per Category

| Test Category | Total Tests | Tests Passed | Tests Failed |
| ------------- | ----------- | ------------ | ------------ |
| NTP |  8 | 8 | 0 |
| Interface State |  102 | 102 | 0 |
| LLDP Topology |  40 | 40 | 0 |
| MLAG |  4 | 4 | 0 |
| BGP |  40 | 40 | 0 |
| Routing Table |  40 | 40 | 0 |
| Loopback0 Reachability |  32 | 32 | 0 |

## Failed Test Results Summary

| Test ID | Node | Test Category | Test Description | Test | Test Result | Failure Reason |
| ------- | ---- | ------------- | ---------------- | ---- | ----------- | -------------- |

## All Test Results

| Test ID | Node | Test Category | Test Description | Test | Test Result | Failure Reason |
| ------- | ---- | ------------- | ---------------- | ---- | ----------- | -------------- |
| 1 | leaf1 | NTP | Synchronised with NTP server | NTP | PASS | - |
| 2 | leaf2 | NTP | Synchronised with NTP server | NTP | PASS | - |
| 3 | leaf3 | NTP | Synchronised with NTP server | NTP | PASS | - |
| 4 | leaf4 | NTP | Synchronised with NTP server | NTP | PASS | - |
| 5 | spine1 | NTP | Synchronised with NTP server | NTP | PASS | - |
| 6 | spine2 | NTP | Synchronised with NTP server | NTP | PASS | - |
| 7 | spine3 | NTP | Synchronised with NTP server | NTP | PASS | - |
| 8 | spine4 | NTP | Synchronised with NTP server | NTP | PASS | - |
| 9 | leaf1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet1 - MLAG_PEER_leaf2_Ethernet1 | PASS | - |
| 10 | leaf1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet2 - MLAG_PEER_leaf2_Ethernet2 | PASS | - |
| 11 | leaf1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet3 - P2P_LINK_TO_SPINE1_Ethernet3 | PASS | - |
| 12 | leaf1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_SPINE2_Ethernet3 | PASS | - |
| 13 | leaf1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet5 - P2P_LINK_TO_SPINE3_Ethernet3 | PASS | - |
| 14 | leaf1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet6 - P2P_LINK_TO_SPINE4_Ethernet3 | PASS | - |
| 15 | leaf1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet7 - host1 | PASS | - |
| 16 | leaf1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet9 - host2 | PASS | - |
| 17 | leaf2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet1 - MLAG_PEER_leaf1_Ethernet1 | PASS | - |
| 18 | leaf2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet2 - MLAG_PEER_leaf1_Ethernet2 | PASS | - |
| 19 | leaf2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet3 - P2P_LINK_TO_SPINE1_Ethernet4 | PASS | - |
| 20 | leaf2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_SPINE2_Ethernet4 | PASS | - |
| 21 | leaf2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet5 - P2P_LINK_TO_SPINE3_Ethernet4 | PASS | - |
| 22 | leaf2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet6 - P2P_LINK_TO_SPINE4_Ethernet4 | PASS | - |
| 23 | leaf2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet7 - host1 | PASS | - |
| 24 | leaf2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet9 - host2 | PASS | - |
| 25 | leaf3 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet1 - MLAG_PEER_leaf4_Ethernet1 | PASS | - |
| 26 | leaf3 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet2 - MLAG_PEER_leaf4_Ethernet2 | PASS | - |
| 27 | leaf3 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet3 - P2P_LINK_TO_SPINE1_Ethernet5 | PASS | - |
| 28 | leaf3 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_SPINE2_Ethernet5 | PASS | - |
| 29 | leaf3 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet5 - P2P_LINK_TO_SPINE3_Ethernet5 | PASS | - |
| 30 | leaf3 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet6 - P2P_LINK_TO_SPINE4_Ethernet5 | PASS | - |
| 31 | leaf3 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet9 -  | PASS | - |
| 32 | leaf3 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet7 - host3 | PASS | - |
| 33 | leaf4 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet1 - MLAG_PEER_leaf3_Ethernet1 | PASS | - |
| 34 | leaf4 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet2 - MLAG_PEER_leaf3_Ethernet2 | PASS | - |
| 35 | leaf4 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet3 - P2P_LINK_TO_SPINE1_Ethernet6 | PASS | - |
| 36 | leaf4 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_SPINE2_Ethernet6 | PASS | - |
| 37 | leaf4 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet5 - P2P_LINK_TO_SPINE3_Ethernet6 | PASS | - |
| 38 | leaf4 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet6 - P2P_LINK_TO_SPINE4_Ethernet6 | PASS | - |
| 39 | leaf4 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet9 -  | PASS | - |
| 40 | leaf4 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet7 - host3 | PASS | - |
| 41 | spine1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet3 - P2P_LINK_TO_LEAF1_Ethernet3 | PASS | - |
| 42 | spine1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_LEAF2_Ethernet3 | PASS | - |
| 43 | spine1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet5 - P2P_LINK_TO_LEAF3_Ethernet3 | PASS | - |
| 44 | spine1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet6 - P2P_LINK_TO_LEAF4_Ethernet3 | PASS | - |
| 45 | spine2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet3 - P2P_LINK_TO_LEAF1_Ethernet4 | PASS | - |
| 46 | spine2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_LEAF2_Ethernet4 | PASS | - |
| 47 | spine2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet5 - P2P_LINK_TO_LEAF3_Ethernet4 | PASS | - |
| 48 | spine2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet6 - P2P_LINK_TO_LEAF4_Ethernet4 | PASS | - |
| 49 | spine3 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet3 - P2P_LINK_TO_LEAF1_Ethernet5 | PASS | - |
| 50 | spine3 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_LEAF2_Ethernet5 | PASS | - |
| 51 | spine3 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet5 - P2P_LINK_TO_LEAF3_Ethernet5 | PASS | - |
| 52 | spine3 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet6 - P2P_LINK_TO_LEAF4_Ethernet5 | PASS | - |
| 53 | spine4 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet3 - P2P_LINK_TO_LEAF1_Ethernet6 | PASS | - |
| 54 | spine4 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_LEAF2_Ethernet6 | PASS | - |
| 55 | spine4 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet5 - P2P_LINK_TO_LEAF3_Ethernet6 | PASS | - |
| 56 | spine4 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet6 - P2P_LINK_TO_LEAF4_Ethernet6 | PASS | - |
| 57 | leaf1 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel1 - MLAG_PEER_leaf2_Po1 | PASS | - |
| 58 | leaf1 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel7 - host1 | PASS | - |
| 59 | leaf1 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel9 - host2 | PASS | - |
| 60 | leaf2 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel1 - MLAG_PEER_leaf1_Po1 | PASS | - |
| 61 | leaf2 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel7 - host1 | PASS | - |
| 62 | leaf2 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel9 - host2 | PASS | - |
| 63 | leaf3 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel1 - MLAG_PEER_leaf4_Po1 | PASS | - |
| 64 | leaf3 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel7 - host3 | PASS | - |
| 65 | leaf4 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel1 - MLAG_PEER_leaf3_Po1 | PASS | - |
| 66 | leaf4 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel7 - host3 | PASS | - |
| 67 | leaf1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4093 - MLAG_PEER_L3_PEERING | PASS | - |
| 68 | leaf1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4094 - MLAG_PEER | PASS | - |
| 69 | leaf1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan30 - B | PASS | - |
| 70 | leaf1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan3019 - MLAG_PEER_L3_iBGP: vrf Tenant_B | PASS | - |
| 71 | leaf1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan10 - DMZ | PASS | - |
| 72 | leaf1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan20 - Internal | PASS | - |
| 73 | leaf1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan3009 - MLAG_PEER_L3_iBGP: vrf VRF_A | PASS | - |
| 74 | leaf2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4093 - MLAG_PEER_L3_PEERING | PASS | - |
| 75 | leaf2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4094 - MLAG_PEER | PASS | - |
| 76 | leaf2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan30 - B | PASS | - |
| 77 | leaf2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan3019 - MLAG_PEER_L3_iBGP: vrf Tenant_B | PASS | - |
| 78 | leaf2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan10 - DMZ | PASS | - |
| 79 | leaf2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan20 - Internal | PASS | - |
| 80 | leaf2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan3009 - MLAG_PEER_L3_iBGP: vrf VRF_A | PASS | - |
| 81 | leaf3 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4093 - MLAG_PEER_L3_PEERING | PASS | - |
| 82 | leaf3 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4094 - MLAG_PEER | PASS | - |
| 83 | leaf3 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan30 - B | PASS | - |
| 84 | leaf3 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan3019 - MLAG_PEER_L3_iBGP: vrf Tenant_B | PASS | - |
| 85 | leaf3 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan10 - DMZ | PASS | - |
| 86 | leaf3 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan20 - Internal | PASS | - |
| 87 | leaf3 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan3009 - MLAG_PEER_L3_iBGP: vrf VRF_A | PASS | - |
| 88 | leaf4 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4093 - MLAG_PEER_L3_PEERING | PASS | - |
| 89 | leaf4 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4094 - MLAG_PEER | PASS | - |
| 90 | leaf4 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan30 - B | PASS | - |
| 91 | leaf4 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan3019 - MLAG_PEER_L3_iBGP: vrf Tenant_B | PASS | - |
| 92 | leaf4 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan10 - DMZ | PASS | - |
| 93 | leaf4 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan20 - Internal | PASS | - |
| 94 | leaf4 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan3009 - MLAG_PEER_L3_iBGP: vrf VRF_A | PASS | - |
| 95 | leaf1 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | PASS | - |
| 96 | leaf2 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | PASS | - |
| 97 | leaf3 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | PASS | - |
| 98 | leaf4 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | PASS | - |
| 99 | leaf1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 100 | leaf1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback1 - VTEP_VXLAN_Tunnel_Source | PASS | - |
| 101 | leaf2 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 102 | leaf2 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback1 - VTEP_VXLAN_Tunnel_Source | PASS | - |
| 103 | leaf3 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 104 | leaf3 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback1 - VTEP_VXLAN_Tunnel_Source | PASS | - |
| 105 | leaf4 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 106 | leaf4 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback1 - VTEP_VXLAN_Tunnel_Source | PASS | - |
| 107 | spine1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 108 | spine2 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 109 | spine3 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 110 | spine4 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 111 | leaf1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: leaf2_Ethernet1 | PASS | - |
| 112 | leaf1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: leaf2_Ethernet2 | PASS | - |
| 113 | leaf1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: spine1_Ethernet3 | PASS | - |
| 114 | leaf1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: spine2_Ethernet3 | PASS | - |
| 115 | leaf1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet5 - remote: spine3_Ethernet3 | PASS | - |
| 116 | leaf1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet6 - remote: spine4_Ethernet3 | PASS | - |
| 117 | leaf2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: leaf1_Ethernet1 | PASS | - |
| 118 | leaf2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: leaf1_Ethernet2 | PASS | - |
| 119 | leaf2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: spine1_Ethernet4 | PASS | - |
| 120 | leaf2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: spine2_Ethernet4 | PASS | - |
| 121 | leaf2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet5 - remote: spine3_Ethernet4 | PASS | - |
| 122 | leaf2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet6 - remote: spine4_Ethernet4 | PASS | - |
| 123 | leaf3 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: leaf4_Ethernet1 | PASS | - |
| 124 | leaf3 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: leaf4_Ethernet2 | PASS | - |
| 125 | leaf3 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: spine1_Ethernet5 | PASS | - |
| 126 | leaf3 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: spine2_Ethernet5 | PASS | - |
| 127 | leaf3 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet5 - remote: spine3_Ethernet5 | PASS | - |
| 128 | leaf3 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet6 - remote: spine4_Ethernet5 | PASS | - |
| 129 | leaf4 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: leaf3_Ethernet1 | PASS | - |
| 130 | leaf4 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: leaf3_Ethernet2 | PASS | - |
| 131 | leaf4 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: spine1_Ethernet6 | PASS | - |
| 132 | leaf4 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: spine2_Ethernet6 | PASS | - |
| 133 | leaf4 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet5 - remote: spine3_Ethernet6 | PASS | - |
| 134 | leaf4 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet6 - remote: spine4_Ethernet6 | PASS | - |
| 135 | spine1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: leaf1_Ethernet3 | PASS | - |
| 136 | spine1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: leaf2_Ethernet3 | PASS | - |
| 137 | spine1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet5 - remote: leaf3_Ethernet3 | PASS | - |
| 138 | spine1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet6 - remote: leaf4_Ethernet3 | PASS | - |
| 139 | spine2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: leaf1_Ethernet4 | PASS | - |
| 140 | spine2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: leaf2_Ethernet4 | PASS | - |
| 141 | spine2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet5 - remote: leaf3_Ethernet4 | PASS | - |
| 142 | spine2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet6 - remote: leaf4_Ethernet4 | PASS | - |
| 143 | spine3 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: leaf1_Ethernet5 | PASS | - |
| 144 | spine3 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: leaf2_Ethernet5 | PASS | - |
| 145 | spine3 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet5 - remote: leaf3_Ethernet5 | PASS | - |
| 146 | spine3 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet6 - remote: leaf4_Ethernet5 | PASS | - |
| 147 | spine4 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: leaf1_Ethernet6 | PASS | - |
| 148 | spine4 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: leaf2_Ethernet6 | PASS | - |
| 149 | spine4 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet5 - remote: leaf3_Ethernet6 | PASS | - |
| 150 | spine4 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet6 - remote: leaf4_Ethernet6 | PASS | - |
| 151 | leaf1 | MLAG | MLAG State active & Status connected | MLAG | PASS | - |
| 152 | leaf2 | MLAG | MLAG State active & Status connected | MLAG | PASS | - |
| 153 | leaf3 | MLAG | MLAG State active & Status connected | MLAG | PASS | - |
| 154 | leaf4 | MLAG | MLAG State active & Status connected | MLAG | PASS | - |
| 155 | leaf1 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 156 | leaf2 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 157 | leaf3 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 158 | leaf4 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 159 | spine1 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 160 | spine2 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 161 | spine3 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 162 | spine4 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 163 | leaf1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.101 | PASS | - |
| 164 | leaf1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.102 | PASS | - |
| 165 | leaf1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.103 | PASS | - |
| 166 | leaf1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.104 | PASS | - |
| 167 | leaf2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.101 | PASS | - |
| 168 | leaf2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.102 | PASS | - |
| 169 | leaf2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.103 | PASS | - |
| 170 | leaf2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.104 | PASS | - |
| 171 | leaf3 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.101 | PASS | - |
| 172 | leaf3 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.102 | PASS | - |
| 173 | leaf3 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.103 | PASS | - |
| 174 | leaf3 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.104 | PASS | - |
| 175 | leaf4 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.101 | PASS | - |
| 176 | leaf4 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.102 | PASS | - |
| 177 | leaf4 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.103 | PASS | - |
| 178 | leaf4 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.104 | PASS | - |
| 179 | spine1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.11 | PASS | - |
| 180 | spine1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.12 | PASS | - |
| 181 | spine1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.13 | PASS | - |
| 182 | spine1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.14 | PASS | - |
| 183 | spine2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.11 | PASS | - |
| 184 | spine2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.12 | PASS | - |
| 185 | spine2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.13 | PASS | - |
| 186 | spine2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.14 | PASS | - |
| 187 | spine3 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.11 | PASS | - |
| 188 | spine3 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.12 | PASS | - |
| 189 | spine3 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.13 | PASS | - |
| 190 | spine3 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.14 | PASS | - |
| 191 | spine4 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.11 | PASS | - |
| 192 | spine4 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.12 | PASS | - |
| 193 | spine4 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.13 | PASS | - |
| 194 | spine4 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.14 | PASS | - |
| 195 | leaf1 | Routing Table | Remote VTEP address | 192.168.102.11 | PASS | - |
| 196 | leaf1 | Routing Table | Remote VTEP address | 192.168.102.13 | PASS | - |
| 197 | leaf2 | Routing Table | Remote VTEP address | 192.168.102.11 | PASS | - |
| 198 | leaf2 | Routing Table | Remote VTEP address | 192.168.102.13 | PASS | - |
| 199 | leaf3 | Routing Table | Remote VTEP address | 192.168.102.11 | PASS | - |
| 200 | leaf3 | Routing Table | Remote VTEP address | 192.168.102.13 | PASS | - |
| 201 | leaf4 | Routing Table | Remote VTEP address | 192.168.102.11 | PASS | - |
| 202 | leaf4 | Routing Table | Remote VTEP address | 192.168.102.13 | PASS | - |
| 203 | leaf1 | Routing Table | Remote Lo0 address | 192.168.101.11 | PASS | - |
| 204 | leaf1 | Routing Table | Remote Lo0 address | 192.168.101.12 | PASS | - |
| 205 | leaf1 | Routing Table | Remote Lo0 address | 192.168.101.13 | PASS | - |
| 206 | leaf1 | Routing Table | Remote Lo0 address | 192.168.101.14 | PASS | - |
| 207 | leaf1 | Routing Table | Remote Lo0 address | 192.168.101.101 | PASS | - |
| 208 | leaf1 | Routing Table | Remote Lo0 address | 192.168.101.102 | PASS | - |
| 209 | leaf1 | Routing Table | Remote Lo0 address | 192.168.101.103 | PASS | - |
| 210 | leaf1 | Routing Table | Remote Lo0 address | 192.168.101.104 | PASS | - |
| 211 | leaf2 | Routing Table | Remote Lo0 address | 192.168.101.11 | PASS | - |
| 212 | leaf2 | Routing Table | Remote Lo0 address | 192.168.101.12 | PASS | - |
| 213 | leaf2 | Routing Table | Remote Lo0 address | 192.168.101.13 | PASS | - |
| 214 | leaf2 | Routing Table | Remote Lo0 address | 192.168.101.14 | PASS | - |
| 215 | leaf2 | Routing Table | Remote Lo0 address | 192.168.101.101 | PASS | - |
| 216 | leaf2 | Routing Table | Remote Lo0 address | 192.168.101.102 | PASS | - |
| 217 | leaf2 | Routing Table | Remote Lo0 address | 192.168.101.103 | PASS | - |
| 218 | leaf2 | Routing Table | Remote Lo0 address | 192.168.101.104 | PASS | - |
| 219 | leaf3 | Routing Table | Remote Lo0 address | 192.168.101.11 | PASS | - |
| 220 | leaf3 | Routing Table | Remote Lo0 address | 192.168.101.12 | PASS | - |
| 221 | leaf3 | Routing Table | Remote Lo0 address | 192.168.101.13 | PASS | - |
| 222 | leaf3 | Routing Table | Remote Lo0 address | 192.168.101.14 | PASS | - |
| 223 | leaf3 | Routing Table | Remote Lo0 address | 192.168.101.101 | PASS | - |
| 224 | leaf3 | Routing Table | Remote Lo0 address | 192.168.101.102 | PASS | - |
| 225 | leaf3 | Routing Table | Remote Lo0 address | 192.168.101.103 | PASS | - |
| 226 | leaf3 | Routing Table | Remote Lo0 address | 192.168.101.104 | PASS | - |
| 227 | leaf4 | Routing Table | Remote Lo0 address | 192.168.101.11 | PASS | - |
| 228 | leaf4 | Routing Table | Remote Lo0 address | 192.168.101.12 | PASS | - |
| 229 | leaf4 | Routing Table | Remote Lo0 address | 192.168.101.13 | PASS | - |
| 230 | leaf4 | Routing Table | Remote Lo0 address | 192.168.101.14 | PASS | - |
| 231 | leaf4 | Routing Table | Remote Lo0 address | 192.168.101.101 | PASS | - |
| 232 | leaf4 | Routing Table | Remote Lo0 address | 192.168.101.102 | PASS | - |
| 233 | leaf4 | Routing Table | Remote Lo0 address | 192.168.101.103 | PASS | - |
| 234 | leaf4 | Routing Table | Remote Lo0 address | 192.168.101.104 | PASS | - |
| 235 | leaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1 - 192.168.101.11 Destination: 192.168.101.11 | PASS | - |
| 236 | leaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1 - 192.168.101.11 Destination: 192.168.101.12 | PASS | - |
| 237 | leaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1 - 192.168.101.11 Destination: 192.168.101.13 | PASS | - |
| 238 | leaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1 - 192.168.101.11 Destination: 192.168.101.14 | PASS | - |
| 239 | leaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1 - 192.168.101.11 Destination: 192.168.101.101 | PASS | - |
| 240 | leaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1 - 192.168.101.11 Destination: 192.168.101.102 | PASS | - |
| 241 | leaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1 - 192.168.101.11 Destination: 192.168.101.103 | PASS | - |
| 242 | leaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1 - 192.168.101.11 Destination: 192.168.101.104 | PASS | - |
| 243 | leaf2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2 - 192.168.101.12 Destination: 192.168.101.11 | PASS | - |
| 244 | leaf2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2 - 192.168.101.12 Destination: 192.168.101.12 | PASS | - |
| 245 | leaf2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2 - 192.168.101.12 Destination: 192.168.101.13 | PASS | - |
| 246 | leaf2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2 - 192.168.101.12 Destination: 192.168.101.14 | PASS | - |
| 247 | leaf2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2 - 192.168.101.12 Destination: 192.168.101.101 | PASS | - |
| 248 | leaf2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2 - 192.168.101.12 Destination: 192.168.101.102 | PASS | - |
| 249 | leaf2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2 - 192.168.101.12 Destination: 192.168.101.103 | PASS | - |
| 250 | leaf2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2 - 192.168.101.12 Destination: 192.168.101.104 | PASS | - |
| 251 | leaf3 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3 - 192.168.101.13 Destination: 192.168.101.11 | PASS | - |
| 252 | leaf3 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3 - 192.168.101.13 Destination: 192.168.101.12 | PASS | - |
| 253 | leaf3 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3 - 192.168.101.13 Destination: 192.168.101.13 | PASS | - |
| 254 | leaf3 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3 - 192.168.101.13 Destination: 192.168.101.14 | PASS | - |
| 255 | leaf3 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3 - 192.168.101.13 Destination: 192.168.101.101 | PASS | - |
| 256 | leaf3 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3 - 192.168.101.13 Destination: 192.168.101.102 | PASS | - |
| 257 | leaf3 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3 - 192.168.101.13 Destination: 192.168.101.103 | PASS | - |
| 258 | leaf3 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3 - 192.168.101.13 Destination: 192.168.101.104 | PASS | - |
| 259 | leaf4 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4 - 192.168.101.14 Destination: 192.168.101.11 | PASS | - |
| 260 | leaf4 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4 - 192.168.101.14 Destination: 192.168.101.12 | PASS | - |
| 261 | leaf4 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4 - 192.168.101.14 Destination: 192.168.101.13 | PASS | - |
| 262 | leaf4 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4 - 192.168.101.14 Destination: 192.168.101.14 | PASS | - |
| 263 | leaf4 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4 - 192.168.101.14 Destination: 192.168.101.101 | PASS | - |
| 264 | leaf4 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4 - 192.168.101.14 Destination: 192.168.101.102 | PASS | - |
| 265 | leaf4 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4 - 192.168.101.14 Destination: 192.168.101.103 | PASS | - |
| 266 | leaf4 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4 - 192.168.101.14 Destination: 192.168.101.104 | PASS | - |
