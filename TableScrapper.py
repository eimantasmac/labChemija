import urllib.request
import re
from bs4 import BeautifulSoup


class Table:

    def GetTable(url):
        html = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(html, "html.parser")
        list_of_rows = []
        all_tables = ""
        for table in soup.findAll('table', {'class': 'infobox'}):

            # remove all extra tags in the HTML Tables
            for div in soup.findAll('span', 'sortkey'):
                div.extract();
            for div in soup.findAll('span', {'style':'display:none'}):
                div.extract();

            #scan through table
            for row in table.findAll('tr')[1:]:
                list_of_cells = []
                for cell in row.findAll('td'):
                    list_of_cells.append(cell.text)
                list_of_rows.append(list_of_cells)

            all_tables += str(table)

        all_tables = re.sub ('<[^>]+>', '', all_tables)
        # print(all_tables)
        return all_tables
