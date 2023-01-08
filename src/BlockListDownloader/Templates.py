class Templates:
    country_code_placeholder: str = "[[[cc]]]"
    mikrotik_address_placeholder: str = "[[[mikrotik_address]]]"
    mikrotik_comment_placeholder: str = "[[[mikrotik_comment]]]"
    mikrotik_list_placeholder: str = "[[[mikrotik_list]]]"
    ipdeny_full_zone: str = f"https://www.ipdeny.com/ipblocks/data/countries/{country_code_placeholder}.zone"
    ipdeny_aggregated_zone: str = f"https://www.ipdeny.com/ipblocks/data/aggregated/{country_code_placeholder}-aggregated.zone"
    mikrotik_rsc_header: str = "/ip firewall address-list\n"
    mikrotik_list_template: str = f'add address="{mikrotik_address_placeholder}" comment="{mikrotik_comment_placeholder}" list="{mikrotik_list_placeholder}"\n'