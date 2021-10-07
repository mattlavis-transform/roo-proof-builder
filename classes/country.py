import os
import sys


class Row(object):
    def __init__(self, country_bloc, original, scheme_class, link_text, sub_text):
        self.country_bloc = country_bloc
        self.original = original
        self.scheme_class = scheme_class
        self.link_text = link_text
        self.sub_text = sub_text
        self.url_base = "https://www.gov.uk/guidance/get-proof-of-origin-for-your-goods"
        self.get_url()

    def get_url(self):
        if self.scheme_class == "origin-declaration":
            self.url = self.url_base + "#origin-declaration"
        elif self.scheme_class == "eur1-eur-med":
            self.url = self.url_base + "#eur1-and-eur-med-movement-certificates"
        elif self.scheme_class == "importers-knowledge":
            self.url = self.url_base + "#importers-knowledge"
        elif self.scheme_class == "gsp-form-a":
            self.url = self.url_base + "#generalised-scheme-of-preferences-form-a"
        else:
            self.url = ""
            print("Missing scheme class on country", self.country_bloc)
            # sys.exit()

class Country(object):
    def __init__(self, row):
        self.country_bloc = row.country_bloc
        self.rows = []
        self.rows.append(row)
        pass
