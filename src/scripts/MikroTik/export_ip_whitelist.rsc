{
    log info message="[export-ipwhitelist] start"
    :local listName "IPWhiteList"; #change this
    :local fileName "IPWhiteList_exported.rsc"; #appends .txt!
    :local buffer;

    :global filteredList [/ip firewall address-list print as-value where list=$listName && dynamic=no];
    :foreach i in=$filteredList do={
        :set $buffer ($buffer."add address=".$i->"address"." comment=\"".$i->"comment"."\" list=".$listName.";\r\n")
    };
    /file print file=$fileName where name="";
    :delay 1s;
    :set $buffer ("/ip firewall address-list;\r\n".$buffer);
    /file set $fileName contents=$buffer;
    log info message="[export-ipwhitelist] end"
}