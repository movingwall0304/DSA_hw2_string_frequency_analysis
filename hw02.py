#基礎資料結構與演算法hw02：統計字串出現頻率

#目標
#1.總共有多少個不重複的英文字
#2.每一個英文字出現次數為和

#加分條件
#1.是否有加註解
#2.是否有結構化
#3.變數與function名稱是否清楚可辨識
#4.是否使用github的commit與push上傳程式碼


#開啟txt文字檔
f = open('hw2_data.txt','r')
#建立空字典
word_count = {}

for line in f:
    #移除換行符號
    line = line.strip()
    #若單字已出現在字典中，則對應value加一
    if line in word_count:
        word_count[line] += 1
    #若字母不存在字典中，則以該單字做為新的key，其對應value加一
    else:
        word_count[line] = 1
print(word_count)

#計算有幾種不重複種類的單字
print('There are {} unique words in the file'.format(len(word_count)))

#請使用者輸入想要知道出現次數的單字
word = input("Which word do you want to know how many times it appears?")
print('{} appears {} times.'.format(word, word_count[word]))
