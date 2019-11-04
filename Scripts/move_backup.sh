#!/bin/bash

sshpass -p $3 rsync -zvh $1@$2:$4$6 ${10} 
sshpass -p $5 rsync -zvh ${10}$6  $7@$8:$9 

