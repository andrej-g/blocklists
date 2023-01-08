import os
import logging

from Blocklist import Blocklist


class IPTables:

    def __init__(self, blocklist: Blocklist, directories: dict, local_ip_ranges: list[str], timestamp: str):
        self.destination_file: str = blocklist.filename \
            .replace(directories["temp"], directories["iptables"]) \
            .replace(f"_{timestamp}", "")
        self.blocklist: Blocklist = blocklist
        self.directories: dict = directories
        self.local_ip_ranges: list[str] = local_ip_ranges

    def process_file(self):
        # strip comments
        # remove local ip ranges
        # pass ip ranges as-is?

        try:
            if os.path.exists(self.destination_file):
                logging.info(f"{self.destination_file} exists, deleting.")
        except Exception as ex:
            logging.error(f"Error deleting {self.destination_file}. {ex}")

        try:
            with open(self.blocklist.filename, "r") as source_file:
                with open(self.destination_file, "w") as destination_file:
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
                            if line.__contains__("::"):
                                continue
                            line = f'{line.split(",")[0]}\n'

                        destination_file.write(line)
            logging.info(f"Wrote {self.destination_file}.")
        except Exception as ex:
            logging.error(f'Error processing {self.blocklist.name}. {ex}')
