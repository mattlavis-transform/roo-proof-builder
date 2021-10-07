import os
import sys


class Prototype(object):
    def __init__(self, excel):
        # Set the paths
        self.template_path = os.path.realpath(os.path.join(os.getcwd(), "templates"))
        self.index_file = os.path.join(self.template_path, "index.html")
        self.country_file = os.path.join(self.template_path, "country.html")
        self.proof_file = os.path.join(self.template_path, "proof.html")

        self.output_path = os.path.realpath(os.path.join(os.getcwd(), "output"))
        self.html_path = os.path.join(self.output_path, "proofs.html")
        self.excel = excel

        self.get_templates()

    def get_templates(self):
        # Load in the templates
        f = open(self.index_file, "r")
        self.index_template = f.read()
        f.close()

        f = open(self.country_file, "r")
        self.country_template = f.read()
        f.close()

        f = open(self.proof_file, "r")
        self.proof_template = f.read()
        f.close()

    def generate_html(self):
        print("Generating HTML")
        countries_html = ""
        for country in self.excel.countries:
            country_html = self.country_template
            country_html = country_html.replace("{{ country_bloc }}", country.country_bloc)
            if len(country.rows) == 1:
                country_html = country_html.replace("one of the following proofs of origin", "the following proof of origin")
                
            proofs_html = ""
            for row in country.rows:
                r = self.proof_template
                r = r.replace("{{ link_text }}", row.link_text)
                r = r.replace("{{ url }}", row.url)
                if row.sub_text != "" and row.sub_text != "n/a":
                    r = r.replace("{{ sub_text }}", "<br>" + row.sub_text)
                else:
                    r = r.replace("{{ sub_text }}", "<br>&nbsp;")

                proofs_html += r

            country_html = country_html.replace("{{ steps }}", proofs_html)
            countries_html += country_html
            pass

        html = self.index_template
        html = html.replace("{{ countries }}", countries_html)
        f = open(self.html_path, "w")
        f.write(html)
        f.close()
