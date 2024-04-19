#빈 리스트에 점수 입력, 합계, 총인원수, 평균 출력
#입력받은 값이 숫자 아닌 문자면 입력 종료
#while문 반복, isdigit으로 구분, append로 추가, break로 반복중단

score=[]
while True:
  score=input("학생의 점수를 입력하세요.")
  if score.isdigit():
    score.append(int(score))
  else:
    break
print(score)
print("합계:", sum(score), "총인원수:", len(score), "평균:",  sum(score)/len(score))