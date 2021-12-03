# TermProject
Term project repo for Cloud Computing. 

### 프로젝트 목적
해당 프로젝트 진행을 통해, aws 원격제어 활용

### 설치 환경
Window 10

### 사용 툴
1. python
2. cmder
3. vs code

### 설치파일 
1. boto3
2. AWS CLI2
3. python3

### 간단한 튜토리얼
AWS Instance(ec2) 확인하기 - https://freesunny.tistory.com/21 


### 시퀸스
1. 인증 시퀸스 받기 (AWS CLI활용)
2. boto3 라이브러리 다운로드 후 boto3 docmunent 사이트 활용


### 구현기능 및 기능 설명
1.   List Instance
      - 현재 본인이 보유하고 있는 Instance 출력
2.   Available Zones
      - 이용가능한 Region 내의 IDC 출력
3.   Start Instance
      - 현재 본인이 보유하고 있는 Instance id 값 출력 후 시작
4.   Available Region 
      - 이용가능한 AWS 물리 저장소 장소 출력
5.   Stop Instance
      - 사용자가 보유한 인스턴스 중 ID값 출력 후 해당 ID의 INSTANCE 멈춤
6.   Create Instance
      - AMI ID 값을 활용하여 인스턴스 생성
7.   Reboot Instance
      - 사용자의 보유 인스턴스 Id를 활용하여 인스턴스 재시작
8.   List Images
      - 사용자가 보유하고 있는 AMI 이미지를 출력
9.   Create Image
      - INSTANCE ID 값을 활용하여 AMI 이미지를 생성
10.  TerminateInstance
      - 사용자가 보유한 Instance ID값을 활용하여 인스턴스 종료(삭제)
11.  DeleteImg
      - 사용자가 보유한 AMI 이미지의 값을 삭제
12.  Print Volume ID
      - 현재 사용자가 인스턴스에 연결한 스토리지의 볼륨 Id값을 출력
21.  Security Group Print
      - 보안그룹 전체 출력
22.  Key Pair Info
      - Print Key Pair
        - 사용자가 보유하고 있는 키페어 출력
      - Create Key Pair
        - 사용자의 키페어 생성
      - Delete Key Pair
        - 사용자의 키페어 삭제
      - Exit 
99. Exit
  

### 참고 사이트
1. boto3 라이브러리
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#instance
2. AWS CLI 인증관련
https://www.daleseo.com/aws-cli-configure/


