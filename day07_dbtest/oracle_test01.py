import cx_Oracle

conn = cx_Oracle.connect('scott','tiger','localhost:1521/xe')
cursor = conn.cursor()
cursor.execute("select * from emp")

# print(cursor)

while True:
    choice=input('''
다음 중에서 하실 일을 골라주세요 :
1-job 검색 2-사원이름 검색
>>>''')

    if choice == '1':
        item={'empno':'','ename':'','job':'','mgr':'','hiredate':'','sal':'','comm':'','deptno':''}
        for item in cursor:
            item['job']=input('job >>>')
            print(item[1],item[2])
    
    else:
        item['ename']=input('이름 입력>>>')
        print(item[1])
    
    conn.close()


# 1.emp 테이블에 job을 입력받아 해당 job인 사원을 출력하세요.
# 2.사원의 이름의 일부를 입력받아서 검색해서 출력 


