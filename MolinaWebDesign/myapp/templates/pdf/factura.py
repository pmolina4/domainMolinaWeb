import pdfkit
import jinja2
from datetime import datetime


my_name = "Pablo Molina"
item1 = "TV"
item2 = "Mueble"
item3 = "Lavadora"
today_date = datetime.today().strftime("%d/%m/%Y, %H:%M:%S")

context = {'my_name' : my_name, "item1" : item1, "item2" : item2, "item3" : item3, "today_date" : today_date}


template_loader = jinja2.FileSystemLoader('MolinaWebDesign/myapp/templates/pdf')
template_env = jinja2.Environment(loader=template_loader)

html_template = 'plantilla.html'

template = template_env.get_template(html_template)

output_text = template.render(context)

config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')

output_pdf = 'pdf_generado.pdf'

pdfkit.from_string(output_text, output_pdf, configuration=config)