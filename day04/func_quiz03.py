import func_basic as fb

menu = {'아이스아메리카노':3000,'라떼':4000,'코코아':3500}
while True:
    choice = input('''
--------------------------------------------------------------
1. 메뉴입력   2. 메뉴수정  3.메뉴목록  4.메뉴삭제  5.프로그램종료
--------------------------------------------------------------
메뉴선택 >>> ''')
    if choice == '1':
        fb.menu_input(menu)
    elif choice == '2':
        fb.menu_updatet(menu)
    elif choice == '3':
        fb.menu_list(menu)
    elif choice == '4':
        fb.menu_delete(menu)
    elif choice == '5':
        print('프로그램을 종료합니다.')
        break
    else:
        print('메뉴를 잘못 선택 하셨습니다.')