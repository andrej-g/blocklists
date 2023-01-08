import logging
import os

from Blocklist import Blocklist
from Templates import Templates


class MikroTik:

    def __init__(self, blocklist: Blocklist, directories: dict, local_ip_ranges: list[str], templates: type[Templates], timestamp: str):
        self.destination_file: str = blocklist.filename \
            .replace(directories["temp"], directories["mikrotik"]) \
            .replace(f"_{timestamp}", "") \
            .replace(".txt", ".rsc")
        self.blocklist: Blocklist = blocklist
        self.directories: dict = directories
        self.local_ip_ranges: list[str] = local_ip_ranges
        self.templates: type[Templates] = templates

    def process_file(self):
        try:
            if os.path.exists(self.destination_file):
                logging.info(f"{self.destination_file} exists, deleting.")
        except Exception as ex:
            logging.error(f"Error deleting {self.destination_file}. {ex}")

        try:
            with open(self.blocklist.filename, "r") as source_file:
                with open(self.destination_file, "w") as destination_file:
                    destination_file.write(self.templates.mikrotik_rsc_header)
                    for line in source_file:
                        # filter out local ip ranges
                        # strip comments

                        if self.local_ip_ranges.__contains__(line.strip()):
                            continue

                        if line.startswith("#"):
                            continue

                        # DigitalOcean exception, as DI's IP ranges come in CSV form
                        # 159.89.32.0/20,US,US-NJ,Clifton,07014
                        # strip everything after (and including) the first comma

                        if self.blocklist.name == "digitalocean":
                            # skip IPV6 addresses
                            if line.__contains__("::"):
                                continue
                            line = line.split(",")[0]

                        newline: str = self.templates.mikrotik_list_template \
                            .replace(self.templates.mikrotik_address_placeholder, line.strip()) \
                            .replace(self.templates.mikrotik_comment_placeholder, self.blocklist.name) \
                            .replace(self.templates.mikrotik_list_placeholder, self.blocklist.name)

                        destination_file.write(newline)
            logging.info(f"Wrote {self.destination_file}.")
        except Exception as ex:
            logging.error(f'Error processing {self.blocklist.name}. {ex}')
