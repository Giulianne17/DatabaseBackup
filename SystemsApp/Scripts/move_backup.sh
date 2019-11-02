#!/bin/bash

sshpass -p $3 ssh $1@$2
echo $3 | sudo -S apt-get install sshpass
sshpass -p $4 rsync -zvh $5/$6  $7@$8:$9 

exit


