from django.shortcuts import render
import random
import requests
# Create your views here.
def lotto(request):
    
    url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=953'
    response = requests.get(url).json()
    
    # 중복없이 6개 숫자와 보너스넘버 뽑는다.
    numbers = [response['drwtNo1'], response['drwtNo2'], response['drwtNo3'], response['drwtNo4'], response['drwtNo5'], response['drwtNo6'], response['bnusNo']]
    bonus_number = numbers[6]
    numbers.pop()
    sorted_numbers = sorted(numbers[:7]) 
    
    # 1000번 시도
    results = [0] * 6
    for _ in range(1000):
        count = 0
        numbers = random.sample(range(1, 46), 6)
        for number in numbers:
            if number in sorted_numbers:
                count += 1
        # 1등
        if count == 6:
            results[0] += 1
        # 2등
        elif count == 5:
            results[1] += 1
        # 3등
        elif count == 4:
            results[2] += 1
        # 4등
        elif count == 3:
            results[3] += 1
        # 5등
        elif count == 2:
            results[4] += 1
        # 꽝
        else:
            results[5] += 1

    context = {
        'numbers': sorted_numbers,
        'bonus_number': bonus_number,
        'results': results
    }

    return render(request, 'pages/lotto.html', context)