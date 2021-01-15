import pymysql
conn = pymysql.connect(host='172.17.0.2',user='root',password= '',port=3306,db='mydb',charset='utf8')
cursor = conn.cursor()



def member_regist(ad_useremail,ad_userpwd):
    #등록
    
    insertSql = """INSERT INTO member(num, email, pwd, created_at) VALUES(null, %s, %s, NOW()) """
    cursor.execute(insertSql,(ad_useremail,ad_userpwd))
    conn.commit()
    #등록확인
    sql1 = 'SELECT num, email,pwd, created_at FROM member WHERE email = %s'
    cursor.execute(sql1,(ad_useremail))
    #db에서 등록된 이메일만 출력한다.
    while True:
        row = cursor.fetchone()
        if row == None:
            break
        print('No:{0}, \tEmail:{1}, \tPassword:{2}, \tCreated On:{3}'.format(row[0], row[1], row[2], row[3]))

def ad_user_repair(repair_email,repair_pwd):
    #수정
    repair_sql = """ UPDATE member SET pwd= %s WHERE email=%s """
    cursor.execute(repair_sql,(repair_pwd,repair_email))
    conn.commit()

    #수정확인
    sql1 = 'SELECT num, email,pwd, created_at FROM member WHERE email = %s'
    cursor.execute(sql1,(repair_email))
    #db에서 등록된 이메일만 출력한다.
    while True:
        row = cursor.fetchone()
        if row == None:
            break
        print('No:{0}, \tEmail:{1}, \tPassword:{2}, \tCreated On:{3}'.format(row[0], row[1], row[2], row[3]))

    print('PWD이 변경되었습니다.')

def ad_user_delete(del_email):
    deleteSql = '''DELETE FROM member WHERE email = %s'''
    cursor.execute(deleteSql, (del_email))
    conn.commit()

#회원 한명검색
def ad_oneuser_search(user_email):
    sql1 = 'SELECT num, email,pwd, created_at FROM member WHERE email = %s'
    cursor.execute(sql1,(user_email))
    #db에서 등록된 이메일만 출력한다.
    while True:
        row = cursor.fetchone()
        if row == None:
            break
        print('No:{0}, \tEmail:{1}, \tPassword:{2}, \tCreated On:{3}'.format(row[0], row[1], row[2], row[3]))

#  전체회원목록조ㅗ히  member search
def ad_alluser_search():
    sql1 = 'SELECT num, email,pwd, created_at FROM member'
    cursor.execute(sql1)
    rows = cursor.fetchall()
    
    for row in rows:
        print('No:{0}, \tEmail:{1}, \tPassword:{2}, \tCreated On:{3}'.format(row[0], row[1], row[2], row[3]))

#해당 이메일 정보 출력    
def searchemail(email):
    
    sql1 = 'SELECT num, email,pwd, created_at FROM member WHERE email = %s'
    cursor.execute(sql1,(email))
    #db에서 등록된 이메일만 출력한다.
    while True:
        row = cursor.fetchone()
        if row == None:
            break
        print('No:{0}, \tEmail:{1}, \tPassword:{2}, \tCreated On:{3}'.format(row[0], row[1], row[2], row[3]))

    print('PWD이 변경되었습니다.')



def item_add(pd_regist_name,pd_regist_price,pd_regist_qty):
    cursor = conn.cursor()
    pd_insertSql = """INSERT INTO item(num, product_name, product_price, product_qty, created_at) VALUES(null, %s, %s, %s, NOW()) """
    cursor.execute(pd_insertSql,(pd_regist_name, pd_regist_price, pd_regist_qty))
    conn.commit()

def itemList_select():
    sql1 = 'Select num, product_name, product_price, product_qty, created_at FROM item'
    cursor.execute(sql1)
    rows = cursor.fetchall()
    
    for row in rows:
        print('No:{0}, \tname:{1}, \tprice:{2}, \tqty:{3}, \tCreated On:{4}'.format(row[0], row[1], row[2], row[3], row[4]))

def item_update(price,repair_qty,reapair_name):

    pd_repair_sql = """ UPDATE item SET product_price= %s, product_qty =%s WHERE product_name=%s """
    cursor.execute(pd_repair_sql,(price,repair_qty,reapair_name))
    conn.commit()
    

def item_delete(name):
    pd_deleteSql = '''DELETE FROM item WHERE product_name = %s'''
    cursor.execute(pd_deleteSql, (name))
    conn.commit()
    print('상품이 삭제 되었습니다.')


def orderList_select():
    sql1 = 'Select num, member_id, item_id, order_qty, order_price, created_at FROM _order'
    cursor.execute(sql1)
    rows = cursor.fetchall()
    for row in rows:
        print('No:{0}, \tmember_id:{1}, \titem_id:{2}, \torder_qty:{3}, \torder_price:{4}, \tcreated_at{5}'.format(row[0], row[1], row[2], row[3],row[4],row[5]))
    print('주문내역조회: 조회완료')

def order_add(member_id,item_id,order_qty,order_price):
    cursor = conn.cursor()
    or_insertSql = """INSERT INTO _order(num, member_id, item_id, 
    order_qty, order_price,created_at) VALUES(null, %s, %s, %s, %s, NOW()) """
    
    cursor.execute(or_insertSql,(member_id, item_id, order_qty, order_price))
    conn.commit()
#########################
def order_update(num,product_name,product_qty):

    #주문번호에 해당하는 item 가격가져오기
    # 주문번호 > item id 찾기    
    sql1 = 'Select num, product_name, product_price, product_qty, created_at FROM item WHERE product_name = %s '
    cursor.execute(sql1,(product_name))
    #아이템의 가격 가져오기
    while True:
        row = cursor.fetchone()
        if row == None:
            break

        #아이템가격 * 수정된 갯수 = 수정된 주문가격
        total_price = row[2] *product_qty

        #수정
        #재고 계산(user_or_item_id,user_or_qty)
        #아이템 재고 - 수정된 갯수 = 수정된 아이템 재고
        update_qty = row[3]- product_qty
        cal_sql = """ UPDATE _order SET order_qty =%s,order_price =%s WHERE num=%s """
        cursor.execute(cal_sql,(update_qty,total_price,num))
        conn.commit()

##########################



# def order_update(member_id, item_id, order_qty):
#     or_select_Sql = 'Select num, product_name, product_price, product_qty, created_at FROM item WHERE product_name = %s '
#     cursor.execute(or_select_Sql,(item_id))

    #수정된 정보 없뎃
    #번호에 해당하는 곳을 찾아가
    
    pd_repair_sql = """ UPDATE _order SET item_id= %s, order_qty =%s,order_price=%s WHERE num=%s """
    #입력받은 상품명 갯수 , 총 주문액을 받아
    cursor.execute(pd_repair_sql,(product_name,product_qty,total_price,num))

    conn.commit()
    print('변경되었습니다.')

def order_delete(num):
    or_deleteSql = '''DELETE FROM _order WHERE num = %s'''
    cursor.execute(or_deleteSql, (num))
    conn.commit()
    print('상품이 삭제 되었습니다.')

def orderList_read():
    or_select_Sql = '''SELECT num, member_id, item_id, order_qty, order_price,created_at FROM _order '''
    cursor.execute(or_select_Sql)
    rows = cursor.fetchall()
    for row in rows:
        print('No:{0}, \tmember_id:{1}, \titem_id:{2}, \torder_qty:{3}, \torder_price:{4}, \tcreated_at{5}'.format(row[0], row[1], row[2], row[3],row[4],row[5]))
    

# 회원별 주문목록? 아이디로 찾아
def orderMember_read(member_id):
    
    or_search_sql = '''SELECT num, member_id, item_id, order_qty, order_price,created_at FROM _order WHERE member_id = %s'''
    cursor.execute(or_search_sql,(member_id))
    while True:
        row = cursor.fetchone()
        if row == None:
            break
        print('No:{0}, \tmember_id:{1}, \titem_id:{2}, \torder_qty:{3}, \torder_price:{4}, \tcreated_at{5}'.format(row[0], row[1], row[2], row[3],row[4],row[5]))

#주간 검색

def weekly(today):
    #오늘 날짜
    # today= time.strftime("%d",time.localtime(time.time()))
    # today = int(today)

    #일주일 리스트만 모으면 됨

    weeklist = []
    or_select_Sql = '''SELECT num, member_id, item_id, order_qty, order_price,created_at FROM _order '''
    cursor.execute(or_select_Sql)
    rows = cursor.fetchall()

    # rows = 1,2,3,4,5,6,7,8,9,10,11
    #한 라인씩 들어와
    for row in rows:
        # name = row[1]
        date = row[5]
    #     타입변경(daytime -> int)
        a =str(date)
        b = a.split(' ')
        c = []
        c= b[0].split('-')
        d = int(c[2])
        week = today -7
        if week < d :
            weeklist.append(row)
    return weeklist
    #     name이 주문한 날짜가 오늘을 기준으로 일주일 동안 주문한 사람들의 리스트를 구하자..


def monthly(this_month):

    monthlist = []
    or_select_Sql = '''SELECT num, member_id, item_id, order_qty, order_price,created_at FROM _order '''
    cursor.execute(or_select_Sql)
    rows = cursor.fetchall()


    # rows = 1,2,3,4,5,6,7,8,9,10,11
    #한 라인씩 들어와
    for row in rows:
    #         name = row[1]
        date = row[5]
    #     타입변경(daytime -> int)
        a =str(date)
        b = a.split(' ')
        c = []
        c= b[0].split('-')
        d = int(c[1])
        if d == this_month:
            monthlist.append(row)
    return monthlist


def bestBuyer(week_orders):

    #일주일치 리스트만 전달해주자 select쓰는 대신
    ne = []
    total_money = 0

    #일주일치 리스트에서 이름선별

    for week_order in week_orders: 
        ne.append(week_order[1])

            #아이디만 쭉가져와


        #------------------------
    #name_list 만들어 줘야함

    name_list = set(ne)
    name_list = list(name_list)


    wek_namelist =[]
    wek_moneylist=[]

    max_money = 0
    #각각의 이름별
    for name in name_list:
        #weeklist에서 해당하는 이름의 ㄱ데이터만 수집
        for week_name in week_orders:
            #주간 리스트에서 이름이 일치허묜
            if week_name[1] == name:
                # 주문가격을 다 더해라

                total_money += week_name[4]
        wek_moneylist.append(total_money)
        wek_namelist.append(name)

        total_money = 0
        #리셋을 안해줘서 계속더해지고 있었음

    max_money = max(wek_moneylist)

    b = wek_moneylist.index(max_money)
    c = wek_namelist[b]
    return c,max_money




def bestItem(weeklists):

    #일주일치 리스트만 전달해주자 select쓰는 대신
    ne = []
    total_qty = 0

    #일주일치 리스트에서 이름선별

    for week_item in weeklists: 
        ne.append(week_item[2])

            #상품명만 쭉가져와


        #------------------------
    #name_list 만들어 줘야함

    item_list = set(ne)
    item_list = list(item_list)


    wek_itemlist =[]
    wek_qtylist=[]

    max_qty = 0
    #각각의 이름별
    for item_id in item_list:
        #weeklist에서 해당하는 이름의 ㄱ데이터만 수집
        for week_itemid in weeklists:
            #주간 리스트에서 이름이 일치허묜
            if week_itemid[2] == item_id:
                # 주문가격을 다 더해라

                total_qty += week_itemid[3]
        wek_qtylist.append(total_qty)
        wek_itemlist.append(item_id)

        total_qty = 0
        #리셋을 안해줘서 계속더해지고 있었음

    max_qty = max(wek_qtylist)

    b = wek_qtylist.index(max_qty)
    c = wek_itemlist[b]
    return c,max_qty




# def best_order():
#     or_sql='''SELECT item_id FROM _order '''
#     cursor.execute(or_sql)
#     item_ids = cursor.fetchall()
#     # for item_id in item_ids:

#     item_list = set(item_ids)
#     max_order = 0
#     for item in item_list:
#         #이름별

#         total_order = 0
#         or_select_Sql = '''SELECT num, member_id, item_id, order_qty, order_price,created_at FROM _order WHERE item_id = %s'''
#         cursor.execute(or_select_Sql,(item))
#         while True:
#             row = cursor.fetchone()
#             if row == None:
#                 break
#             total_order += row[3]
        
#         # print('상품명:',item,'주문갯수:',total_order)
#         if total_order>max_order:
#             bestorder = item
#             max_order = total_order
#             b = str(bestorder)
#             b = b.replace("(","")
#             b = b.replace(")","")
#             b = b.replace(",","")
#             b = b.replace("'","")
        
#             return b,max_order










# 첫번째시도 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#     #일주일치 리스트만 전달해주자 select쓰는 대신
#     ne = []
# #이름 선별
#     #일주일치 리스트에서 이름선별

#     for week_order in week_orders: 
#         ne.append(week_order[1])
# #         print(ne)
#             #아이디만 쭉가져와
        
    
#         #------------------------
# #name_list 만들어 줘야함

#     name_list = set(ne)
#     print(name_list)
    
#     max_money = 0
#     #각각의 이름별
#     for name in name_list:
        
#         #총 구매가격
#         total_money = 0
#         or_select_Sql = '''SELECT num, member_id, item_id, order_qty, order_price,created_at FROM _order WHERE member_id = %s'''
#         cursor.execute(or_select_Sql,(name))
#         while True:
#             row = cursor.fetchone()
#             if row == None:
#                 break
#             total_money += row[4]
            
#         #최고 구매자 구하기(기존값이 새로운 변수보다 작으면 새로운 변수를 대입)
#             if total_money>max_money:
#                 bestbuyer = name
#                 max_money = total_money
#         # max_money가 money 보다 크면 
#                 a = str(bestbuyer)
#                 a =a.replace("(","")
#                 a =a.replace(")","")
#                 a =a.replace(",","")
#                 a =a.replace("'","")
#                 if None:
#                     print('')
#     #         max_money = total_money
#     # return bestbuyer,max_money     
     
    
#     return a,max_money

    #c총구매액에서 최대 를 찾고 
    #사용자 이름 추출

# 원본~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# def bestBuyer():
#     #일주일치 리스트만 전달해주자 select쓰는 대신
#     or_select_Sql = '''SELECT member_id FROM _order '''
#     cursor.execute(or_select_Sql)
#     rows = cursor.fetchall()
# #이름 선별
#     name_list = set(rows)
#     max_money = 0
#     #각각의 이름별
#     for name in name_list:
        
#         #총 구매가격
#         total_money = 0
#         or_select_Sql = '''SELECT num, member_id, item_id, order_qty, order_price,created_at FROM _order WHERE member_id = %s'''
#         cursor.execute(or_select_Sql,(name))
#         while True:
#             row = cursor.fetchone()
#             if row == None:
#                 break
#             total_money += row[4]
            
#         #최고 구매자 구하기(기존값이 새로운 변수보다 작으면 새로운 변수를 대입)
#             if total_money>max_money:
#                 bestbuyer = name
#                 max_money = total_money
#         # max_money가 money 보다 크면 
#                 a = str(bestbuyer)
#                 a =a.replace("(","")
#                 a =a.replace(")","")
#                 a =a.replace(",","")
#                 a =a.replace("'","")
#                 if None:
#                     print('')
#     #         max_money = total_money
#     # return bestbuyer,max_money     
     
    
#     return a,max_money

#     #c총구매액에서 최대 를 찾고 
#     #사용자 이름 추출



# 오답예제
#       if total_order>max_order:
#             bestorder = item
#             max_order = total_order
#             b = str(bestorder)
#             b.replace("(","")
#             b.replace(")","")
#             b.replace(",","")
#             b.replace("'","")
        
#             print('최고의 상품:',b,'총주문 갯수:',max_order)
#             if None:
#                 print('')
# #none?