import cx_Oracle

#if needed, place an 'r' before any parameter in order to address any special character such as '\'.
dsn_tns = cx_Oracle.makedsn('mendel.ekol.com', '1521', service_name='LY01D.LILYUM.EKOL.COM')

#if needed, place an 'r' before any parameter in order to address any special character such as '\'. 
# For example, if your user name contains '\', you'll need to place 'r' before the user name: user=r'User Name'
conn = cx_Oracle.connect(user='RAINBOW', password='WmzaFB4tCW9ggTUcfcdn', dsn=dsn_tns) 
cursor = conn.cursor()
sql = "INSERT INTO DOC_SERIALS (ORG_CODE, DOC_TYPE,SERIAL_TYPE, SERIAL_NO) VALUES (:ORG_CODE, :DOC_TYPE, :SERIAL_TYPE, :SERIAL_NO)"
try:
  cursor.execute (sql,ORG_CODE='TKNO', DOC_TYPE='IF',SERIAL_TYPE='IF', SERIAL_NO='123123')
except cx_Oracle.DatabaseError as e:
  errorObj, = e.args
  print(errorObj.message)
  exit (1)

cursor.close ()
conn.commit ()
conn.close()
