# Log2multichain

# Description

Log collector capable to process rsyslog logs and send them to a MultiChain stream providing immutable audit trail.

Could be useful when multiple entities want to have a common shared and immutable audit trail.

# How to configure


1. Configure variable from configs.py file.
2. Configure rsyslog log collection using directives like:

```
[root@stage ~]# cat /etc/rsyslog.d/50-myapp.conf 
module(load="omprog")


if $programname == 'AppWorkflow' and $msg contains 'Application' then action(type="omprog"
       binary="/opt/bluedrive/p3-venv/bin/python3.6 /opt/bluedrive/log2multichain/log2multichain.py"
       template="RSYSLOG_TraditionalFileFormat")

```

# Support
For support you can contact me via e-mail: alexandru.bujor at bluedrive.ro

https://bluedrive.ro

