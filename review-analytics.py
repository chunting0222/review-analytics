data =[]
count = 0 # 計次功用
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 # count = count + 1
		if count % 1000 == 0:
			print(len(data)) # 觀看程式跑的進度

print('檔案讀取完了，總共有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)

print('留言的平均長度為', sum_len / len(data))

new =[]
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆資料長度小於100')
print(new[0])
print(new[1])
print(new[2])