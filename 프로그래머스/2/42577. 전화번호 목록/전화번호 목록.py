def solution(phone_book):
    phone_set = set(phone_book)  # 해시셋 생성
    
    for number in phone_book:
        for i in range(1, len(number)):  
            if number[:i] in phone_set:  # 접두어가 존재하는지 확인
                return False  
    
    return True