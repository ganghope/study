import openpyxl
 # 엑셀과 시트 불러오기
wb = openpyxl.load_workbook(filename='불러올 파일명.xlsx')
wb2 = openpyxl.load_workbook(filename='저장할 파일명.xlsx')
a_sheet = wb['시트1']
b_sheet = wb2['시트1']

 # 평균을 구하는 함수 생성
def average(list):
    return (sum(list)) / len(list)

 # 키값은 중복되지 않는 성질을 이용해 딕셔너리형태로 생성
baseList = {}
for i in range(2,1199): # 불러올 파일의 원하는 구간만큼
    baseList[a_sheet['b' + str(i)].value] = 0 # 모든 품목코드를 키값:0의 형태로 저장
for j in range(0,len(baseList.keys())): # 키값마다 불러와서
    code = list(baseList.keys())[j] # 변수에 저장
    lis = []
    for n in range(2,1199): # 해당 키값과 일치하는 항목 발견시
        if code == a_sheet['b'+str(n)].value:
            lis.append(a_sheet['e'+str(n)].value) # 키값에 해당하는 리스트에 값을 추가
    for nu in range(2,4128): # 저장할 파일의 필요한 구간만큼
        if code == b_sheet['a'+str(nu)].value: # 저장할 파일에 해당 키값의 일치여부 확인
            b_sheet['f'+str(nu)] = average(lis) # 일치할때 값의 평균을 작성

wb2.save('완성본.xlsx') # 작성이 끝난 파일 저장
print('완료')