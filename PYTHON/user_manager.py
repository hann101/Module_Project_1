import pymysql
conn = pymysql.connect(host='172.17.0.2',user='root',password= '',port=3306,db='mydb',charset='utf8')
cursor = conn.cursor()

#사용자 로그인 화면
def user_login(login_emial,login_pwd):
    #db에서 입력한 id 찾고 
    select_Sql = '''SELECT num, email, pwd, created_at FROM member WHERE email = %s'''
    cursor.execute(select_Sql,(login_emial))
    #해당 pwd랑 이매치시켜서 맞으면 통과
    while True:
        row = cursor.fetchone()
        if row == None:
            break
        #검색 >일치
        if row[2] == login_pwd:
            print('\n',' '*17,'로그인 성공!')
            permit = 1
            return permit
            #권한 부여
        else:
            print('비밀번호가 다릅니다.')

#상품목록 조회
def item_list(login_emial):
  
    sql1 = 'Select num, product_name, product_price, product_qty, created_at FROM item'
    cursor.execute(sql1)
    rows = cursor.fetchall()
    print('\n'*2)
    print('#'*50)
    print(' '*16,'\n상품목록')
    print('\n')

    for row in rows:
        print('No:{0}, 상품명:{1}, 가격:{2}, 재고:{3}, 기입시간:{4}'.format(row[0], row[1], row[2], row[3], row[4]))
    
    print('\n')
    print('#'*50)

#상품 재고확인
def item_remain(product_name):

    sql1 = 'Select  product_name,  product_qty FROM item WHERE product_name= %s'
    cursor.execute(sql1,(product_name))
    while True:
        row = cursor.fetchone()
        if row == None:
            break
        if row[1] < 1:
            print('\n')
            print('\t상품명:{0}, \t재고량:{1}'.format(row[0], row[1]))
            print('\n죄송합니다..\n재고가 없으니 다른상품을 주문해주세요!')
        else:
            print('\n\n\t주문전 재고량')
            print('-'*50)
            print('\t상품명:{0} \t재고량:{1}'.format(row[0], row[1]))
            
            return 1
            

def item_nowqty(product_name):
    cursor = conn.cursor()
    sql1 = 'Select  product_name,  product_qty FROM item WHERE product_name= %s'
    cursor.execute(sql1,(product_name))
    while True:
        row = cursor.fetchone()
        if row == None:
            break
        print('\n')
        print('\n\t주문후 재고량')
        print('-'*50)
        print('\t상품명:{0} \t재고량:{1}'.format(row[0], row[1]))
    
  
            



#상품주문
def order_item(login_emial,user_or_item_id,user_or_qty):
    #주문 갯수 만큼 기존 주문리스트 재고에서 빼준다,

    #주문한 상품의 갯수에 따른 총 가격 계산
    #아이템 아이디 반드시 일치해야됨.. 오타방지만들어야
    #이게 error만듬 (%s빼먹음 ->)
    or_select_Sql = 'Select num, product_name, product_price, product_qty, created_at FROM item WHERE product_name = %s '
    cursor.execute(or_select_Sql,(user_or_item_id))
    # try:
    while True:
            row = cursor.fetchone()
            if row == None:
                break
            user_or_price = row[2] *user_or_qty

    #재고 계산(user_or_item_id,user_or_qty)

            update_qty = row[3]- user_or_qty
            cal_sql = """ UPDATE item SET  product_qty =%s WHERE product_name=%s """
            cursor.execute(cal_sql,(update_qty,user_or_item_id))
            conn.commit()


    
    #주문등록
    or_insertSql = """INSERT INTO _order(num, member_id, item_id, order_qty, order_price,created_at) VALUES(null, %s, %s, %s, %s, NOW()) """
    #값을 안넣고 싶으면 null을 넣는다! None값이 들어감...
    sql1 = 'Select num, member_id, item_id, order_qty, order_price, created_at FROM _order'
    cursor.execute(sql1)
    cursor.execute(or_insertSql,(login_emial, user_or_item_id, user_or_qty, user_or_price))
    conn.commit()
    print('\n\t주문완료\n')

    # sql1 = 'Select  product_name,  product_qty FROM item WHERE product_name= %s'
    # cursor.execute(sql1,(user_or_item_id))
    # while True:
    #     row = cursor.fetchone()
    #     if row == None:
    #         break
    #     print('\n 현재재고!')
    #     print('\t상품명:{0}, \t재고량:{1}'.format(row[0], row[1]))
        



def ordered_list(login_emial):    #주문정보확인(사용자):
    or_select_Sql = '''SELECT num, member_id, item_id, order_qty, order_price,created_at FROM _order WHERE member_id = %s'''
    cursor.execute(or_select_Sql,(login_emial))
    while True:
        row = cursor.fetchone()
        if row == None:
            break
        if row[2] == 'Empty':
            print('\n주문내역없음')
            print('\n')
            break
        else:
            print('No:{0}, member_id:{1}, item_id:{2}, order_qty:{3},order_price:{4},created_at{5}'.format(row[0], row[1], row[2], row[3],row[4],row[5]))




    