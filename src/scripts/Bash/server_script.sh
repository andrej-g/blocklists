#!/bin/bash

TELEGRAM_BIN="/usr/local/bin/telegram.sh/telegram"

SERVERNAME="SERVERNAME"
LOGTAG="[$SERVERNAME BLOCKLIST UPDATER]"

GIT_REPO="https://github.com/andrej-g/blocklists.git"
BLOCKLIST_ROOT_DIR="/usr/local/sbin/blocklists/"
BLOCKLIST_GIT_DIR="/usr/local/sbin/blocklists/blocklists/"
BLOCKLIST_SET_DIR="/usr/local/sbin/blocklists/blocklists/iptables/"

declare -A BLOCKSETS
BLOCKSETS=(
  ["firehol_l1"]="firehol_l1.txt"
  ["firehol_l2"]="firehol_l2.txt"
  ["digitalocean"]="digitalocean.txt"
  ["brazil_full"]="brazil_full.txt"
  ["china_full"]="china_full.txt"
  ["hong_kong_full"]="hong_kong_full.txt"
  ["hungary_full"]="hungary_full.txt"
  ["india_full"]="india_full.txt"
  ["pakistan_full"]="pakistan_full.txt"
  ["russian_federation_full"]="russian_federation_full.txt"
  ["taiwan_full"]="taiwan_full.txt"
  ["turkey_full"]="turkey_full.txt"
  ["ukraine_full"]="ukraine_full.txt"
)

# region functions

logInfo () {
  local log="$LOGTAG INFO - $1"
  echo "$log"
  logger "$log"
}

logWarning () {
  local log="$LOGTAG WARN - $1"
  echo "$log"
  logger "$log"
}

logError () {
  local log="$LOGTAG ERROR - $1"
  echo "$log"
  logger "$log"
}

logErrorTelegram () {
  $TELEGRAM_BIN -H "<b>${LOGTAG}</b> - &#10060; $1"
}

# endregion

logInfo "blocklist update start."

# check if $BLOCKLIST_GIT_DIR exists, clone repository if not
# should execute only on first script run, additional checks below
if [ ! -d "$BLOCKLIST_GIT_DIR" ]; then
  logInfo "blocklist dir doesn't exist, cloning."
  cd $BLOCKLIST_GIT_DIR
  git clone $GIT_REPO
  cd $BLOCKLIST_ROOT_DIR
fi;

# naively check if $BLOCKLIST_GIT_DIR/.git exists
# if true pull repository, else exit

if [ ! -d "$BLOCKLIST_GIT_DIR/.git" ]; then
  logError ".git doesn't exist but should. Aborting."
  logErrorTelegram ".git doesn't exist but should. Aborting."
  exit 1
else
  logInfo ".git exists, pulling new version."
  cd $BLOCKLIST_GIT_DIR
  git pull
  cd $BLOCKLIST_ROOT_DIR
fi;

cd $BLOCKLIST_SET_DIR

for blockset in "${!BLOCKSETS[@]}"; do

  SET_NAME=$blockset
  SET_FILENAME=${BLOCKSETS[$SET_NAME]}

  echo "$SET_NAME $SET_FILENAME"

  if [ ! -f "./$SET_FILENAME" ]; then
    logWarning "$SET_FILENAME for $SET_NAME doesn't exist, skipping."
    continue
  fi;

  logInfo "updating set $SET_NAME from $SET_FILENAME."

  logInfo "deleting iptables rule for $SET_NAME"
  iptables -D INPUT -m set --match-set $SET_NAME src -j DROP
  sleep 1
  logInfo "flushing ipset $SET_NAME"
  ipset flush $SET_NAME
  sleep 1
  logInfo "destroying ipset $SET_NAME"
  ipset destroy $SET_NAME
  sleep 1
  logInfo "creating ipset $SET_NAME"
  ipset create $SET_NAME hash:net
  sleep 1
  logInfo "reading ipset $SET_NAME from $SET_FILENAME"
  while read line; do ipset add $SET_NAME $line; done < ./$SET_FILENAME
  logInfo "adding iptables rule for $SET_NAME"
  iptables -I INPUT -m set --match-set $SET_NAME src -j DROP

done;

logInfo "saving ipsets"
iposet save > /etc/ipset.conf

logInfo "saving iptables"
netfilter-persistent save

logInfo "reloading iptables"
netfilter-persistent reload

logInfo "blocklist update end"