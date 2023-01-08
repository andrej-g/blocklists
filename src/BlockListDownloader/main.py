import os
import requests
import datetime
import logging

from Blocklist import Blocklist
from Templates import Templates
from MikroTik import MikroTik
from IPTables import IPTables

logging.basicConfig(
    filename="blocklistdownloader.log",
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

timestamp: str = datetime.datetime.now().strftime("%Y-%m-%d")

local_ip_ranges = [
    "0.0.0.0/8",
    "224.0.0.0/3",
    "10.0.0.0/8",
    "172.16.0.0/12",
    "192.168.0.0/16",
    "127.0.0.0/8",
    "169.254.0.0/16"
]

directories: dict = {
    "temp": "./temp",
    "mikrotik": "./mikrotik",
    "iptables": "./iptables"
}

country_codes: dict = {
    "brazil": "br",
    "russian_federation": "ru",
    "ukraine": "ua",
    "india": "in",
    "china": "cn",
    "taiwan": "tw",
    "hong_kong": "hk",
    "hungary": "hu",
    "turkey": "tr",
    "pakistan": "pk"
}

blocklists = [
    Blocklist("firehol_l1",
              "https://iplists.firehol.org/files/firehol_level1.netset",
              f'{directories["temp"]}/firehol_l1_{timestamp}.txt'),
    Blocklist("firehol_l2",
              "https://iplists.firehol.org/files/firehol_level2.netset",
              f'{directories["temp"]}/firehol_l2_{timestamp}.txt'),
    Blocklist("digitalocean",
              "https://digitalocean.com/geo/google.csv",
              f'{directories["temp"]}/digitalocean_{timestamp}.txt')
]


def check_directories():
    logging.info("\n-------------------------\n--- Checking directories.\n-------------------------")
    for directory, path in directories.items():
        if not os.path.isdir(path):
            logging.info(f"{path} doesn't exist. Creating.")
            try:
                os.mkdir(path)
            except Exception as ex:
                logging.fatal(f"Fatal exception when creating {path}. {ex}")
        else:
            logging.info(f"{path} exists.")


def generate_download_urls():
    logging.info("\n--------------------------------\n--- Generating blocklist urls...\n--------------------------------")
    for country, country_code in country_codes.items():
        logging.info(f"[{country_code}] {country}")
        blocklists.append(Blocklist(f"{country}_full",
                                    Templates.ipdeny_full_zone.replace(Templates.country_code_placeholder, country_code),
                                    f'{directories["temp"]}/{country}_full_{timestamp}.txt'))
        blocklists.append(Blocklist(f"{country}_aggregated",
                                    Templates.ipdeny_aggregated_zone.replace(Templates.country_code_placeholder, country_code),
                                    f'{directories["temp"]}/{country}_aggregated_{timestamp}.txt'))


def download_blocklists():
    logging.info("\n-----------------------------\n--- Downloading blocklists...\n-----------------------------")
    for blocklist in blocklists:
        try:
            logging.info(f"[{blocklist.name}]")
            if not os.path.exists(blocklist.filename):
                logging.info(f"{blocklist.filename} doesn't exist, downloading.")
                request = requests.get(blocklist.url)
                with open(blocklist.filename, "wb") as out:
                    out.write(request.content)
            else:
                logging.info(f"{blocklist.filename} exist, skipping.")
        except Exception as ex:
            logging.error(f"Error downloading {blocklist.name}. {ex}")


def process_blocklists():
    logging.info("\n----------------------------\n--- Processing blocklists...\n----------------------------")
    for blocklist in blocklists:
        logging.info(f'[{blocklist.name}]')

        if not os.path.exists(blocklist.filename):
            logging.error(f"{blocklist.filename} doesn't exist!")
            break

        logging.info("MikroTik")
        mikrotik: MikroTik = MikroTik(blocklist, directories, local_ip_ranges, Templates, timestamp)
        mikrotik.process_file()

        logging.info("IPTables")
        iptables: IPTables = IPTables(blocklist, directories, local_ip_ranges, timestamp)
        iptables.process_file()


if __name__ == '__main__':
    logging.info("---> Start.")
    check_directories()
    generate_download_urls()
    download_blocklists()
    process_blocklists()
    logging.info("End. <---")
