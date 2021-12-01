import boto3

# ec2 객체 모음
ec2 = boto3.resource('ec2')
ec2client = boto3.client('ec2')

print("Create EC2 INSTANCE")

ec2client.run_instances(
    ImageId="ami-0d718c3d715cec4a7",
    MinCount=1,
    MaxCount=1,
    InstanceType = "t2.micro",
    KeyName="aws1"
)


'''
response = ec2client.describe_instances()
for instances in response['Reservations']:
     print(instances)
'''


'''
regions = [region['RegionName'] for region in available_region.describe_regions()['Regions']]
endpoint = [endpoint['Endpoint'] for endpoint in available_region.describe_vpc_endpoints()['Endpoints']]
print("[Region]: ",regions)
print("[EndPoint]:",endpoint)
'''

# 이미지 테스트
'''
image = ec2.Image('ami-0f649625b95d5bd72')
print(image.creation_date)
'''

'''
for instance in ec2.instances.all():
    print(instance.instance_id , instance.state, instance.instance_type, instance.ami_launch_index, instance.monitoring)

selectid = str(input('Enter instance id : '))
result = ec2client.stop_instances(
    InstanceIds=[
        selectid,
        ],
)
print(result)
'''

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
    available_region = ec2client.describe_availability_zones()
    print(available_region)

def StartInstance():
    print("StartInstance\n")
    selectid = str(input('Enter instance id : '))
    result = ec2client.start_instances(
    InstanceIds=[
        selectid,
        ],
    )
    print(result)

def AvailableRegions():
    print("AvailableRegions\n")
    available_region = ec2client.describe_regions()
    print(available_region)

def StopInstance():
    print("StopInstance\n")
    selectid = str(input('Enter instance id : '))
    result = ec2client.stop_instances(
    InstanceIds=[
        selectid,
        ],
    )
    print(result)
    
def CreateInstance():
    print("CreateInstance\n")

def RebootInstance():
    print("RebootInstance\n")
    response = ec2client.reboot_instances(
    InstanceIds=[
        selectid,
    ],
    DryRun=True|False
    )
    print(result)
    

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