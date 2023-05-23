def solution(numer1, denom1, numer2, denom2):
    answer = []
    print(max(denom1,denom2),denom1*denom2+1)
    for i in range(max(denom1,denom2),denom1*denom2+1):
        if denom1%i==0 and denom2%i==0:
            answer.append(int((numer1*(denom1/i))+(numer2*(denom2/i))))
            answer.append(i)
            break
    return answer

print(solution(1,2,3,4))