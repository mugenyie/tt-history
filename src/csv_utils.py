# coding=utf-8
"""
The MIT License

Copyright (c) 2013 Mustafa İlhan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

import cStringIO
import csv
import json

from data_model_converter import DataModelConverter


class CsvUtils:

    def jsonToCsv(self, data):
        fieldnames = DataModelConverter.CSV_FILE_FIELDS
        fileStream = cStringIO.StringIO()
        csvWriter = csv.DictWriter(fileStream, fieldnames=fieldnames)
        csvWriter.writerow(dict(zip(fieldnames, fieldnames)))
        for obj in data:
            csvWriter.writerow(obj)
        content = fileStream.getvalue()
        fileStream.close()
        return content

    def csvToJson(self, filename):
        jsonData = []
        with open(filename) as f:
            f_csv = csv.DictReader(f)
            for row in f_csv:
                jsonData.append(row)
        return jsonData