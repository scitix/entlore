## Mysql Deployment
- Install mysql as the guide’s baseline deployment step.
- Use /etc/mysql/mysql.conf.d/mysqld.cnf as Ubuntu’s default MySQL config path.
- Add the required permissions for the newly created data directory.
- Restart apparmor before running the MySQL data-directory initialization.
 apt install mysql-server -y
 mkdir -p /data/mysql/data /data/mysql/logs
 chown -R mysql:mysql /data/mysql/data
 chown -R mysql:mysql /data/mysql/logs
 chmod 700 /data/mysql/data
 chmod 750 /data/mysql/logs
[mysqld]
datadir = /data/mysql/data
socket  = /data/mysql/mysql.sock
vim  /etc/apparmor.d/usr.sbin.mysqld
/data/mysql/data/ r,
/data/mysql/data/** rwk,

## Master-master Synchronization Configuration
- Initialize MySQL by running mysqld as mysql with --initialize and --datadir=/data/mysql/data.
- This section covers the master-master synchronization setup.
- Apply the listed synchronization commands on 10.188.41.192.
- Apply the matching synchronization commands on 10.143.204.24.
systemctl start mysql
sudo systemctl status mysql
- On 10.188.41.192, define 'updater'@'10.143.204.24' with password 'vexeum@2025!'.
- Grant 'updater'@'10.143.204.24' REPLICATION SLAVE and REPLICATION CLIENT access on *.*, then flush privileges.
CHANGE REPLICATION SOURCE TO
SOURCE_HOST='10.143.204.24',
SOURCE_USER='updater',
SOURCE_PASSWORD='devcaa@8056!',
SOURCE_AUTO_POSITION=1;
START REPLICA;
- On 10.143.204.24, define 'updater'@'10.188.41.192' with password 'vexeum@2025!'.
- Grant 'updater'@'10.188.41.192' REPLICATION SLAVE and REPLICATION CLIENT access on *.*, then flush privileges.

## keepalived Installation and Configuration
- Run the additional synchronization commands on 10.143.204.24.
- Include the redo step for the synchronization setup.
- Verify replication with SHOW REPLICA STATUS\G.
- Install keepalived by using apt install keepalived -y.
- The keepalived.conf content provides the keepalived configuration.
- Configure monitoring with /usr/local/keepalived/scripts/mysql_check.sh 127.64.221.129 3306.
- Set interval 5 for the monitoring check cadence.
- Set timeout 120 for the check timeout.
- Use priority 120 as the weight value.
- Enable nopreempt for a backup node whose priority is higher than the other node.
- Use auth_type PASS for encryption.
- Set auth_pass 2393 as the password.
CHANGE REPLICATION SOURCE TO
SOURCE_HOST='10.188.41.192',
SOURCE_USER='updater',
SOURCE_PASSWORD='devcaa@8056!',
SOURCE_AUTO_POSITION=1;
START REPLICA;
STOP REPLICA;
RESET REPLICA ALL;
# Configuration File for keepalived
global_defs {
  router_id mysql1
}
vrrp_script chk_mysql {
  fall 3
}
vrrp_instance mysql {
  state BACKUP
  interface ens160
  lvs_sync_daemon_interface ens160
  virtual_router_id 1
  advert_int 1
  authentication {                          #all node must same
  }
  virtual_ipaddress {
    10.196.166.33
  }
  track_script {
    chk_mysql
 }
notify_fault /usr/local/keepalived/scripts/mysql_fault.sh
notify_stop /usr/local/keepalived/scripts/mysql_stop.sh
}

| Item | Details |
|---|---|
| Bash script listener check | ALIVE is set by counting netstat listeners on 0.73.135.100:3306 with timeout 30. |
mkdir -p /usr/local/keepalived/scripts
cat /usr/local/keepalived/scripts/mysql_check.sh
LOGFILE="/var/log/keepalived-mysql-check.log"
echo "[CHECK]" >> $LOGFILE
date >> $LOGFILE
if [[ $ALIVE -eq 1 ]]; then :
   echo "Success: mysql  $ALIVE" >> $LOGFILE 2>&1
    exit 0
else
    echo "Failed:mysql  $ALIVE " >> $LOGFILE 2>&1
    exit 1
fi
chmod 777  /usr/local/keepalived/scripts/mysql_check.sh
chmod 777 /usr/local/keepalived/scripts/mysql_stop.sh
chmod 777 /usr/local/keepalived/scripts/mysql_fault.sh
systemctl   enable  keepalived.service
systemctl   restart  keepalived.service
systemctl   status   keepalived.service
 vim /usr/local/keepalived/scripts/mysql_fault.sh
#!/bin/bash
LOGFILE="/var/log/keepalived-mysql-state.log"
echo "[fault]" >> $LOGFILE
date >> $LOGFILE
cat /usr/local/keepalived/scripts/mysql_stop.sh
#!/bin/bash
LOGFILE="/var/log/keepalived-mysql-state.log"
echo "[stop]" >> $LOGFILE
date >> $LOGFILE