import speedtest

st = speedtest.Speedtest()
option= int(input('''
1) Download tezligi
2) Upload tezligi
Tanlash uchun kerakli sonni kiriting: '''))
if option == 1:
    print(st.download(), 'b/s')
elif option == 2:
    print(st.upload(), 'b/s')
else:
    print('Siz noto`g`ri son kiritdingiz!')
