#!/usr/bin/sh

# os.tmpdir from node.js
for OS_TMPDIR in "$TMPDIR" "$TMP" "$TEMP" /tmp
do
  test -n "$OS_TMPDIR" && break
done

# kill any currently running Discord
if pgrep Discord ; then
  pkill Discord
  sleep 1
  pkill -9 Discord
fi

# This is probably just paranoia, but some people claim that clearing out
# cache and/or the sock file fixes bugs for them, so here we go
for DIR in /home/* ; do
  rm -rf "$DIR/.config/discord/Cache"
  rm -rf "$DIR/.config/discord/GPUCache"

  # A previous bug made some files in this folder owned by root
  # and discord will hang if those files are present
  SETTINGS_FILE="$DIR/.config/discord/Crashpad/settings.dat"
  if [ -f "$SETTINGS_FILE" ]; then
    OWNER=$(stat -c "%U" "$SETTINGS_FILE")
    if [ "$OWNER" = "root" ]; then
      rm -rf "$DIR/.config/discord/Crashpad"
    fi
  fi
done
rm -f "$OS_TMPDIR/discord.sock"

### START OF PATCH (SKIP CHECK UPDATE POP-UP) ###
# Check if discord user configuration directory exist
DISCORD_USER_CONFIG_DIR="/home/$(logname)/.config/discord"
DISCORD_USER_SETTINGS_JSON_FILE="/home/$(logname)/.config/discord/settings.json"
if [ ! -d "$DISCORD_USER_CONFIG_DIR" ]; then
    mkdir -m 700 "$DISCORD_USER_CONFIG_DIR"
    chown $(logname):$(logname) "$DISCORD_USER_CONFIG_DIR"
fi

# If 'settings.json' file doesn't exist: create file and set "SKIP_HOST_UPDATE" to true
if [ ! -f "$DISCORD_USER_SETTINGS_JSON_FILE" ]; then
    echo '{
    "SKIP_HOST_UPDATE": true
}' >"$DISCORD_USER_SETTINGS_JSON_FILE"
    chmod 644 "$DISCORD_USER_SETTINGS_JSON_FILE"
    chown $(logname):$(logname) "$DISCORD_USER_SETTINGS_JSON_FILE"
# If 'settings.json' file exist and if "SKIP_HOST_UPDATE" doesn't set : keep user settings
# and add "SKIP_HOST_UPDATE" line to the file
elif ! grep "SKIP_HOST_UPDATE" "$DISCORD_USER_SETTINGS_JSON_FILE"; then
    echo "$(grep -v '^}' $DISCORD_USER_SETTINGS_JSON_FILE),
	\"SKIP_HOST_UPDATE\": true
}" >"$DISCORD_USER_SETTINGS_JSON_FILE"
fi
### END OF PATCH (SKIP CHECK UPDATE POP-UP) ###