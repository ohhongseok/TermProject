#main.py 정의
#메인 실행 함수 및 메뉴 화면 제공 및 실제 기능 func 호출
import boto3
import function_defi

# ec2 객체 모음


#기능 테스트용 필드

#기능 테스트용 필드 끝

def MainMenu():
    print("--------------------------------------------------\n")
    print("-----------------------메뉴-----------------------\n")
    print("1. list instance             2. available zones\n")
    print("3. start instance            4. available regions\n")
    print("5. stop instance             6. create instance\n")
    print("7. reboot instance           8. list images\n")
    print("9. create image             10. terminate instance\n")
    print("11.delete AMI Img           12. volume\n")
    print("                            98. Key Fair Info\n")
    print("                            99. quit\n")
    print("--------------------------------------------------\n")
    print("--------------------------------------------------\n")

#메인메뉴 번호 호출부분
def SelectMenu():
    SelectNum = int(input('Select Number : ')) 
    return SelectNum

MainMenu()

Number = SelectMenu()

while True :
    if Number==1:
        function_defi.ListInstance()
    elif Number==2:
        function_defi.AvailableZone()
    elif Number==3:
        function_defi.StartInstance()
    elif Number==4:
        function_defi.AvailableRegions()
    elif Number==5:
        function_defi.StopInstance()    
    elif Number==6:
        function_defi.CreateInstance()
    elif Number==7:
        function_defi.RebootInstance()
    elif Number==8:
        function_defi.ListImages()
    elif Number==9:
        function_defi.CreateImage()
    elif Number==10:
        function_defi.TermianteInstance()
    elif Number==11:
        function_defi.DeleteImg()    
    elif Number==12:
        function_defi.Volume()    
    elif Number==99:
        break 
    MainMenu() 
    Number = SelectMenu()
    
print("프로그램 종료\n") 
