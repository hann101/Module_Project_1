#이 폴더는 로컬 폴더이다.. '127.0.0.1'가 주소
#로컬로 접속하면 '127.0.0.1',, 컨테이너로 접속할때는 '172.17.0.2'

######################최종


import pymysql
conn = pymysql.connect(host='172.17.0.2',user='root',password= '',port=3306,db='mydb',charset='utf8')
cursor = conn.cursor()
import user_manager
import admin_manager
import time

while True:

    #메 인화면
    print('\n'*2)
    print('#'*50)
    print('\n',' '*14,'1. 회원 로그인 ',' \n',' '*14,'2. 관리자 로그인','\n',' '*14,'3. 프로그램 종료\n')
    print('#'*50)
    try:
        user = int(input('\n입력:'))
        print('\n')
        #회원 로그인
        if user == 1:

            #회원가입을 위한 while문
            while True:
                print('#'*50)
                print('\n')
                print(' '*14,'1. 회원 로그인 화면\n',' '*17,'2 .회원 가입\n',' '*17,'3. 뒤로가기')
                print('\n')
                print('#'*50)
                try:
                    num = int(input('\n실행:'))
                    print('\n')

                    if num == 1:

                        print('#'*50)
                        print('\n'*2)
                        print(' '*16,'회원 로그인 화면')
                        print('\n'*2)
                        print('#'*50)

                        login_emial = str(input('\nEmail:'))
                    
                        login_pwd = str(input('PWD:'))
                        #로그인 되면
                        if user_manager.user_login(login_emial,login_pwd) ==1:
                            access = 1

                            if access == 1:
                                while True:
                                    try:
                                        print('\n'*2)
                                        print('#'*50)
                                        
                                        print('\n'*2,' '*8,'1. 상품목록 조회(& 상품주문) \n',' '*15,'2. MY 주문내역\n',' '*14,'3. 회원정보 수정\n',' '*16,'4. 회원 탈퇴\n',' '*16,'5. 로그아웃\n')
                                        print('\n')
                                        print('#'*50)
                                        user_input = int(input('\n입력:'))
                                        

                                        #상품목록조회 &주문하기
                                        if user_input == 1:
                                        
                                            user_manager.item_list(login_emial)
                                            print('\n상품을 주문하시겠습니까?')
                                            print("\n1. 주문하기 \n2. 나가기 ")
                                            order_sel = int(input('\n입력:'))
                                            if order_sel == 1:
                                                user_or_item_id = input('\n상품명:')
                                                user_or_qty  = int(input('주문갯수:'))
                                                # or_regist_order_price = int(input('주문가격:')) 
                                                if user_manager.item_remain(user_or_item_id) == 1:
                                                    user_manager.order_item(login_emial, user_or_item_id, user_or_qty)    
                                                    user_manager.item_nowqty(user_or_item_id)
                                                    print('\n')
                                                        
                                                #나가기
                                                elif order_sel == 2:
                                                    print('메인화면으로 이동')
                                        
                                        #my주문내역
                                        elif user_input == 2:
                                            user_manager.ordered_list(login_emial)
                                        
                                        #회원정보수정
                                        elif user_input == 3:
                                            repair_email = input('(PWD수정)email 입력:')
                                            repair_pwd = input('(PWD수정)수정할 PWD입력:')
                                            print('\n')
                                            admin_manager.ad_user_repair(repair_email,repair_pwd)
                                            print('\n'*2)
                                        
                                        #회원정보 삭제
                                        elif user_input == 4:
                                            
                                
                                            print('\n',' '*17,'#회원탈퇴# ')
                                            del_email = input('(삭제)Email입력:')
                                            print('\n')
                                            admin_manager.ad_user_delete(del_email)
                                            print('\n')
                                            print('회원이 삭제 되었습니다.')
                                            print('\n'*2)
                                            access =0
                                            break


                                        # elif user_input == 4:
                                            
                                            
                                            
                                        
                                        #나가기
                                        elif user_input == 5:
                                            print('\n로그아웃\n')
                                       
                                            break
                                    except:
                                        print('오타입니다. 다시 입력해주세요!')

                        else:
                            print('\n비밀번호가 다릅니다.\n')  
                    #회원가입하면 order 0으로 지정
                    elif num == 2:
                        print('#'*50)
                        print('\n'*3)
                        print(''*19,'회원 가입')
                        print('\n'*3)
                        print('#'*50)
                        print('\n'*3)
                        usr_regist_id = str(input('Email:'))
                        usr_regist_pwd = str(input('PassWord:'))
                        print('\n')
                        admin_manager.member_regist(usr_regist_id,usr_regist_pwd)
                        
                        #회원가입하면 주문이 없을을 알림
                        #로그인하고 주문 내역확일 할 때 사용
                        admin_manager.order_add(usr_regist_id,'Empty',0,0)
                        break
                    
                    elif num ==3:
                        break
                except:
                    print('\n오타입니다! \n번호만 입력해주세요!')
                    print('\n')
        #관리자 로그인
        elif user == 2:
            #관리자 로그인 화면
            print('#'*50)
            print('\n',' '*12,'1. 관리자 로그인 화면\n')
            print('#'*50)
            login_admin = str(input('\n(Admin)ID:'))
            login_adminpwd = str(input('(Admin)PWD:'))
            

            if login_admin == 'admin' and login_adminpwd =='admin1234':
                print('\n',' '*17,'로그인 성공!\n')
                print('\n')

                

                #관리자화면
                while True:
                    try:
                        print('#'*50)
                        print('\n',' '*13,'관리자님 환영합니다!')
                        print('\n',' '*17,'1. 회원관리 \n',' '*17,'2. 주문관리 \n',' '*17,'3. 상품관리\n',' '*17,'4. 로그아웃\n')
                        print('#'*50)
                        admin_input = int(input('\n입력:'))
                        print('\n'*2)

                        #회원관리
                        if admin_input == 1:
                            print('#'*50)
                            print('\n',' '*18,'회원관리\n \n',' '*19,'1.등록 \n',' '*19,'2.수정 \n',' '*19,'3.삭제\n',' '*16,'4.회원검색 \n',' '*15,'5.전체회원목록\n')
                            print('#'*50)
                            sel_1 = int(input('\n실행:'))
                            print('\n')
                            
                            
                            
                            #등록
                            if sel_1 == 1:
                                ad_useremail = input('\n(회원등록) Email:')
                                ad_userpwd = input('(회원등록) PWD:')
                                print('\n')
                                admin_manager.member_regist(ad_useremail,ad_userpwd)
                                print('\n회원등록완료')                        
                                print('\n'*2)

                            #수정
                            elif sel_1 == 2:
                                repair_email = input('(PWD수정)email 입력:')
                                repair_pwd = input('(PWD수정)수정할 PWD입력:')
                                print('\n')
                                admin_manager.ad_user_repair(repair_email,repair_pwd)
                                print('\n'*2)
                            
                            #삭제
                            elif sel_1 == 3:
                                del_email = input('(삭제)Email입력:')
                                print('\n')
                                admin_manager.ad_user_delete(del_email)
                                print('\n')
                                print('회원이 삭제 되었습니다.')
                                print('\n'*2)
                
                            #개인계정찾기
                            elif sel_1 == 4:
                                ad_search_user = input('(검색)Email 입력:')
                                print('\n')
                                admin_manager.ad_oneuser_search(ad_search_user)
                                print('\n'*2)
                                

                            #전체회원목록
                            elif sel_1 == 5:
                                
                                admin_manager.ad_alluser_search() 
                                print('\n'*2)

                        #주문관리
                        elif admin_input == 2:
                            admin_input = 0
                            print('#'*50)
                            print('\n',' '*18,'주문관리\n \n',' '*19,'1.등록 \n',' '*19,'2.수정 \n',' '*19,'3.삭제 \n',' '*17,'4.목록조회\n')
                            print('#'*50)
                            sel_2 = int(input('\n실행:'))
                            print('\n')
                            
                            #주문등록
                            if sel_2 == 1:
                                or_regist_member_id = input('(등록) Email 입력:')
                                or_regist_item_id = input('(등록) 상품명 입력:')
                                or_regist_order_qty  = int(input('(등록) 주문 갯수:'))
                                # or_regist_order_price = int(input('(등록) 주문 가격:'))
                                #주문갯수에 맞게 알아서 가격이 측정되야함

                                print('\n')
                                user_manager.order_item(or_regist_member_id,or_regist_item_id,or_regist_order_qty)
                                print('\n'*2)
                            #주문수정
                            elif sel_2 ==2:
                                #목록에서 번호 찾아서 수정
                                admin_manager.orderList_read()
                                print('\n주문번호를 선택해주세요!')

                                or_reapair_num =int(input('\n(수정)주문번호:'))
                                or_reapair_name = input('(수정)상품명:')
                                # or_repair_price = input('(수정)상품가격:')
                                #자동 가격
                                or_repair_qty  = int(input('(수정)상품갯수:'))
                                print('\n')
                                admin_manager.order_update(or_reapair_num,or_reapair_name,or_repair_qty)
                                print('\n'*2)

                            #주문삭제
                            elif sel_2 ==3:
                                or_delete_num = input("(삭제)주문번호:")
                                print('\n')
                                admin_manager.order_delete(or_delete_num)
                                print('\n'*2)
                            #목록조회 
                            elif sel_2 ==4:
                                print('#'*50)
                                print('\n'," "*19,'목록조회\n \n'," "*16,'1.전체주문목록 \n'," "*14,'2.회원별 주문 목록 ')
                                print(" "*12,'3.주/월별 최다 금액 주문자 \n'," "*13,'4.주/월별 최다 주문상품')
                                print('\n')
                                print('#'*50)
                                print('\n')
                                sel_24 = int(input('입력:'))
                                print('\n')
                                #전체주문목록
                                if sel_24 == 1:
                                    admin_manager.orderList_read()
                                    print('\n주문내역조회: 조회완료')
                                    print('\n'*2)

                                #회원별 주문 목록
                                elif sel_24 ==2:
                                    or_search_email =input('Email:')
                                    print('\n')
                                    admin_manager.orderMember_read(or_search_email)
                                    print('\n'*2)
                                # 주/월별 최다 금액 주문자
                                elif sel_24 ==3:


                                    #오늘 날짜
                                    today = time.strftime("%d",time.localtime(time.time()))
                                    today = int(today)


                                    #이번달
                                    this_month= time.strftime("%m",time.localtime(time.time()))
                                    this_month = int(this_month)
                                    


                                    print('#'*50)
                                    print('\n'," "*12,'이번주 최다 금액 주문자\n')
                                    # a,b = admin_manager.bestBuyer()
                                    week_list = admin_manager.weekly(today)
                                    wbuyer,wmoneny = admin_manager.bestBuyer(week_list)
                               
                                    print(" "*3,'* 최고의 구매자:',wbuyer,'총구매 액수:',wmoneny,' *')
                                    # print('최고 구매금액 주문자:',a,'총 금액수:',b)
                                    #여기서 none 발생

                                    month_list = admin_manager.monthly(this_month)
                                    mbuyer,mmoney = admin_manager.bestBuyer(month_list)
                                    print('\n'," "*13,'이번달 최다 금액 주문자\n')
                                    
                                    print(" "*3,'* 최고의 구매자:',mbuyer,'총구매 액수:',mmoney,' *')
                                    print('\n')
                                    print('#'*50)                               
                                    print('\n'*2)

                                # 주/월별 최다 주문 상품
                                elif sel_24 == 4:  
                                    #주별 최다 주문
                                    week_list = admin_manager.weekly(today)
                                    witem,wqty = admin_manager.bestItem(month_list) 

                                    print('#'*50)
                                    print('\n'," "*12,'이번주 최다 주문 상품\n')
                                    print(" "*10,'상품명:',witem,'주문갯수:',wqty)
                                    
                                    
                                    #월별 최다 주문 
                                    month_list = admin_manager.monthly(this_month)
                                    mitem,mqty = admin_manager.bestItem(month_list)  
                                    print('\n'," "*13,'4.이번달 최다 주문 상품\n')
                                    print(" "*10,'상품명:',mitem,'주문갯수:',mqty)
                                    print('#'*50)  
                                    print('\n'*2)                             


                        #상품관리
                        elif admin_input == 3:

                            print('#'*50)
                            print('\n'," "*18,'상품관리\n \n'," "*19,'1.등록\n'," "*19,'2.수정 \n'," "*19,'3.삭제 \n')
                            print('#'*50)
                            print('\n')
                            sel_3 = int(input('입력:'))
                            print('\n')

                            #등록
                            if sel_3 ==1:
                                pd_regist_name = input('상품명:')
                                pd_regist_price = input('상품가격:')
                                pd_regist_qty  = input('상품갯수:')
                                print('\n')
                                admin_manager.item_add(pd_regist_name,pd_regist_price,pd_regist_qty)
                                admin_manager.itemList_select()
                                print('\n'*2)
                            #수정
                            elif sel_3 ==2:
                                pd_reapair_name = input('상품명:')
                                pd_repair_price = input('(수정)상품가격:')
                                pd_repair_qty  = input('(수정)상품갯수:')
                                admin_manager.item_update(pd_repair_price,pd_repair_qty,pd_reapair_name)
                                print('\n')
                                print('변경되었습니다.')
                                print('\n'*2)
                            #삭제               
                            elif sel_3 ==3:
                                print('\n')
                                pd_del_name = input('(삭제)상품명 입력:')
                                admin_manager.item_delete(pd_del_name)
                                print('\n'*2)
                            admin_input = 0

                        #로그아웃
                        elif admin_input == 4:
                            break
                    except:
                        print('\n오타입!')
                        # 니다! \n번호만 입력해주세요
                        print('\n')

            else:
                print('\n접속불가')
        
        elif user == 3:
            break
    except:
        print('\n오타입니다! \n번호만 입력해주세요!')
        print('\n')
