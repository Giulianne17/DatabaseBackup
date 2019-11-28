#!/bin/bash
sshpass -p $3 rsync -zvh $1@$2:$4$5 $6 

