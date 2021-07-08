# 진수 변환기
이 프로젝트는 학교 정보과목의 세특을 위해 제작되었습니다. (20916 이동훈)

## 소개
+ 이 프로젝트는 **Python 3.8.10** 을 이용해 제작되었습니다.
+ 이 프로젝트는 세특 제출용이며, 정보시간에 배운 내용들을 이용한 문제 해결 과정이 자세히 서술되어있습니다.
+ 간단하게 모듈을 사용해서 계산할수도 있지만, 교과서의 **문제해결과 프로그래밍** 단원을 이용하기 위해, 학교에서 배운 계산방법을 이용하여 최대한 사람처럼 계산하도록 구현하였습니다.
+ 시간상 CLI 형식으로 제작하였습니다. (시간날때 GUI로 바꿀 예정입니다.)

---------------------------------------
### 문제분석
문제 : 정보시간에 우리는 2진수를 10진수로, 10진수를 2진수로, 2진수를 16진수로 바꾸는등 2진수, 10진수, 16진수들을 변환하는 방법을 배웠다.
하지만 우리가 손으로 직접 계산을 하게 되면 큰 숫자의 계산에는 너무 오랜시간이 걸린다.


#### 문제의 이해와 분석

현재상태 : 커다란 수에 대한 진수의 변환이 너무 오래 걸린다.
목표상태 : 빠른 속도로 진수의 변환을 계산한다.
조건 : 없음
필요한 정보 : 진수의 변환을 계산하는 방법


#### 문제의 분해
+ 진수변환에 필요한 계산식은 무었인가
+ 어떤것이 계산의 속도가 빠른가
+ 어떻게하면 계산을 효율적으로 할수 있는가

------------------------------------
### 문제의 구조화
어떤 계산이 필요한지 구조화 해 보았다.

![image](https://user-images.githubusercontent.com/77449586/124903715-330c8a80-e01f-11eb-9b9b-b928bc78f2c0.png)

------------------------------------
### 알고리즘
알고리즘의 다섯가지 조건은
* 0개 이상의 입력
* 1개 이상의 출력
* 수행가능성
* 명확성
* 유한성
이 있다. 이 조건들에 맞춰 알고리즘을 짜보자.

#### 알고리즘 설계
이 프로젝트에선 **의사코드** 를 이용해 구성한뒤, **순서도** 를 이용하여 알고리즘을 설계해볼것이다. 우선 간단한 틀을 잡아보도록 하자.

이 프로그램은 다음과 같은 방식으로 사용될것이다.
1. 계산의 종류를 고른다. (예시 : 2진수 => 10진수, 2진수 => 16진수 등등..)
2. 변환(계산)할 값을 입력한다.
3. 계산한다.
4. 계산된값을 출력한다.
5. 더 계산할것인지 물어본다.
6. 만약 사용자가 계속 계산한다고 입력하면 1번의 과정으로 돌아가고, 아니면 프로그램을 종료한다.

그리고 계산은 다음과 같은 방식으로 이루어 질 것이다.

**2진수 => 10진수**
1. 2진수의 총 길이를 측정한다. => 변수에 길이를 할당한다.
2. 뒤에서부터 1인지, 0인지 측정한 뒤, 1이라면 2*{전체길이-현재index} 를 결괏값에 더한다.
3. 만약 현재index == 0 이라면 결괏값을 리턴하고, 아니라면 2번으로 다시 돌아간다.

**2진수 => 16진수**
1. 뒤에서부터 4글자를 자른다.
2. 잘라진 조각을 10진수로 변환한다.
3. 변환된 조각을 16진수로 변환한다. (dict 이용) (1일때 1, 10일때 A 등의 패턴매칭 방법으로 배웠음으로, 그대로 활용)
4. 결괏괎에 합친다. (문자열 방식으로)
5. 만약 계산할게 남아있다면 1번으로 돌아간다.

**10진수 => 2진수**
1. 입력된 값을 2로 나눈다.
2. 나머지와 몫을 따로 저장한다.
3. 나머지의 값을 결괏값의 마지막에 넣는다.
4. 만약 몫이 1 또는 0 이라면 몫을 결괏값의 마지막에 넣은뒤 결괏값을 리턴하고, 아니라면 1번으로 돌아간다.

**10진수 => 16진수** (16 이상에서의 10진수를 바로 16진수로 변환하는 계산법을 배우지 않았기 때문에, 아래의 방식을 사용함)
1. 10진수를 2진수로 변환한다 (위의 10진수 => 2진수 알고리즘 사용)
2. 변환된 2진수를 16진수로 변환한다. (위의 2진수 => 16진수를 이용)
3. 변환된 16진수를 리턴한다.

**16진수 => 2진수**
1. 한글자씩 뒤에서부터 분리한다.
2. 분리된 글자를 2진수로 변환한다. (dict 이용하며, 만약 마지막 글자가 아니면 4글자까지 앞의 공백을 0으로 처리한다.)
3. 만약 입력된 수가 남아있다면 1번으로 돌아가고 아니라면 결괏값을 리턴한다.


