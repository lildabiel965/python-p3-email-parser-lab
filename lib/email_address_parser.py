import re

class EmailAddressParser:
    def __init__(self, email_addresses):
        self.email_addresses = email_addresses

    def parse(self):
        # Split by commas or spaces
        addresses = re.split(r"[,\s]+", self.email_addresses)
        # Remove empty strings and strip whitespace
        cleaned_addresses = [address.strip() for address in addresses if address.strip()]
        # Filter out non-email strings using a simple regex pattern
        email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        valid_emails = [address for address in cleaned_addresses if re.match(email_pattern, address)]
        # Ensure uniqueness and sort alphabetically
        unique_emails = sorted(list(set(valid_emails)))
        return unique_emails