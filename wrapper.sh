#!/usr/bin/bash

# Path to discord binary
DISCORD_BIN=$(dirname $(readlink -f $0))/Discord

# Run python script to disable check updates
/usr/lib64/discord/disable-breaking-updates.py

# Launch discord
exec "$DISCORD_BIN" "$@"
