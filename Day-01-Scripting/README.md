Automated Backup Script
## this script take backup from folder with archeving and named her date and move it to another path and print message success or fail in terminal

## steps
1- vi autobackup.sh
2- copy and paste in autobackup
  #!/bin/bash

SOURCE="/home/alaa/file22"
DEST="/home/alaa/15-Days_Devops-Bootcamp/Day-01-Scripting"
DATE=$(date +%Y-%m-%d)
FILE_NAME="backup_$DATE.tar.gz"
tar -czf "$DEST/$FILE_NAME" "$SOURCE"

if [ $? -eq 0 ]
then
    echo "Backup created successfully"
    echo "Location: $DEST/$FILE_NAME"
else
    echo "Backup failed"
fi
~      
3- run: bash autobackup.sh 
