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
char_count = {}

for line in f:
    #移除換行符號
    line = line.strip()
    if line in char_count:
        char_count[line] += 1
    else:
        char_count[line] = 1
    