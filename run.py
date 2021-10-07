from classes.excel import Excel
from classes.prototype import Prototype


excel = Excel()
excel.read()
prototype = Prototype(excel)
prototype.generate_html()
