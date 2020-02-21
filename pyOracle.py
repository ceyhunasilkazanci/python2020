import cx_Oracle

#if needed, place an 'r' before any parameter in order to address any special character such as '\'.
dsn_tns = cx_Oracle.makedsn('mendel.ekol.com', '1521', service_name='LY01D.LILYUM.EKOL.COM')

#if needed, place an 'r' before any parameter in order to address any special character such as '\'. 
# For example, if your user name contains '\', you'll need to place 'r' before the user name: user=r'User Name'
conn = cx_Oracle.connect(user='RAINBOW', password='WmzaFB4tCW9ggTUcfcdn', dsn=dsn_tns) 

sql = "INSERT INTO dept (deptno, dname, loc) VALUES (:deptno, :dname, :loc)"

c = conn.cursor()
# use triple quotes if you want to spread your query across multiple lines
c.execute('select ORG_CODE,SERIAL_TYPE,SERIAL_NO from DOC_SERIALS' ) 
for row in c:
    # this only shows the first two columns. To add an additional column you'll need to add , '-', row[2], etc.
    print (row[0], '-', row[1], '-', row[2]) 
conn.close()

