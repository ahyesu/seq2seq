import pandas as pd

data_head = [] #빈 리스트 생성
data_text = []

for i in range (1,402):
	file_name = str(i)+'.txt' # 텍스트 파일 이름 
	file_name = file_name.rjust(7,'0') # 001.txt, 011.txt로 만들어주기 위해

	file_name_headlines= 'D:\\캡스톤\\archive\\BBC News Summary\\News Articles\\business\\'+ file_name
	file_name_text = 'D:\\캡스톤\\archive\\BBC News Summary\\Summaries\\business\\' + file_name


	#print(file_name)

	f_head = open(file_name_headlines,'rt')
	f_text = open(file_name_text,'rt')
	
	firstline_head = f_head.readline()
	firstline_text = f_text.readline()
	

	data_head.append(firstline_head[:-1]) # \n 제거
	data_text.append(firstline_text[:-1])
	

before_df = ({'headlines' : data_head, \
              'text' : data_text}) #딕셔너리 생성



df = pd.DataFrame(before_df)

df.to_csv('sport.csv', index = False, encoding = 'cp949') #csv 생성

	

#print(df)

