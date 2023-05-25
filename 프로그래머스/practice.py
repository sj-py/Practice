def solution(numer1, denom1, numer2, denom2):
    answer = []
    for i in range(max(denom1,denom2),denom1*denom2+1):
        if i%denom1==0 and i%denom2==0:
            answer.append(int((numer1*(i/denom1)+(numer2*(i/denom2)))))
            answer.append(i)
            break
    return answer

print(solution(1,1,1,1))