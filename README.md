# 진수 변환기

이 프로젝트는 학교 정보과목의 세특을 위해 제작되었습니다. (20916 이동훈)

## 소개

+ 이 프로젝트는 **Python 3.8.10** 을 이용해 제작되었습니다.
+ vscode 에디터를 사용하였습니다.
+ 이 프로젝트는 세특 제출용이며, 정보시간에 배운 내용들을 이용한 문제 해결 과정이 자세히 서술되어있습니다.
+ 간단하게 모듈을 사용해서 계산할수도 있지만, 교과서의 **문제해결과 프로그래밍** 단원을 이용하기 위해, 학교에서 배운 계산방법을 이용하여 최대한 사람처럼 계산하도록 구현하였습니다.
+ 시간상 CLI 형식으로 제작하였습니다. (시간날때 GUI로 바꿀 예정입니다.)
+ black code style 를 사용하여, 설명이 긴 줄일경우 이상하게 잘릴수도 있습니다.

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

+ 0개 이상의 입력
+ 1개 이상의 출력
+ 수행가능성
+ 명확성
+ 유한성
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
3. 나머지의 값을 결괏값의 제일 앞에 넣는다.
4. 만약 몫이 1 또는 0 이라면 몫을 결괏값의 제일 앞에 넣은뒤 결괏값을 리턴하고, 아니라면 1번으로 돌아간다.

**10진수 => 16진수** (16 이상에서의 10진수를 바로 16진수로 변환하는 계산법을 배우지 않았기 때문에, 아래의 방식을 사용함)

1. 10진수를 2진수로 변환한다 (위의 10진수 => 2진수 알고리즘 사용)
2. 변환된 2진수를 16진수로 변환한다. (위의 2진수 => 16진수를 이용)
3. 변환된 16진수를 리턴한다.

**16진수 => 2진수**

1. 한글자씩 뒤에서부터 분리한다.
2. 분리된 글자를 2진수로 변환한다. (dict 이용하며, 만약 마지막 글자가 아니면 4글자까지 앞의 공백을 0으로 처리한다.)
3. 만약 입력된 수가 남아있다면 1번으로 돌아가고 아니라면 결괏값을 리턴한다.

**16진수 => 10진수**

1. 위의 16진수 => 2진수를 이용해 2진수로 변환한다.
2. 변환된 2진수를 2진수 => 10진수를 이용해 10진수로 변환한다.
3. 결괏값을 리턴한다.

**순서도 그리기**
위의 내용을 순서도로 그려보았다. (잘 안보일때를 대비해 파일을 첨부함. <https://app.diagrams.net/> 에서 파일을 열수 있다.)
![ddd](https://user-images.githubusercontent.com/77449586/125057628-6b29d100-e0e4-11eb-888a-31e4d8aaef95.png)

### 코드 짜기

이제 위에서 구성한것들을 바탕으로 코드를 짜보자.

우선 값을 받아오는 부분을 만들어야 한다.
파이썬에서의 값 입력은 `input()` 이라는 내장함수를 이용한다.

사용예시

```python
input_value = input("콘솔에 나타날 글씨")
print(input_value) # 콘솔에 입력한 값이 그대로 출력된다.
```

그리고 우리의 프로그램은 다시 시작하는 기능도 들어있어서, 바닥에 코드를 짜게된다면 다시 시작하는(처음과정으로 돌아가는) 기능을 구현할수 없다.
따라서 값을 입력받는 함수를 만들어 볼것이다.

값 입력 함수

```python
def starting():
    input_num = input("변환할 수를 입력해주세요...\n>>") # 콘솔에 input() 함수안의 문자열을 출력하고, 입력받은 값을 input_num에 저장한다.
    input_num_type = int(
        input(
            """입력한 수가 몇진수인지 아래의 표를보고 숫자를 입력해주세요.
    1. 2진수
    2. 10진수
    3. 16진수
    >>"""
        )
    ) # 콘솔에 input() 함수안의 문자열을 출력하고, 입력받은 값을 input_num_type 에 저장한다.
    convert_num_type = int(
        input(
            """입력한 수를 어떤수로 변환하시겠습니까?
    1. 2진수
    2. 10진수
    3. 16진수
    >>"""
        )
    ) # 콘솔에 input() 함수안의 문자열을 출력하고, 입력받은 값을 convert_num_type 에 저장한다.

```

위의 코드는 변환할수, 변환할수의 진수, 변환시킬 수의 진수를 입력받아 각각 `input_num`, `input_num_type`, `convert_num_type` 라는 이름의 변수에 저장된다.
또한 input() 함수는 값을 문자열 형태로 받아오기때문에, type를 나타내는 변수는 모두 정수형으로 변환해준다.
그리고 순서도에서 입력값의 진수, 변환값의 진수에따라 다른 기능이 실행되는 부분이 있다. 그 부분도 한번 구현해 보자.

```python
# 위의 코드블럭에서 이어짐...
    try:
        if input_num_type == 1:  # 만약 입력값이 2진수일때
            if convert_num_type == 1:  # 만약 출력할 값이 2진수일때
                ...
            elif convert_num_type == 2:  # 만약 출력할 값이 10진수일때
                ...
            elif convert_num_type == 3:  # 만약 출력할 값이 16진수일때
                ...
            else:
                raise ValueError("올바르지 않은 입력값입니다. [1, 2, 3] 중 하나를 입력해주세요.")
        elif input_num_type == 2:  # 만약 입력값이 10진수일때
            if convert_num_type == 1:  # 만약 출력할 값이 2진수일때
                ...
            elif convert_num_type == 2:  # 만약 출력할 값이 10진수일때
                ...
            elif convert_num_type == 3:  # 만약 출력할 값이 16진수일때
                ...
            else:
                raise ValueError("올바르지 않은 입력값입니다. [1, 2, 3] 중 하나를 입력해주세요.")
        elif input_num_type == 3:  # 만약 입력값이 16진수일때
            if convert_num_type == 1:  # 만약 출력할 값이 2진수일때
                ...
            elif convert_num_type == 2:  # 만약 출력할 값이 10진수일때
                ...
            elif convert_num_type == 3:  # 만약 출력할 값이 16진수일때
                ...
            else:
                raise ValueError("올바르지 않은 입력값입니다. [1, 2, 3] 중 하나를 입력해주세요.")
        else:
            raise ValueError("올바르지 않은 입력값입니다. [1, 2, 3] 중 하나를 입력해주세요.")
    except ValueError:
        ...
    except Exception as error:
        print(f"알수없는 오류가 발생하였습니다. {error}")

```

아직 계산하는 함수를 만들어두지 않았기때문에 if문 안의 내용은 ... (pass) 로 설정해놓았다.
코드를 한번 보자면 input_num_type 를 먼저 확인한후, 그 안에서 convert_num_type 를 확인해 각각의 함수를 실행시킨다.
여기에서 사용자가 만약 `4` 또는 `사` 같이 case가 지정되지 않은 값을 입력할경우에는 예상치 못한 오류가 일어날확률이 매우 높다.
그런 오류를 방지하기위해 만약 `1, 2, 3` 외에 다른값을 입력했을시엔 ValueError를 일으키며 처음으로 돌아갈지 물어보게 될것이다.

이제 계산에 필요한 에셋을 만들어보자.
순서도를 보면 10진수 - 16진수 같은 표들이 몇개 있다. 이 표들을 파이썬의 dict 형식으로 만들어보자.

```python
dict_10_16 = {
    "0": "0",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "10": "A",
    "11": "B",
    "12": "C",
    "13": "D",
    "14": "E",
    "15": "F",
}

dict_16_2 = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}

dict_2_16 = {
    "0000": "0",
    "0001": "1",
    "0010": "2",
    "0011": "3",
    "0100": "4",
    "0101": "5",
    "0110": "6",
    "0111": "7",
    "1000": "8",
    "1001": "9",
    "1010": "A",
    "1011": "B",
    "1100": "C",
    "1101": "D",
    "1110": "E",
    "1111": "F",
}
```

**입력값이 2진수인 경우**

보통 2진수에서 다른수로 바꾸는 경우가 제일 간단하기때문에, 먼저 입력값이 2진수인 경우의 코드를 만들어보자.

우선 가장 간단한 2진수를 입력받아 2진수를 출력하는(이런 경우는 거의 없겠지만) 경우를 만들어보자.

```python
def _2_to_2(num: str) -> str:
    return num
```

이것처럼 간단하게 나타낼수있다.

그 다음은 2진수를 입력받아 10진수를 출력하는 경우를 만들어보자.
![image](https://user-images.githubusercontent.com/77449586/125193057-8bdd5c80-e285-11eb-801d-e5add32c814c.png)
위의 순서도를 참고하여 만들어 볼것이다.

```python
def _2_to_10(num: str) -> int:
    num = str(
        num
    )  # 정수형 (int)은 제일뒤의 글자를 자르는 등의 행위에는 적합하지 않음으로, 자르는것에 적합한 문자열(str) 으로 변환한다.
    index = 0  # 2의 0제곱 부터 시작함으로, 초기 인덱스값을 0으로 할당한다.
    res = 0  # 뒤에서 수의 연산(더하기) 가 사용됨으로, 정수형을 사용한다.
    while (
        num
    ):  # 기본적으로 문자열은 ""(아무것도 없는상태) 일때 False 를 반환한다. 즉, 해석하자면 "num 안에 문자가 남아있을때" 가 된다.
        num_bit = num[-1:]  # 2진수를 10진수로 바꾸는 계산방식을 사용하기 위해 num의 제일 뒷자리를 자른다.
        if len(num) == 1:  # 만약 num의 길이가 1이라면
            num = ""  # num 을 ""(False를 반환하도록) 으로 만든다.
        else:  # 위의 조건이 성립하지 않으면
            num = num[:-1]  # num은 기존의 num에서 제일 마지막글자를 제외한 문자열이다.
        if num_bit == "1":  # 만약 위에서 자른 조각이 "1" 이라면
            res += (
                2 ** index
            )  # 2진수-10진수 계산방식 이용하여 2에 index를 제곱한다. (python 에서의 ** 는 제곱연산자 이다.)
        index += 1  # index에 1을 더한다.
    return res  # 만약 이곳에 도달한다면, 계산이 모두 끝난것이므로, 결괏값을 반환한다.
```

그 다음은 2진수를 입력받아 16진수를 출력하는 경우이다.
![image](https://user-images.githubusercontent.com/77449586/125193061-94359780-e285-11eb-9c83-13f7f599ecb0.png)

```python
def _2_to_16(num: str) -> str:
    num = str(num)
    res = []  # 나중에 순서를 뒤집기 편한 리스트에 결괏값을 저장한다.
    while num:  # str(문자열)형은 ""(아무것도 없을때) 일때 False 이다. 그러므로 num이라는 문자열 안에 내용이 있을때 반복한다.
        if len(num) <= 3:  # 만약 숫자의 길이가 3이하일때
            num_bit = num[-4:]  # 숫자의 조각은 뒤에서부터 4글자 까지이다.
            num = ""  # 오류를 방지하기 위해 num의 값을 False로 할당한다.
        else:  # 아니면
            num_bit = num[-4:]  # 숫자의 조각은 뒤에서부터 4글자 까지이다.
            num = num[:-4]  # 초기 입력값을 2진수로 변환한것의 처음부터 뒤에서 4글자 앞까지를 초기값에 재할당한다.
        if len(num_bit) != 4 and len(num_bit) != 0:  # 만약 숫자조각이 4글자가 아니고 0글자도 아니라면
            num_bit = f"{num_bit:0>4}"  # 숫자조각을 우측으로 정렬하고, 공백을 0으로 채운다.
        num_16 = dict_2_16[
            num_bit
        ]  # 위에서 정의한 에셋중 2진수와 16진수의 관계를 나타내는곳에서 num_bit 에 대응하는 값을 num_16에 할당한다.
        res.append(num_16)  # 결괏값을 리스트에 더한다.
    res.reverse()  # 리스트 안의 값을 뒤집는다.
    res = "".join(res)  # 문자열 형식으로 리스트 안의 내용을 모두 합친다.
    return res  # 결괏값을 반환한다.
```

우리는 학교 정보시간에 2진수를 16진수로 변환하는 경우에는 표를 사용했었음으로, 위와 같이 dict에 대입하는 방식으로 사용하였다.

**입력값이 10진수인 경우**
이제 입력값이 10진수인 경우의 계산함수를 만들어보자.

10진수를 10진수로 바꾸는 경우에도 입력값을 그대로 돌려주면 된다.

```python
def _10_to_10(num: str) -> str:
    return num
```

다음으로 10진수를 2진수로 바꿔보도록 하자.

![image](https://user-images.githubusercontent.com/77449586/125116200-53277100-e127-11eb-8da4-b7923757dd5f.png)

위의 순서도를 참고하여 코드를 작성해보자.

```python
def _10_to_2(
    num: str,
) -> str:  # 10진수를 2진수로 바꾸는 함수이다. 입력값의 타입은 타입힌트를 통해 "정수형" 임을 명시해두었다.
    num = int(num) #계산을 위해 정수형으로 변환한다.
    res = []  # 나중에 순서를 뒤집기 편한 리스트에 결괏값을 저장한다.
    while num > 1:  # 수가 1보다 크면 반복한다.
        num_quotient = num // 2  # 입력값을 2로나눈 몫이다.
        num_remainder = num % 2  # 입력값을 2로나눈 나머지다.
        res.append(str(num_remainder))  # 리스트에 나머지를 추가한다.
        num = num_quotient  # num 값을 몫으로 재할당한다.
    res.append(str(num_quotient))  # 이 코드가 실행되는것은 num이 1이하가 되었을 때이다. 2진수 계산법에따라 몫을 추가한다.
    res.reverse()  # 리스트 안의 값을 뒤집는다.
    res = "".join(res)  # 문자열 형식으로 리스트 안의 내용을 모두 합친다.
    return res  # 결괏값을 반환한다.
```

10진수를 2진수로 바꾸는 계산법은 초기값을 2로나누고 그 나머지를 결괏값의 앞에 넣고, 더이상 나눌수없을때 몫을 앞에 넣는것이다.
이 계산방법을 이용하여 위의 코드를 작성하였다.

다음은 10진수를 16진수로 바꾸는것이다.
우리는 학교에서 10진수를 16진수로 변환하는 방법을 배웠고, 내용은 다음과 같다.

1. 수를 2진수로 변환한다.
2. 2진수로 변환된 수를 16진수로 변환한다.

순서도는 다음과 같다.
![image](https://user-images.githubusercontent.com/77449586/125193119-d2cb5200-e285-11eb-829f-8812683c6810.png)
어라? 뭔가 구조가 익숙하지 않은가?
그렇다! 우리는 이미 10진수를 2진수로 변환하는 경우와, 2진수를 16진수로 변환하는 경우를 이미 만들어 놨다.
이미 코드가 있음에도 다시 새로 만드는 작업은 매우 비효율적이며, 코드의 용량이 늘어나고, 개발의 피로도도 증가할것이다.

만약 이미 존재하는 코드를 무시하고 코드를 만들면 다음과 같은 결과가 나타난다.

```python
def _10_to_16(num: str)-> str:  # 10진수를 16진수로 바꾸는 함수이다. 입력값의 타입은 타입힌트를 통해 "정수형" 임을 명시해두었다.
    res = []  # 나중에 순서를 뒤집기 편한 리스트에 결괏값을 저장한다.
    while num > 1:  # 수가 1보다 크면 반복한다.
        num_quotient = num // 2  # 입력값을 2로나눈 몫이다.
        num_remainder = num % 2  # 입력값을 2로나눈 나머지다.
        res.append(str(num_remainder))  # 리스트에 나머지를 추가한다.
        num = num_quotient  # num 값을 몫으로 재할당한다.
    res.append(str(num_quotient))  # 이 코드가 실행되는것은 num이 1이하가 되었을 때이다. 2진수 계산법에따라 몫을 추가한다.
    res.reverse()  # 리스트 안의 값을 뒤집는다.
    res = "".join(res)  # 문자열 형식으로 리스트 안의 내용을 모두 합친다.
    num = res  # 결괏값을 num에 할당한다.
    res = []  # 리스트를 초기화한다.

    while num:  # str(문자열)형은 ""(아무것도 없을때) 일때 False 이다. 그러므로 num이라는 문자열 안에 내용이 있을때 반복한다.
        if len(num) <= 3:  # 만약 숫자의 길이가 3이하일때
            num_bit = num[-4:]  # 숫자의 조각은 뒤에서부터 4글자 까지이다.
            num = ""  # 오류를 방지하기 위해 num의 값을 False로 할당한다.
        else:  # 아니면
            num_bit = num[-4:]  # 숫자의 조각은 뒤에서부터 4글자 까지이다.
            num = num[:-4]  # 초기 입력값을 2진수로 변환한것의 처음부터 뒤에서 4글자 앞까지를 초기값에 재할당한다.
        if len(num_bit) != 4 and len(num_bit) != 0:  # 만약 숫자조각이 4글자가 아니고 0글자도 아니라면
            num_bit = f"{num_bit:0>4}"  # 숫자조각을 우측으로 정렬하고, 공백을 0으로 채운다.
        num_16 = dict_2_16[
            num_bit
        ]  # 위에서 정의한 에셋중 2진수와 16진수의 관계를 나타내는곳에서 num_bit 에 대응하는 값을 num_16에 할당한다.
        res.append(num_16)  # 결괏값을 리스트에 더한다.
    res.reverse()  # 리스트 안의 값을 뒤집는다.
    res = "".join(res)  # 문자열 형식으로 리스트 안의 내용을 모두 합친다.
    return res  # 결괏값을 반환한다.
```

위와 같은 코드로 나타낼수 있다.
하지만 위의 코드는 매우 길고, 비효율적이고, 알아보기 어렵다.
그렇다면 이미 만들어놓은 코드를 사용하면 어떻게 될까?

```python
def _10_to_16(
    num: str,
) -> str:  # 10진수를 16진수로 바꾸는 함수이다. 입력값의 타입은 타입힌트를 통해 "정수형" 임을 명시해두었다.
    num = str(_10_to_2(num))  # 입력값을 2진수로 변환한다.
    res = _2_to_16(num)  # 2진수로 변환된 입력값을 16진수로 변환한다.
    return res  # 결괏값을 반환한다.
```

놀랍게도 저게 끝이다!
처음의 코드와 비교하면 매우 간결해지는것을 확인할수 있다.

**입력값이 16진수인 경우**
다음으로는 입력값이 16진수 경우의 코드를 만들어보자.

16진수를 16진수로 변환하는 경우 역시 그냥 입력값을 반환하면 된다.

```python
def _16_to_16(num: str) -> str:
    return num
```

다음은 16진수를 입력받아 2진수를 반환하는 경우이다.
![image](https://user-images.githubusercontent.com/77449586/125194721-74a26d00-e28d-11eb-9885-d8845f2779aa.png)
```python
def _16_to_2(num: str) -> str:
    res = [] # 나중에 순서를 뒤집기 편한 리스트에 결괏값을 저장한다.
    while num: # str(문자열)형은 ""(아무것도 없을때) 일때 False 이다. 그러므로 num이라는 문자열 안에 내용이 있을때 반복한다.
        num_bit = num[-1:] # num_bit 에 num의 제일 마지막 글자를 할당한다.
        if len(num) == 1: # 만약 num의 길이가 1이라면
            num = "" # num에 공백을 할당한다.
        else: #위의 조건이 성립하지 않는다면
            num = num[:-1] # num은 초기num의 제일마지막글자를 제외한 값이다.
        res.append(dict_16_2[num_bit]) #list에 dict_16_2에 num_bit를 대입한 결괏값을 대입한다.
    res.reverse() # 리스트를 뒤집는다.
    res = "".join(res) #리스트를 문자열로 합친다.
    return res#결괏값을 반환한다.
```

이 코드를 한번 테스트 해보자.

```python
print(_16_to_2("68E432")) # 011010001110010000110010
```

앞에 `0` 이 붙어있어 가독성이 좋지않다.
만약 앞에 0이 붙어있다면 없애주도록 수정해보자.

```python
def _16_to_2(num: str) -> str:
    res = []  # 나중에 순서를 뒤집기 편한 리스트에 결괏값을 저장한다.
    while num:  # str(문자열)형은 ""(아무것도 없을때) 일때 False 이다. 그러므로 num이라는 문자열 안에 내용이 있을때 반복한다.
        num_bit = num[-1:]  # num_bit 에 num의 제일 마지막 글자를 할당한다.
        if len(num) == 1:  # 만약 num의 길이가 1이라면
            num = ""  # num에 공백을 할당한다.
        else:  # 위의 조건이 성립하지 않는다면
            num = num[:-1]  # num은 초기num의 제일마지막글자를 제외한 값이다.
        res.append(dict_16_2[num_bit])  # list에 dict_16_2에 num_bit를 대입한 결괏값을 대입한다.
    res.reverse()  # 리스트를 뒤집는다.
    res = "".join(res)  # 리스트를 문자열로 합친다.
    while True:  # 계속 반복한다는 의미이다.
        if res[:1] == "0":  # 만약 제일 앞글자가 0이라면
            res = res[1:]  # res는 res에서 제일앞글자(0)를 제외한 값이다.
        else:  # 위의 조건이 성립하지 않는다면
            break  # 반복문을 탈출(정지) 한다.
    return res  # 결괏값을 반환한다.
```

다음과 같이 수정함으로써 앞의 0들을 제거할수있다.

마지막으로 16진수를 10진수로 변환하는 경우이다.
![image](https://user-images.githubusercontent.com/77449586/125194731-7ec46b80-e28d-11eb-94e8-37d4e18232f8.png)

어라? 이것도 위에서 같은 기능이 있었던것 같다.
위의 순서도에서는 16진수를 2진수로 바꾼후, 2진수를 10진수로 만들었는데, 우리는 이미 다 만들어놨다.
그렇다면 만들어 놓은것으로 코드를 짜보자!

```python
def _16_to_10(num: str) -> int:
    num = _16_to_2(num)  # 입력값을 2진수로 변환한다.
    res = _2_to_10(num)  # 2진수로 변환된 값을 10진수로 변환한다.
    return res
```

마찬가지로 매우 간단하다!

자 이제 우리는 계산의 모든 경우의 코드를 짜보았다.

그런데 파이썬에 대한 지식이 조금은 있는 사람들은 뭔가 수상한것을 발견했을것이다.
보통 파이썬에서 함수를 만들땐 다음과 같이 선언한다.

```python
def 함수이름(변수명):
    # do something
    ... # pass와 같은 역할을 하며, 아무것도 안한다는 뜻이다.
```

하지만 위의 코드에서는 이런식으로 선언하였다.

```python
def 함수이름(변수명:str) -> str:
    # do something
    ...
```

그렇다. 변수명 뒤와, 괄호뒤에 타입이 생겼다!
그렇다면 이것들은 왜 넣는것일까
그냥 멋을 내기 위해서였을까? 아니다.
파이썬에서 저런식으로 변수와 리턴값의 타입을 지정해주는것을 "타입힌트"(영어론 "type hint" 또는 "annotation" 이라 부른다.) 라고한다.
이 타입힌트는 실질적으로는 코드에 **아무런 영향을 주지 못한다.**
하지만 이런식으로 타입을 지정해놓으면 개발할때 매우 편해진다.
다음의 사진은 타입힌트를 지정하지 않고, 그 함수를 사용할때의 모습이다.
![image](https://user-images.githubusercontent.com/77449586/125194786-ac111980-e28d-11eb-94e8-f49e6af296a3.png)
이때, 에디터는 변수들의 타입이 무었인지 모르기때문에, any로 지정한다.
이번엔 타입을 지정한뒤 다시 사용해보자!
![image](https://user-images.githubusercontent.com/77449586/125194818-d06cf600-e28d-11eb-9786-4a5aa5b0ca5a.png)
이것처럼 에디터가 "num의 타입은 int이고, 리턴값도 int야!" 라고 알려주는것을 볼수있다.

타입힌트처럼 코드실행엔 영향을 주진 않지만, 개발에 도움을 주는것이 또 있는데, 그것은 바로 문서화(docstring)이다!
docstring은 함수 아래에 """ """ 같이 쌍따옴표를 3번씩 사용하여 적고, 여러줄을 작성할수 있다.
아래는 docstring를 작성하고, 사용하는 모습이다.
![image](https://user-images.githubusercontent.com/77449586/125194933-5e48e100-e28e-11eb-8442-f8db58828e12.png)
이런식으로 코드들을 문서화 해놓으면 매우 편해진다!

이제 처음에 값을 입력받는 코드와, 메인코드를 완성시켜보자.

**코드 마무리 하기**

제일 처음에 짰던 값을 입력받는 코드는 다음과 같이 완성할수 있다.
```python
def starting():
    input_num = input(
        "변환할 수를 입력해주세요...\n>>"
    )  # 콘솔에 input() 함수안의 문자열을 출력하고, 입력받은 값을 input_num에 저장한다.
    input_num_type = int(
        input(
            """입력한 수가 몇진수인지 아래의 표를보고 숫자를 입력해주세요.
    1. 2진수
    2. 10진수
    3. 16진수
    >>"""
        )
    )  # 콘솔에 input() 함수안의 문자열을 출력하고, 입력받은 값을 input_num_type 에 저장한다.
    convert_num_type = int(
        input(
            """입력한 수를 어떤수로 변환하시겠습니까?
    1. 2진수
    2. 10진수
    3. 16진수
    >>"""
        )
    )  # 콘솔에 input() 함수안의 문자열을 출력하고, 입력받은 값을 convert_num_type 에 저장한다.
    try:
        if input_num_type == 1:  # 만약 입력값이 2진수일때
            if convert_num_type == 1:  # 만약 출력할 값이 2진수일때
                res = _2_to_2(input_num)
            elif convert_num_type == 2:  # 만약 출력할 값이 10진수일때
                res = _2_to_10(input_num)
            elif convert_num_type == 3:  # 만약 출력할 값이 16진수일때
                res = _2_to_16(input_num)
            else:
                raise ValueError("올바르지 않은 입력값입니다. [1, 2, 3] 중 하나를 입력해주세요.")
        elif input_num_type == 2:  # 만약 입력값이 10진수일때
            if convert_num_type == 1:  # 만약 출력할 값이 2진수일때
                res = _10_to_2(input_num)
            elif convert_num_type == 2:  # 만약 출력할 값이 10진수일때
                res = _10_to_10(input_num)
            elif convert_num_type == 3:  # 만약 출력할 값이 16진수일때
                res = _10_to_16(input_num)
            else:
                raise ValueError("올바르지 않은 입력값입니다. [1, 2, 3] 중 하나를 입력해주세요.")
        elif input_num_type == 3:  # 만약 입력값이 16진수일때
            if convert_num_type == 1:  # 만약 출력할 값이 2진수일때
                res = _2_to_2(input_num)
            elif convert_num_type == 2:  # 만약 출력할 값이 10진수일때
                res = _2_to_10(input_num)
            elif convert_num_type == 3:  # 만약 출력할 값이 16진수일때
                res = _2_to_16(input_num)
            else:
                raise ValueError("올바르지 않은 입력값입니다. [1, 2, 3] 중 하나를 입력해주세요.")
        else:
            raise ValueError("올바르지 않은 입력값입니다. [1, 2, 3] 중 하나를 입력해주세요.")
    except ValueError:
        ...
    except Exception as error:
        print(f"알수없는 오류가 발생하였습니다. {error}")

    return res
```

그리고, 시작시키고 반복하거나 종료하는 기능을 가진 메인함수도 만들어보자.
