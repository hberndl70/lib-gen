# BASICS

## In a firewall rule what does the CIDR notation `1.1.1.1/0` mean?

[ ] All IP addresses starting with `1.1.1` are allowed.

[ ] Only the IP `1.1.1.1` is allowed.

[x] The whole internet is allowed.

[ ] Nothing is allowed.

[ ] The notation is incorrect.

===

# BASICS

##  What is an IP address? 

[x] A numerical label assigned to each device connected to a computer network that uses the Internet Protocol.

[ ] An identifier both for the host and the host’s location.

===

# BASICS

##  What is ICMP good for?

[x] To ping a server if it is running.

[ ] To keep a TCP connection alive.

[x] To indicate if fragmentation is needed.

[ ] None of the above.

===

# BASICS

##  Which of the following is a valid IPv6 address?

[x] `fe80::1`

[ ] `1:1:1:1`

[x] `db8:0:0:0:0:0:accc:1`

[ ] `1.1.1.1`

[ ] `192.168.0.356`

===

# BASICS

## How does a browser know a website certificate is valid?

[ ] The certificate is signed by a government entity.

[x] The certificate is signed by a known Certificate Authority.

[ ] The certificate is signed the Domain Owner.

[ ] None of the above.

===

# BASICS

## What is the difference between TCP and UDP?

[ ] TCP is used for control, UDP for data flow.

[x] TCP provides a continuous stream of packets, where UDP sends single packets.

[x] TCP has protections against losing packets, UDP does not

[ ] TCP and UDP are essentially the same.

===

# BASICS

## Which of the following IPv4 address are valid?

[ ] `192.168.0.356`

[ ] `fe80::1`

[x] `10.0.0.1`

[ ] `172.24.0.1.2`

[x] `1.1.1.1`

[ ] `19.3.2`

===

# CLOUD ARCHITECTURE

## Which of the following is true about the Exoscale Object Storage?

[ ] It can be plugged in to an Exoscale instance as a second disk

[x] It can be used as a long-term file storage.

[ ] It simulates a full file system.

===

# CLOUD ARCHITECTURE

## Which of the following hinders a web application from scaling to multiple servers?

[ ] Having a relational database.

[x] Writing files to the local disk.

[x] Not having a shared session storage.

===

# CLOUD ARCHITECTURE

## What is the most typical way of creating backups in an on-premises system?

[ ] Database snapshots

[x] Disk snapshots of the virtual machine

[ ] File backups

===

# CLOUD ARCHITECTURE

## Which of the following can be used to remotely manage Windows machines programmatically on Exoscale?

[ ] SSH

[x] WinRM

[ ] VNC

===

# CLOUD ARCHITECTURE

## What is cloud-init?

[ ] A tool to quickly configure Exoscale.

[x] A tool to run an automated program at the start of an instance.

[ ] A best practice configuration for clouds.

===

# CLOUD ARCHITECTURE

## Why do you use a CI/CD system?

[x] To speed up releases of a particular software.

[x] To enable more frequent, smaller releases.

[x] To reduce manual errors.

[ ] None of the above.

===

# CLOUD ARCHITECTURE

## What are the drawbacks of locally attached disks?

[ ] Worse access speed.

[x] When the physical hardware fails, the data on the disk may be lost.

[ ] None of the above.

===

# CLOUD ARCHITECTURE

## What is Infrastructure as Code?

[ ] The process of deploying code onto a cloud infrastructure.

[x] The concept of writing code, which is then used to automatically create a cloud infrastructure.

[ ] An export that saves your cloud configuration for archive purposes.

===

# CLOUD ARCHITECTURE

## What are microservices?

[ ] A new business idea that service providers should only focus on a single task.

[x] Breaking up large, complex applications into smaller parts that communicate with each other.

[ ] None of the above.

===

# CLOUD ARCHITECTURE

## Which of the following is true about snapshot backups?

[ ] Snapshots are the state of the art way to create backups.

[x] Snapshots do not guarantee the consistency of a backup while the instance is running.

[x] Shutting down an instance before making a snapshot guarantees a consistent backup.

===

# CLOUD ARCHITECTURE

## What are the benefits of locally attached disks?

[x] Faster access speeds.

[ ] Fault-tolerance, even when the physical hardware fails.

[ ] None of the above.

===

# CLOUD ARCHITECTURE

## What does CI stand for in CI/CD?

[x] Continuous Integration

[ ] Continuous Installation

[ ] Contingency Instance

[ ] None of the above

===

# CLOUD ARCHITECTURE

## What does CD stand for in CI/CD?

[ ] Continuous Development

[x] Continuous Delivery

[ ] Continuity Description

[ ] None of the above

===

# CLOUD ARCHITECTURE

## What is the benefit of microservices?

[ ] Easier to manage.

[x] Easier to scale under load.

[ ] Easier to debug, smaller services.

===

# CLOUD ARCHITECTURE

## What is important for a good CI/CD pipeline?

[ ] There must be a dedicated person to trigger the builds.

[x] Automated tests.

[ ] The software must run in a cloud.

[x] A high degree of automation.

===

# CLOUD ARCHITECTURE

## How does a typical CI/CD integration work?

[x] Code Versioning System `->` CI/CD `->` Production

[ ] CI/CD `->` Code Versioning System `->` Production

[ ] Production `->` CI/CD `->` Code Versioning System

===

# CLOUD ARCHITECTURE

## What is NFS?

[ ] Network Flux Storage

[x] Network File System

[ ] Network Fault System

[ ] Network Fibre System

===

# CLOUD SECURITY

## What is TOTP?

[x] A time-based two-factor authentication system.

[ ] A hardware token.

[ ] A firewall.

===

# CLOUD SECURITY

## What is Server Side Request Forgery?

[ ] When an attacker gets the server to execute arbitrary code.

[x] When an attacker gets the server to fetch and return information from a separate internal system.

[ ] When an attacker injects malicious code in a website.

===

# CLOUD SECURITY

## Which of the following are best practices when deploying web servers?

[x] Deploy TLS

[x] Deploy HSTS

[x] Deploy CSRF-Token

===

# CLOUD SECURITY

## Which of the following is a security scanning tool?

[x] nmap

[x] Burp Suite

[x] Nessus

[ ] None of the above.

===

# CLOUD SECURITY

## Which of the following are security best practices?

[x] Every company should make sure every employee has their own account and passwords are not shared.

[x] Every company should enforce two-factor authentication.

[ ] Every company should create their own, custom encryption to stop attackers.

[x] Every company should regularly scan their infrastructure for security problems.

[x] Every company should use encrypted connections whenever feasible.

[x] Every company should conduct disaster recovery drills.

===

# CONNECTIVITY

## Based on what factors can security groups filter?

[x] Network parameters (IP address, port, protocol)

[ ] The requested web address

[ ] Encryption

===

# CONNECTIVITY

## What is the default EGRESS policy on Exoscale Security Groups?

[x] Accept

[ ] Deny

===

# CONNECTIVITY

## How can you connect an on-premises setup to an Exoscale private network?

[x] Using a VPN.

[x] Using an SD-WAN solution.

[x] Using MPLS

===

# CONNECTIVITY

## What is the default INGRESS policy on Exoscale Security Groups?

[ ] Accept

[x] Deny

===

# CONNECTIVITY

## If a security group has no rules set up, can two servers in that security group communicate with each other?

[ ] Yes

[x] No

===

# CONNECTIVITY

## What purpose does a VPN serve?

[ ] It protects you from hackers by encrypting your IP address.

[x] It creates a virtual, encrypted network connection between two points over the Internet that behaves like a long network cable.

[ ] None of the above.

===

# CONNECTIVITY

## What is the purpose of a load balancer?

[ ] It makes sure the electricity is properly balanced over the cables.

[x] It balances incoming traffic between multiple backend servers to ensure good performance and redundancy.

[x] In some cases it handles the connection encryption to save resources on the backend servers.

[ ] It lets an application run on multiple servers without any changes to the application.

===

# CONNECTIVITY

## What are Exoscale Security Groups?

[ ] An auditing tool

[x] Network firewalls

[ ] A virus scanner

===

# CONNECTIVITY

## Which of the following is true about unmanaged (v1) Elastic IP addresses?

[ ] They can act as a load balancer and be active on multiple instances at the same time.

[x] They provide an IP address that can be moved between machines, but cannot be active on multiple machines at the same time.

===

# CONNECTIVITY

## Which of the following is true on an Exoscale public network?

[x] You can only send packets with the Exoscale-assigned MAC address.

[x] You can only send packets with the Exoscale-assigned IP address.

[ ] None of the above, you can send with any MAC or IP.

===

# CONNECTIVITY

## Which of the following is true on an Exoscale private network?

[ ] You can send a packet with any MAC address.

[x] You can send a packet with any IP address.

[ ] Neither, you can only use MAC and IP addresses that have been assigned.

===

# CONNECTIVITY

## Which interfaces does the firewall configured by Exoscale Security Groups apply to?

[x] Public

[ ] Private

===

# CONNECTIVITY

## Which of the following is true about managed (v2) Elastic IPs?

[x] They can be used as a simple load balancer.

[ ] Managed elastic IPs have to be added to the instance on the instance itself.

[ ] Managed elastic IPs can terminate an encrypted (TLS) connections.

===

# CONTAINER ARCHITECTURE 

## Where are container images typically stored?

[ ] On the Exoscale object storage

[x] In a registry

[ ] In a repository

[ ] On the build server

===

# CONTAINER ARCHITECTURE 

## Which of the following is a container orchestrator?

[x] Docker Swarm

[x] Kubernetes

[x] OpenShift

[x] Rancher

===

# CONTAINER ARCHITECTURE 

## What is the result of a container build process?

[ ] A container

[x] A container image

[ ] A registry

[ ] A template

[ ] A repository

===

# CONTAINER ARCHITECTURE 

## Which of the following are included in Kubernetes by default?

[ ] A registry

[ ] A redundant storage

[x] An API

[ ] A CI/CD system

===

# CONTAINER ARCHITECTURE 

## What is Rancher?

[x] A Kubernetes management platform

[ ] A container build tool

[ ] A container deployment tool

===

# CONTAINER ARCHITECTURE 

## What are containers in the context of a cloud?

[ ] A standard way of storing data in the cloud.

[x] A standard way of packaging software with the run-time environment and shipping it to production.

[ ] A standard way of moving data across the network.

[ ] A standard way to package video data.

===

# CONTAINER ARCHITECTURE 

## What is the difference between a virtual machine and a container?

[x] Containers typically share the underlying operating system, while virtual machines each have their own operating system.

[ ] With containers operating systems are no longer needed.

[ ] Virtual machines can be limited in how much resources they use, where containers cannot.

[ ] They are basically the same.

===

# CONTAINER ARCHITECTURE 

## How is the file called that containers are built from?

[ ] Containerfile

[x] Dockerfile

[ ] Recipe

[ ] Docker

[ ] Kubefile

===

# DATABASE ARCHITECTURE

## Which company owns MSSQL / SQL Server?

[x] Microsoft

[ ] Oracle

[ ] Amazon

[ ] Teradata

[ ] SAP

[ ] Owned by an Open Source Association

===

# DATABASE ARCHITECTURE

## How many database nodes do you need at least for a strictly consistent, distributed database setup?

[ ] At least 1

[ ] At least 2

[x] At least 3

[ ] At least 4

[ ] At least 5

===

# DATABASE ARCHITECTURE

## What is a split-brain?

[ ] When the cluster configuration is not valid and the cluster cannot function.

[ ] When the cluster is split into a production and development part.

[x] When the cluster splits into two parts and they contain conflicting data.

===

# DATABASE ARCHITECTURE

## Which of the following is a relational database system?

[x] MySQL

[x] Oracle

[x] PostgreSQL

[ ] MongoDB

[ ] Redis

[ ] Exoscale Object Storage

===

# DATABASE ARCHITECTURE

## Which database system does MariaDB originate from?

[ ] It is an original software

[x] MySQL

[ ] PostgreSQL

[ ] MongoDB

[ ] Redis

[ ] ElasticSearch

===

# DATABASE ARCHITECTURE

## Which company owns MySQL?

[ ] Microsoft

[x] Oracle

[ ] Amazon

[ ] Teradata

[ ] SAP

[ ] Owned by an Open Source Association

===

# DATABASE ARCHITECTURE

## What is a quorum?

[x] A majority vote in a cluster of servers.

[ ] When a smaller group of machines splits off a bigger cluster and forms their own cluster.

[ ] When the cluster breaks apart and can no longer function

[ ] When the cluster splits into two parts and they contain conflicting data.

===

# MONITORING

## Which of the following are self-hosted monitoring software?

[x] Icinga

[ ] New Relic

[ ] UptimeRobot

[ ] DataDog

[x] Zabbix

===

# MONITORING

## Which of the following are a good way to monitor if my web application is running properly?

[x] Deploy a software that actively loads the web application every few minutes.

[x] Deploy a software that collects the statistics from the web application and checks if enough users access it, no errors happen, etc.

[x] Deploy a software that scans the error logs of the application for anomalies.

===

# MONITORING

## Which of the following tools have built-in alerting?

[X] Prometheus

[ ] Supervisord

[ ] Helm

[X] Icinga

===