import boto3

ec2 = boto3.resource('ec2')

for instance in ec2.instances.all():
    print(instance.instance_id , instance.state, instance.instance_type, instance.ami_launch_index, instance.monitoring)

'''
def MainMenu():
    print("--------------------------------------------------\n")
    print("1. list instance             2. available zones\n")
    print("3. start instance            4. available regions\n")
    print("5. stop instance             6. create instance\n")
    print("7. reboot instance           8. list images\n")
    print("                            99. quit\n")
    print("--------------------------------------------------\n")
    
def SelectMenu():
    SelectNum = int(input('Select Number : ')) 
    return SelectNum

#Main Functrion
#1. list instance
def ListInstance():
    print("ListInstance\n")
    for instance in ec2.instances.all():
        print(instance.instance_id , instance.state, instance.instance_type, instance.ami_launch_index, instance.monitoring)


def AvailableZone():
    print("AvailableZone\n")

def StartInstance():
    print("StartInstance\n")

def AvailableRegions():
    print("AvailableRegions\n")

def StopInstance():
    print("StopInstance\n")

def CreateInstance():
    print("CreateInstance\n")

def RebootInstance():
    print("RebootInstance\n")

def ListImages():
    print("ListImages\n")

MainMenu()

Number = SelectMenu()

while True :
    if Number==1:
        ListInstance()
    elif Number==2:
        AvailableZone()
    elif Number==3:
        StartInstance()
    elif Number==4:
        AvailableRegions()
    elif Number==5:
        StopInstance()    
    elif Number==6:
        CreateInstance()
    elif Number==7:
        RebootInstance()
    elif Number==8:
        ListImages()
    elif Number==99:
        break  
    Number = SelectMenu()
    
print("프로그램 종료\n") 
'''