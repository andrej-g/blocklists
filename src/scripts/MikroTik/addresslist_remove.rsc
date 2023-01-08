# remove addresslists

log info message="[addresslist remove] removing address lists start"

# IPWhiteList
log info message="[addresslist remove] remove IP White List"
/ip firewall address-list remove [/ip firewall address-list find list="IPWhiteList"]

# not_in_internet
log info message="[addresslist remove] remove not_in_internet"
/ip firewall address-list remove [/ip firewall address-list find list="not_in_internet"]

# brazil_aggregated
log info message="[addresslist remove] remove Brazil - aggregated"
/ip firewall address-list remove [/ip firewall address-list find list="brazil_aggregated"]

# china_aggregated
log info message="[addresslist remove] remove China - aggregated"
/ip firewall address-list remove [/ip firewall address-list find list="china_aggregated"]

# digitalocean
log info message="[addresslist remove] remove DigitalOcean"
/ip firewall address-list remove [/ip firewall address-list find list="digitalocean"]

# firehol_l1
log info message="[addresslist remove] remove FireHOL Level 1"
/ip firewall address-list remove [/ip firewall address-list find list="firehol_l1"]

# firehol_l2
log info message="[addresslist remove] remove FireHOL Level 2"
/ip firewall address-list remove [/ip firewall address-list find list="firehol_l2"]

# hong_kong_aggregated
log info message="[addresslist remove] remove Hong Kong - aggregated"
/ip firewall address-list remove [/ip firewall address-list find list="hong_kong_aggregated"]

# hungary_aggregated
log info message="[addresslist remove] remove Hungary - aggregated"
/ip firewall address-list remove [/ip firewall address-list find list="hungary_aggregated"]

# india_aggregated
log info message="[addresslist remove] remove India - aggregated"
/ip firewall address-list remove [/ip firewall address-list find list="india_aggregated"]

# pakistan_aggregated
log info message="[addresslist remove] remove Pakistan - aggregated"
/ip firewall address-list remove [/ip firewall address-list find list="pakistan_aggregated"]

# russian_federation_aggregated
log info message="[addresslist remove] remove Russian federation - aggregated"
/ip firewall address-list remove [/ip firewall address-list find list="russian_federation_aggregated"]

# taiwan_aggregated
log info message="[addresslist remove] remove Taiwan - aggregated"
/ip firewall address-list remove [/ip firewall address-list find list="taiwan_aggregated"]

# turkey_aggregated
log info message="[addresslist remove] remove Turkey - aggregated"
/ip firewall address-list remove [/ip firewall address-list find list="turkey_aggregated"]

# ukraine_aggregated
log info message="[addresslist remove] remove Ukraine - aggregated"
/ip firewall address-list remove [/ip firewall address-list find list="ukraine_aggregated"]

log info message="[addresslist remove] removing address lists end"