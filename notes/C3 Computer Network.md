> [!summary] Quick View
> A network connects devices so data can move between them. IP gets data to the right **network**; MAC gets it to the right **device**.

> [!important] What 4.1 examines
> Five outcomes. (4.2 Web Applications is the other half of Module 4 — taught later.)
>
> | Outcome | Where |
> | ------- | ----- |
> | 4.1.1 LAN, WAN, intranet, structure of the internet | Network Types, Internet ≠ Web |
> | 4.1.2 IP addressing and DNS | Addressing, DNS |
> | 4.1.3 need for communication protocols | Why Protocols Are Needed |
> | 4.1.4 how data is transmitted in a packet-switching network | Packet Switching |
> | 4.1.5 client–server architecture | Client–Server vs Peer-to-Peer |
>
> Everything else here — topologies, the switch's SAT, DHCP, SMTP/POP3/IMAP, RAID — came from the C3a lecture and videos. **Not named** in y27. Read it, don't drill it. The 2020–2024 papers are the old syllabus, so use them for the concepts, not to guess what's coming.

## Network Types

| Type | Scale |
| ---- | ----- |
| PAN | personal, a few metres |
| LAN | one room or building |
| WLAN | wireless LAN |
| CAN | campus — several nearby LANs |
| MAN | city scale |
| WAN | country or global; the internet is a WAN |
| SAN | storage area network |

> [!important] Internet ≠ Web
> | | Is |
> | --- | -- |
> | Internet | the infrastructure — cables, routers, connected machines |
> | Web | one service on it — pages and links, over HTTP |
>
> Email, DNS and file transfer also run on the internet but are not the web.

- Backbone: **fibre optic cable**, much of it undersea.
- Satellite reaches where cables can't, but the round trip adds **latency**.

**Intranet** — an organisation's private network using internet technologies (web pages, email), with controlled external access.

## Client–Server vs Peer-to-Peer

| | Client–server | Peer-to-peer |
| --- | ------------- | ------------ |
| Roles | server provides, clients request | every device does both |
| Data | centralised on the server | spread across devices |
| Backup / admin | done centrally | done on each device |
| Cost | needs dedicated server hardware | no dedicated hardware |
| Failure | server is a single point of failure | no single point of failure |
| Suits | large networks | small networks |

## Why Protocols Are Needed

A protocol is an agreed set of rules for communication. Without one:

- devices from different manufacturers, running different software, cannot interpret each other's data
- there is no agreement on message **format**, **order**, **speed** or **error checking**
- receivers cannot identify message boundaries

## Hosts, Nodes and Media

| Term | Meaning |
| ---- | ------- |
| Host | a client or server on the network |
| Node | anything on the network — host, switch or router |
| Medium | the physical or wireless path the signal travels |

Media: copper cable carries electrical signals, fibre optic carries light pulses, wireless carries electromagnetic waves.

## Addressing

| Address | Identifies | Scope |
| ------- | ---------- | ----- |
| MAC | the physical device | delivery **within** a LAN |
| IP | the device's network location | routing **between** networks |

- **MAC** — 48-bit, hexadecimal, e.g. `00-16-EA-06-6C-3E`, built into the NIC
- **IPv4** — 32-bit, four decimal numbers `0`–`255` separated by dots, e.g. `192.168.0.1`

**Two ways to identify a device on a LAN:** its MAC address and its IP address.

Two ways to allocate an IP address:

- **Statically** — set by hand, and it stays put
- **Dynamically** — assigned automatically from a pool by a **DHCP** server, on a lease

> [!important]
> ARP finds a device's MAC address from its IP address within a LAN.

> [!important] Along the route
> Destination **IP stays the same** end-to-end; **MAC changes at every hop** to identify the next device on the link.
>
>
> ```mermaid
> flowchart LR
>     PC([PC]) -->|"MAC: PC to A"| RA[router A]
>     RA -->|"MAC: A to B"| RB[router B]
>     RB -->|"MAC: B to server"| S([server])
> ```
>

MAC is fixed in the NIC; IP changes when moving networks.

### Private vs Public IP

| | Private | Public |
| --- | ------- | ------ |
| Used | inside a LAN | on the internet |
| Routable on the internet | no | yes |
| Assigned by | the local router / DHCP | the ISP |
| Example | `192.168.0.3` | `192.166.122.7` |

Going out, the router swaps the private source IP for its public one; coming back, it swaps it back.

### Subnet Mask and Gateway

The subnet mask decides whether two IP addresses are on the same local network.

```text
IP:          192.168.0.10
Subnet mask: 255.255.255.0
Network:     192.168.0        < the part the mask keeps
```

Send non-local traffic to the **default gateway** (router).

## Packet Switching

The internet uses packet switching.

- data is split into packets
- each packet travels independently and may take a different route
- the destination reassembles them in order using the sequence numbers

| Packet part | Contains |
| ----------- | -------- |
| Header | source IP, destination IP, protocol, sequence number |
| Payload | the data |
| Trailer | error check, e.g. CRC |

Circuit switching reserves a fixed path throughout communication. Packet switching is more resilient: packets can reroute around failures.

**Why data is divided into packets** — small packets share the links fairly rather than one large transfer blocking them, and a corrupted packet only needs that packet resent, not the whole file.

**Why packets are sequentially numbered** — they arrive out of order after taking different routes, so the numbers let the destination **reassemble them correctly** and spot any that are missing.

**Disadvantage, and how it is handled** — packets may arrive out of order, be delayed, or be lost. Sequence numbers reorder them; anything that fails its error check or never arrives is **requested again and retransmitted**.

**Role of a router** — it inspects each packet's destination **IP address** and forwards it along the best available route towards that network, hop by hop.

## TCP

Transmission Control Protocol — **connection-oriented** and **reliable**. A session has three stages: set up, transfer, close.

### Three-Way Handshake

```mermaid
sequenceDiagram
    participant C as Client
    participant S as Server
    C->>S: SYN
    S->>C: SYN + ACK
    C->>S: ACK
    Note over C,S: connection established
```

| Step | Meaning |
| ---- | ------- |
| `SYN` | "can we talk?" |
| `SYN + ACK` | "yes — and can we talk?" |
| `ACK` | "yes" |

Closing takes **four** steps: `FIN`, `ACK`, `FIN`, `ACK` — each side must close its own direction.

During transfer TCP guarantees packets are **delivered** and **reassembled in order**, requesting retransmission of anything missing.

| State | Meaning |
| ----- | ------- |
| LISTEN | server waiting for a connection request |
| ESTABLISHED | handshake done, data flowing |
| CLOSED | no connection |

## Switches and Routers

| Device | Layer | Uses | Purpose |
| ------ | ----- | ---- | ------- |
| Hub | 1 | no addressing | broadcasts to every port |
| Switch | 2 | MAC addresses | connects devices **inside** one LAN |
| Router | 3 | IP addresses | connects **different** networks |

A switch builds a **Source Address Table (SAT)**:

1. starts empty
2. records the source MAC address and port of each incoming frame
3. broadcasts to all other ports when the destination is unknown
4. once a reply arrives, sends future traffic straight to the correct port

## Topologies

| Topology | Idea | Risk |
| -------- | ---- | ---- |
| Bus | all devices share one cable | a cable break collapses the network |
| Ring | devices form a closed loop | one failure can disrupt traffic |
| Star | all devices connect to a central switch | the switch is a single point of failure |
| Mesh | devices connect to many or all others | high cost and complexity |

Star is the most common in a LAN. For a fully meshed network:

```text
connections = n * (n - 1) / 2
```

## Servers

A server provides services to clients: web, DNS, DHCP, mail, file.

Enterprise servers are built for reliability — run 24/7, handle many concurrent connections, and may use ECC RAM, RAID storage, redundant power supplies and hot-swappable drives.

## DNS

Translates domain names into IP addresses, so nobody has to memorise numbers.

```text
www.yijc.edu.sg  ->  192.168.0.12
```

1. browser asks the resolver
2. resolver asks a root server
3. root points to the TLD server (`.com`, `.sg`)
4. TLD points to the authoritative name server
5. authoritative server returns the IP address

## DHCP

Dynamic Host Configuration Protocol — automatically gives a device its IP address, subnet mask, default gateway and DNS server.

Addresses are handed out on a **lease**. When the lease expires the address returns to the pool for reuse.

## Email Protocols

| Protocol | Purpose |
| -------- | ------- |
| SMTP | sends mail from client to server, and between mail servers |
| POP3 | downloads mail to one device, usually removing it from the server |
| IMAP | keeps mail on the server and syncs it across devices |

SMTP runs over TCP to help ensure delivery.

> [!example]- Filius hands-on settings
> Peer-to-peer:
>
> ```text
> Notebook 1: 192.168.0.10
> Notebook 2: 192.168.0.11
> Subnet:     255.255.255.0
> ```
>
> Two LANs joined by a router:
>
> ```text
> LAN1 network: 192.168.0      Router NIC1: 192.168.0.1
> LAN2 network: 192.168.1      Router NIC2: 192.168.1.1
> ```
>
> Devices in LAN1 use gateway `192.168.0.1`; devices in LAN2 use `192.168.1.1`.
>
> DNS server:
>
> ```text
> DNS server: 192.168.2.10     Domain:     www.yijc.edu.sg
> Router NIC: 192.168.2.1      Web server: 192.168.0.12
> ```
>
> Tests:
>
> ```text
> ping 192.168.0.11
> ipconfig
> http://192.168.0.12
> http://www.yijc.edu.sg
> ```

## Exam

> [!important] 2025 Promo P1 Q6 — from USB drives to a LAN to the cloud `[8]`
> **(a)** Two disadvantages of sharing files on removable drives `[2]`, any two:
> - data lost if the drive is misplaced, stolen or damaged
> - malware spreads between machines
> - unauthorised access to the data
> - no real-time collaboration
>
> **(b)** Two LAN functions besides file sharing `[2]`, any two:
> - shared printers and scanners
> - one shared internet connection to the ISP
> - software installed once on an application server
> - internal mail or messaging
> - centralised backup
> - centralised security: authentication, firewall, antivirus
>
> **(c)** Two advantages of a cloud provider `[2]`, any two:
> - no upfront hardware cost, pay only for what you use, no maintenance
> - scales up or down with demand
> - ready immediately, without buying and setting up hardware
> - high availability through redundancy
> - accessible from anywhere with an internet connection
>
> **(d)** One more cloud service and its benefit `[1+1]` — IaaS (virtual networks, firewalls), PaaS (databases, web hosting) or SaaS (Microsoft 365, Google Workspace).
>
> Cloud computing is outside y27; the 2025 promo asked it anyway.

> [!important] 2024 Promo P1 Q5 — joining two companies' LANs `[2+2+2+2+1]`
> **(a)** A = **switch** (inside a LAN), B = **router** (between LANs).
>
> **(b)** Two differences, any two:
>
> | | Switch | Router |
> | --- | ------ | ------ |
> | Connects | devices **within** one network | **different** networks |
> | Forwards by | MAC address | IP address |
> | Job | delivers to the right device | picks the best path between networks |
>
> **(c)** Joining networks by cable, one each:
> - **Advantage:** more reliable (less interference), faster with lower latency, more secure (needs physical access), consistent through walls
> - **Disadvantage:** costly to install, inflexible when moving or adding devices, needs maintenance, hard to scale
>
> **(d)** Connecting via the internet instead: **security risk** — hacking, data breaches, cyberattacks `[2]`.
> **(e)** Fix: a **VPN**, **firewall** or passwords, or **encrypt** the data, e.g. over HTTPS `[1]`.
>
> 2026 Mastery P1 Q5 repeats (a) and (b).

## Related

- [[C2 Data representation]]
- [[LT10d Hashing]]
