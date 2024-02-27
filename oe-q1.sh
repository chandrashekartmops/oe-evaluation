#!/bin/bash

# Define the directory where the logs are located
logs_dir="/path/to/logs"

# Define the directory where the backup will be stored
backup_dir="/path/to/backup"

# Create the backup directory if it doesn't exist
mkdir -p "$backup_dir"

# Get the current date in YYYYMMDD format
current_date=$(date +"%Y%m%d")

# Create the archive filename
archive_name="logs-$current_date.tar.gz"

# Find all .log files within the logs directory and its subdirectories
find "$logs_dir" -type f -name "*.log" -print0 |
  # Compress the files into a single archive
  tar -czvf "$backup_dir/$archive_name" --null -T -

echo "Backup completed: $backup_dir/$archive_name"
