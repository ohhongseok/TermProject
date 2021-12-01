#function_defi 정의
#실제 구현 func 동작부분, 기능에 대한 함수를 모아놨음
import boto3

ec2 = boto3.resource('ec2')
ec2client = boto3.client('ec2')

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
    print(available_region)

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
    available_region = ec2client.describe_regions()
    print(available_region)

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
     
def TermianteInstance():
    print("\n")
    print("Terminate Instance\n")
    forSelectInstance()
    selectInstance = str(input('인스턴스 id 입력 : '))
    ec2client.terminate_instance(
        InstanceId=selectInstance
    )
    
def DeleteImg():
    print("\n")
    print("Delete AMI Image\n")
    forSelectImage()
    selectAMI_ID = str(input('AMI Image id 입력 : '))
    
    delImg=ec2client.deregister_image(
        ImageId=selectAMI_ID
    )
def Volume():
    print("\n")
    print("Delete AMI Image\n")
    for volumme in ec2.volumes.all():
        print(volumme.volume_id)


#기능함수 보조
#간단한 인스턴스 출력 리스트 / 이미지 출력 리스트 함수 구현
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
        