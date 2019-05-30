import openpyxl
 # 엑셀과 시트를 불러온다
wb = openpyxl.load_workbook(filename='불러올 파일명.xlsx')
wb2 = openpyxl.load_workbook(filename='저장할 파일명.xlsx')
a_sheet = wb['시트1']
b_sheet = wb2['시트1']
 # 품목코드와 가격을 딕셔너리 형태로 저장
baseList = {}
for i in range(2,5052): # 불러올파일 필요구간
    baseList[a_sheet['b' + str(i)].value] = a_sheet['e' + str(i)].value # b열의 품목코드와 e열의 가격을 저장
print(len(baseList)) # 코드가 몇개있는지 확인

for a in range(0,1167): # print(len(baseList)) 수량 : 키값에 접근하기 위해
    code = list(baseList.keys())[a] # 변수에 키값을 하나씩 저장
    for b in range(2,6595): # 작성해야할 원가표 총 6594개
        if code == b_sheet['a'+str(b)].value: # 코드와 저장할 파일에 코드를 비교
            b_sheet['e'+str(b)] = baseList[code] # 일치할경우 저장할 파일의 e열에 해당 코드값에 대한 밸류(가격)을 넘김
            if a < 10000: # 반복을 위한 단순조건
                continue
wb2.save('완성본.xlsx') # 작성 완료된 파일을 저장
print('완료')