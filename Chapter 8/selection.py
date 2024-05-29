import cgi
data = cgi.FieldStorage()

answer = data.getvalue('cat')

city = data.getvalue('CityList')

print('Content-type:text/html\r\n\r\n')

print('<!DOCTYPE HTML>')
print('<html lang-"en">')
print('<head>')
print('<meta charset="UTF-8">')
print('<title>Python Response</title>')
print('</head>')
print('<body>')
print('<h1>', city, '</h1>')
print('<a href="selection.html">Back</a>')
print('</body>')
print('</html>')