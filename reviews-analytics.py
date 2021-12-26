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
