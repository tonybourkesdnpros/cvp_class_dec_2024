# leaf1

## Table of Contents

- [Management](#management)
  - [DNS Domain](#dns-domain)
  - [Management API HTTP](#management-api-http)
- [MLAG](#mlag)
  - [MLAG Summary](#mlag-summary)
  - [MLAG Device Configuration](#mlag-device-configuration)
- [Spanning Tree](#spanning-tree)
  - [Spanning Tree Summary](#spanning-tree-summary)
  - [Spanning Tree Device Configuration](#spanning-tree-device-configuration)
- [Internal VLAN Allocation Policy](#internal-vlan-allocation-policy)
  - [Internal VLAN Allocation Policy Summary](#internal-vlan-allocation-policy-summary)
  - [Internal VLAN Allocation Policy Configuration](#internal-vlan-allocation-policy-configuration)
- [VLANs](#vlans)
  - [VLANs Summary](#vlans-summary)
  - [VLANs Device Configuration](#vlans-device-configuration)
- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Port-Channel Interfaces](#port-channel-interfaces)
  - [Loopback Interfaces](#loopback-interfaces)
  - [VLAN Interfaces](#vlan-interfaces)
  - [VXLAN Interface](#vxlan-interface)
- [Routing](#routing)
  - [Service Routing Protocols Model](#service-routing-protocols-model)
  - [Virtual Router MAC Address](#virtual-router-mac-address)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [Static Routes](#static-routes)
  - [Router BGP](#router-bgp)
- [BFD](#bfd)
  - [Router BFD](#router-bfd)
- [Multicast](#multicast)
  - [IP IGMP Snooping](#ip-igmp-snooping)
- [Filters](#filters)
  - [Prefix-lists](#prefix-lists)
  - [Route-maps](#route-maps)
- [VRF Instances](#vrf-instances)
  - [VRF Instances Summary](#vrf-instances-summary)
  - [VRF Instances Device Configuration](#vrf-instances-device-configuration)

## Management

### DNS Domain

#### DNS domain: atd.lab

#### DNS Domain Device Configuration

```eos
dns domain atd.lab
!
```

### Management API HTTP

#### Management API HTTP Summary

| HTTP | HTTPS | Default Services |
| ---- | ----- | ---------------- |
| False | True | - |

#### Management API VRF Access

| VRF Name | IPv4 ACL | IPv6 ACL |
| -------- | -------- | -------- |
| MGMT | - | - |

#### Management API HTTP Configuration

```eos
!
management api http-commands
   protocol https
   no shutdown
   !
   vrf MGMT
      no shutdown
```

## MLAG

### MLAG Summary

| Domain-id | Local-interface | Peer-address | Peer-link |
| --------- | --------------- | ------------ | --------- |
| mlag1 | Vlan4094 | 10.255.252.21 | Port-Channel1 |

Dual primary detection is disabled.

### MLAG Device Configuration

```eos
!
mlag configuration
   domain-id mlag1
   local-interface Vlan4094
   peer-address 10.255.252.21
   peer-link Port-Channel1
   reload-delay mlag 300
   reload-delay non-mlag 330
```

## Spanning Tree

### Spanning Tree Summary

STP mode: **mstp**

#### MSTP Instance and Priority

| Instance(s) | Priority |
| -------- | -------- |
| 0 | 4096 |

#### Global Spanning-Tree Settings

- Spanning Tree disabled for VLANs: **4093-4094**

### Spanning Tree Device Configuration

```eos
!
spanning-tree mode mstp
no spanning-tree vlan-id 4093-4094
spanning-tree mst 0 priority 4096
```

## Internal VLAN Allocation Policy

### Internal VLAN Allocation Policy Summary

| Policy Allocation | Range Beginning | Range Ending |
| ------------------| --------------- | ------------ |
| ascending | 1006 | 1199 |

### Internal VLAN Allocation Policy Configuration

```eos
!
vlan internal order ascending range 1006 1199
```

## VLANs

### VLANs Summary

| VLAN ID | Name | Trunk Groups |
| ------- | ---- | ------------ |
| 10 | DMZ | - |
| 20 | Internal | - |
| 30 | B | - |
| 3009 | MLAG_iBGP_VRF_A | LEAF_PEER_L3 |
| 3019 | MLAG_iBGP_Tenant_B | LEAF_PEER_L3 |
| 4093 | LEAF_PEER_L3 | LEAF_PEER_L3 |
| 4094 | MLAG_PEER | MLAG |

### VLANs Device Configuration

```eos
!
vlan 10
   name DMZ
!
vlan 20
   name Internal
!
vlan 30
   name B
!
vlan 3009
   name MLAG_iBGP_VRF_A
   trunk group LEAF_PEER_L3
!
vlan 3019
   name MLAG_iBGP_Tenant_B
   trunk group LEAF_PEER_L3
!
vlan 4093
   name LEAF_PEER_L3
   trunk group LEAF_PEER_L3
!
vlan 4094
   name MLAG_PEER
   trunk group MLAG
```

## Interfaces

### Ethernet Interfaces

#### Ethernet Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |
| Ethernet1 | MLAG_PEER_leaf2_Ethernet1 | *trunk | *- | *- | *['LEAF_PEER_L3', 'MLAG'] | 1 |
| Ethernet2 | MLAG_PEER_leaf2_Ethernet2 | *trunk | *- | *- | *['LEAF_PEER_L3', 'MLAG'] | 1 |
| Ethernet7 | host1 | *access | *10 | *- | *- | 7 |
| Ethernet9 | host2 | *access | *30 | *- | *- | 9 |

*Inherited from Port-Channel Interface

##### IPv6

| Interface | Description | Type | Channel Group | IPv6 Address | VRF | MTU | Shutdown | ND RA Disabled | Managed Config Flag | IPv6 ACL In | IPv6 ACL Out |
| --------- | ----------- | ---- | --------------| ------------ | --- | --- | -------- | -------------- | -------------------| ----------- | ------------ |
| Ethernet3 | P2P_LINK_TO_SPINE1_Ethernet3 | routed | - | - | default | 1550 | False | - | - | - | - |
| Ethernet4 | P2P_LINK_TO_SPINE2_Ethernet3 | routed | - | - | default | 1550 | False | - | - | - | - |
| Ethernet5 | P2P_LINK_TO_SPINE3_Ethernet3 | routed | - | - | default | 1550 | False | - | - | - | - |
| Ethernet6 | P2P_LINK_TO_SPINE4_Ethernet3 | routed | - | - | default | 1550 | False | - | - | - | - |

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description MLAG_PEER_leaf2_Ethernet1
   no shutdown
   channel-group 1 mode active
!
interface Ethernet2
   description MLAG_PEER_leaf2_Ethernet2
   no shutdown
   channel-group 1 mode active
!
interface Ethernet3
   description P2P_LINK_TO_SPINE1_Ethernet3
   no shutdown
   mtu 1550
   no switchport
   ipv6 enable
!
interface Ethernet4
   description P2P_LINK_TO_SPINE2_Ethernet3
   no shutdown
   mtu 1550
   no switchport
   ipv6 enable
!
interface Ethernet5
   description P2P_LINK_TO_SPINE3_Ethernet3
   no shutdown
   mtu 1550
   no switchport
   ipv6 enable
!
interface Ethernet6
   description P2P_LINK_TO_SPINE4_Ethernet3
   no shutdown
   mtu 1550
   no switchport
   ipv6 enable
!
interface Ethernet7
   description host1
   no shutdown
   channel-group 7 mode active
!
interface Ethernet9
   description host2
   no shutdown
   channel-group 9 mode active
```

### Port-Channel Interfaces

#### Port-Channel Interfaces Summary

##### L2

| Interface | Description | Type | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ---- | ----- | ----------- | ------------| --------------------- | ------------------ | ------- | -------- |
| Port-Channel1 | MLAG_PEER_leaf2_Po1 | switched | trunk | - | - | ['LEAF_PEER_L3', 'MLAG'] | - | - | - | - |
| Port-Channel7 | host1 | switched | access | 10 | - | - | - | - | 7 | - |
| Port-Channel9 | host2 | switched | access | 30 | - | - | - | - | 9 | - |

#### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel1
   description MLAG_PEER_leaf2_Po1
   no shutdown
   switchport
   switchport mode trunk
   switchport trunk group LEAF_PEER_L3
   switchport trunk group MLAG
!
interface Port-Channel7
   description host1
   no shutdown
   switchport
   switchport access vlan 10
   mlag 7
   spanning-tree portfast
!
interface Port-Channel9
   description host2
   no shutdown
   switchport
   switchport access vlan 30
   mlag 9
   spanning-tree portfast
```

### Loopback Interfaces

#### Loopback Interfaces Summary

##### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | EVPN_Overlay_Peering | default | 192.168.101.11/32 |
| Loopback1 | VTEP_VXLAN_Tunnel_Source | default | 192.168.102.11/32 |

##### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | EVPN_Overlay_Peering | default | - |
| Loopback1 | VTEP_VXLAN_Tunnel_Source | default | - |


#### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description EVPN_Overlay_Peering
   no shutdown
   ip address 192.168.101.11/32
!
interface Loopback1
   description VTEP_VXLAN_Tunnel_Source
   no shutdown
   ip address 192.168.102.11/32
```

### VLAN Interfaces

#### VLAN Interfaces Summary

| Interface | Description | VRF |  MTU | Shutdown |
| --------- | ----------- | --- | ---- | -------- |
| Vlan10 | DMZ | VRF_A | - | False |
| Vlan20 | Internal | VRF_A | - | False |
| Vlan30 | B | Tenant_B | - | False |
| Vlan3009 | MLAG_PEER_L3_iBGP: vrf VRF_A | VRF_A | 1550 | False |
| Vlan3019 | MLAG_PEER_L3_iBGP: vrf Tenant_B | Tenant_B | 1550 | False |
| Vlan4093 | MLAG_PEER_L3_PEERING | default | 1550 | False |
| Vlan4094 | MLAG_PEER | default | 1550 | False |

##### IPv4

| Interface | VRF | IP Address | IP Address Virtual | IP Router Virtual Address | VRRP | ACL In | ACL Out |
| --------- | --- | ---------- | ------------------ | ------------------------- | ---- | ------ | ------- |
| Vlan10 |  VRF_A  |  -  |  10.1.10.1/24  |  -  |  -  |  -  |  -  |
| Vlan20 |  VRF_A  |  -  |  10.1.20.1/24  |  -  |  -  |  -  |  -  |
| Vlan30 |  Tenant_B  |  -  |  10.1.30.1/24  |  -  |  -  |  -  |  -  |
| Vlan3009 |  VRF_A  |  10.255.251.20/31  |  -  |  -  |  -  |  -  |  -  |
| Vlan3019 |  Tenant_B  |  10.255.251.20/31  |  -  |  -  |  -  |  -  |  -  |
| Vlan4093 |  default  |  -  |  -  |  -  |  -  |  -  |  -  |
| Vlan4094 |  default  |  10.255.252.20/31  |  -  |  -  |  -  |  -  |  -  |

#### VLAN Interfaces Device Configuration

```eos
!
interface Vlan10
   description DMZ
   no shutdown
   vrf VRF_A
   ip address virtual 10.1.10.1/24
!
interface Vlan20
   description Internal
   no shutdown
   vrf VRF_A
   ip address virtual 10.1.20.1/24
!
interface Vlan30
   description B
   no shutdown
   vrf Tenant_B
   ip address virtual 10.1.30.1/24
!
interface Vlan3009
   description MLAG_PEER_L3_iBGP: vrf VRF_A
   no shutdown
   mtu 1550
   vrf VRF_A
   ip address 10.255.251.20/31
!
interface Vlan3019
   description MLAG_PEER_L3_iBGP: vrf Tenant_B
   no shutdown
   mtu 1550
   vrf Tenant_B
   ip address 10.255.251.20/31
!
interface Vlan4093
   description MLAG_PEER_L3_PEERING
   no shutdown
   mtu 1550
   ipv6 enable
!
interface Vlan4094
   description MLAG_PEER
   no shutdown
   mtu 1550
   no autostate
   ip address 10.255.252.20/31
```

### VXLAN Interface

#### VXLAN Interface Summary

| Setting | Value |
| ------- | ----- |
| Source Interface | Loopback1 |
| UDP port | 4789 |
| EVPN MLAG Shared Router MAC | mlag-system-id |

##### VLAN to VNI, Flood List and Multicast Group Mappings

| VLAN | VNI | Flood List | Multicast Group |
| ---- | --- | ---------- | --------------- |
| 10 | 10010 | - | - |
| 20 | 10020 | - | - |
| 30 | 10030 | - | - |

##### VRF to VNI and Multicast Group Mappings

| VRF | VNI | Multicast Group |
| ---- | --- | --------------- |
| Tenant_B | 20 | - |
| VRF_A | 10 | - |

#### VXLAN Interface Device Configuration

```eos
!
interface Vxlan1
   description leaf1_VTEP
   vxlan source-interface Loopback1
   vxlan virtual-router encapsulation mac-address mlag-system-id
   vxlan udp-port 4789
   vxlan vlan 10 vni 10010
   vxlan vlan 20 vni 10020
   vxlan vlan 30 vni 10030
   vxlan vrf Tenant_B vni 20
   vxlan vrf VRF_A vni 10
```

## Routing

### Service Routing Protocols Model

Multi agent routing protocol model enabled

```eos
!
service routing protocols model multi-agent
```

### Virtual Router MAC Address

#### Virtual Router MAC Address Summary

##### Virtual Router MAC Address: 02:1c:73:00:00:99

#### Virtual Router MAC Address Configuration

```eos
!
ip virtual-router mac-address 02:1c:73:00:00:99
```

### IP Routing

#### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | True (ipv6 interfaces) |
| MGMT | False |
| Tenant_B | True |
| VRF_A | True |

#### IP Routing Device Configuration

```eos
!
ip routing ipv6 interfaces
no ip routing vrf MGMT
ip routing vrf Tenant_B
ip routing vrf VRF_A
```

### IPv6 Routing

#### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | True |
| MGMT | false |
| Tenant_B | false |
| VRF_A | false |

#### IPv6 Routing Device Configuration

```eos
!
ipv6 unicast-routing
```

### Static Routes

#### Static Routes Summary

| VRF | Destination Prefix | Next Hop IP             | Exit interface      | Administrative Distance       | Tag               | Route Name                    | Metric         |
| --- | ------------------ | ----------------------- | ------------------- | ----------------------------- | ----------------- | ----------------------------- | -------------- |
| MGMT | 0.0.0.0/0 | 192.168.0.1 | - | 1 | - | - | - |

#### Static Routes Device Configuration

```eos
!
ip route vrf MGMT 0.0.0.0/0 192.168.0.1
```

### Router BGP

#### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65111|  192.168.101.11 |

| BGP Tuning |
| ---------- |
| no bgp default ipv4-unicast |
| maximum-paths 4 ecmp 4 |

#### Router BGP Peer Groups

##### EVPN-OVERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | evpn |
| Source | Loopback0 |
| BFD | True |
| Ebgp multihop | 3 |
| Send community | all |
| Maximum routes | 0 (no limit) |

##### IPv4-UNDERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Send community | all |
| Maximum routes | 12000 |

##### MLAG-IPv4-UNDERLAY-PEER

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Remote AS | 65111 |
| Next-hop self | True |
| Send community | all |
| Maximum routes | 12000 |

#### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain | Route-Reflector Client | Passive |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- | ---------------------- | ------- |
| 192.168.101.101 | 65100 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.102 | 65100 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.103 | 65100 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.104 | 65100 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 10.255.251.21 | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | Tenant_B | - | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | - | - | - | - | - |
| 10.255.251.21 | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | VRF_A | - | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | - | - | - | - | - |

#### BGP Neighbor Interfaces

| Neighbor Interface | VRF | Peer Group | Remote AS | Peer Filter |
| ------------------ | --- | ---------- | --------- | ----------- |
| Ethernet3 | default | IPv4-UNDERLAY-PEERS | 65100 | - |
| Ethernet4 | default | IPv4-UNDERLAY-PEERS | 65100 | - |
| Ethernet5 | default | IPv4-UNDERLAY-PEERS | 65100 | - |
| Ethernet6 | default | IPv4-UNDERLAY-PEERS | 65100 | - |
| Vlan4093 | default | MLAG-IPv4-UNDERLAY-PEER | 65111 | - |

#### Router BGP EVPN Address Family

##### EVPN Peer Groups

| Peer Group | Activate | Encapsulation |
| ---------- | -------- | ------------- |
| EVPN-OVERLAY-PEERS | True | default |

#### Router BGP VLANs

| VLAN | Route-Distinguisher | Both Route-Target | Import Route Target | Export Route-Target | Redistribute |
| ---- | ------------------- | ----------------- | ------------------- | ------------------- | ------------ |
| 10 | 192.168.101.11:10010 | 10010:10010 | - | - | learned |
| 20 | 192.168.101.11:10020 | 10020:10020 | - | - | learned |
| 30 | 192.168.101.11:10030 | 10030:10030 | - | - | learned |

#### Router BGP VRFs

| VRF | Route-Distinguisher | Redistribute |
| --- | ------------------- | ------------ |
| Tenant_B | 192.168.101.11:20 | connected |
| VRF_A | 192.168.101.11:10 | connected |

#### Router BGP Device Configuration

```eos
!
router bgp 65111
   router-id 192.168.101.11
   maximum-paths 4 ecmp 4
   no bgp default ipv4-unicast
   neighbor EVPN-OVERLAY-PEERS peer group
   neighbor EVPN-OVERLAY-PEERS update-source Loopback0
   neighbor EVPN-OVERLAY-PEERS bfd
   neighbor EVPN-OVERLAY-PEERS ebgp-multihop 3
   neighbor EVPN-OVERLAY-PEERS send-community
   neighbor EVPN-OVERLAY-PEERS maximum-routes 0
   neighbor IPv4-UNDERLAY-PEERS peer group
   neighbor IPv4-UNDERLAY-PEERS send-community
   neighbor IPv4-UNDERLAY-PEERS maximum-routes 12000
   neighbor MLAG-IPv4-UNDERLAY-PEER peer group
   neighbor MLAG-IPv4-UNDERLAY-PEER remote-as 65111
   neighbor MLAG-IPv4-UNDERLAY-PEER next-hop-self
   neighbor MLAG-IPv4-UNDERLAY-PEER description leaf2
   neighbor MLAG-IPv4-UNDERLAY-PEER send-community
   neighbor MLAG-IPv4-UNDERLAY-PEER maximum-routes 12000
   neighbor MLAG-IPv4-UNDERLAY-PEER route-map RM-MLAG-PEER-IN in
   neighbor interface Ethernet3 peer-group IPv4-UNDERLAY-PEERS remote-as 65100
   neighbor interface Ethernet4 peer-group IPv4-UNDERLAY-PEERS remote-as 65100
   neighbor interface Ethernet5 peer-group IPv4-UNDERLAY-PEERS remote-as 65100
   neighbor interface Ethernet6 peer-group IPv4-UNDERLAY-PEERS remote-as 65100
   neighbor interface Vlan4093 peer-group MLAG-IPv4-UNDERLAY-PEER remote-as 65111
   neighbor 192.168.101.101 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.101 remote-as 65100
   neighbor 192.168.101.101 description spine1
   neighbor 192.168.101.102 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.102 remote-as 65100
   neighbor 192.168.101.102 description spine2
   neighbor 192.168.101.103 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.103 remote-as 65100
   neighbor 192.168.101.103 description spine3
   neighbor 192.168.101.104 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.104 remote-as 65100
   neighbor 192.168.101.104 description spine4
   redistribute connected route-map RM-CONN-2-BGP
   !
   vlan 10
      rd 192.168.101.11:10010
      route-target both 10010:10010
      redistribute learned
   !
   vlan 20
      rd 192.168.101.11:10020
      route-target both 10020:10020
      redistribute learned
   !
   vlan 30
      rd 192.168.101.11:10030
      route-target both 10030:10030
      redistribute learned
   !
   address-family evpn
      neighbor EVPN-OVERLAY-PEERS activate
   !
   address-family ipv4
      no neighbor EVPN-OVERLAY-PEERS activate
      neighbor IPv4-UNDERLAY-PEERS next-hop address-family ipv6 originate
      neighbor IPv4-UNDERLAY-PEERS activate
      neighbor MLAG-IPv4-UNDERLAY-PEER next-hop address-family ipv6 originate
      neighbor MLAG-IPv4-UNDERLAY-PEER activate
   !
   vrf Tenant_B
      rd 192.168.101.11:20
      route-target import evpn 20:20
      route-target export evpn 20:20
      router-id 192.168.101.11
      neighbor 10.255.251.21 peer group MLAG-IPv4-UNDERLAY-PEER
      redistribute connected
      !
      address-family ipv4
         no neighbor 10.255.251.21 next-hop address-family ipv6
   !
   vrf VRF_A
      rd 192.168.101.11:10
      route-target import evpn 10:10
      route-target export evpn 10:10
      router-id 192.168.101.11
      neighbor 10.255.251.21 peer group MLAG-IPv4-UNDERLAY-PEER
      redistribute connected
      !
      address-family ipv4
         no neighbor 10.255.251.21 next-hop address-family ipv6
```

## BFD

### Router BFD

#### Router BFD Multihop Summary

| Interval | Minimum RX | Multiplier |
| -------- | ---------- | ---------- |
| 1200 | 1200 | 3 |

#### Router BFD Device Configuration

```eos
!
router bfd
   multihop interval 1200 min-rx 1200 multiplier 3
```

## Multicast

### IP IGMP Snooping

#### IP IGMP Snooping Summary

| IGMP Snooping | Fast Leave | Interface Restart Query | Proxy | Restart Query Interval | Robustness Variable |
| ------------- | ---------- | ----------------------- | ----- | ---------------------- | ------------------- |
| Enabled | - | - | - | - | - |

#### IP IGMP Snooping Device Configuration

```eos
```

## Filters

### Prefix-lists

#### Prefix-lists Summary

##### PL-LOOPBACKS-EVPN-OVERLAY

| Sequence | Action |
| -------- | ------ |
| 10 | permit 192.168.101.0/24 eq 32 |
| 20 | permit 192.168.102.0/24 eq 32 |

#### Prefix-lists Device Configuration

```eos
!
ip prefix-list PL-LOOPBACKS-EVPN-OVERLAY
   seq 10 permit 192.168.101.0/24 eq 32
   seq 20 permit 192.168.102.0/24 eq 32
```

### Route-maps

#### Route-maps Summary

##### RM-CONN-2-BGP

| Sequence | Type | Match | Set | Sub-Route-Map | Continue |
| -------- | ---- | ----- | --- | ------------- | -------- |
| 10 | permit | ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY | - | - | - |

##### RM-MLAG-PEER-IN

| Sequence | Type | Match | Set | Sub-Route-Map | Continue |
| -------- | ---- | ----- | --- | ------------- | -------- |
| 10 | permit | - | origin incomplete | - | - |

#### Route-maps Device Configuration

```eos
!
route-map RM-CONN-2-BGP permit 10
   match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY
!
route-map RM-MLAG-PEER-IN permit 10
   description Make routes learned over MLAG Peer-link less preferred on spines to ensure optimal routing
   set origin incomplete
```

## VRF Instances

### VRF Instances Summary

| VRF Name | IP Routing |
| -------- | ---------- |
| MGMT | disabled |
| Tenant_B | enabled |
| VRF_A | enabled |

### VRF Instances Device Configuration

```eos
!
vrf instance MGMT
!
vrf instance Tenant_B
!
vrf instance VRF_A
```
