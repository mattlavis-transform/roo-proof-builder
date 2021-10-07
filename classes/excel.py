import xlrd
import os
from classes.country import Row, Country


class Excel(object):
    def __init__(self):
        self.excel_path = os.path.realpath(os.path.join(os.getcwd(), "source", "proofs of origin.xlsx"))
        self.rows = []
        self.countries = []

    def read(self):
        wb = xlrd.open_workbook(self.excel_path)
        sheet = wb.sheet_by_index(0)
        rowcount = sheet.nrows

        for i in range(2, rowcount):
            country_bloc = sheet.cell_value(i, 0)
            original = sheet.cell_value(i, 1)
            scheme_class = sheet.cell_value(i, 2)
            link_text = sheet.cell_value(i, 3)
            sub_text = sheet.cell_value(i, 4)

            if country_bloc.strip() != "":
                row = Row(country_bloc, original, scheme_class, link_text, sub_text)
                self.rows.append(row)
                
        self.rows = sorted(self.rows, key=lambda country: country.country_bloc)
        self.form_countries()

    def form_countries(self):
        for row in self.rows:
            matched = False
            for country in self.countries:
                if country.country_bloc == row.country_bloc:
                    country.rows.append(row)
                    matched = True
                    break
            if not matched:
                country = Country(row)
                self.countries.append(country)

        a = 1
