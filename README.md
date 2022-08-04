# Using-Python-with-Excel

#### Pandas is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language.
#### Pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool,
built on top of the Python programming language.


### >> import pandas as pd

#### openpyxl is a Python library to read/write Excel 2010 xlsx/xlsm/xltx/xltm files.
#### It was born from lack of existing library to read/write natively from Python the Office Open XML format.
#### All kudos to the PHPExcel team as openpyxl was initially based on PHPExcel.

### >> from openpyxl.workbook import workbook
### >> from openpyxl import load_workbook
### >> from openpyxl.chart import BarChart, PieChart, Reference, Series, PieChart3D

from openpyxl import Workbook
>> wb = Workbook()

#### grab the active worksheet
>> ws = wb.active

#### Data can be assigned directly to cells
>> ws['A1'] = 42

#### Rows can also be appended
>> ws.append([1, 2, 3])

#### Python types will automatically be converted
>> import datetime
>> ws['A2'] = datetime.datetime.now()

#### Save the file
>> wb.save("sample.xlsx")