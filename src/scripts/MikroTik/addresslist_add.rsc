# load address lists from usb (/disk2/blocklists)

log info message="[addresslist add] import address lists start"

log info message="[addresslist add] import IP White List"
import /disk2/IPWhiteList_exported.rsc.txt

log info message="[addresslist add] import not_in_internet"
import /disk2/not_in_internet.rsc

log info message="[addresslist add] import Brazil - aggregated"
import /disk2/blocklists/brazil_aggregated.rsc

log info message="[addresslist add] import China - aggregated"
import /disk2/blocklists/china_aggregated.rsc

log info message="[addresslist add] import DigitalOcean"
import /disk2/blocklists/digitalocean.rsc

log info message="[addresslist add] import FireHOL Level 1"
import /disk2/blocklists/firehol_l1.rsc

log info message="[addresslist add] import FireHOL Level 2"
import /disk2/blocklists/firehol_l2.rsc

log info message="[addresslist add] import Hong Kong - aggregated"
import /disk2/blocklists/hong_kong_aggregated.rsc

log info message="[addresslist add] import Hungary - aggregated"
import /disk2/blocklists/hungary_aggregated.rsc

log info message="[addresslist add] import India - aggregated"
import /disk2/blocklists/india_aggregated.rsc

log info message="[addresslist add] import Pakistan - aggregated"
import /disk2/blocklists/pakistan_aggregated.rsc

log info message="[addresslist add] import Russian federation - aggregated"
import /disk2/blocklists/russian_federation_aggregated.rsc

log info message="[addresslist add] import Taiwan - aggregated"
import /disk2/blocklists/taiwan_aggregated.rsc

log info message="[addresslist add] import Turkey - aggregated"
import /disk2/blocklists/turkey_aggregated.rsc

log info message="[addresslist add] import Ukraine - aggregated"
import /disk2/blocklists/ukraine_aggregated.rsc

log info message="[addresslist add] import address lists end"