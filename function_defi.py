#function_defi 정의
#실제 구현 func 동작부분, 기능에 대한 함수를 모아놨음
import boto3

ec2 = boto3.resource('ec2')
ec2client = boto3.client('ec2')
keypairinfo = ec2client.describe_key_pairs()

#메뉴 기능 구현 부분
def ListInstance():
    print("\n")
    print("ListInstance\n")
    for instance in ec2.instances.all():
        print("[Instance ID] "+instance.instance_id , 
              " [Instance Name] "+instance.state.get('Name'), 
              " [Instance Type] "+instance.instance_type, 
              " [Instance Image ID] "+instance.image_id, 
              " [Instance State] "+instance.monitoring.get('State'))

def AvailableZone():
    print("\n")
    print("AvailableZone\n")
    available_region = ec2client.describe_availability_zones()
    RegionArr = available_region.get("AvailabilityZones")
    for ReginInfo in RegionArr:
        print("[id] "+ReginInfo.get("ZoneId"),
              " [region] "+ReginInfo.get("RegionName"),
              " [zone] "+ReginInfo.get("ZoneName")
              
              )

def StartInstance():
    print("\n")
    print("StartInstance\n")
    forSelectInstance()
    selectid = str(input('Enter instance id : '))
    result = ec2client.start_instances(
    InstanceIds=[
        selectid,
        ],
    )
    print(result)

def AvailableRegions():
    print("\n")
    print("AvailableRegions\n")
    AvailaleRegionArr = ec2client.describe_regions().get('Regions')
    for RegionInfo in AvailaleRegionArr:
        print("[Region] "+RegionInfo.get("RegionName"),
              " [endpoint] "+RegionInfo.get("Endpoint")
              )

def StopInstance():
    print("\n")
    print("StopInstance\n")
    forSelectInstance()
    selectid = str(input('Enter instance id : '))
    result = ec2client.stop_instances(
    InstanceIds=[
        selectid,
        ],
    )
    print(result)
    
def CreateInstance():
    print("\n")
    print("CreateInstance\n")
    print("EC2 인스턴스 생성중..")
    
    ec2client.run_instances(
        ImageId="ami-0d718c3d715cec4a7",
        MinCount=1,
        MaxCount=1,
        InstanceType = "t2.micro",
        KeyName="aws1"
    )
    print(ec2client.describe_instances()["Reservations"][0]["Instances"][0]["InstanceId"]+"인스턴스 생성 완료")


def RebootInstance():
    print("\n")
    print("RebootInstance\n")
    forSelectInstance()
    selectid = str(input('Enter instance id : '))
    response = ec2client.reboot_instances(
    InstanceIds=[
        selectid,
    ],
    )
    print(response)
    

def ListImages():
    print("\n")
    print("ListImages\n")
    amiImage = ec2client.describe_images(Owners=['self'])
    for image in amiImage['Images']:
        print ("[ImageID] "+image['ImageId']," [Name] "+image['Name']," [Owner] "+image['OwnerId'])

# 추가 구현 instance 부분
def CreateImage():
    print("\n")
    print("Create AMI\n")
    forSelectInstance()
    selectInstance = str(input('인스턴스 id 입력 : '))
    imgName = str(input('이미지 이름 입력 : '))
    imgDesc = str(input('이미지 설명 추가 : '))
     
    ec2client.create_image(
        InstanceId=selectInstance,
        Name=imgName,
        Description=imgDesc,
        NoReboot=True
    )
     
def CopyImage():
    print("\n")
    print("Copy AMI\n")
    
    setName = str(input('이름 설정 : '))
    setDescription = str(input("설명 : "))
    setAMIImage = str(input('AMI 이미지 선택 : '))
    setRegion = str(input('지역 선택(기본 us-east-2) :'))
    
    result = ec2client.copy_image(
        Name = setName,
        Description =setDescription,
        SourceImageId=setAMIImage,
        SourceRegion=setRegion
    )
     
def TermianteInstance():
    print("\n")
    print("Terminate Instance\n")
    forSelectInstance()
    selectInstance = str(input('인스턴스 id 입력 : '))
    ec2client.terminate_instances(
        InstanceIds=
        [
            selectInstance,
        ]
    )
    
def DeleteImg():
    print("\n")
    print("Delete AMI Image\n")
    forSelectImage()
    selectAMI_ID = str(input('AMI Image id 입력 : '))
    
    delImg=ec2client.deregister_image(
        ImageId=selectAMI_ID
    )

def Security():
    response = ec2client.describe_instances()
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            print("Instance: " + instance['InstanceId'])
            for securityGroup in instance['SecurityGroups']:
                print("SG ID: {}, Name: {}".format(securityGroup['GroupId'], securityGroup['GroupName']))
    
#키페어 관리 부분
def KeyFunction():
    print("\n")
    print("KeyFunction\n")
    KeyMenu()
    SelectNum = int(input('Select Number : '))
    while True:
        if SelectNum == 1:
            PrintKeyPair()
        elif SelectNum ==2:
            CreateKeyPair()        
        elif SelectNum ==99:
            break   
        KeyMenu()
        SelectNum = int(input('Select Number : '))
            
def PrintKeyPair():
    print("\n")
    print("PrintKeyPair\n")
    keyPairArr = keypairinfo.get("KeyPairs")
    for KeyInfo in keyPairArr:
        print("[KeyName] "+KeyInfo.get("KeyName"), 
              " [KeyPairId] "+KeyInfo.get("KeyPairId"),
              " [KeyType] "+KeyInfo.get("KeyType"))
        
def CreateKeyPair():
    print("\n")
    print("CreateKeyPair(RSA Only\n")
    keyname = input('키 이름을 입력하세요 : ')
    ec2client.create_key_pair(
        KeyName=keyname,
        KeyType='rsa'
    )
    try:
        print(keyname+" 생성 완료")
    except ValueError as m :
        print(m)    

def DeleteKeyPair():
    print("\n")
    print("DeleteKeyPair\n")
    KeyPairMenu()
    DelKeyPair = input("삭제할 키페어 ID 선택 : ")
    keypairinfo.delecte(
        KeyPairId=DelKeyPair
    )
    try:
        print(DelKeyPair+" 삭제 완료")
    except ValueError as m :
        print(m)
# 볼륨 ID 출력
def Volume():
    print("\n")
    print("Print Volume ID\n")
    for volumme in ec2.volumes.all():
        print(volumme.volume_id)
        

# 볼륨 관리 함수 끝

#기능함수 보조
#간단한 인스턴스 및 / 이미지 출력 리스트 함수 구현, 메뉴화면 구성 부분
def forSelectInstance():
    print("----------------------------------------------------------\n")
    print("-------------------인스턴스 리스트------------------------\n")
    for instance in ec2.instances.all():
        print("[Instance ID] "+instance.instance_id , " [Instance Name] "+instance.state.get('Name'))
    print("----------------------------------------------------------\n")
    print("----------------------------------------------------------\n")
    
def forSelectImage():
    print("----------------------------------------------------------\n")
    print("--------------------이미지 리스트-------------------------\n")
    amiImage = ec2client.describe_images(Owners=['self'])
    for image in amiImage['Images']:
        print ("[ImageID] "+image['ImageId']," [Name] "+image['Name'])
    print("----------------------------------------------------------\n")
    print("----------------------------------------------------------\n")
        
def KeyMenu():
    print("----------------------------------------------------------\n")
    print("--------------------키페어 관리 메뉴----------------------\n")
    print("1. 보유 키페어 출력          2. 키페어 생성\n")
    print("3. 보유 키페어 삭제          99. 나가기\n")
    print("----------------------------------------------------------\n")
    print("----------------------------------------------------------\n")

def KeyPairMenu():
    print("----------------------------------------------------------\n")
    print("---------------------키페어 리스트------------------------\n")
    PrintKeyPair()
    
def VolumeMenu():
    print("----------------------------------------------------------\n")
    print("--------------------볼륨 관리 메뉴----------------------\n")
    print("1. 보유 볼륨 출력           2. 볼륨 생성\n")
    print("3. 보유 볼륨 삭제          99. 나가기\n")
    print("----------------------------------------------------------\n")
    print("----------------------------------------------------------\n")