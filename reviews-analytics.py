# 計算留言筆數及每筆留言平均長度

reviews = []
reviews_len = []
count = 0 		# 計算留言筆數
sum_len = 0 	# 字串總長度
with open('reviews.txt', 'r') as f:
	for line in f:
		reviews.append(line) 	# 將每筆留言存至清單reviews
		sum_len = sum_len + len(reviews[count])
		count += 1
		if count % 5000 == 0:
			print(count)

print('總共有', count, '筆留言')

avg_len = sum_len / count
print('平均留言長度是：', round(avg_len, 2), '個字母')

# 計算每個單字被使用的次數
wc = {} # word_count
for line in reviews:
	words = line.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1

print('輸入超過100萬次以上的單字：')
for word in wc:
	if wc[word] > 1000000:
		print(word,wc[word])

# 讓使用者查詢單字使用次數
while True:
	print('結束請按\'Q\'\n')
	key = input('請輸入要查詢使用次數的字：')
	if key == 'Q':
		break
	elif key not in wc:
		print('沒有使用過這個字！')
	else:
		print(key, '的使用次數：', wc[key])

