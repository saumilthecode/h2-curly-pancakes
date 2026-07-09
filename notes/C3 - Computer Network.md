> [!summary] Quick View
> A computer network connects devices so data can move through local hardware, routers, servers, and global links.

## Hosts, Nodes, and Media

| Term | Meaning |
| ---- | ------- |
| Host | client or server on a network |
| Node | network interface used by a device, such as NIC, Wi-Fi, Bluetooth, or infrared |
| Medium | physical or wireless path carrying the signal |

Network media:

- copper cable carries electrical signals
- fibre optic cable carries light pulses
- wireless carries electromagnetic waves

## Network Types

| Type | Scale |
| ---- | ----- |
| PAN | personal area, a few metres |
| LAN | local area, usually a room/building |
| WLAN | wireless LAN |
| CAN | campus area, multiple nearby LANs |
| MAN | metropolitan area, city scale |
| WAN | wide area, country/global scale; the internet is a WAN |
| SAN | storage area network for high-speed data storage |

## Topologies

| Topology | Idea | Risk |
| -------- | ---- | ---- |
| Bus | all devices share one cable | cable break can collapse network |
| Ring | devices form a closed loop | single failure can disrupt traffic |
| Star | all devices connect to a central switch | switch is single point of failure |
| Mesh | devices connect to many or all others | high cost and complexity |

For a fully meshed network:

```text
connections = n * (n - 1) / 2
```

## Switches and Routers

| Device | Layer | Uses | Purpose |
| ------ | ----- | ---- | ------- |
| Hub | Layer 1 | no addressing | broadcasts to all ports |
| Switch | Layer 2 | MAC addresses | connects devices inside one LAN |
| Router | Layer 3 | IP addresses | connects different networks |

A switch builds a Source Address Table (SAT):

- it starts empty
- it records source MAC addresses and ports from incoming frames
- if destination is unknown, it broadcasts to other ports
- after replies, future traffic can be sent directly to the correct port

## MAC and IP Addresses

| Address | Meaning | Scope |
| ------- | ------- | ----- |
| MAC address | physical device identity | local delivery inside LAN |
| IP address | logical network location | routing between networks |

MAC address:

- 48-bit hexadecimal
- example: `00-16-EA-06-6C-3E`
- usually built into the network interface

IPv4 address:

- 32-bit address
- often written as four decimal numbers
- example: `192.168.0.1`

The IP address gets data to the correct network. The MAC address gets data to the correct device inside that local network.

## Subnet Mask and Gateway

A subnet mask decides whether two IP addresses are in the same local network.

Example:

```text
IP:          192.168.0.10
Subnet mask: 255.255.255.0
Network:     192.168.0
```

If a destination is outside the local network, the device sends the packet to its default gateway, usually the router.

## Packet Switching

The internet uses packet switching.

- Data is split into packets.
- Each packet can travel independently.
- Packets may take different routes.
- The destination reassembles them in order.

Packet parts:

| Part | Contains |
| ---- | -------- |
| Header | source IP, destination IP, protocol, sequence number |
| Payload | actual data |
| Trailer | error checking such as CRC |

Circuit switching reserves one fixed path for the whole communication. Packet switching is more flexible and resilient for internet traffic.

## Servers

A server provides services to clients.

Examples:

- web server
- DNS server
- DHCP server
- mail server
- file server

Enterprise servers are designed for reliability:

- run 24/7
- handle many concurrent connections
- may use ECC RAM
- may use RAID storage
- may use redundant power supplies
- may support hot-swappable drives

## DNS

DNS means Domain Name System.

It translates names into IP addresses.

```text
www.yijc.edu.sg -> 192.168.0.12
```

Basic lookup path:

1. browser asks resolver
2. resolver may ask root server
3. root server points to TLD server such as `.com` or `.sg`
4. TLD points to authoritative name server
5. authoritative server returns the IP address

DNS avoids memorising numerical IP addresses.

## DHCP

DHCP means Dynamic Host Configuration Protocol.

It automatically gives devices network settings:

- IP address
- subnet mask
- default gateway
- DNS server

DHCP uses leases. When a device leaves and the lease expires, the IP address returns to the pool.

## Email Protocols

| Protocol | Purpose |
| -------- | ------- |
| SMTP | sends email from client to server and between mail servers |
| POP3 | downloads mail to one device, often removing it from the server |
| IMAP | keeps mail on the server and synchronises across devices |

SMTP uses TCP to help ensure mail delivery.

## Filius Hands-On Settings

Peer-to-peer example:

```text
Notebook 1: 192.168.0.10
Notebook 2: 192.168.0.11
Subnet:    255.255.255.0
```

LANs connected by router:

```text
LAN1 network: 192.168.0
Router NIC1: 192.168.0.1

LAN2 network: 192.168.1
Router NIC2: 192.168.1.1
```

Devices in LAN1 use gateway `192.168.0.1`. Devices in LAN2 use gateway `192.168.1.1`.

DNS server example:

```text
DNS server: 192.168.2.10
Router NIC: 192.168.2.1
Domain:     www.yijc.edu.sg
Web server: 192.168.0.12
```

Useful tests:

```text
ping 192.168.0.11
ipconfig
http://192.168.0.12
http://www.yijc.edu.sg
```

## Related

- [[C2 - Data representation]]
- [[File Handling]]
