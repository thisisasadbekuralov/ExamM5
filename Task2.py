import pdfkit
import threading

# 2-masala 2- variant

def main(a):
    pdfkit.from_url(
        base_url + str(a) + '/', 'sinonim' + str(a) + '.html', configuration=config)


path_wkhtmltopdf = r"C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
base_url = 'https://tilshunos.com/sinonims/'


threads = []

for i in range(1, 13):
    thread = threading.Thread(target=main, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()




