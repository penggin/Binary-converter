# Binary converter
# made by penggin
import string


def main():
    starting()


def starting():
    input_num = int(input("변환할 수를 입력해주세요...\n>>"))
    input_num_type = int(
        input(
            """입력한 수가 몇진수인지 아래의 표를보고 숫자를 입력해주세요.
    1. 2진수
    2. 10진수
    3. 16진수
    >>"""
        )
    )
    convert_num_type = int(
        input(
            """입력한 수를 어떤수로 변환하시겠습니까?
    1. 2진수
    2. 10진수
    3. 16진수
    >>"""
        )
    )
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


# assets
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
# 10진수
def _10_to_10(num):
    return num


def _10_to_2(num: int):  # 10진수를 2진수로 바꾸는 함수이다. 입력값의 타입은 타입힌트를 통해 "정수형" 임을 명시해두었다.
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


def _10_to_16(num: int):  # 10진수를 16진수로 바꾸는 함수이다. 입력값의 타입은 타입힌트를 통해 "정수형" 임을 명시해두었다.
    res = []  # 나중에 순서를 뒤집기 편한 리스트에 결괏값을 저장한다.
    num = str(_10_to_2(num))  # 먼저 입력값을 2진수로 변환한다.
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


print(_10_to_16(946914612448))
