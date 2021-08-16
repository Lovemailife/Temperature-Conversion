print('攝氏華氏溫度換算器')
tepmtrans=input('請問你要換算 攝氏/華氏 ?')

if tepmtrans == '攝氏':
    c = input('請輸入溫度:')
    c = int (c)
    f = c * 1.8 + 32   
    print('華氏溫度:', f,'°F')

if tepmtrans == '華氏':
    f = input ('請輸入華氏溫度:')
    f = int (f)
    c = ( f - 32 ) / 1.8
    print('攝氏溫度:', c,'°C')

#github 上傳
#git add 檔名.py
#git commit -m "version"
#git push -u origin main