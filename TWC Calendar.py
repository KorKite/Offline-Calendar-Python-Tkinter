from tkinter import *


#캔버스
#크롤
integ = Tk()
integ.title("TWC Online")
integ.geometry('800x622')

iniPphoto=PhotoImage(file="배경.gif")
iniP=Label(integ, image=iniPphoto)
iniP.place(x=0,y=0)

checkL = Label(integ, text="")
checkL.place(x=1,y=3)
idinfo={"1":["2","3"]}

f=open("회원정보.txt",'rt',encoding='UTF8')
spl=f.read()
spla=spl.split("/*")
pp=int((int(spl.count("/*")))/3)
ppp=pp+1
for t in range(1,ppp):
    i=3*t-3
    a=spla[i]
    b=spla[i+1]
    c=spla[i+2]
    idinfo[a]=[b,c]
f.close


def 로그인():
    idlog=hssx.get()
    passlog=hx.get()
    
    if idlog in idinfo:
        idcheck=idinfo[idlog]
        idcheck2=idcheck[0]
        if idcheck2 == passlog:
            checkL.configure(text="로그인 완료")
            integ.destroy()

            cal = Tk()
            cal.title("{}의 캘린더".format(idcheck[1]))
            cal.geometry('600x625')

            calLL=Label(cal, text="월 별 색깔은 탄생석의 색깔입니다", font=("휴먼엑스포", 15))
            calLL.place(x=10, y=600)
            
            
            calPphoto=PhotoImage(file="subcal.gif")
            calL=Label(cal, image=calPphoto)
            calL.pack()

            con=['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']

            f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
            con=eval(f.read())
            f.close
            
            
            
            def jan():
                jan=Tk()
                jan.title("1월 달력")
                jan.geometry('700x600')
                
                
                janL=Label(jan, text="", font=('휴먼엑스포', 15))
                janL.place(x=350,y=0)

                LL=Label(jan, text="1월 달력", font=('휴먼엑스포', 20))
                LL.place(x=0, y=0)


                LL=Label(jan, text="일", fg="red", font=('휴먼엑스포', 15))
                LL.place(x=25, y=65)
                LL=Label(jan, text="월", font=('휴먼엑스포', 15))
                LL.place(x=105, y=65)
                LL=Label(jan, text="화", font=('휴먼엑스포', 15))
                LL.place(x=185, y=65)
                LL=Label(jan, text="수", font=('휴먼엑스포', 15))
                LL.place(x=265, y=65)
                LL=Label(jan, text="목", font=('휴먼엑스포', 15))
                LL.place(x=345, y=65)
                LL=Label(jan, text="금", font=('휴먼엑스포', 15))
                LL.place(x=425, y=65)
                LL=Label(jan, text="토", fg="blue", font=('휴먼엑스포', 15))
                LL.place(x=505, y=65)
                
                
                
                def jan1ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    janL.configure(text="1일에 할일: {}".format(con[0]))
                    f.close

                    al=Tk()
                    al.geometry('150x100')
                    al.title("공휴일 알림")
                    alL=Label(al, text="신정입니다", font=("휴먼엑스포", 15), fg="red")
                    alL.place(x=20, y=30)

                    def 종료():
                        al.destroy()

                    alB=Button(al, text="닫기", width=0, height=0, font=(10), command=종료)
                    alB.place(x=40, y=60)


                    


                    def jan1sa():
                        od=test.get()
                        test.delete(0,END)
                        con[0]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        janL.configure(text="1일에 할일: {}".format(con[0]))
                        

                    
                        
                    janb=Button(jan,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jan1sa)
                    janb.place(x=250,y=10)

                    test=Entry(jan, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)

                


                def jan2ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    janL.configure(text="2일에 할일: {}".format(con[1]))
                    f.close
                    
                    def jan2sa():
                        td=test.get()
                        test.delete(0,END)
                        con[1]=td
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        janL.configure(text="2일에 할일: {}".format(con[1]))

                    janb=Button(jan,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jan2sa)
                    janb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jan, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def jan3ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    janL.configure(text="3일에 할일:{}".format(con[2]))
                    f.close

                    
                    def jan3sa():
                        thd=test.get()
                        test.delete(0,END)
                        con[2]=thd
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        janL.configure(text="3일에 할일:{}".format(con[2]))

                    janb=Button(jan,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jan3sa)
                    janb.place(x=250,y=10)   



                    txt=StringVar()
                    test=Entry(jan, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def jan4ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    janL.configure(text="4일에 할일: {}".format(con[3]))
                    f.close
                    

                    def jan4sa():
                        od=test.get()
                        test.delete(0,END)
                        con[3]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        janL.configure(text="4일에 할일: {}".format(con[3]))
                        
                    janb=Button(jan,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jan4sa)
                    janb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jan, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)


                def jan5ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    janL.configure(text="5일에 할일: {}".format(con[4]))
                    f.close
                    

                    def jan5sa():
                        od=test.get()
                        test.delete(0,END)
                        con[4]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        janL.configure(text="5일에 할일: {}".format(con[4]))
                        
                    janb=Button(jan,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jan5sa)
                    janb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jan, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)
                    
                def jan6ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    janL.configure(text="6일에 할일: {}".format(con[5]))
                    f.close
                    

                    def jan6sa():
                        od=test.get()
                        test.delete(0,END)
                        con[5]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        janL.configure(text="6일에 할일: {}".format(con[5]))
                        
                    janb=Button(jan,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jan6sa)
                    janb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jan, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def jan7ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    janL.configure(text="7일에 할일: {}".format(con[6]))
                    f.close
                    

                    def jan7sa():
                        od=test.get()
                        test.delete(0,END)
                        con[6]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        janL.configure(text="7일에 할일: {}".format(con[6]))
                        
                    janb=Button(jan,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jan7sa)
                    janb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jan, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def jan8ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    janL.configure(text="8일에 할일: {}".format(con[7]))
                    f.close
                    

                    def jan8sa():
                        od=test.get()
                        test.delete(0,END)
                        con[7]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        janL.configure(text="8일에 할일: {}".format(con[0]))
                        
                    janb=Button(jan,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jan8sa)
                    janb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jan, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def jan9ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    janL.configure(text="9일에 할일: {}".format(con[8]))
                    f.close
                    

                    def jan9sa():
                        od=test.get()
                        test.delete(0,END)
                        con[8]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        janL.configure(text="9일에 할일: {}".format(con[8]))
                        
                    janb=Button(jan,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jan9sa)
                    janb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jan, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def jan10ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    janL.configure(text="10일에 할일: {}".format(con[9]))
                    f.close
                    

                    def jan10sa():
                        od=test.get()
                        test.delete(0,END)
                        con[9]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        janL.configure(text="10일에 할일: {}".format(con[9]))
                        
                    janb=Button(jan,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jan10sa)
                    janb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jan, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def jan11ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    janL.configure(text="11일에 할일: {}".format(con[10]))
                    f.close
                    

                    def jan11sa():
                        od=test.get()
                        test.delete(0,END)
                        con[10]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        janL.configure(text="11일에 할일: {}".format(con[10]))
                        
                    janb=Button(jan,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jan11sa)
                    janb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jan, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def jan12ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    janL.configure(text="12일에 할일: {}".format(con[11]))
                    f.close
                    

                    def jan12sa():
                        od=test.get()
                        test.delete(0,END)
                        con[11]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        janL.configure(text="12일에 할일: {}".format(con[11]))
                        
                    janb=Button(jan,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jan12sa)
                    janb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jan, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def jan13ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    janL.configure(text="13일에 할일: {}".format(con[12]))
                    f.close
                    

                    def jan13sa():
                        od=test.get()
                        test.delete(0,END)
                        con[12]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        janL.configure(text="13일에 할일: {}".format(con[12]))
                        
                    janb=Button(jan,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jan13sa)
                    janb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jan, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def jan14ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    janL.configure(text="14일에 할일: {}".format(con[13]))
                    f.close
                    

                    def jan14sa():
                        od=test.get()
                        test.delete(0,END)
                        con[13]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        janL.configure(text="14일에 할일: {}".format(con[13]))
                        
                    janb=Button(jan,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jan14sa)
                    janb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jan, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def jan15ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    janL.configure(text="15일에 할일: {}".format(con[14]))
                    f.close
                    

                    def jan15sa():
                        od=test.get()
                        test.delete(0,END)
                        con[14]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        janL.configure(text="15일에 할일: {}".format(con[14]))
                        
                    janb=Button(jan,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jan15sa)
                    janb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jan, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def jan16ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    janL.configure(text="16일에 할일: {}".format(con[15]))
                    f.close
                    

                    def jan16sa():
                        od=test.get()
                        test.delete(0,END)
                        con[15]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        janL.configure(text="16일에 할일: {}".format(con[15]))
                        
                    janb=Button(jan,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jan16sa)
                    janb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jan, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def jan17ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    janL.configure(text="17일에 할일: {}".format(con[16]))
                    f.close
                    

                    def jan17sa():
                        od=test.get()
                        test.delete(0,END)
                        con[16]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        janL.configure(text="17일에 할일: {}".format(con[16]))
                        
                    janb=Button(jan,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jan17sa)
                    janb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jan, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def jan18ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    janL.configure(text="18일에 할일: {}".format(con[17]))
                    f.close
                    

                    def jan18sa():
                        od=test.get()
                        test.delete(0,END)
                        con[17]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        janL.configure(text="18일에 할일: {}".format(con[17]))
                        
                    janb=Button(jan,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jan18sa)
                    janb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jan, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def jan19ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    janL.configure(text="19일에 할일: {}".format(con[18]))
                    f.close
                    

                    def jan19sa():
                        od=test.get()
                        test.delete(0,END)
                        con[18]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        janL.configure(text="19일에 할일: {}".format(con[18]))
                        
                    janb=Button(jan,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jan19sa)
                    janb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jan, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def jan20ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    janL.configure(text="20일에 할일: {}".format(con[19]))
                    f.close
                    

                    def jan20sa():
                        od=test.get()
                        test.delete(0,END)
                        con[19]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        janL.configure(text="20일에 할일: {}".format(con[19]))
                        
                    janb=Button(jan,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jan20sa)
                    janb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jan, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def jan21ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    janL.configure(text="21일에 할일: {}".format(con[20]))
                    f.close
                    

                    def jan21sa():
                        od=test.get()
                        test.delete(0,END)
                        con[20]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        janL.configure(text="21일에 할일: {}".format(con[20]))
                        
                    janb=Button(jan,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jan21sa)
                    janb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jan, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def jan22ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    janL.configure(text="22일에 할일: {}".format(con[21]))
                    f.close
                    

                    def jan22sa():
                        od=test.get()
                        test.delete(0,END)
                        con[21]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        janL.configure(text="22일에 할일: {}".format(con[21]))
                        
                    janb=Button(jan,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jan22sa)
                    janb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jan, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def jan23ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    janL.configure(text="23일에 할일: {}".format(con[22]))
                    f.close
                    

                    def jan23sa():
                        od=test.get()
                        test.delete(0,END)
                        con[22]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        janL.configure(text="23일에 할일: {}".format(con[22]))
                        
                    janb=Button(jan,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jan23sa)
                    janb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jan, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def jan24ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    janL.configure(text="24일에 할일: {}".format(con[23]))
                    f.close
                    

                    def jan24sa():
                        od=test.get()
                        test.delete(0,END)
                        con[23]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        janL.configure(text="24일에 할일: {}".format(con[23]))
                        
                    janb=Button(jan,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jan24sa)
                    janb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jan, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def jan25ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    janL.configure(text="25일에 할일: {}".format(con[24]))
                    f.close
                    

                    def jan25sa():
                        od=test.get()
                        test.delete(0,END)
                        con[24]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        janL.configure(text="25일에 할일: {}".format(con[24]))
                        
                    janb=Button(jan,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jan25sa)
                    janb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jan, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def jan26ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    janL.configure(text="26일에 할일: {}".format(con[25]))
                    f.close
                    

                    def jan26sa():
                        od=test.get()
                        test.delete(0,END)
                        con[25]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        janL.configure(text="26일에 할일: {}".format(con[25]))
                        
                    janb=Button(jan,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jan26sa)
                    janb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jan, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def jan27ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    janL.configure(text="27일에 할일: {}".format(con[26]))
                    f.close
                    

                    def jan27sa():
                        od=test.get()
                        test.delete(0,END)
                        con[26]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        janL.configure(text="27일에 할일: {}".format(con[26]))
                        
                    janb=Button(jan,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jan27sa)
                    janb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jan, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def jan28ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    janL.configure(text="28일에 할일: {}".format(con[27]))
                    f.close
                    

                    def jan28sa():
                        od=test.get()
                        test.delete(0,END)
                        con[27]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        janL.configure(text="28일에 할일: {}".format(con[27]))
                        
                    janb=Button(jan,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jan28sa)
                    janb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jan, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def jan29ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    janL.configure(text="29일에 할일: {}".format(con[28]))
                    f.close
                    

                    def jan29sa():
                        od=test.get()
                        test.delete(0,END)
                        con[28]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        janL.configure(text="29일에 할일: {}".format(con[28]))
                        
                    janb=Button(jan,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jan29sa)
                    janb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jan, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def jan30ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    janL.configure(text="30일에 할일: {}".format(con[29]))
                    f.close
                    

                    def jan30sa():
                        od=test.get()
                        test.delete(0,END)
                        con[29]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        janL.configure(text="30일에 할일: {}".format(con[29]))
                        
                    janb=Button(jan,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jan30sa)
                    janb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jan, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def jan31ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    janL.configure(text="31일에 할일: {}".format(con[30]))
                    f.close
                    

                    def jan31sa():
                        od=test.get()
                        test.delete(0,END)
                        con[30]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        janL.configure(text="31일에 할일: {}".format(con[30]))
                        
                    janb=Button(jan,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jan31sa)
                    janb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jan, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)


                jan1b=Button(jan,text="1",fg="red", width=0, height=0, font=('휴먼엑스포', 20), command=jan1ex)
                jan1b.place(x=180,y=100)

                jan2b=Button(jan,text="2", width=0, height=0, font=('휴먼엑스포', 20), command=jan2ex)
                jan2b.place(x=260,y=100)

                jan3b=Button(jan,text="3", width=0, height=0, font=('휴먼엑스포', 20), command=jan3ex)
                jan3b.place(x=340,y=100)

                jan4b=Button(jan,text="4", width=0, height=0, font=('휴먼엑스포', 20), command=jan4ex)
                jan4b.place(x=420,y=100)

                jan5b=Button(jan,text="5", width=0, height=0, font=('휴먼엑스포', 20), command=jan5ex)
                jan5b.place(x=500,y=100)

                jan6b=Button(jan,text="6", width=0, height=0, font=('휴먼엑스포', 20), command=jan6ex)
                jan6b.place(x=20,y=200)

                jan7b=Button(jan,text="7", width=0, height=0, font=('휴먼엑스포', 20), command=jan7ex)
                jan7b.place(x=100,y=200)

                jan8b=Button(jan,text="8", width=0, height=0, font=('휴먼엑스포', 20), command=jan8ex)
                jan8b.place(x=180,y=200)

                jan9b=Button(jan,text="9", width=0, height=0, font=('휴먼엑스포', 20), command=jan9ex)
                jan9b.place(x=260,y=200)

                jan10b=Button(jan,text="10", width=0, height=0, font=('휴먼엑스포', 20), command=jan10ex)
                jan10b.place(x=340,y=200)

                jan11b=Button(jan,text="11", width=0, height=0, font=('휴먼엑스포', 20), command=jan11ex)
                jan11b.place(x=420,y=200)

                jan12b=Button(jan,text="12", width=0, height=0, font=('휴먼엑스포', 20), command=jan12ex)
                jan12b.place(x=500,y=200)

                jan13b=Button(jan,text="13", width=0, height=0, font=('휴먼엑스포', 20), command=jan13ex)
                jan13b.place(x=20,y=300)

                jan14b=Button(jan,text="14", width=0, height=0, font=('휴먼엑스포', 20), command=jan14ex)
                jan14b.place(x=100,y=300)

                jan15b=Button(jan,text="15", width=0, height=0, font=('휴먼엑스포', 20), command=jan15ex)
                jan15b.place(x=180,y=300)

                jan16b=Button(jan,text="16", width=0, height=0, font=('휴먼엑스포', 20), command=jan16ex)
                jan16b.place(x=260,y=300)

                jan17b=Button(jan,text="17", width=0, height=0, font=('휴먼엑스포', 20), command=jan17ex)
                jan17b.place(x=340,y=300)

                jan18b=Button(jan,text="18", width=0, height=0, font=('휴먼엑스포', 20), command=jan18ex)
                jan18b.place(x=420,y=300)

                jan19b=Button(jan,text="19", width=0, height=0, font=('휴먼엑스포', 20), command=jan19ex)
                jan19b.place(x=500,y=300)

                jan20b=Button(jan,text="20", width=0, height=0, font=('휴먼엑스포', 20), command=jan20ex)
                jan20b.place(x=20,y=400)

                jan21b=Button(jan,text="21", width=0, height=0, font=('휴먼엑스포', 20), command=jan21ex)
                jan21b.place(x=100,y=400)

                jan22b=Button(jan,text="22", width=0, height=0, font=('휴먼엑스포', 20), command=jan22ex)
                jan22b.place(x=180,y=400)

                jan23b=Button(jan,text="23", width=0, height=0, font=('휴먼엑스포', 20), command=jan23ex)
                jan23b.place(x=260,y=400)

                jan24b=Button(jan,text="24", width=0, height=0, font=('휴먼엑스포', 20), command=jan24ex)
                jan24b.place(x=340,y=400)

                jan25b=Button(jan,text="25", width=0, height=0, font=('휴먼엑스포', 20), command=jan25ex)
                jan25b.place(x=420,y=400)

                jan26b=Button(jan,text="26", width=0, height=0, font=('휴먼엑스포', 20), command=jan26ex)
                jan26b.place(x=500,y=400)

                jan27b=Button(jan,text="27", width=0, height=0, font=('휴먼엑스포', 20), command=jan27ex)
                jan27b.place(x=20,y=500)

                jan28b=Button(jan,text="28", width=0, height=0, font=('휴먼엑스포', 20), command=jan28ex)
                jan28b.place(x=100,y=500)

                jan29b=Button(jan,text="29", width=0, height=0, font=('휴먼엑스포', 20), command=jan29ex)
                jan29b.place(x=180,y=500)

                jan30b=Button(jan,text="30", width=0, height=0, font=('휴먼엑스포', 20), command=jan30ex)
                jan30b.place(x=260,y=500)

                jan31b=Button(jan,text="31", width=0, height=0, font=('휴먼엑스포', 20), command=jan31ex)
                jan31b.place(x=340,y=500)
                
      

                def 월간1():
                    toj=Tk()
                    toj.title("1월 총 계획")
                    toj.geometry('700x700')

                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    f.close
                    
                    for i in range(0,31):
                        tojL=Label(toj, text="1월 {}일:{}".format(i+1,con[i]), font=('휴먼엑스포', 15))
                        tojL.place(x=0,y=i*20)
                        
                    
                tojb=Button(jan, text="월간", height=0, font=('휴먼엑스포', 20), command=월간1)   
                tojb.place(x=450,y=500)

                jan.mainloop()
                
            janb=Button(cal, text="1월", width=4, height=2, fg='dark red',font=('휴먼엑스포', 20), command=jan)   
            janb.place(x=110,y=120)



            def feb():
                feb=Tk()
                feb.title("2월 달력")
                feb.geometry('700x600')
                febL=Label(feb, text="", font=('휴먼엑스포', 10))
                febL.place(x=350,y=0)
                LL=Label(feb, text="2월 달력", font=('휴먼엑스포', 20))
                LL.place(x=0, y=0)

                LL=Label(feb, text="일", fg="red", font=('휴먼엑스포', 15))
                LL.place(x=25, y=65)
                LL=Label(feb, text="월", font=('휴먼엑스포', 15))
                LL.place(x=105, y=65)
                LL=Label(feb, text="화", font=('휴먼엑스포', 15))
                LL.place(x=185, y=65)
                LL=Label(feb, text="수", font=('휴먼엑스포', 15))
                LL.place(x=265, y=65)
                LL=Label(feb, text="목", font=('휴먼엑스포', 15))
                LL.place(x=345, y=65)
                LL=Label(feb, text="금", font=('휴먼엑스포', 15))
                LL.place(x=425, y=65)
                LL=Label(feb, text="토", fg="blue", font=('휴먼엑스포', 15))
                LL.place(x=505, y=65)
                

                def feb1ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    febL.configure(text="1일에 할일: {}".format(con[31]))
                    f.close
                    

                    def feb1sa():
                        od=test.get()
                        test.delete(0,END)
                        con[31]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        febL.configure(text="1일에 할일: {}".format(con[31]))
                        
                    febb=Button(feb,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=feb1sa)
                    febb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(feb, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def feb2ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    febL.configure(text="2일에 할일: {}".format(con[32]))
                    f.close
                    

                    def feb2sa():
                        od=test.get()
                        test.delete(0,END)
                        con[32]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        febL.configure(text="2일에 할일: {}".format(con[32]))
                        
                    febb=Button(feb,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=feb2sa)
                    febb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(feb, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def feb3ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    febL.configure(text="3일에 할일: {}".format(con[33]))
                    f.close

                    al=Tk()
                    al.geometry('150x100')
                    al.title("공휴일 알림")
                    alL=Label(al, text="설 연휴", font=("휴먼엑스포", 15), fg="red")
                    alL.place(x=20, y=30)

                    def 종료():
                        al.destroy()

                    alB=Button(al, text="닫기", width=0, height=0, font=(10), command=종료)
                    alB.place(x=40, y=60)

                    def feb3sa():
                        od=test.get()
                        test.delete(0,END)
                        con[33]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        febL.configure(text="3일에 할일: {}".format(con[33]))
                        
                    febb=Button(feb,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=feb3sa)
                    febb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(feb, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def feb4ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    febL.configure(text="4일에 할일: {}".format(con[34]))
                    f.close

                    al=Tk()
                    al.geometry('150x100')
                    al.title("공휴일 알림")
                    alL=Label(al, text="설 연휴", font=("휴먼엑스포", 15), fg="red")
                    alL.place(x=20, y=30)

                    def 종료():
                        al.destroy()

                    alB=Button(al, text="닫기", width=0, height=0, font=(10), command=종료)
                    alB.place(x=40, y=60)
                    

                    def feb4sa():
                        od=test.get()
                        test.delete(0,END)
                        con[34]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        febL.configure(text="4일에 할일: {}".format(con[34]))
                        
                    febb=Button(feb,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=feb4sa)
                    febb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(feb, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def feb5ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    febL.configure(text="5일에 할일: {}".format(con[35]))
                    f.close

                    al=Tk()
                    al.geometry('150x100')
                    al.title("공휴일 알림")
                    alL=Label(al, text="설 연휴", font=("휴먼엑스포", 15), fg="red")
                    alL.place(x=20, y=30)

                    def 종료():
                        al.destroy()

                    alB=Button(al, text="닫기", width=0, height=0, font=(10), command=종료)
                    alB.place(x=40, y=60)

                    def feb5sa():
                        od=test.get()
                        test.delete(0,END)
                        con[35]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        febL.configure(text="5일에 할일: {}".format(con[35]))
                        
                    febb=Button(feb,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=feb5sa)
                    febb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(feb, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def feb6ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    febL.configure(text="6일에 할일: {}".format(con[36]))
                    f.close
                    al=Tk()
                    al.geometry('150x100')
                    al.title("공휴일 알림")
                    alL=Label(al, text="설 연휴", font=("휴먼엑스포", 15), fg="red")
                    alL.place(x=20, y=30)

                    def 종료():
                        al.destroy()

                    alB=Button(al, text="닫기", width=0, height=0, font=(10), command=종료)
                    alB.place(x=40, y=60)
                    

                    def feb6sa():
                        od=test.get()
                        test.delete(0,END)
                        con[36]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        febL.configure(text="6일에 할일: {}".format(con[36]))
                        
                    febb=Button(feb,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=feb6sa)
                    febb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(feb, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def feb7ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    febL.configure(text="7일에 할일: {}".format(con[37]))
                    f.close
                    

                    def feb7sa():
                        od=test.get()
                        test.delete(0,END)
                        con[37]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        febL.configure(text="7일에 할일: {}".format(con[37]))
                        
                    febb=Button(feb,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=feb7sa)
                    febb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(feb, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def feb8ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    febL.configure(text="8일에 할일: {}".format(con[38]))
                    f.close
                    

                    def feb8sa():
                        od=test.get()
                        test.delete(0,END)
                        con[38]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        febL.configure(text="8일에 할일: {}".format(con[38]))
                        
                    febb=Button(feb,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=feb8sa)
                    febb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(feb, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def feb9ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    febL.configure(text="9일에 할일: {}".format(con[39]))
                    f.close
                    

                    def feb9sa():
                        od=test.get()
                        test.delete(0,END)
                        con[39]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        febL.configure(text="9일에 할일: {}".format(con[39]))
                        
                    febb=Button(feb,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=feb9sa)
                    febb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(feb, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def feb10ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    febL.configure(text="10일에 할일: {}".format(con[40]))
                    f.close
                    

                    def feb10sa():
                        od=test.get()
                        test.delete(0,END)
                        con[40]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        febL.configure(text="10일에 할일: {}".format(con[40]))
                        
                    febb=Button(feb,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=feb10sa)
                    febb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(feb, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def feb11ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    febL.configure(text="11일에 할일: {}".format(con[41]))
                    f.close
                    

                    def feb11sa():
                        od=test.get()
                        test.delete(0,END)
                        con[41]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        febL.configure(text="11일에 할일: {}".format(con[41]))
                        
                    febb=Button(feb,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=feb11sa)
                    febb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(feb, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def feb12ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    febL.configure(text="12일에 할일: {}".format(con[42]))
                    f.close
                    

                    def feb12sa():
                        od=test.get()
                        test.delete(0,END)
                        con[42]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        febL.configure(text="12일에 할일: {}".format(con[42]))
                        
                    febb=Button(feb,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=feb12sa)
                    febb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(feb, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def feb13ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    febL.configure(text="13일에 할일: {}".format(con[43]))
                    f.close
                    

                    def feb13sa():
                        od=test.get()
                        test.delete(0,END)
                        con[43]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        febL.configure(text="13일에 할일: {}".format(con[43]))
                        
                    febb=Button(feb,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=feb13sa)
                    febb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(feb, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def feb14ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    febL.configure(text="14일에 할일: {}".format(con[44]))
                    f.close
                    

                    def feb14sa():
                        od=test.get()
                        test.delete(0,END)
                        con[44]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        febL.configure(text="14일에 할일: {}".format(con[44]))
                        
                    febb=Button(feb,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=feb14sa)
                    febb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(feb, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def feb15ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    febL.configure(text="15일에 할일: {}".format(con[45]))
                    f.close
                    

                    def feb15sa():
                        od=test.get()
                        test.delete(0,END)
                        con[45]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        febL.configure(text="15일에 할일: {}".format(con[45]))
                        
                    febb=Button(feb,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=feb15sa)
                    febb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(feb, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def feb16ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    febL.configure(text="16일에 할일: {}".format(con[46]))
                    f.close
                    

                    def feb16sa():
                        od=test.get()
                        test.delete(0,END)
                        con[46]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        febL.configure(text="16일에 할일: {}".format(con[46]))
                        
                    febb=Button(feb,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=feb16sa)
                    febb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(feb, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def feb17ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    febL.configure(text="17일에 할일: {}".format(con[47]))
                    f.close
                    

                    def feb17sa():
                        od=test.get()
                        test.delete(0,END)
                        con[47]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        febL.configure(text="17일에 할일: {}".format(con[47]))
                        
                    febb=Button(feb,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=feb17sa)
                    febb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(feb, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def feb18ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    febL.configure(text="18일에 할일: {}".format(con[48]))
                    f.close
                    

                    def feb18sa():
                        od=test.get()
                        test.delete(0,END)
                        con[48]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        febL.configure(text="18일에 할일: {}".format(con[48]))
                        
                    febb=Button(feb,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=feb18sa)
                    febb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(feb, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def feb19ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    febL.configure(text="19일에 할일: {}".format(con[49]))
                    f.close
                    

                    def feb19sa():
                        od=test.get()
                        test.delete(0,END)
                        con[49]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        febL.configure(text="19일에 할일: {}".format(con[49]))
                        
                    febb=Button(feb,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=feb19sa)
                    febb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(feb, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def feb20ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    febL.configure(text="20일에 할일: {}".format(con[50]))
                    f.close
                    

                    def feb20sa():
                        od=test.get()
                        test.delete(0,END)
                        con[50]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        febL.configure(text="20일에 할일: {}".format(con[50]))
                        
                    febb=Button(feb,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=feb20sa)
                    febb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(feb, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def feb21ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    febL.configure(text="21일에 할일: {}".format(con[51]))
                    f.close
                    

                    def feb21sa():
                        od=test.get()
                        test.delete(0,END)
                        con[51]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        febL.configure(text="21일에 할일: {}".format(con[51]))
                        
                    febb=Button(feb,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=feb21sa)
                    febb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(feb, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def feb22ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    febL.configure(text="22일에 할일: {}".format(con[52]))
                    f.close
                    

                    def feb22sa():
                        od=test.get()
                        test.delete(0,END)
                        con[52]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        febL.configure(text="22일에 할일: {}".format(con[52]))
                        
                    febb=Button(feb,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=feb22sa)
                    febb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(feb, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def feb23ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    febL.configure(text="23일에 할일: {}".format(con[53]))
                    f.close
                    

                    def feb23sa():
                        od=test.get()
                        test.delete(0,END)
                        con[53]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        febL.configure(text="23일에 할일: {}".format(con[53]))
                        
                    febb=Button(feb,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=feb23sa)
                    febb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(feb, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def feb24ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    febL.configure(text="24일에 할일: {}".format(con[54]))
                    f.close
                    

                    def feb24sa():
                        od=test.get()
                        test.delete(0,END)
                        con[54]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        febL.configure(text="24일에 할일: {}".format(con[54]))
                        
                    febb=Button(feb,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=feb24sa)
                    febb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(feb, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def feb25ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    febL.configure(text="25일에 할일: {}".format(con[55]))
                    f.close
                    

                    def feb25sa():
                        od=test.get()
                        test.delete(0,END)
                        con[55]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        febL.configure(text="25일에 할일: {}".format(con[55]))
                        
                    febb=Button(feb,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=feb25sa)
                    febb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(feb, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def feb26ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    febL.configure(text="26일에 할일: {}".format(con[56]))
                    f.close
                    

                    def feb26sa():
                        od=test.get()
                        test.delete(0,END)
                        con[56]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        febL.configure(text="26일에 할일: {}".format(con[56]))
                        
                    febb=Button(feb,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=feb26sa)
                    febb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(feb, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def feb27ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    febL.configure(text="27일에 할일: {}".format(con[57]))
                    f.close
                    

                    def feb27sa():
                        od=test.get()
                        test.delete(0,END)
                        con[57]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        febL.configure(text="27일에 할일: {}".format(con[57]))
                        
                    febb=Button(feb,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=feb27sa)
                    febb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(feb, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def feb28ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    febL.configure(text="28일에 할일: {}".format(con[58]))
                    f.close
                    

                    def feb28sa():
                        od=test.get()
                        test.delete(0,END)
                        con[58]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        febL.configure(text="28일에 할일: {}".format(con[58]))
                        
                    febb=Button(feb,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=feb28sa)
                    febb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(feb, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                

                


                feb1b=Button(feb,text="1", width=0, height=0, font=('휴먼엑스포', 20), command=feb1ex)
                feb1b.place(x=420,y=100)
                feb2b=Button(feb,text="2", width=0, height=0, font=('휴먼엑스포', 20), command=feb2ex)
                feb2b.place(x=500,y=100)
                feb3b=Button(feb,text="3",fg="red", width=0, height=0, font=('휴먼엑스포', 20), command=feb3ex)
                feb3b.place(x=20,y=200)
                feb4b=Button(feb,text="4",fg="red", width=0, height=0, font=('휴먼엑스포', 20), command=feb4ex)
                feb4b.place(x=100,y=200)
                feb5b=Button(feb,text="5",fg="red", width=0, height=0, font=('휴먼엑스포', 20), command=feb5ex)
                feb5b.place(x=180,y=200)
                feb6b=Button(feb,text="6", width=0, height=0, font=('휴먼엑스포', 20), command=feb6ex)
                feb6b.place(x=260,y=200)
                feb7b=Button(feb,text="7", width=0, height=0, font=('휴먼엑스포', 20), command=feb7ex)
                feb7b.place(x=340,y=200)
                feb8b=Button(feb,text="8", width=0, height=0, font=('휴먼엑스포', 20), command=feb8ex)
                feb8b.place(x=420,y=200)
                feb9b=Button(feb,text="9", width=0, height=0, font=('휴먼엑스포', 20), command=feb9ex)
                feb9b.place(x=500,y=200)
                feb10b=Button(feb,text="10", width=0, height=0, font=('휴먼엑스포', 20), command=feb10ex)
                feb10b.place(x=20,y=300)
                feb11b=Button(feb,text="11", width=0, height=0, font=('휴먼엑스포', 20), command=feb11ex)
                feb11b.place(x=100,y=300)
                feb12b=Button(feb,text="12", width=0, height=0, font=('휴먼엑스포', 20), command=feb12ex)
                feb12b.place(x=180,y=300)
                feb13b=Button(feb,text="13", width=0, height=0, font=('휴먼엑스포', 20), command=feb13ex)
                feb13b.place(x=260,y=300)
                feb14b=Button(feb,text="14", width=0, height=0, font=('휴먼엑스포', 20), command=feb14ex)
                feb14b.place(x=340,y=300)
                feb15b=Button(feb,text="15", width=0, height=0, font=('휴먼엑스포', 20), command=feb15ex)
                feb15b.place(x=420,y=300)
                feb16b=Button(feb,text="16", width=0, height=0, font=('휴먼엑스포', 20), command=feb16ex)
                feb16b.place(x=500,y=300)
                feb17b=Button(feb,text="17", width=0, height=0, font=('휴먼엑스포', 20), command=feb17ex)
                feb17b.place(x=20,y=400)
                feb18b=Button(feb,text="18", width=0, height=0, font=('휴먼엑스포', 20), command=feb18ex)
                feb18b.place(x=100,y=400)
                feb19b=Button(feb,text="19", width=0, height=0, font=('휴먼엑스포', 20), command=feb19ex)
                feb19b.place(x=180,y=400)
                feb20b=Button(feb,text="20", width=0, height=0, font=('휴먼엑스포', 20), command=feb20ex)
                feb20b.place(x=260,y=400)
                feb21b=Button(feb,text="21", width=0, height=0, font=('휴먼엑스포', 20), command=feb21ex)
                feb21b.place(x=340,y=400)
                feb22b=Button(feb,text="22", width=0, height=0, font=('휴먼엑스포', 20), command=feb22ex)
                feb22b.place(x=420,y=400)
                feb23b=Button(feb,text="23", width=0, height=0, font=('휴먼엑스포', 20), command=feb23ex)
                feb23b.place(x=500,y=400)
                feb24b=Button(feb,text="24", width=0, height=0, font=('휴먼엑스포', 20), command=feb24ex)
                feb24b.place(x=20,y=500)
                feb25b=Button(feb,text="25", width=0, height=0, font=('휴먼엑스포', 20), command=feb25ex)
                feb25b.place(x=100,y=500)
                feb26b=Button(feb,text="26", width=0, height=0, font=('휴먼엑스포', 20), command=feb26ex)
                feb26b.place(x=180,y=500)
                feb27b=Button(feb,text="27", width=0, height=0, font=('휴먼엑스포', 20), command=feb27ex)
                feb27b.place(x=260,y=500)
                feb28b=Button(feb,text="28", width=0, height=0, font=('휴먼엑스포', 20), command=feb28ex)
                feb28b.place(x=340,y=500)

                def 월간2():
                    toj=Tk()
                    toj.title("2월 총 계획")
                    toj.geometry('700x700')

                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    f.close
                    
                    for i in range(31,59):
                        tojL=Label(toj, text="2월 {}일:{}".format(i-30,con[i]), font=('휴먼엑스포', 15))
                        tojL.place(x=0,y=(i-31)*20)
                        
                    
                tojb=Button(feb, text="월간", height=0, font=('휴먼엑스포', 20), command=월간2)   
                tojb.place(x=450,y=500)

            febb=Button(cal, text="2월", width=4, height=2, fg='purple', font=('휴먼엑스포', 20), command=feb)   
            febb.place(x=260,y=120)


            def mar():
                mar=Tk()
                mar.title("3월 달력")
                mar.geometry('700x600')
                marL=Label(mar, text="", font=('휴먼엑스포', 20))
                marL.place(x=350,y=0)

                
                marL=Label(mar, text="", font=('휴먼엑스포', 15))
                marL.place(x=350,y=0)

                LL=Label(mar, text="3월 달력", font=('휴먼엑스포', 20))
                LL.place(x=0, y=0)


                LL=Label(mar, text="일", fg="red", font=('휴먼엑스포', 15))
                LL.place(x=25, y=65)
                LL=Label(mar, text="월", font=('휴먼엑스포', 15))
                LL.place(x=105, y=65)
                LL=Label(mar, text="화", font=('휴먼엑스포', 15))
                LL.place(x=185, y=65)
                LL=Label(mar, text="수", font=('휴먼엑스포', 15))
                LL.place(x=265, y=65)
                LL=Label(mar, text="목", font=('휴먼엑스포', 15))
                LL.place(x=345, y=65)
                LL=Label(mar, text="금", font=('휴먼엑스포', 15))
                LL.place(x=425, y=65)
                LL=Label(mar, text="토", fg="blue", font=('휴먼엑스포', 15))
                LL.place(x=505, y=65)
                


                

                def mar1ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    marL.configure(text="1일에 할일: {}".format(con[59]))
                    f.close
                    al=Tk()
                    al.geometry('300x100')
                    al.title("공휴일 알림")
                    alL=Label(al, text="3.1절, 태극기를 게양합시다", font=("휴먼엑스포", 15), fg="red")
                    alL.place(x=20, y=30)

                    def 종료():
                        al.destroy()

                    alB=Button(al, text="닫기", width=0, height=0, font=(10), command=종료)
                    alB.place(x=40, y=60)
                    

                    def mar1sa():
                        od=test.get()
                        test.delete(0,END)
                        con[59]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        marL.configure(text="1일에 할일: {}".format(con[59]))
                    marb=Button(mar,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=mar1sa)
                    marb.place(x=250,y=10)

                    test=Entry(mar, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)
                    
                def mar2ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    marL.configure(text="2일에 할일: {}".format(con[60]))
                    f.close
                    

                    def mar2sa():
                        od=test.get()
                        test.delete(0,END)
                        con[60]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        marL.configure(text="2일에 할일: {}".format(con[60]))
                    marb=Button(mar,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=mar2sa)
                    marb.place(x=250,y=10)

                    test=Entry(mar, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)

                def mar3ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    marL.configure(text="3일에 할일: {}".format(con[61]))
                    f.close
                    

                    def mar3sa():
                        od=test.get()
                        test.delete(0,END)
                        con[61]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        marL.configure(text="3일에 할일: {}".format(con[61]))
                    marb=Button(mar,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=mar3sa)
                    marb.place(x=250,y=10)

                    test=Entry(mar, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)

                def mar4ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    marL.configure(text="4일에 할일: {}".format(con[62]))
                    f.close
                    

                    def mar4sa():
                        od=test.get()
                        test.delete(0,END)
                        con[62]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        marL.configure(text="4일에 할일: {}".format(con[62]))
                        
                    marb=Button(mar,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=mar4sa)
                    marb.place(x=250,y=10)

                    test=Entry(mar, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)

                def mar5ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    marL.configure(text="5일에 할일: {}".format(con[63]))
                    f.close
                    

                    def mar5sa():
                        od=test.get()
                        test.delete(0,END)
                        con[63]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        marL.configure(text="5일에 할일: {}".format(con[63]))
                    marb=Button(mar,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=mar5sa)
                    marb.place(x=250,y=10)

                    test=Entry(mar, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)
                def mar6ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    marL.configure(text="6일에 할일: {}".format(con[64]))
                    f.close
                    

                    def mar6sa():
                        od=test.get()
                        test.delete(0,END)
                        con[64]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        marL.configure(text="6일에 할일: {}".format(con[64]))
                    marb=Button(mar,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=mar6sa)
                    marb.place(x=250,y=10)

                    test=Entry(mar, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)
                def mar7ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    marL.configure(text="7일에 할일: {}".format(con[65]))
                    f.close
                    

                    def mar7sa():
                        od=test.get()
                        test.delete(0,END)
                        con[65]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        marL.configure(text="7일에 할일: {}".format(con[65]))
                    marb=Button(mar,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=mar7sa)
                    marb.place(x=250,y=10)

                    test=Entry(mar, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)

                def mar8ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    marL.configure(text="8일에 할일: {}".format(con[66]))
                    f.close
                    

                    def mar8sa():
                        od=test.get()
                        test.delete(0,END)
                        con[66]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        marL.configure(text="8일에 할일: {}".format(con[66]))

                    marb=Button(mar,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=mar8sa)
                    marb.place(x=250,y=10)

                    test=Entry(mar, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)
                def mar9ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    marL.configure(text="9일에 할일: {}".format(con[67]))
                    f.close
                    

                    def mar9sa():
                        od=test.get()
                        test.delete(0,END)
                        con[67]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        marL.configure(text="9일에 할일: {}".format(con[67]))
                    marb=Button(mar,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=mar9sa)
                    marb.place(x=250,y=10)

                    test=Entry(mar, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)
                    
                def mar10ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    marL.configure(text="10일에 할일: {}".format(con[68]))
                    f.close
                    

                    def mar10sa():
                        od=test.get()
                        test.delete(0,END)
                        con[68]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        marL.configure(text="10일에 할일: {}".format(con[68]))
                    marb=Button(mar,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=mar10sa)
                    marb.place(x=250,y=10)

                    test=Entry(mar, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)
                def mar11ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    marL.configure(text="11일에 할일: {}".format(con[69]))
                    f.close
                    

                    def mar11sa():
                        od=test.get()
                        test.delete(0,END)
                        con[69]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        marL.configure(text="11일에 할일: {}".format(con[69]))
                    marb=Button(mar,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=mar11sa)
                    marb.place(x=250,y=10)

                    test=Entry(mar, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)

                def mar12ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    marL.configure(text="12일에 할일: {}".format(con[70]))
                    f.close
                    

                    def mar12sa():
                        od=test.get()
                        test.delete(0,END)
                        con[70]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        marL.configure(text="12일에 할일: {}".format(con[70]))
                    marb=Button(mar,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=mar12sa)
                    marb.place(x=250,y=10)

                    test=Entry(mar, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)
                        
                def mar13ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    marL.configure(text="13일에 할일: {}".format(con[71]))
                    f.close
                    

                    def mar13sa():
                        od=test.get()
                        test.delete(0,END)
                        con[71]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        marL.configure(text="13일에 할일: {}".format(con[71]))
                    marb=Button(mar,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=mar13sa)
                    marb.place(x=250,y=10)

                    test=Entry(mar, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)
                def mar14ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    marL.configure(text="14일에 할일: {}".format(con[72]))
                    f.close
                    

                    def mar14sa():
                        od=test.get()
                        test.delete(0,END)
                        con[72]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        marL.configure(text="14일에 할일: {}".format(con[72]))
                    marb=Button(mar,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=mar14sa)
                    marb.place(x=250,y=10)

                    test=Entry(mar, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)
                        
                def mar15ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    marL.configure(text="15일에 할일: {}".format(con[73]))
                    f.close
                    

                    def mar15sa():
                        od=test.get()
                        test.delete(0,END)
                        con[73]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        marL.configure(text="15일에 할일: {}".format(con[73]))
                    marb=Button(mar,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=mar15sa)
                    marb.place(x=250,y=10)

                    test=Entry(mar, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)

                def mar16ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    marL.configure(text="16일에 할일: {}".format(con[74]))
                    f.close
                    

                    def mar16sa():
                        od=test.get()
                        test.delete(0,END)
                        con[74]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        marL.configure(text="16일에 할일: {}".format(con[74]))
                    marb=Button(mar,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=mar16sa)
                    marb.place(x=250,y=10)

                    test=Entry(mar, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)
                def mar17ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    marL.configure(text="17일에 할일: {}".format(con[75]))
                    f.close
                    

                    def mar17sa():
                        od=test.get()
                        test.delete(0,END)
                        con[75]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        marL.configure(text="17일에 할일: {}".format(con[75]))
                    marb=Button(mar,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=mar17sa)
                    marb.place(x=250,y=10)

                    test=Entry(mar, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)
                def mar18ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    marL.configure(text="18일에 할일: {}".format(con[76]))
                    f.close
                    

                    def mar18sa():
                        od=test.get()
                        test.delete(0,END)
                        con[76]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        marL.configure(text="18일에 할일: {}".format(con[76]))
                    marb=Button(mar,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=mar18sa)
                    marb.place(x=250,y=10)

                    test=Entry(mar, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)
                def mar19ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    marL.configure(text="19일에 할일: {}".format(con[77]))
                    f.close
                    

                    def mar19sa():
                        od=test.get()
                        test.delete(0,END)
                        con[77]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        marL.configure(text="19일에 할일: {}".format(con[77]))
                    marb=Button(mar,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=mar19sa)
                    marb.place(x=250,y=10)

                    test=Entry(mar, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)
                def mar20ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    marL.configure(text="20일에 할일: {}".format(con[78]))
                    f.close
                    

                    def mar20sa():
                        od=test.get()
                        test.delete(0,END)
                        con[78]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        marL.configure(text="20일에 할일: {}".format(con[78]))
                    marb=Button(mar,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=mar20sa)
                    marb.place(x=250,y=10)

                    test=Entry(mar, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)
                def mar21ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    marL.configure(text="21일에 할일: {}".format(con[79]))
                    f.close
                    

                    def mar21sa():
                        od=test.get()
                        test.delete(0,END)
                        con[79]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        marL.configure(text="21일에 할일: {}".format(con[79]))
                    marb=Button(mar,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=mar21sa)
                    marb.place(x=250,y=10)

                    test=Entry(mar, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)
                def mar22ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    marL.configure(text="22일에 할일: {}".format(con[80]))
                    f.close
                    

                    def mar22sa():
                        od=test.get()
                        test.delete(0,END)
                        con[80]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        marL.configure(text="22일에 할일: {}".format(con[80]))
                    marb=Button(mar,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=mar22sa)
                    marb.place(x=250,y=10)

                    test=Entry(mar, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)
                def mar23ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    marL.configure(text="23일에 할일: {}".format(con[81]))
                    f.close
                    

                    def mar23sa():
                        od=test.get()
                        test.delete(0,END)
                        con[81]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        marL.configure(text="23일에 할일: {}".format(con[81]))
                    marb=Button(mar,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=mar23sa)
                    marb.place(x=250,y=10)

                    test=Entry(mar, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)
                def mar24ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    marL.configure(text="24일에 할일: {}".format(con[82]))
                    f.close
                    

                    def mar24sa():
                        od=test.get()
                        test.delete(0,END)
                        con[82]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        marL.configure(text="24일에 할일: {}".format(con[82]))
                    marb=Button(mar,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=mar24sa)
                    marb.place(x=250,y=10)

                    test=Entry(mar, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)
                def mar25ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    marL.configure(text="25일에 할일: {}".format(con[83]))
                    f.close
                    

                    def mar25sa():
                        od=test.get()
                        test.delete(0,END)
                        con[83]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        marL.configure(text="25일에 할일: {}".format(con[83]))
                    marb=Button(mar,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=mar25sa)
                    marb.place(x=250,y=10)

                    test=Entry(mar, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)
                        
                def mar26ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    marL.configure(text="26일에 할일: {}".format(con[84]))
                    f.close
                    

                    def mar26sa():
                        od=test.get()
                        test.delete(0,END)
                        con[84]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        marL.configure(text="26일에 할일: {}".format(con[84]))
                    marb=Button(mar,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=mar26sa)
                    marb.place(x=250,y=10)

                    test=Entry(mar, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)
                def mar27ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    marL.configure(text="27일에 할일: {}".format(con[85]))
                    f.close
                    

                    def mar27sa():
                        od=test.get()
                        test.delete(0,END)
                        con[85]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        marL.configure(text="27일에 할일: {}".format(con[85]))
                    marb=Button(mar,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=mar27sa)
                    marb.place(x=250,y=10)

                    test=Entry(mar, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)
                def mar28ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    marL.configure(text="28일에 할일: {}".format(con[86]))
                    f.close
                    

                    def mar28sa():
                        od=test.get()
                        test.delete(0,END)
                        con[86]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        marL.configure(text="28일에 할일: {}".format(con[86]))
                    marb=Button(mar,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=mar28sa)
                    marb.place(x=250,y=10)

                    test=Entry(mar, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)
                def mar29ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    marL.configure(text="29일에 할일: {}".format(con[87]))
                    f.close
                    

                    def mar29sa():
                        od=test.get()
                        test.delete(0,END)
                        con[87]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        marL.configure(text="29일에 할일: {}".format(con[87]))
                    marb=Button(mar,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=mar29sa)
                    marb.place(x=250,y=10)

                    test=Entry(mar, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)
                        
                def mar30ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    marL.configure(text="30일에 할일: {}".format(con[88]))
                    f.close
                    

                    def mar30sa():
                        od=test.get()
                        test.delete(0,END)
                        con[88]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        marL.configure(text="30일에 할일: {}".format(con[88]))
                    marb=Button(mar,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=mar30sa)
                    marb.place(x=250,y=10)

                    test=Entry(mar, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)
                def mar31ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    marL.configure(text="31일에 할일: {}".format(con[89]))
                    f.close
                    

                    def mar31sa():
                        od=test.get()
                        test.delete(0,END)
                        con[89]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        marL.configure(text="31일에 할일: {}".format(con[89]))
                    marb=Button(mar,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=mar31sa)
                    marb.place(x=250,y=10)

                    test=Entry(mar, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)
                mar1b=Button(mar,text="1",fg="red", width=0, height=0, font=('휴먼엑스포', 20), command=mar1ex)
                mar1b.place(x=420,y=100)

                mar2b=Button(mar,text="2", width=0, height=0, font=('휴먼엑스포', 20), command=mar2ex)
                mar2b.place(x=500,y=100)

                mar3b=Button(mar,text="3", width=0, height=0, font=('휴먼엑스포', 20), command=mar3ex)
                mar3b.place(x=20,y=200)

                mar4b=Button(mar,text="4", width=0, height=0, font=('휴먼엑스포', 20), command=mar4ex)
                mar4b.place(x=100,y=200)

                mar5b=Button(mar,text="5", width=0, height=0, font=('휴먼엑스포', 20), command=mar5ex)
                mar5b.place(x=180,y=200)

                mar6b=Button(mar,text="6", width=0, height=0, font=('휴먼엑스포', 20), command=mar6ex)
                mar6b.place(x=260,y=200)

                mar7b=Button(mar,text="7", width=0, height=0, font=('휴먼엑스포', 20), command=mar7ex)
                mar7b.place(x=340,y=200)

                mar8b=Button(mar,text="8", width=0, height=0, font=('휴먼엑스포', 20), command=mar8ex)
                mar8b.place(x=420,y=200)

                mar9b=Button(mar,text="9", width=0, height=0, font=('휴먼엑스포', 20), command=mar9ex)
                mar9b.place(x=500,y=200)

                mar10b=Button(mar,text="10", width=0, height=0, font=('휴먼엑스포', 20), command=mar10ex)
                mar10b.place(x=20,y=300)

                mar11b=Button(mar,text="11", width=0, height=0, font=('휴먼엑스포', 20), command=mar11ex)
                mar11b.place(x=100,y=300)

                mar12b=Button(mar,text="12", width=0, height=0, font=('휴먼엑스포', 20), command=mar12ex)
                mar12b.place(x=180,y=300)

                mar13b=Button(mar,text="13", width=0, height=0, font=('휴먼엑스포', 20), command=mar13ex)
                mar13b.place(x=260,y=300)

                mar14b=Button(mar,text="14", width=0, height=0, font=('휴먼엑스포', 20), command=mar14ex)
                mar14b.place(x=340,y=300)

                mar15b=Button(mar,text="15", width=0, height=0, font=('휴먼엑스포', 20), command=mar15ex)
                mar15b.place(x=420,y=300)

                mar16b=Button(mar,text="16", width=0, height=0, font=('휴먼엑스포', 20), command=mar16ex)
                mar16b.place(x=500,y=300)

                mar17b=Button(mar,text="17", width=0, height=0, font=('휴먼엑스포', 20), command=mar17ex)
                mar17b.place(x=20,y=400)

                mar18b=Button(mar,text="18", width=0, height=0, font=('휴먼엑스포', 20), command=mar18ex)
                mar18b.place(x=100,y=400)

                mar19b=Button(mar,text="19", width=0, height=0, font=('휴먼엑스포', 20), command=mar19ex)
                mar19b.place(x=180,y=400)

                mar20b=Button(mar,text="20", width=0, height=0, font=('휴먼엑스포', 20), command=mar20ex)
                mar20b.place(x=260,y=400)

                mar21b=Button(mar,text="21", width=0, height=0, font=('휴먼엑스포', 20), command=mar21ex)
                mar21b.place(x=340,y=400)

                mar22b=Button(mar,text="22", width=0, height=0, font=('휴먼엑스포', 20), command=mar22ex)
                mar22b.place(x=420,y=400)

                mar23b=Button(mar,text="23", width=0, height=0, font=('휴먼엑스포', 20), command=mar23ex)
                mar23b.place(x=500,y=400)

                mar24b=Button(mar,text="24", width=0, height=0, font=('휴먼엑스포', 20), command=mar24ex)
                mar24b.place(x=20,y=500)

                mar25b=Button(mar,text="25", width=0, height=0, font=('휴먼엑스포', 20), command=mar25ex)
                mar25b.place(x=100,y=500)

                mar26b=Button(mar,text="26", width=0, height=0, font=('휴먼엑스포', 20), command=mar26ex)
                mar26b.place(x=180,y=500)

                mar27b=Button(mar,text="27", width=0, height=0, font=('휴먼엑스포', 20), command=mar27ex)
                mar27b.place(x=260,y=500)

                mar28b=Button(mar,text="28", width=0, height=0, font=('휴먼엑스포', 20), command=mar28ex)
                mar28b.place(x=340,y=500)

                mar29b=Button(mar,text="29", width=0, height=0, font=('휴먼엑스포', 20), command=mar29ex)
                mar29b.place(x=420,y=500)

                mar30b=Button(mar,text="30", width=0, height=0, font=('휴먼엑스포', 20), command=mar30ex)
                mar30b.place(x=500,y=500)

                mar31b=Button(mar,text="31", width=0, height=0, font=('휴먼엑스포', 20), command=mar31ex)
                mar31b.place(x=20,y=600)

                

                
                
                
                def 월간3():
                    toj=Tk()
                    toj.title("3월 총 계획")
                    toj.geometry('700x700')

                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    f.close
                    
                    for i in range(59,90):
                        tojL=Label(toj, text="3월 {}일:{}".format(i-58,con[i]), font=('휴먼엑스포', 15))
                        tojL.place(x=0,y=(i-59)*20)
                        
                    
                tojb=Button(mar, text="월간", height=0, font=('휴먼엑스포', 20), command=월간3)   
                tojb.place(x=580,y=500)

            marb=Button(cal, text="3월", width=4, height=2, fg='aquamarine', font=('휴먼엑스포', 20), command=mar)   
            marb.place(x=410,y=120)

            def apr():
                apr=Tk()
                apr.title("4월 달력")
                apr.geometry('700x600')
                aprL=Label(apr, text="", font=('휴먼엑스포', 20))
                aprL.place(x=430,y=0)

                aprL=Label(apr, text="", font=('휴먼엑스포', 15))
                aprL.place(x=350,y=0)
    
                LL=Label(apr, text="4월 달력", font=('휴먼엑스포', 20))
                LL.place(x=0, y=0)
    
    
                LL=Label(apr, text="일", fg="red", font=('휴먼엑스포', 15))
                LL.place(x=25, y=65)
                LL=Label(apr, text="월", font=('휴먼엑스포', 15))
                LL.place(x=105, y=65)
                LL=Label(apr, text="화", font=('휴먼엑스포', 15))
                LL.place(x=185, y=65)
                LL=Label(apr, text="수", font=('휴먼엑스포', 15))
                LL.place(x=265, y=65)
                LL=Label(apr, text="목", font=('휴먼엑스포', 15))
                LL.place(x=345, y=65)
                LL=Label(apr, text="금", font=('휴먼엑스포', 15))
                LL.place(x=425, y=65)
                LL=Label(apr, text="토", fg="blue", font=('휴먼엑스포', 15))
                LL.place(x=505, y=65)


                

                def apr1ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    aprL.configure(text="1일에 할일: {}".format(con[90]))
                    f.close
                    

                    def apr1sa():
                        od=test.get()
                        test.delete(0,END)
                        con[90]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        aprL.configure(text="1일에 할일: {}".format(con[90]))
                        
                    aprb=Button(apr,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=apr1sa)
                    aprb.place(x=250,y=10)

                    test=Entry(apr, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)

                def apr2ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    aprL.configure(text="2일에 할일: {}".format(con[91]))
                    f.close
                    

                    def apr2sa():
                        od=test.get()
                        test.delete(0,END)
                        con[91]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        aprL.configure(text="2일에 할일: {}".format(con[91]))
                    aprb=Button(apr,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=apr2sa)
                    aprb.place(x=250,y=10)

                    test=Entry(apr, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)

                def apr3ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    aprL.configure(text="3일에 할일: {}".format(con[92]))
                    f.close
                    

                    def apr3sa():
                        od=test.get()
                        test.delete(0,END)
                        con[92]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        aprL.configure(text="3일에 할일: {}".format(con[92]))
                    aprb=Button(apr,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=apr3sa)
                    aprb.place(x=250,y=10)

                    test=Entry(apr, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)

                def apr4ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    aprL.configure(text="4일에 할일: {}".format(con[93]))
                    f.close
                    

                    def apr4sa():
                        od=test.get()
                        test.delete(0,END)
                        con[93]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        aprL.configure(text="4일에 할일: {}".format(con[93]))
                    aprb=Button(apr,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=apr4sa)
                    aprb.place(x=250,y=10)

                    test=Entry(apr, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)

                def apr5ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    aprL.configure(text="5일에 할일: {}".format(con[94]))
                    f.close
                    

                    def apr5sa():
                        od=test.get()
                        test.delete(0,END)
                        con[94]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        aprL.configure(text="5일에 할일: {}".format(con[94]))
                    aprb=Button(apr,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=apr5sa)
                    aprb.place(x=250,y=10)

                    test=Entry(apr, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)

                def apr6ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    aprL.configure(text="6일에 할일: {}".format(con[95]))
                    f.close
                    

                    def apr6sa():
                        od=test.get()
                        test.delete(0,END)
                        con[95]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        aprL.configure(text="6일에 할일: {}".format(con[95]))
                    aprb=Button(apr,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=apr6sa)
                    aprb.place(x=250,y=10)

                    test=Entry(apr, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)

                        
                def apr7ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    aprL.configure(text="7일에 할일: {}".format(con[96]))
                    f.close
                    

                    def apr7sa():
                        od=test.get()
                        test.delete(0,END)
                        con[96]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        aprL.configure(text="7일에 할일: {}".format(con[96]))
                    aprb=Button(apr,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=apr7sa)
                    aprb.place(x=250,y=10)

                    test=Entry(apr, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)

                def apr8ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    aprL.configure(text="8일에 할일: {}".format(con[97]))
                    f.close
                    

                    def apr8sa():
                        od=test.get()
                        test.delete(0,END)
                        con[97]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        aprL.configure(text="8일에 할일: {}".format(con[97]))
                    aprb=Button(apr,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=apr8sa)
                    aprb.place(x=250,y=10)

                    test=Entry(apr, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)

                def apr9ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    aprL.configure(text="9일에 할일: {}".format(con[98]))
                    f.close
                    

                    def apr9sa():
                        od=test.get()
                        test.delete(0,END)
                        con[98]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        aprL.configure(text="9일에 할일: {}".format(con[98]))
                    aprb=Button(apr,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=apr9sa)
                    aprb.place(x=250,y=10)

                    test=Entry(apr, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)

                def apr10ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    aprL.configure(text="10일에 할일: {}".format(con[99]))
                    f.close
                    

                    def apr10sa():
                        od=test.get()
                        test.delete(0,END)
                        con[99]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        aprL.configure(text="10일에 할일: {}".format(con[99]))
                    aprb=Button(apr,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=apr10sa)
                    aprb.place(x=250,y=10)

                    test=Entry(apr, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)

                def apr11ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    aprL.configure(text="11일에 할일: {}".format(con[100]))
                    f.close
                    

                    def apr11sa():
                        od=test.get()
                        test.delete(0,END)
                        con[100]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        aprL.configure(text="11일에 할일: {}".format(con[100]))
                    aprb=Button(apr,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=apr11sa)
                    aprb.place(x=250,y=10)

                    test=Entry(apr, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)

                def apr12ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    aprL.configure(text="12일에 할일: {}".format(con[101]))
                    f.close
                    

                    def apr12sa():
                        od=test.get()
                        test.delete(0,END)
                        con[101]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        aprL.configure(text="12일에 할일: {}".format(con[101]))
                    aprb=Button(apr,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=apr12sa)
                    aprb.place(x=250,y=10)

                    test=Entry(apr, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)

                def apr13ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    aprL.configure(text="13일에 할일: {}".format(con[102]))
                    f.close
                    

                    def apr13sa():
                        od=test.get()
                        test.delete(0,END)
                        con[102]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        aprL.configure(text="13일에 할일: {}".format(con[102]))
                    aprb=Button(apr,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=apr13sa)
                    aprb.place(x=250,y=10)

                    test=Entry(apr, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)

                        
                def apr14ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    aprL.configure(text="14일에 할일: {}".format(con[103]))
                    f.close
                    

                    def apr14sa():
                        od=test.get()
                        test.delete(0,END)
                        con[103]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        aprL.configure(text="14일에 할일: {}".format(con[103]))
                    aprb=Button(apr,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=apr14sa)
                    aprb.place(x=250,y=10)

                    test=Entry(apr, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)

                def apr15ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    aprL.configure(text="15일에 할일: {}".format(con[104]))
                    f.close
                    

                    def apr15sa():
                        od=test.get()
                        test.delete(0,END)
                        con[104]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        aprL.configure(text="15일에 할일: {}".format(con[104]))
                    aprb=Button(apr,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=apr15sa)
                    aprb.place(x=250,y=10)

                    test=Entry(apr, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)

                def apr16ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    aprL.configure(text="16일에 할일: {}".format(con[105]))
                    f.close
                    

                    def apr16sa():
                        od=test.get()
                        test.delete(0,END)
                        con[105]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        aprL.configure(text="16일에 할일: {}".format(con[105]))
                    aprb=Button(apr,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=apr16sa)
                    aprb.place(x=250,y=10)

                    test=Entry(apr, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)

                def apr17ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    aprL.configure(text="17일에 할일: {}".format(con[106]))
                    f.close
                    

                    def apr17sa():
                        od=test.get()
                        test.delete(0,END)
                        con[106]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        aprL.configure(text="17일에 할일: {}".format(con[106]))
                    aprb=Button(apr,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=apr17sa)
                    aprb.place(x=250,y=10)

                    test=Entry(apr, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)

                def apr18ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    aprL.configure(text="18일에 할일: {}".format(con[107]))
                    f.close
                    

                    def apr18sa():
                        od=test.get()
                        test.delete(0,END)
                        con[107]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        aprL.configure(text="18일에 할일: {}".format(con[107]))
                    aprb=Button(apr,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=apr18sa)
                    aprb.place(x=250,y=10)

                    test=Entry(apr, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)

                def apr19ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    aprL.configure(text="19일에 할일: {}".format(con[108]))
                    f.close
                    

                    def apr19sa():
                        od=test.get()
                        test.delete(0,END)
                        con[108]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        aprL.configure(text="19일에 할일: {}".format(con[108]))
                    aprb=Button(apr,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=apr19sa)
                    aprb.place(x=250,y=10)

                    test=Entry(apr, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)

                def apr20ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    aprL.configure(text="20일에 할일: {}".format(con[109]))
                    f.close
                    

                    def apr20sa():
                        od=test.get()
                        test.delete(0,END)
                        con[109]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        aprL.configure(text="20일에 할일: {}".format(con[109]))
                    aprb=Button(apr,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=apr20sa)
                    aprb.place(x=250,y=10)

                    test=Entry(apr, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)

                def apr21ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    aprL.configure(text="21일에 할일: {}".format(con[110]))
                    f.close
                    

                    def apr21sa():
                        od=test.get()
                        test.delete(0,END)
                        con[110]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        aprL.configure(text="21일에 할일: {}".format(con[110]))
                    aprb=Button(apr,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=apr21sa)
                    aprb.place(x=250,y=10)

                    test=Entry(apr, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)

                def apr22ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    aprL.configure(text="22일에 할일: {}".format(con[111]))
                    f.close
                    

                    def apr22sa():
                        od=test.get()
                        test.delete(0,END)
                        con[111]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        aprL.configure(text="22일에 할일: {}".format(con[111]))
                    aprb=Button(apr,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=apr22sa)
                    aprb.place(x=250,y=10)

                    test=Entry(apr, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)


                def apr23ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    aprL.configure(text="23일에 할일: {}".format(con[112]))
                    f.close
                    

                    def apr23sa():
                        od=test.get()
                        test.delete(0,END)
                        con[112]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        aprL.configure(text="23일에 할일: {}".format(con[112]))
                    aprb=Button(apr,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=apr23sa)
                    aprb.place(x=250,y=10)

                    test=Entry(apr, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)

                        
                def apr24ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    aprL.configure(text="24일에 할일: {}".format(con[113]))
                    f.close
                    

                    def apr24sa():
                        od=test.get()
                        test.delete(0,END)
                        con[113]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        aprL.configure(text="24일에 할일: {}".format(con[113]))
                    aprb=Button(apr,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=apr24sa)
                    aprb.place(x=250,y=10)

                    test=Entry(apr, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)

                def apr25ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    aprL.configure(text="25일에 할일: {}".format(con[114]))
                    f.close
                    

                    def apr25sa():
                        od=test.get()
                        test.delete(0,END)
                        con[114]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        aprL.configure(text="25일에 할일: {}".format(con[114]))
                    aprb=Button(apr,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=apr25sa)
                    aprb.place(x=250,y=10)

                    test=Entry(apr, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)

                def apr26ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    aprL.configure(text="26일에 할일: {}".format(con[115]))
                    f.close
                    

                    def apr26sa():
                        od=test.get()
                        test.delete(0,END)
                        con[115]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        aprL.configure(text="26일에 할일: {}".format(con[115]))
                    aprb=Button(apr,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=apr26sa)
                    aprb.place(x=250,y=10)

                    test=Entry(apr, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)

                def apr27ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    aprL.configure(text="27일에 할일: {}".format(con[116]))
                    f.close
                    

                    def apr27sa():
                        od=test.get()
                        test.delete(0,END)
                        con[116]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        aprL.configure(text="27일에 할일: {}".format(con[116]))
                    aprb=Button(apr,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=apr27sa)
                    aprb.place(x=250,y=10)

                    test=Entry(apr, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)

                def apr28ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    aprL.configure(text="28일에 할일: {}".format(con[117]))
                    f.close
                    

                    def apr28sa():
                        od=test.get()
                        test.delete(0,END)
                        con[117]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        aprL.configure(text="28일에 할일: {}".format(con[117]))
                    aprb=Button(apr,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=apr28sa)
                    aprb.place(x=250,y=10)

                    test=Entry(apr, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)

                def apr29ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    aprL.configure(text="29일에 할일: {}".format(con[118]))
                    f.close
                    

                    def apr29sa():
                        od=test.get()
                        test.delete(0,END)
                        con[118]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        aprL.configure(text="29일에 할일: {}".format(con[118]))
                    aprb=Button(apr,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=apr29sa)
                    aprb.place(x=250,y=10)

                    test=Entry(apr, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)

                def apr30ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    aprL.configure(text="30일에 할일: {}".format(con[119]))
                    f.close
                    

                    def apr30sa():
                        od=test.get()
                        test.delete(0,END)
                        con[119]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        aprL.configure(text="30일에 할일: {}".format(con[119]))
                    aprb=Button(apr,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=apr30sa)
                    aprb.place(x=250,y=10)

                    test=Entry(apr, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)

                apr1b=Button(apr,text="1", width=0, height=0, font=('휴먼엑스포', 20), command=apr1ex)
                apr1b.place(x=100,y=100)

                apr2b=Button(apr,text="2", width=0, height=0, font=('휴먼엑스포', 20), command=apr2ex)
                apr2b.place(x=180,y=100)

                apr3b=Button(apr,text="3", width=0, height=0, font=('휴먼엑스포', 20), command=apr3ex)
                apr3b.place(x=260,y=100)

                apr4b=Button(apr,text="4", width=0, height=0, font=('휴먼엑스포', 20), command=apr4ex)
                apr4b.place(x=340,y=100)

                apr5b=Button(apr,text="5", width=0, height=0, font=('휴먼엑스포', 20), command=apr5ex)
                apr5b.place(x=420,y=100)

                apr6b=Button(apr,text="6", width=0, height=0, font=('휴먼엑스포', 20), command=apr6ex)
                apr6b.place(x=500,y=100)

                apr7b=Button(apr,text="7", width=0, height=0, font=('휴먼엑스포', 20), command=apr7ex)
                apr7b.place(x=20,y=200)

                apr8b=Button(apr,text="8", width=0, height=0, font=('휴먼엑스포', 20), command=apr8ex)
                apr8b.place(x=100,y=200)

                apr9b=Button(apr,text="9", width=0, height=0, font=('휴먼엑스포', 20), command=apr9ex)
                apr9b.place(x=180,y=200)

                apr10b=Button(apr,text="10", width=0, height=0, font=('휴먼엑스포', 20), command=apr10ex)
                apr10b.place(x=260,y=200)

                apr11b=Button(apr,text="11", width=0, height=0, font=('휴먼엑스포', 20), command=apr11ex)
                apr11b.place(x=340,y=200)

                apr12b=Button(apr,text="12", width=0, height=0, font=('휴먼엑스포', 20), command=apr12ex)
                apr12b.place(x=420,y=200)

                apr13b=Button(apr,text="13", width=0, height=0, font=('휴먼엑스포', 20), command=apr13ex)
                apr13b.place(x=500,y=200)

                apr14b=Button(apr,text="14", width=0, height=0, font=('휴먼엑스포', 20), command=apr14ex)
                apr14b.place(x=20,y=300)

                apr15b=Button(apr,text="15", width=0, height=0, font=('휴먼엑스포', 20), command=apr15ex)
                apr15b.place(x=100,y=300)

                apr16b=Button(apr,text="16", width=0, height=0, font=('휴먼엑스포', 20), command=apr16ex)
                apr16b.place(x=180,y=300)

                apr17b=Button(apr,text="17", width=0, height=0, font=('휴먼엑스포', 20), command=apr17ex)
                apr17b.place(x=260,y=300)

                apr18b=Button(apr,text="18", width=0, height=0, font=('휴먼엑스포', 20), command=apr18ex)
                apr18b.place(x=340,y=300)

                apr19b=Button(apr,text="19", width=0, height=0, font=('휴먼엑스포', 20), command=apr19ex)
                apr19b.place(x=420,y=300)

                apr20b=Button(apr,text="20", width=0, height=0, font=('휴먼엑스포', 20), command=apr20ex)
                apr20b.place(x=500,y=300)

                apr21b=Button(apr,text="21", width=0, height=0, font=('휴먼엑스포', 20), command=apr21ex)
                apr21b.place(x=20,y=400)

                apr22b=Button(apr,text="22", width=0, height=0, font=('휴먼엑스포', 20), command=apr22ex)
                apr22b.place(x=100,y=400)

                apr23b=Button(apr,text="23", width=0, height=0, font=('휴먼엑스포', 20), command=apr23ex)
                apr23b.place(x=180,y=400)

                apr24b=Button(apr,text="24", width=0, height=0, font=('휴먼엑스포', 20), command=apr24ex)
                apr24b.place(x=260,y=400)

                apr25b=Button(apr,text="25", width=0, height=0, font=('휴먼엑스포', 20), command=apr25ex)
                apr25b.place(x=340,y=400)

                apr26b=Button(apr,text="26", width=0, height=0, font=('휴먼엑스포', 20), command=apr26ex)
                apr26b.place(x=420,y=400)

                apr27b=Button(apr,text="27", width=0, height=0, font=('휴먼엑스포', 20), command=apr27ex)
                apr27b.place(x=500,y=400)

                apr28b=Button(apr,text="28", width=0, height=0, font=('휴먼엑스포', 20), command=apr28ex)
                apr28b.place(x=20,y=500)

                apr29b=Button(apr,text="29", width=0, height=0, font=('휴먼엑스포', 20), command=apr29ex)
                apr29b.place(x=100,y=500)

                apr30b=Button(apr,text="30", width=0, height=0, font=('휴먼엑스포', 20), command=apr30ex)
                apr30b.place(x=180,y=500)

 

                def 월간4():
                    toj=Tk()
                    toj.title("4월 총 계획")
                    toj.geometry('700x700')

                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    f.close
                    
                    for i in range(90,120):
                        tojL=Label(toj, text="4월 {}일:{}".format(i-89,con[i]), font=('휴먼엑스포', 15))
                        tojL.place(x=0,y=(i-90)*20)
                        
                    
                tojb=Button(apr, text="월간", height=0, font=('휴먼엑스포', 20), command=월간4)   
                tojb.place(x=580,y=400)

            aprb=Button(cal, text="4월", width=4, height=2, fg='silver', font=('휴먼엑스포', 20), command=apr)   
            aprb.place(x=110,y=230)

             
            def may():
                may=Tk()
                may.title("5월 달력")
                may.geometry('700x600')
                mayL=Label(may, text="", font=('휴먼엑스포', 20))
                mayL.place(x=510,y=0)

                mayL=Label(may, text="", font=('휴먼엑스포', 15))
                mayL.place(x=350,y=0)
    
                LL=Label(may, text="5월 달력", font=('휴먼엑스포', 20))
                LL.place(x=0, y=0)


                LL=Label(may, text="일", fg="red", font=('휴먼엑스포', 15))
                LL.place(x=25, y=65)
                LL=Label(may, text="월", font=('휴먼엑스포', 15))
                LL.place(x=105, y=65)
                LL=Label(may, text="화", font=('휴먼엑스포', 15))
                LL.place(x=185, y=65)
                LL=Label(may, text="수", font=('휴먼엑스포', 15))
                LL.place(x=265, y=65)
                LL=Label(may, text="목", font=('휴먼엑스포', 15))
                LL.place(x=345, y=65)
                LL=Label(may, text="금", font=('휴먼엑스포', 15))
                LL.place(x=425, y=65)
                LL=Label(may, text="토", fg="blue", font=('휴먼엑스포', 15))
                LL.place(x=505, y=65)

                def may1ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    mayL.configure(text="1일에 할일: {}".format(con[120]))
                    f.close
                    

                    def may1sa():
                        od=test.get()
                        test.delete(0,END)
                        con[120]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        mayL.configure(text="1일에 할일: {}".format(con[120]))
                    mayb=Button(may,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=may1sa)
                    mayb.place(x=250,y=10)

                    test=Entry(may, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)

                def may2ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    mayL.configure(text="2일에 할일: {}".format(con[121]))
                    f.close
                    

                    def may2sa():
                        od=test.get()
                        test.delete(0,END)
                        con[121]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        mayL.configure(text="2일에 할일: {}".format(con[121]))
                    mayb=Button(may,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=may2sa)
                    mayb.place(x=250,y=10)

                    test=Entry(may, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)
                def may3ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    mayL.configure(text="3일에 할일: {}".format(con[122]))
                    f.close
                    

                    def may3sa():
                        od=test.get()
                        test.delete(0,END)
                        con[122]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        mayL.configure(text="3일에 할일: {}".format(con[122]))
                    mayb=Button(may,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=may3sa)
                    mayb.place(x=250,y=10)

                    test=Entry(may, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)
                def may4ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    mayL.configure(text="4일에 할일: {}".format(con[123]))
                    f.close
                    

                    def may4sa():
                        od=test.get()
                        test.delete(0,END)
                        con[123]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        mayL.configure(text="4일에 할일: {}".format(con[123]))
                    mayb=Button(may,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=may4sa)
                    mayb.place(x=250,y=10)

                    test=Entry(may, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)
                def may5ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    mayL.configure(text="5일에 할일: {}".format(con[124]))
                    f.close
                    al=Tk()
                    al.geometry('150x100')
                    al.title("공휴일 알림")
                    alL=Label(al, text="어린이날", font=("휴먼엑스포", 15), fg="red")
                    alL.place(x=20, y=30)

                    def 종료():
                        al.destroy()

                    alB=Button(al, text="닫기", width=0, height=0, font=(10), command=종료)
                    alB.place(x=40, y=60)

                    def may5sa():
                        od=test.get()
                        test.delete(0,END)
                        con[124]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        mayL.configure(text="5일에 할일: {}".format(con[124]))
                    mayb=Button(may,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=may5sa)
                    mayb.place(x=250,y=10)

                    test=Entry(may, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)
                def may6ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    mayL.configure(text="6일에 할일: {}".format(con[125]))
                    f.close
                    al=Tk()
                    al.geometry('150x100')
                    al.title("공휴일 알림")
                    alL=Label(al, text="대체공휴일", font=("휴먼엑스포", 15), fg="red")
                    alL.place(x=20, y=30)

                    def 종료():
                        al.destroy()

                    alB=Button(al, text="닫기", width=0, height=0, font=(10), command=종료)
                    alB.place(x=40, y=60)

                    def may6sa():
                        od=test.get()
                        test.delete(0,END)
                        con[125]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        mayL.configure(text="6일에 할일: {}".format(con[125]))
                    mayb=Button(may,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=may6sa)
                    mayb.place(x=250,y=10)

                    test=Entry(may, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)
                def may7ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    mayL.configure(text="7일에 할일: {}".format(con[126]))
                    f.close
                    

                    def may7sa():
                        od=test.get()
                        test.delete(0,END)
                        con[126]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        mayL.configure(text="7일에 할일: {}".format(con[126]))
                    mayb=Button(may,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=may7sa)
                    mayb.place(x=250,y=10)

                    test=Entry(may, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)
                def may8ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    mayL.configure(text="8일에 할일: {}".format(con[127]))
                    f.close
                    

                    def may8sa():
                        od=test.get()
                        test.delete(0,END)
                        con[127]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        mayL.configure(text="8일에 할일: {}".format(con[127]))
                    mayb=Button(may,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=may8sa)
                    mayb.place(x=250,y=10)

                    test=Entry(may, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)
                def may9ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    mayL.configure(text="9일에 할일: {}".format(con[128]))
                    f.close
                    

                    def may9sa():
                        od=test.get()
                        test.delete(0,END)
                        con[128]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        mayL.configure(text="9일에 할일: {}".format(con[128]))
                    mayb=Button(may,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=may9sa)
                    mayb.place(x=250,y=10)

                    test=Entry(may, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)

                def may10ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    mayL.configure(text="10일에 할일: {}".format(con[129]))
                    f.close
                    

                    def may10sa():
                        od=test.get()
                        test.delete(0,END)
                        con[129]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        mayL.configure(text="10일에 할일: {}".format(con[129]))
                    mayb=Button(may,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=may10sa)
                    mayb.place(x=250,y=10)

                    test=Entry(may, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)
                def may11ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    mayL.configure(text="11일에 할일: {}".format(con[130]))
                    f.close
                    

                    def may11sa():
                        od=test.get()
                        test.delete(0,END)
                        con[130]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        mayL.configure(text="11일에 할일: {}".format(con[130]))
                    mayb=Button(may,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=may11sa)
                    mayb.place(x=250,y=10)

                    test=Entry(may, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)
                def may12ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    mayL.configure(text="12일에 할일: {}".format(con[131]))
                    f.close
                    al=Tk()
                    al.geometry('150x100')
                    al.title("공휴일 알림")
                    alL=Label(al, text="석가탄신일", font=("휴먼엑스포", 15), fg="red")
                    alL.place(x=20, y=30)

                    def 종료():
                        al.destroy()

                    alB=Button(al, text="닫기", width=0, height=0, font=(10), command=종료)
                    alB.place(x=40, y=60)
                    

                    def may12sa():
                        od=test.get()
                        test.delete(0,END)
                        con[131]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        mayL.configure(text="12일에 할일: {}".format(con[131]))
                    mayb=Button(may,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=may12sa)
                    mayb.place(x=250,y=10)

                    test=Entry(may, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)
                def may13ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    mayL.configure(text="13일에 할일: {}".format(con[132]))
                    f.close
                    

                    def may13sa():
                        od=test.get()
                        test.delete(0,END)
                        con[132]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        mayL.configure(text="13일에 할일: {}".format(con[132]))
                    mayb=Button(may,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=may13sa)
                    mayb.place(x=250,y=10)

                    test=Entry(may, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)
                def may14ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    mayL.configure(text="14일에 할일: {}".format(con[133]))
                    f.close
                    

                    def may14sa():
                        od=test.get()
                        test.delete(0,END)
                        con[133]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        mayL.configure(text="14일에 할일: {}".format(con[133]))
                    mayb=Button(may,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=may14sa)
                    mayb.place(x=250,y=10)

                    test=Entry(may, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)
                def may15ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    mayL.configure(text="15일에 할일: {}".format(con[134]))
                    f.close
                    

                    def may15sa():
                        od=test.get()
                        test.delete(0,END)
                        con[134]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        mayL.configure(text="15일에 할일: {}".format(con[134]))
                    mayb=Button(may,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=may15sa)
                    mayb.place(x=250,y=10)

                    test=Entry(may, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)
                def may16ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    mayL.configure(text="16일에 할일: {}".format(con[135]))
                    f.close
                    

                    def may16sa():
                        od=test.get()
                        test.delete(0,END)
                        con[135]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        mayL.configure(text="16일에 할일: {}".format(con[135]))
                    mayb=Button(may,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=may16sa)
                    mayb.place(x=250,y=10)

                    test=Entry(may, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)
                def may17ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    mayL.configure(text="17일에 할일: {}".format(con[136]))
                    f.close
                    

                    def may17sa():
                        od=test.get()
                        test.delete(0,END)
                        con[136]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        mayL.configure(text="17일에 할일: {}".format(con[136]))
                    mayb=Button(may,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=may17sa)
                    mayb.place(x=250,y=10)

                    test=Entry(may, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)
                def may18ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    mayL.configure(text="18일에 할일: {}".format(con[137]))
                    f.close
                    

                    def may18sa():
                        od=test.get()
                        test.delete(0,END)
                        con[137]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        mayL.configure(text="18일에 할일: {}".format(con[137]))
                    mayb=Button(may,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=may18sa)
                    mayb.place(x=250,y=10)

                    test=Entry(may, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)
                def may19ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    mayL.configure(text="19일에 할일: {}".format(con[138]))
                    f.close
                    

                    def may19sa():
                        od=test.get()
                        test.delete(0,END)
                        con[138]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        mayL.configure(text="19일에 할일: {}".format(con[138]))
                    mayb=Button(may,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=may19sa)
                    mayb.place(x=250,y=10)

                    test=Entry(may, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)
                def may20ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    mayL.configure(text="20일에 할일: {}".format(con[139]))
                    f.close
                    

                    def may20sa():
                        od=test.get()
                        test.delete(0,END)
                        con[139]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        mayL.configure(text="20일에 할일: {}".format(con[139]))
                    mayb=Button(may,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=may20sa)
                    mayb.place(x=250,y=10)

                    test=Entry(may, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)
                def may21ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    mayL.configure(text="21일에 할일: {}".format(con[140]))
                    f.close
                    

                    def may21sa():
                        od=test.get()
                        test.delete(0,END)
                        con[140]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        mayL.configure(text="21일에 할일: {}".format(con[140]))
                    mayb=Button(may,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=may21sa)
                    mayb.place(x=250,y=10)

                    test=Entry(may, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)
                def may22ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    mayL.configure(text="22일에 할일: {}".format(con[141]))
                    f.close
                    

                    def may22sa():
                        od=test.get()
                        test.delete(0,END)
                        con[141]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        mayL.configure(text="22일에 할일: {}".format(con[141]))
                    mayb=Button(may,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=may22sa)
                    mayb.place(x=250,y=10)

                    test=Entry(may, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)
                def may23ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    mayL.configure(text="23일에 할일: {}".format(con[142]))
                    f.close
                    

                    def may23sa():
                        od=test.get()
                        test.delete(0,END)
                        con[142]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        mayL.configure(text="23일에 할일: {}".format(con[142]))
                    mayb=Button(may,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=may23sa)
                    mayb.place(x=250,y=10)

                    test=Entry(may, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)
                def may24ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    mayL.configure(text="24일에 할일: {}".format(con[143]))
                    f.close
                    

                    def may24sa():
                        od=test.get()
                        test.delete(0,END)
                        con[143]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        mayL.configure(text="24일에 할일: {}".format(con[143]))
                    mayb=Button(may,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=may24sa)
                    mayb.place(x=250,y=10)

                    test=Entry(may, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)
                def may25ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    mayL.configure(text="25일에 할일: {}".format(con[144]))
                    f.close
                    

                    def may25sa():
                        od=test.get()
                        test.delete(0,END)
                        con[144]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        mayL.configure(text="25일에 할일: {}".format(con[144]))
                    mayb=Button(may,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=may25sa)
                    mayb.place(x=250,y=10)

                    test=Entry(may, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)
                def may26ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    mayL.configure(text="26일에 할일: {}".format(con[145]))
                    f.close
                    

                    def may26sa():
                        od=test.get()
                        test.delete(0,END)
                        con[145]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        mayL.configure(text="26일에 할일: {}".format(con[145]))
                    mayb=Button(may,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=may26sa)
                    mayb.place(x=250,y=10)

                    test=Entry(may, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)
                def may27ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    mayL.configure(text="27일에 할일: {}".format(con[146]))
                    f.close
                    

                    def may27sa():
                        od=test.get()
                        test.delete(0,END)
                        con[146]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        mayL.configure(text="27일에 할일: {}".format(con[146]))
                    mayb=Button(may,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=may27sa)
                    mayb.place(x=250,y=10)

                    test=Entry(may, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)
                def may28ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    mayL.configure(text="28일에 할일: {}".format(con[147]))
                    f.close
                    

                    def may28sa():
                        od=test.get()
                        test.delete(0,END)
                        con[147]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        mayL.configure(text="28일에 할일: {}".format(con[147]))
                    mayb=Button(may,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=may28sa)
                    mayb.place(x=250,y=10)

                    test=Entry(may, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)
                def may29ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    mayL.configure(text="29일에 할일: {}".format(con[148]))
                    f.close
                    

                    def may29sa():
                        od=test.get()
                        test.delete(0,END)
                        con[148]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        mayL.configure(text="29일에 할일: {}".format(con[148]))
                    mayb=Button(may,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=may29sa)
                    mayb.place(x=250,y=10)

                    test=Entry(may, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)
                        
                def may30ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    mayL.configure(text="30일에 할일: {}".format(con[149]))
                    f.close
                    

                    def may30sa():
                        od=test.get()
                        test.delete(0,END)
                        con[149]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        mayL.configure(text="30일에 할일: {}".format(con[149]))
                    mayb=Button(may,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=may30sa)
                    mayb.place(x=250,y=10)

                    test=Entry(may, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)

                def may31ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    mayL.configure(text="31일에 할일: {}".format(con[150]))
                    f.close
                    

                    def may31sa():
                        od=test.get()
                        test.delete(0,END)
                        con[150]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        mayL.configure(text="31일에 할일: {}".format(con[150]))
                    mayb=Button(may,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=may31sa)
                    mayb.place(x=250,y=10)

                    test=Entry(may, width='40')
                    test.grid(row='0', column='2',columnspan='2', padx='0')
                    test.place(x=350, y=40)                   
           



                may1b=Button(may,text="1", width=0, height=0, font=('휴먼엑스포', 20), command=may1ex)
                may1b.place(x=260,y=100)

                may2b=Button(may,text="2", width=0, height=0, font=('휴먼엑스포', 20), command=may2ex)
                may2b.place(x=340,y=100)

                may3b=Button(may,text="3", width=0, height=0, font=('휴먼엑스포', 20), command=may3ex)
                may3b.place(x=420,y=100)

                may4b=Button(may,text="4", width=0, height=0, font=('휴먼엑스포', 20), command=may4ex)
                may4b.place(x=500,y=100)

                may5b=Button(may,text="5",fg="red", width=0, height=0, font=('휴먼엑스포', 20), command=may5ex)
                may5b.place(x=20,y=200)

                may6b=Button(may,text="6",fg="red", width=0, height=0, font=('휴먼엑스포', 20), command=may6ex)
                may6b.place(x=100,y=200)

                may7b=Button(may,text="7", width=0, height=0, font=('휴먼엑스포', 20), command=may7ex)
                may7b.place(x=180,y=200)

                may8b=Button(may,text="8", width=0, height=0, font=('휴먼엑스포', 20), command=may8ex)
                may8b.place(x=260,y=200)

                may9b=Button(may,text="9", width=0, height=0, font=('휴먼엑스포', 20), command=may9ex)
                may9b.place(x=340,y=200)

                may10b=Button(may,text="10", width=0, height=0, font=('휴먼엑스포', 20), command=may10ex)
                may10b.place(x=420,y=200)

                may11b=Button(may,text="11", width=0, height=0, font=('휴먼엑스포', 20), command=may11ex)
                may11b.place(x=500,y=200)

                may12b=Button(may,text="12",fg="red", width=0, height=0, font=('휴먼엑스포', 20), command=may12ex)
                may12b.place(x=20,y=300)

                may13b=Button(may,text="13", width=0, height=0, font=('휴먼엑스포', 20), command=may13ex)
                may13b.place(x=100,y=300)

                may14b=Button(may,text="14", width=0, height=0, font=('휴먼엑스포', 20), command=may14ex)
                may14b.place(x=180,y=300)

                may15b=Button(may,text="15", width=0, height=0, font=('휴먼엑스포', 20), command=may15ex)
                may15b.place(x=260,y=300)

                may16b=Button(may,text="16", width=0, height=0, font=('휴먼엑스포', 20), command=may16ex)
                may16b.place(x=340,y=300)

                may17b=Button(may,text="17", width=0, height=0, font=('휴먼엑스포', 20), command=may17ex)
                may17b.place(x=420,y=300)

                may18b=Button(may,text="18", width=0, height=0, font=('휴먼엑스포', 20), command=may18ex)
                may18b.place(x=500,y=300)

                may19b=Button(may,text="19", width=0, height=0, font=('휴먼엑스포', 20), command=may19ex)
                may19b.place(x=20,y=400)

                may20b=Button(may,text="20", width=0, height=0, font=('휴먼엑스포', 20), command=may20ex)
                may20b.place(x=100,y=400)

                may21b=Button(may,text="21", width=0, height=0, font=('휴먼엑스포', 20), command=may21ex)
                may21b.place(x=180,y=400)

                may22b=Button(may,text="22", width=0, height=0, font=('휴먼엑스포', 20), command=may22ex)
                may22b.place(x=260,y=400)

                may23b=Button(may,text="23", width=0, height=0, font=('휴먼엑스포', 20), command=may23ex)
                may23b.place(x=340,y=400)

                may24b=Button(may,text="24", width=0, height=0, font=('휴먼엑스포', 20), command=may24ex)
                may24b.place(x=420,y=400)

                may25b=Button(may,text="25", width=0, height=0, font=('휴먼엑스포', 20), command=may25ex)
                may25b.place(x=500,y=400)

                may26b=Button(may,text="26", width=0, height=0, font=('휴먼엑스포', 20), command=may26ex)
                may26b.place(x=20,y=500)

                may27b=Button(may,text="27", width=0, height=0, font=('휴먼엑스포', 20), command=may27ex)
                may27b.place(x=100,y=500)

                may28b=Button(may,text="28", width=0, height=0, font=('휴먼엑스포', 20), command=may28ex)
                may28b.place(x=180,y=500)

                may29b=Button(may,text="29", width=0, height=0, font=('휴먼엑스포', 20), command=may29ex)
                may29b.place(x=260,y=500)

                may30b=Button(may,text="30", width=0, height=0, font=('휴먼엑스포', 20), command=may30ex)
                may30b.place(x=340,y=500)

                may31b=Button(may,text="31", width=0, height=0, font=('휴먼엑스포', 20), command=may31ex)
                may31b.place(x=420,y=500)

                
                
             
                def 월간5():
                    toj=Tk()
                    toj.title("5월 총 계획")
                    toj.geometry('700x700')

                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    f.close
                    
                    for i in range(120,151):
                        tojL=Label(toj, text="5월 {}일:{}".format(i-119,con[i]), font=('휴먼엑스포', 15))
                        tojL.place(x=0,y=(i-120)*20)
                        
                    
                tojb=Button(may, text="월간", height=0, font=('휴먼엑스포', 20), command=월간5)
                tojb.place(x=500,y=500)


            mayb=Button(cal, text="5월", width=4, height=2, fg='green', font=('휴먼엑스포', 20), command=may)   
            mayb.place(x=260,y=230)




                                       
                
            def jun():
                jun=Tk()
                jun.title("6월 달력")
                jun.geometry('700x700')
                junL=Label(jun, text="", font=('휴먼엑스포', 20))
                junL.place(x=350,y=0)

                LL=Label(jun, text="6월 달력", font=('휴먼엑스포', 20))
                LL.place(x=0, y=0)

                LL=Label(jun, text="일", fg="red", font=('휴먼엑스포', 15))
                LL.place(x=25, y=65)
                LL=Label(jun, text="월", font=('휴먼엑스포', 15))
                LL.place(x=105, y=65)
                LL=Label(jun, text="화", font=('휴먼엑스포', 15))
                LL.place(x=185, y=65)
                LL=Label(jun, text="수", font=('휴먼엑스포', 15))
                LL.place(x=265, y=65)
                LL=Label(jun, text="목", font=('휴먼엑스포', 15))
                LL.place(x=345, y=65)
                LL=Label(jun, text="금", font=('휴먼엑스포', 15))
                LL.place(x=425, y=65)
                LL=Label(jun, text="토", fg="blue", font=('휴먼엑스포', 15))
                LL.place(x=505, y=65)

                def jun1ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    junL.configure(text="1일에 할일: {}".format(con[151]))
                    f.close
                    

                    def jun1sa():
                        od=test.get()
                        test.delete(0,END)
                        con[151]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        junL.configure(text="1일에 할일: {}".format(con[151]))

                    junb=Button(jun,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jun1sa)
                    junb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jun, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)


                def jun2ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    junL.configure(text="2일에 할일: {}".format(con[152]))
                    f.close
                    

                    def jun2sa():
                        od=test.get()
                        test.delete(0,END)
                        con[152]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        junL.configure(text="2일에 할일: {}".format(con[152]))

                    junb=Button(jun,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jun2sa)
                    junb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jun, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)


                def jun3ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    junL.configure(text="3일에 할일: {}".format(con[153]))
                    f.close
                    

                    def jun3sa():
                        od=test.get()
                        test.delete(0,END)
                        con[153]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        junL.configure(text="3일에 할일: {}".format(con[153]))

                    junb=Button(jun,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jun3sa)
                    junb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jun, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)



                def jun4ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    junL.configure(text="4일에 할일: {}".format(con[154]))
                    f.close
                    

                    def jun4sa():
                        od=test.get()
                        test.delete(0,END)
                        con[154]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        junL.configure(text="4일에 할일: {}".format(con[154]))

                    junb=Button(jun,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jun4sa)
                    junb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jun, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)


                def jun5ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    junL.configure(text="5일에 할일: {}".format(con[155]))
                    f.close
                    

                    def jun5sa():
                        od=test.get()
                        test.delete(0,END)
                        con[155]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        junL.configure(text="5일에 할일: {}".format(con[155]))

                    junb=Button(jun,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jun5sa)
                    junb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jun, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)


                def jun6ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    junL.configure(text="6일에 할일: {}".format(con[156]))
                    f.close
                    al=Tk()
                    al.geometry('300x100')
                    al.title("공휴일 알림")
                    alL=Label(al, text="현충일, 태극기를 게양합시다", font=("휴먼엑스포", 15), fg="red")
                    alL.place(x=20, y=30)

                    def 종료():
                        al.destroy()

                    alB=Button(al, text="닫기", width=0, height=0, font=(10), command=종료)
                    alB.place(x=40, y=60)
                    

                    def jun6sa():
                        od=test.get()
                        test.delete(0,END)
                        con[156]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        junL.configure(text="6일에 할일: {}".format(con[156]))

                    junb=Button(jun,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jun6sa)
                    junb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jun, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)


                def jun7ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    junL.configure(text="7일에 할일: {}".format(con[157]))
                    f.close
                    

                    def jun7sa():
                        od=test.get()
                        test.delete(0,END)
                        con[157]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        junL.configure(text="7일에 할일: {}".format(con[157]))

                    junb=Button(jun,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jun7sa)
                    junb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jun, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)


                def jun8ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    junL.configure(text="8일에 할일: {}".format(con[158]))
                    f.close
                    

                    def jun8sa():
                        od=test.get()
                        test.delete(0,END)
                        con[158]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        junL.configure(text="8일에 할일: {}".format(con[158]))

                    junb=Button(jun,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jun8sa)
                    junb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jun, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)



                def jun9ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    junL.configure(text="9일에 할일: {}".format(con[159]))
                    f.close
                    

                    def jun9sa():
                        od=test.get()
                        test.delete(0,END)
                        con[159]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        junL.configure(text="9일에 할일: {}".format(con[159]))

                    junb=Button(jun,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jun9sa)
                    junb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jun, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)


                def jun10ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    junL.configure(text="10일에 할일: {}".format(con[160]))
                    f.close
                    

                    def jun10sa():
                        od=test.get()
                        test.delete(0,END)
                        con[160]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        junL.configure(text="10일에 할일: {}".format(con[160]))

                    junb=Button(jun,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jun10sa)
                    junb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jun, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)


                def jun11ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    junL.configure(text="11일에 할일: {}".format(con[161]))
                    f.close
                    

                    def jun11sa():
                        od=test.get()
                        test.delete(0,END)
                        con[161]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        junL.configure(text="2일에 할일: {}".format(con[161]))

                    junb=Button(jun,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jun11sa)
                    junb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jun, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)


                def jun12ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    junL.configure(text="12일에 할일: {}".format(con[162]))
                    f.close
                    

                    def jun12sa():
                        od=test.get()
                        test.delete(0,END)
                        con[162]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        junL.configure(text="12일에 할일: {}".format(con[162]))

                    junb=Button(jun,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jun12sa)
                    junb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jun, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)





                def jun13ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    junL.configure(text="13일에 할일: {}".format(con[163]))
                    f.close
                    

                    def jun13sa():
                        od=test.get()
                        test.delete(0,END)
                        con[163]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        junL.configure(text="13일에 할일: {}".format(con[163]))

                    junb=Button(jun,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jun13sa)
                    junb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jun, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)




                def jun14ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    junL.configure(text="14일에 할일: {}".format(con[164]))
                    f.close
                    

                    def jun14sa():
                        od=test.get()
                        test.delete(0,END)
                        con[164]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        junL.configure(text="14일에 할일: {}".format(con[164]))

                    junb=Button(jun,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jun14sa)
                    junb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jun, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)



                def jun15ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    junL.configure(text="15일에 할일: {}".format(con[165]))
                    f.close
                    

                    def jun15sa():
                        od=test.get()
                        test.delete(0,END)
                        con[165]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        junL.configure(text="15일에 할일: {}".format(con[165]))

                    junb=Button(jun,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jun15sa)
                    junb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jun, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)


                def jun16ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    junL.configure(text="16일에 할일: {}".format(con[166]))
                    f.close
                    

                    def jun16sa():
                        od=test.get()
                        test.delete(0,END)
                        con[166]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        junL.configure(text="16일에 할일: {}".format(con[166]))

                    junb=Button(jun,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jun16sa)
                    junb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jun, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)



                def jun17ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    junL.configure(text="17일에 할일: {}".format(con[167]))
                    f.close
                    

                    def jun17sa():
                        od=test.get()
                        test.delete(0,END)
                        con[167]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        junL.configure(text="17일에 할일: {}".format(con[167]))

                    junb=Button(jun,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jun17sa)
                    junb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jun, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)



                def jun18ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    junL.configure(text="18일에 할일: {}".format(con[168]))
                    f.close
                    

                    def jun18sa():
                        od=test.get()
                        test.delete(0,END)
                        con[168]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        junL.configure(text="18일에 할일: {}".format(con[168]))

                    junb=Button(jun,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jun18sa)
                    junb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jun, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)



                def jun19ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    junL.configure(text="19일에 할일: {}".format(con[169]))
                    f.close
                    

                    def jun19sa():
                        od=test.get()
                        test.delete(0,END)
                        con[169]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        junL.configure(text="19일에 할일: {}".format(con[169]))

                    junb=Button(jun,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jun19sa)
                    junb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jun, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)



                def jun20ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    junL.configure(text="20일에 할일: {}".format(con[170]))
                    f.close
                    

                    def jun20sa():
                        od=test.get()
                        test.delete(0,END)
                        con[170]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        junL.configure(text="20일에 할일: {}".format(con[170]))

                    junb=Button(jun,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jun20sa)
                    junb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jun, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)




                def jun21ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    junL.configure(text="21일에 할일: {}".format(con[171]))
                    f.close
                    

                    def jun21sa():
                        od=test.get()
                        test.delete(0,END)
                        con[171]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        junL.configure(text="21일에 할일: {}".format(con[171]))

                    junb=Button(jun,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jun21sa)
                    junb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jun, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)



                def jun22ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    junL.configure(text="22일에 할일: {}".format(con[172]))
                    f.close
                    

                    def jun22sa():
                        od=test.get()
                        test.delete(0,END)
                        con[172]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        junL.configure(text="22일에 할일: {}".format(con[172]))

                    junb=Button(jun,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jun22sa)
                    junb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jun, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)



                def jun23ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    junL.configure(text="23일에 할일: {}".format(con[173]))
                    f.close
                    

                    def jun23sa():
                        od=test.get()
                        test.delete(0,END)
                        con[173]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        junL.configure(text="23일에 할일: {}".format(con[173]))

                    junb=Button(jun,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jun23sa)
                    junb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jun, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)



                def jun24ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    junL.configure(text="24일에 할일: {}".format(con[174]))
                    f.close
                    

                    def jun24sa():
                        od=test.get()
                        test.delete(0,END)
                        con[174]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        junL.configure(text="24일에 할일: {}".format(con[174]))

                    junb=Button(jun,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jun24sa)
                    junb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jun, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)




                def jun25ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    junL.configure(text="25일에 할일: {}".format(con[175]))
                    f.close
                    

                    def jun25sa():
                        od=test.get()
                        test.delete(0,END)
                        con[175]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        junL.configure(text="25일에 할일: {}".format(con[175]))

                    junb=Button(jun,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jun25sa)
                    junb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jun, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)




                def jun26ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    junL.configure(text="26일에 할일: {}".format(con[176]))
                    f.close
                    

                    def jun26sa():
                        od=test.get()
                        test.delete(0,END)
                        con[176]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        junL.configure(text="26일에 할일: {}".format(con[176]))

                    junb=Button(jun,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jun26sa)
                    junb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jun, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)



                def jun27ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    junL.configure(text="27일에 할일: {}".format(con[177]))
                    f.close
                    

                    def jun27sa():
                        od=test.get()
                        test.delete(0,END)
                        con[177]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        junL.configure(text="27일에 할일: {}".format(con[177]))

                    junb=Button(jun,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jun27sa)
                    junb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jun, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                    


                def jun28ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    junL.configure(text="28일에 할일: {}".format(con[178]))
                    f.close
                    

                    def jun28sa():
                        od=test.get()
                        test.delete(0,END)
                        con[178]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        junL.configure(text="28일에 할일: {}".format(con[178]))

                    junb=Button(jun,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jun28sa)
                    junb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jun, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)





                def jun29ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    junL.configure(text="29일에 할일: {}".format(con[179]))
                    f.close
                    

                    def jun29sa():
                        od=test.get()
                        test.delete(0,END)
                        con[179]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        junL.configure(text="29일에 할일: {}".format(con[179]))

                    junb=Button(jun,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jun29sa)
                    junb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jun, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)




                def jun30ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    junL.configure(text="30일에 할일: {}".format(con[180]))
                    f.close
                    

                    def jun30sa():
                        od=test.get()
                        test.delete(0,END)
                        con[180]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        junL.configure(text="30일에 할일: {}".format(con[180]))

                    junb=Button(jun,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jun30sa)
                    junb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jun, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)




                jun1b=Button(jun,text="1", width=0, height=0, font=('휴먼엑스포', 20), command=jun1ex)
                jun1b.place(x=500,y=100)

                jun2b=Button(jun,text="2", width=0, height=0, font=('휴먼엑스포', 20), command=jun2ex)
                jun2b.place(x=20,y=200)

                jun3b=Button(jun,text="3", width=0, height=0, font=('휴먼엑스포', 20), command=jun3ex)
                jun3b.place(x=100,y=200)

                jun4b=Button(jun,text="4", width=0, height=0, font=('휴먼엑스포', 20), command=jun4ex)
                jun4b.place(x=180,y=200)

                jun5b=Button(jun,text="5", width=0, height=0, font=('휴먼엑스포', 20), command=jun5ex)
                jun5b.place(x=260,y=200)

                jun6b=Button(jun,text="6", fg="red", width=0, height=0, font=('휴먼엑스포', 20), command=jun6ex)
                jun6b.place(x=340,y=200)

                jun7b=Button(jun,text="7", width=0, height=0, font=('휴먼엑스포', 20), command=jun7ex)
                jun7b.place(x=420,y=200)

                jun8b=Button(jun,text="8", width=0, height=0, font=('휴먼엑스포', 20), command=jun8ex)
                jun8b.place(x=500,y=200)

                jun9b=Button(jun,text="9", width=0, height=0, font=('휴먼엑스포', 20), command=jun9ex)
                jun9b.place(x=20,y=300)

                jun10b=Button(jun,text="10", width=0, height=0, font=('휴먼엑스포', 20), command=jun10ex)
                jun10b.place(x=100,y=300)

                jun11b=Button(jun,text="11", width=0, height=0, font=('휴먼엑스포', 20), command=jun11ex)
                jun11b.place(x=180,y=300)

                jun12b=Button(jun,text="12", width=0, height=0, font=('휴먼엑스포', 20), command=jun12ex)
                jun12b.place(x=260,y=300)

                jun13b=Button(jun,text="13", width=0, height=0, font=('휴먼엑스포', 20), command=jun13ex)
                jun13b.place(x=340,y=300)

                jun14b=Button(jun,text="14", width=0, height=0, font=('휴먼엑스포', 20), command=jun14ex)
                jun14b.place(x=420,y=300)

                jun15b=Button(jun,text="15", width=0, height=0, font=('휴먼엑스포', 20), command=jun15ex)
                jun15b.place(x=500,y=300)

                jun16b=Button(jun,text="16", width=0, height=0, font=('휴먼엑스포', 20), command=jun16ex)
                jun16b.place(x=20,y=400)

                jun17b=Button(jun,text="17", width=0, height=0, font=('휴먼엑스포', 20), command=jun17ex)
                jun17b.place(x=100,y=400)

                jun18b=Button(jun,text="18", width=0, height=0, font=('휴먼엑스포', 20), command=jun18ex)
                jun18b.place(x=180,y=400)

                jun19b=Button(jun,text="19", width=0, height=0, font=('휴먼엑스포', 20), command=jun19ex)
                jun19b.place(x=260,y=400)

                jun20b=Button(jun,text="20", width=0, height=0, font=('휴먼엑스포', 20), command=jun20ex)
                jun20b.place(x=340,y=400)

                jun21b=Button(jun,text="21", width=0, height=0, font=('휴먼엑스포', 20), command=jun21ex)
                jun21b.place(x=420,y=400)

                jun22b=Button(jun,text="22", width=0, height=0, font=('휴먼엑스포', 20), command=jun22ex)
                jun22b.place(x=500,y=400)

                jun23b=Button(jun,text="23", width=0, height=0, font=('휴먼엑스포', 20), command=jun23ex)
                jun23b.place(x=20,y=500)

                jun24b=Button(jun,text="24", width=0, height=0, font=('휴먼엑스포', 20), command=jun24ex)
                jun24b.place(x=100,y=500)

                jun25b=Button(jun,text="25", width=0, height=0, font=('휴먼엑스포', 20), command=jun25ex)
                jun25b.place(x=180,y=500)

                jun26b=Button(jun,text="26", width=0, height=0, font=('휴먼엑스포', 20), command=jun26ex)
                jun26b.place(x=260,y=500)

                jun27b=Button(jun,text="27", width=0, height=0, font=('휴먼엑스포', 20), command=jun27ex)
                jun27b.place(x=340,y=500)

                jun28b=Button(jun,text="28", width=0, height=0, font=('휴먼엑스포', 20), command=jun28ex)
                jun28b.place(x=420,y=500)

                jun29b=Button(jun,text="29", width=0, height=0, font=('휴먼엑스포', 20), command=jun29ex)
                jun29b.place(x=500,y=500)

                jun30b=Button(jun,text="30", width=0, height=0, font=('휴먼엑스포', 20), command=jun30ex)
                jun30b.place(x=20,y=600)

                def 월간6():
                    toj=Tk()
                    toj.title("6월 총 계획")
                    toj.geometry('700x700')

                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    f.close
                    
                    for i in range(151,181):
                        tojL=Label(toj, text="6월 {}일:{}".format(i-150,con[i]), font=('휴먼엑스포', 15))
                        tojL.place(x=0,y=(i-151)*20)

                         
                tojb=Button(jun, text="월간", height=0, font=('휴먼엑스포', 20), command=월간6)   
                tojb.place(x=580,y=500)




            junb=Button(cal, text="6월", width=4, height=2, fg='ivory', font=('휴먼엑스포', 20), command=jun)   
            junb.place(x=410,y=230)


            def jul():
                jul=Tk()
                jul.title("7월 달력")
                jul.geometry('700x600')
                julL=Label(jul, text="", font=('휴먼엑스포', 20))
                julL.place(x=350,y=0)
                LL=Label(jul, text="7월 달력", font=('휴먼엑스포', 20))
                LL.place(x=0, y=0)

                LL=Label(jul, text="일", fg="red", font=('휴먼엑스포', 15))
                LL.place(x=25, y=65)
                LL=Label(jul, text="월", font=('휴먼엑스포', 15))
                LL.place(x=105, y=65)
                LL=Label(jul, text="화", font=('휴먼엑스포', 15))
                LL.place(x=185, y=65)
                LL=Label(jul, text="수", font=('휴먼엑스포', 15))
                LL.place(x=265, y=65)
                LL=Label(jul, text="목", font=('휴먼엑스포', 15))
                LL.place(x=345, y=65)
                LL=Label(jul, text="금", font=('휴먼엑스포', 15))
                LL.place(x=425, y=65)
                LL=Label(jul, text="토", fg="blue", font=('휴먼엑스포', 15))
                LL.place(x=505, y=65)

                

                def jul1ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    julL.configure(text="1일에 할일: {}".format(con[181]))
                    f.close
                    

                    def jul1sa():
                        od=test.get()
                        test.delete(0,END)
                        con[181]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        julL.configure(text="1일에 할일: {}".format(con[181]))


                    julb=Button(jul,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jul1sa)
                    julb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jul, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)


                def jul2ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    julL.configure(text="2일에 할일: {}".format(con[182]))
                    f.close
                    

                    def jul2sa():
                        od=test.get()
                        test.delete(0,END)
                        con[182]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        julL.configure(text="2일에 할일: {}".format(con[182]))
                        

                    julb=Button(jul,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jul2sa)
                    julb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jul, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)


                def jul3ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    julL.configure(text="3일에 할일: {}".format(con[183]))
                    f.close
                    

                    def jul3sa():
                        od=test.get()
                        test.delete(0,END)
                        con[183]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        julL.configure(text="3일에 할일: {}".format(con[183]))
                        

                    julb=Button(jul,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jul3sa)
                    julb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jul, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)


                def jul4ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    julL.configure(text="4일에 할일: {}".format(con[184]))
                    f.close
                    

                    def jul4sa():
                        od=test.get()
                        test.delete(0,END)
                        con[184]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        julL.configure(text="4일에 할일: {}".format(con[184]))
                        

                    julb=Button(jul,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jul4sa)
                    julb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jul, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)



                def jul5ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    julL.configure(text="5일에 할일: {}".format(con[185]))
                    f.close
                    

                    def jul5sa():
                        od=test.get()
                        test.delete(0,END)
                        con[185]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        julL.configure(text="5일에 할일: {}".format(con[185]))
                        

                    julb=Button(jul,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jul5sa)
                    julb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jul, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)


                def jul6ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    julL.configure(text="6일에 할일: {}".format(con[186]))
                    f.close
                    

                    def jul6sa():
                        od=test.get()
                        test.delete(0,END)
                        con[186]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        julL.configure(text="6일에 할일: {}".format(con[186]))
                        

                    julb=Button(jul,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jul6sa)
                    julb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jul, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)


                def jul7ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    julL.configure(text="7일에 할일: {}".format(con[187]))
                    f.close
                    

                    def jul7sa():
                        od=test.get()
                        test.delete(0,END)
                        con[187]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        julL.configure(text="7일에 할일: {}".format(con[187]))
                        

                    julb=Button(jul,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jul7sa)
                    julb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jul, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)



                def jul8ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    julL.configure(text="8일에 할일: {}".format(con[188]))
                    f.close
                    

                    def jul8sa():
                        od=test.get()
                        test.delete(0,END)
                        con[188]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        julL.configure(text="8일에 할일: {}".format(con[188]))
                        

                    julb=Button(jul,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jul8sa)
                    julb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jul, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)


                def jul9ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    julL.configure(text="9일에 할일: {}".format(con[189]))
                    f.close
                    

                    def jul9sa():
                        od=test.get()
                        test.delete(0,END)
                        con[189]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        julL.configure(text="9일에 할일: {}".format(con[189]))
                        

                    julb=Button(jul,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jul9sa)
                    julb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jul, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)


                def jul10ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    julL.configure(text="10일에 할일: {}".format(con[190]))
                    f.close
                    

                    def jul10sa():
                        od=test.get()
                        test.delete(0,END)
                        con[190]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        julL.configure(text="10일에 할일: {}".format(con[190]))
                        

                    julb=Button(jul,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jul10sa)
                    julb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jul, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)



                def jul11ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    julL.configure(text="11일에 할일: {}".format(con[191]))
                    f.close
                    

                    def jul11sa():
                        od=test.get()
                        test.delete(0,END)
                        con[191]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        julL.configure(text="11일에 할일: {}".format(con[191]))
                        

                    julb=Button(jul,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jul11sa)
                    julb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jul, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)



                def jul12ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    julL.configure(text="12일에 할일: {}".format(con[192]))
                    f.close
                    

                    def jul12sa():
                        od=test.get()
                        test.delete(0,END)
                        con[192]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        julL.configure(text="12일에 할일: {}".format(con[192]))
                        

                    julb=Button(jul,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jul12sa)
                    julb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jul, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)



                def jul13ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    julL.configure(text="13일에 할일: {}".format(con[193]))
                    f.close
                    

                    def jul13sa():
                        od=test.get()
                        test.delete(0,END)
                        con[193]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        julL.configure(text="13일에 할일: {}".format(con[193]))
                        

                    julb=Button(jul,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jul13sa)
                    julb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jul, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)



                def jul14ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    julL.configure(text="14일에 할일: {}".format(con[194]))
                    f.close
                    

                    def jul14sa():
                        od=test.get()
                        test.delete(0,END)
                        con[194]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        julL.configure(text="14일에 할일: {}".format(con[194]))
                        

                    julb=Button(jul,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jul14sa)
                    julb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jul, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)



                def jul15ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    julL.configure(text="15일에 할일: {}".format(con[195]))
                    f.close
                    

                    def jul15sa():
                        od=test.get()
                        test.delete(0,END)
                        con[195]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        julL.configure(text="15일에 할일: {}".format(con[195]))
                        

                    julb=Button(jul,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jul15sa)
                    julb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jul, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)



                def jul16ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    julL.configure(text="16일에 할일: {}".format(con[196]))
                    f.close
                    

                    def jul16sa():
                        od=test.get()
                        test.delete(0,END)
                        con[196]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        julL.configure(text="16일에 할일: {}".format(con[196]))
                        

                    julb=Button(jul,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jul16sa)
                    julb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jul, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)



                def jul17ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    julL.configure(text="17일에 할일: {}".format(con[197]))
                    f.close
                    

                    def jul17sa():
                        od=test.get()
                        test.delete(0,END)
                        con[197]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        julL.configure(text="17일에 할일: {}".format(con[197]))
                        

                    julb=Button(jul,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jul17sa)
                    julb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jul, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)


                def jul18ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    julL.configure(text="18일에 할일: {}".format(con[198]))
                    f.close
                    

                    def jul18sa():
                        od=test.get()
                        test.delete(0,END)
                        con[198]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        julL.configure(text="18일에 할일: {}".format(con[198]))
                        

                    julb=Button(jul,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jul18sa)
                    julb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jul, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)



                def jul19ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    julL.configure(text="19일에 할일: {}".format(con[199]))
                    f.close
                    

                    def jul19sa():
                        od=test.get()
                        test.delete(0,END)
                        con[199]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        julL.configure(text="19일에 할일: {}".format(con[199]))
                        

                    julb=Button(jul,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jul19sa)
                    julb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jul, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)



                def jul20ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    julL.configure(text="20일에 할일: {}".format(con[200]))
                    f.close
                    

                    def jul20sa():
                        od=test.get()
                        test.delete(0,END)
                        con[200]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        julL.configure(text="20일에 할일: {}".format(con[200]))
                        

                    julb=Button(jul,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jul20sa)
                    julb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jul, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)




                def jul21ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    julL.configure(text="21일에 할일: {}".format(con[201]))
                    f.close
                    

                    def jul21sa():
                        od=test.get()
                        test.delete(0,END)
                        con[201]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        julL.configure(text="21일에 할일: {}".format(con[201]))
                        

                    julb=Button(jul,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jul21sa)
                    julb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jul, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)



                def jul22ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    julL.configure(text="22일에 할일: {}".format(con[202]))
                    f.close
                    

                    def jul22sa():
                        od=test.get()
                        test.delete(0,END)
                        con[202]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        julL.configure(text="22일에 할일: {}".format(con[202]))
                        

                    julb=Button(jul,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jul22sa)
                    julb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jul, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)



                def jul23ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    julL.configure(text="23일에 할일: {}".format(con[203]))
                    f.close
                    

                    def jul23sa():
                        od=test.get()
                        test.delete(0,END)
                        con[203]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        julL.configure(text="23일에 할일: {}".format(con[203]))
                        

                    julb=Button(jul,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jul23sa)
                    julb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jul, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)



                def jul24ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    julL.configure(text="24일에 할일: {}".format(con[204]))
                    f.close
                    

                    def jul24sa():
                        od=test.get()
                        test.delete(0,END)
                        con[204]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        julL.configure(text="24일에 할일: {}".format(con[204]))
                        

                    julb=Button(jul,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jul24sa)
                    julb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jul, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)



                def jul25ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    julL.configure(text="25일에 할일: {}".format(con[205]))
                    f.close
                    

                    def jul25sa():
                        od=test.get()
                        test.delete(0,END)
                        con[205]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        julL.configure(text="25일에 할일: {}".format(con[205]))
                        

                    julb=Button(jul,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jul25sa)
                    julb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jul, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)



                def jul26ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    julL.configure(text="26일에 할일: {}".format(con[206]))
                    f.close
                    

                    def jul26sa():
                        od=test.get()
                        test.delete(0,END)
                        con[206]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        julL.configure(text="26일에 할일: {}".format(con[206]))
                        

                    julb=Button(jul,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jul26sa)
                    julb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jul, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)



                def jul27ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    julL.configure(text="27일에 할일: {}".format(con[207]))
                    f.close
                    

                    def jul27sa():
                        od=test.get()
                        test.delete(0,END)
                        con[207]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        julL.configure(text="27일에 할일: {}".format(con[207]))
                        

                    julb=Button(jul,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jul27sa)
                    julb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jul, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)



                def jul28ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    julL.configure(text="28일에 할일: {}".format(con[208]))
                    f.close
                    

                    def jul28sa():
                        od=test.get()
                        test.delete(0,END)
                        con[208]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        julL.configure(text="28일에 할일: {}".format(con[208]))
                        

                    julb=Button(jul,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jul28sa)
                    julb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jul, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)



                def jul29ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    julL.configure(text="29일에 할일: {}".format(con[209]))
                    f.close
                    

                    def jul29sa():
                        od=test.get()
                        test.delete(0,END)
                        con[209]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        julL.configure(text="29일에 할일: {}".format(con[209]))
                        

                    julb=Button(jul,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jul29sa)
                    julb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jul, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)



                def jul30ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    julL.configure(text="30일에 할일: {}".format(con[210]))
                    f.close
                    

                    def jul30sa():
                        od=test.get()
                        test.delete(0,END)
                        con[210]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        julL.configure(text="30일에 할일: {}".format(con[210]))
                        

                    julb=Button(jul,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jul30sa)
                    julb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jul, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)



                def jul31ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    julL.configure(text="31일에 할일: {}".format(con[211]))
                    f.close
                    

                    def jul31sa():
                        od=test.get()
                        test.delete(0,END)
                        con[211]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        julL.configure(text="31일에 할일: {}".format(con[211]))
                        

                    julb=Button(jul,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=jul31sa)
                    julb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(jul, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)


                jul1b=Button(jul,text="1", width=0, height=0, font=('휴먼엑스포', 20), command=jul1ex)
                jul1b.place(x=100,y=100)

                jul2b=Button(jul,text="2", width=0, height=0, font=('휴먼엑스포', 20), command=jul2ex)
                jul2b.place(x=180,y=100)

                jul3b=Button(jul,text="3", width=0, height=0, font=('휴먼엑스포', 20), command=jul3ex)
                jul3b.place(x=260,y=100)

                jul4b=Button(jul,text="4", width=0, height=0, font=('휴먼엑스포', 20), command=jul4ex)
                jul4b.place(x=340,y=100)

                jul5b=Button(jul,text="5", width=0, height=0, font=('휴먼엑스포', 20), command=jul5ex)
                jul5b.place(x=420,y=100)

                jul6b=Button(jul,text="6", width=0, height=0, font=('휴먼엑스포', 20), command=jul6ex)
                jul6b.place(x=500,y=100)

                jul7b=Button(jul,text="7", width=0, height=0, font=('휴먼엑스포', 20), command=jul7ex)
                jul7b.place(x=20,y=200)

                jul8b=Button(jul,text="8", width=0, height=0, font=('휴먼엑스포', 20), command=jul8ex)
                jul8b.place(x=100,y=200)

                jul9b=Button(jul,text="9", width=0, height=0, font=('휴먼엑스포', 20), command=jul9ex)
                jul9b.place(x=180,y=200)

                jul10b=Button(jul,text="10", width=0, height=0, font=('휴먼엑스포', 20), command=jul10ex)
                jul10b.place(x=260,y=200)

                jul11b=Button(jul,text="11", width=0, height=0, font=('휴먼엑스포', 20), command=jul11ex)
                jul11b.place(x=340,y=200)

                jul12b=Button(jul,text="12", width=0, height=0, font=('휴먼엑스포', 20), command=jul12ex)
                jul12b.place(x=420,y=200)

                jul13b=Button(jul,text="13", width=0, height=0, font=('휴먼엑스포', 20), command=jul13ex)
                jul13b.place(x=500,y=200)

                jul14b=Button(jul,text="14", width=0, height=0, font=('휴먼엑스포', 20), command=jul14ex)
                jul14b.place(x=20,y=300)

                jul15b=Button(jul,text="15", width=0, height=0, font=('휴먼엑스포', 20), command=jul15ex)
                jul15b.place(x=100,y=300)

                jul16b=Button(jul,text="16", width=0, height=0, font=('휴먼엑스포', 20), command=jul16ex)
                jul16b.place(x=180,y=300)

                jul17b=Button(jul,text="17", width=0, height=0, font=('휴먼엑스포', 20), command=jul17ex)
                jul17b.place(x=260,y=300)

                jul18b=Button(jul,text="18", width=0, height=0, font=('휴먼엑스포', 20), command=jul18ex)
                jul18b.place(x=340,y=300)

                jul19b=Button(jul,text="19", width=0, height=0, font=('휴먼엑스포', 20), command=jul19ex)
                jul19b.place(x=420,y=300)

                jul20b=Button(jul,text="20", width=0, height=0, font=('휴먼엑스포', 20), command=jul20ex)
                jul20b.place(x=500,y=300)

                jul21b=Button(jul,text="21", width=0, height=0, font=('휴먼엑스포', 20), command=jul21ex)
                jul21b.place(x=20,y=400)

                jul22b=Button(jul,text="22", width=0, height=0, font=('휴먼엑스포', 20), command=jul22ex)
                jul22b.place(x=100,y=400)

                jul23b=Button(jul,text="23", width=0, height=0, font=('휴먼엑스포', 20), command=jul23ex)
                jul23b.place(x=180,y=400)

                jul24b=Button(jul,text="24", width=0, height=0, font=('휴먼엑스포', 20), command=jul24ex)
                jul24b.place(x=260,y=400)

                jul25b=Button(jul,text="25", width=0, height=0, font=('휴먼엑스포', 20), command=jul25ex)
                jul25b.place(x=340,y=400)
                
                jul26b=Button(jul,text="26", width=0, height=0, font=('휴먼엑스포', 20), command=jul26ex)
                jul26b.place(x=420,y=400)

                jul27b=Button(jul,text="27", width=0, height=0, font=('휴먼엑스포', 20), command=jul27ex)
                jul27b.place(x=500,y=400)

                jul28b=Button(jul,text="28", width=0, height=0, font=('휴먼엑스포', 20), command=jul28ex)
                jul28b.place(x=20,y=500)

                jul29b=Button(jul,text="29", width=0, height=0, font=('휴먼엑스포', 20), command=jul29ex)
                jul29b.place(x=100,y=500)

                jul30b=Button(jul,text="30", width=0, height=0, font=('휴먼엑스포', 20), command=jul30ex)
                jul30b.place(x=180,y=500)

                jul31b=Button(jul,text="31", width=0, height=0, font=('휴먼엑스포', 20), command=jul31ex)
                jul31b.place(x=260,y=500)


                def 월간7():
                    toj=Tk()
                    toj.title("7월 총 계획")
                    toj.geometry('700x700')

                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    f.close
                    
                    for i in range(181,212):
                        tojL=Label(toj, text="7월 {}일:{}".format(i-180,con[i]), font=('휴먼엑스포', 15))
                        tojL.place(x=0,y=(i-181)*20)

                         
                tojulb=Button(jul, text="월간", height=0, font=('휴먼엑스포', 20), command=월간7)   
                tojulb.place(x=450,y=500)


            julb=Button(cal, text="7월", width=4, height=2, fg='red', font=('휴먼엑스포', 20), command=jul)   
            julb.place(x=110,y=340)



            def aug():
                aug=Tk()
                aug.title("8월 달력")
                aug.geometry('700x600')
                '''
                augP=PhotoImage(file="aug1.gif")
                augPlabel=Label(jan, image=augP)
                augPlabel.pack()
                '''
                augL=Label(aug, text="", font=('휴먼엑스포', 20))
                augL.place(x=350,y=0)

                LL=Label(aug, text="8월 달력", font=('휴먼엑스포', 20))
                LL.place(x=0, y=0)

                LL=Label(aug, text="일", fg="red", font=('휴먼엑스포', 15))
                LL.place(x=25, y=65)
                LL=Label(aug, text="월", font=('휴먼엑스포', 15))
                LL.place(x=105, y=65)
                LL=Label(aug, text="화", font=('휴먼엑스포', 15))
                LL.place(x=185, y=65)
                LL=Label(aug, text="수", font=('휴먼엑스포', 15))
                LL.place(x=265, y=65)
                LL=Label(aug, text="목", font=('휴먼엑스포', 15))
                LL.place(x=345, y=65)
                LL=Label(aug, text="금", font=('휴먼엑스포', 15))
                LL.place(x=425, y=65)
                LL=Label(aug, text="토", fg="blue", font=('휴먼엑스포', 15))
                LL.place(x=505, y=65)

                def aug1ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    augL.configure(text="1일에 할일: {}".format(con[212]))
                    f.close
                    

                    def aug1sa():
                        od=test.get()
                        test.delete(0,END)
                        con[212]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        augL.configure(text="1일에 할일: {}".format(con[212]))
                        
                    augb=Button(aug,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=aug1sa)
                    augb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(aug, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def aug2ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    augL.configure(text="2일에 할일: {}".format(con[213]))
                    f.close
                    

                    def aug2sa():
                        od=test.get()
                        test.delete(0,END)
                        con[213]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        augL.configure(text="2일에 할일: {}".format(con[213]))
                        
                    augb=Button(aug,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=aug2sa)
                    augb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(aug, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def aug3ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    augL.configure(text="3일에 할일: {}".format(con[214]))
                    f.close
                    

                    def aug3sa():
                        od=test.get()
                        test.delete(0,END)
                        con[214]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        augL.configure(text="3일에 할일: {}".format(con[214]))
                        
                    augb=Button(aug,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=aug3sa)
                    augb.place(x=250,y=10)
                    
                    txt=StringVar()
                    test=Entry(aug, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                    
                def aug4ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    augL.configure(text="4일에 할일: {}".format(con[215]))
                    f.close
                    

                    def aug4sa():
                        od=test.get()
                        test.delete(0,END)
                        con[215]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        augL.configure(text="4일에 할일: {}".format(con[215]))
                        
                    augb=Button(aug,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=aug4sa)
                    augb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(aug, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                    
                def aug5ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    augL.configure(text="5일에 할일: {}".format(con[216]))
                    f.close
                    

                    def aug5sa():
                        od=test.get()
                        test.delete(0,END)
                        con[216]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        augL.configure(text="4일에 할일: {}".format(con[216]))
                        
                    augb=Button(aug,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=aug5sa)
                    augb.place(x=250,y=10)
                

                    txt=StringVar()
                    test=Entry(aug, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)
                    
                def aug6ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    augL.configure(text="6일에 할일: {}".format(con[217]))
                    f.close
                    

                    def aug6sa():
                        od=test.get()
                        test.delete(0,END)
                        con[217]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        augL.configure(text="6일에 할일: {}".format(con[217]))
                        
                    augb=Button(aug,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=aug6sa)
                    augb.place(x=250,y=10)
                

                    txt=StringVar()
                    test=Entry(aug, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)
                    
                def aug7ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    augL.configure(text="7일에 할일: {}".format(con[218]))
                    f.close
                    

                    def aug7sa():
                        od=test.get()
                        test.delete(0,END)
                        con[218]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        augL.configure(text="7일에 할일: {}".format(con[218]))
                        
                    augb=Button(aug,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=aug7sa)
                    augb.place(x=250,y=10)
                

                    txt=StringVar()
                    test=Entry(aug, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def aug8ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    augL.configure(text="8일에 할일: {}".format(con[219]))
                    f.close
                    

                    def aug8sa():
                        od=test.get()
                        test.delete(0,END)
                        con[219]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        augL.configure(text="8일에 할일: {}".format(con[219]))
                        
                    augb=Button(aug,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=aug8sa)
                    augb.place(x=250,y=10)
                

                    txt=StringVar()
                    test=Entry(aug, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)


                def aug9ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    augL.configure(text="9일에 할일: {}".format(con[220]))
                    f.close
                    

                    def aug9sa():
                        od=test.get()
                        test.delete(0,END)
                        con[220]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        augL.configure(text="9일에 할일: {}".format(con[220]))
                        
                    augb=Button(aug,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=aug9sa)
                    augb.place(x=250,y=10)
                

                    txt=StringVar()
                    test=Entry(aug, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)
                   
                def aug10ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    augL.configure(text="10일에 할일: {}".format(con[221]))
                    f.close
                    

                    def aug10sa():
                        od=test.get()
                        test.delete(0,END)
                        con[221]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        augL.configure(text="10일에 할일: {}".format(con[221]))
                        
                    augb=Button(aug,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=aug10sa)
                    augb.place(x=250,y=10)                

                    txt=StringVar()
                    test=Entry(aug, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)
                    
                def aug11ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    augL.configure(text="11일에 할일: {}".format(con[222]))
                    f.close
                    

                    def aug11sa():
                        od=test.get()
                        test.delete(0,END)
                        con[222]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        augL.configure(text="11일에 할일: {}".format(con[222]))
                        
                    augb=Button(aug,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=aug11sa)
                    augb.place(x=250,y=10)                

                    txt=StringVar()
                    test=Entry(aug, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def aug12ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    augL.configure(text="12일에 할일: {}".format(con[223]))
                    f.close
                    

                    def aug12sa():
                        od=test.get()
                        test.delete(0,END)
                        con[223]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        augL.configure(text="12일에 할일: {}".format(con[223]))
                        
                    augb=Button(aug,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=aug12sa)
                    augb.place(x=250,y=10)                

                    txt=StringVar()
                    test=Entry(aug, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)
                    
                def aug13ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    augL.configure(text="13일에 할일: {}".format(con[224]))
                    f.close
                    

                    def aug13sa():
                        od=test.get()
                        test.delete(0,END)
                        con[224]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        augL.configure(text="13일에 할일: {}".format(con[224]))
                        
                    augb=Button(aug,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=aug13sa)
                    augb.place(x=250,y=10)                

                    txt=StringVar()
                    test=Entry(aug, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def aug14ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    augL.configure(text="14일에 할일: {}".format(con[225]))
                    f.close
                    

                    def aug14sa():
                        od=test.get()
                        test.delete(0,END)
                        con[225]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        augL.configure(text="14일에 할일: {}".format(con[225]))
                        
                    augb=Button(aug,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=aug14sa)
                    augb.place(x=250,y=10)                

                    txt=StringVar()
                    test=Entry(aug, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)
                    
                def aug15ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    augL.configure(text="15일에 할일: {}".format(con[226]))
                    f.close
                    al=Tk()
                    al.geometry('300x100')
                    al.title("공휴일 알림")
                    alL=Label(al, text="광복절, 태극기를 게양합시다", font=("휴먼엑스포", 15), fg="red")
                    alL.place(x=20, y=30)

                    def 종료():
                        al.destroy()

                    alB=Button(al, text="닫기", width=0, height=0, font=(10), command=종료)
                    alB.place(x=40, y=60)

                    def aug15sa():
                        od=test.get()
                        test.delete(0,END)
                        con[226]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        augL.configure(text="15일에 할일: {}".format(con[226]))
                        
                    augb=Button(aug,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=aug15sa)
                    augb.place(x=250,y=10)                

                    txt=StringVar()
                    test=Entry(aug, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)
                        
                def aug16ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    augL.configure(text="16일에 할일: {}".format(con[227]))
                    f.close
                    

                    def aug16sa():
                        od=test.get()
                        test.delete(0,END)
                        con[227]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        augL.configure(text="16일에 할일: {}".format(con[227]))
                        
                    augb=Button(aug,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=aug16sa)
                    augb.place(x=250,y=10)                

                    txt=StringVar()
                    test=Entry(aug, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def aug17ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    augL.configure(text="17일에 할일: {}".format(con[228]))
                    f.close
                    

                    def aug17sa():
                        od=test.get()
                        test.delete(0,END)
                        con[228]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        augL.configure(text="17일에 할일: {}".format(con[228]))
                        
                    augb=Button(aug,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=aug17sa)
                    augb.place(x=250,y=10)                

                    txt=StringVar()
                    test=Entry(aug, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)
                
                def aug18ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    augL.configure(text="18일에 할일: {}".format(con[229]))
                    f.close
                    

                    def aug18sa():
                        od=test.get()
                        test.delete(0,END)
                        con[229]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        augL.configure(text="18일에 할일: {}".format(con[229]))
                        
                    augb=Button(aug,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=aug18sa)
                    augb.place(x=250,y=10)                

                    txt=StringVar()
                    test=Entry(aug, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)
                    
                def aug19ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    augL.configure(text="19일에 할일: {}".format(con[230]))
                    f.close
                    

                    def aug19sa():
                        od=test.get()
                        test.delete(0,END)
                        con[230]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        augL.configure(text="19일에 할일: {}".format(con[230]))
                        
                    augb=Button(aug,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=aug19sa)
                    augb.place(x=250,y=10)                

                    txt=StringVar()
                    test=Entry(aug, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)
                    
                def aug20ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    augL.configure(text="20일에 할일: {}".format(con[231]))
                    f.close
                    

                    def aug20sa():
                        od=test.get()
                        test.delete(0,END)
                        con[231]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        augL.configure(text="20일에 할일: {}".format(con[231]))
                        
                    augb=Button(aug,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=aug20sa)
                    augb.place(x=250,y=10)                

                    txt=StringVar()
                    test=Entry(aug, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def aug21ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    augL.configure(text="21일에 할일: {}".format(con[232]))
                    f.close
                    

                    def aug21sa():
                        od=test.get()
                        test.delete(0,END)
                        con[232]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        augL.configure(text="21일에 할일: {}".format(con[232]))
                        
                    augb=Button(aug,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=aug21sa)
                    augb.place(x=250,y=10)                

                    txt=StringVar()
                    test=Entry(aug, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)
                    
                def aug22ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    augL.configure(text="22일에 할일: {}".format(con[233]))
                    f.close
                    

                    def aug22sa():
                        od=test.get()
                        test.delete(0,END)
                        con[233]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        augL.configure(text="22일에 할일: {}".format(con[233]))
                        
                    augb=Button(aug,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=aug22sa)
                    augb.place(x=250,y=10)                

                    txt=StringVar()
                    test=Entry(aug, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                    
                def aug23ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    augL.configure(text="23일에 할일: {}".format(con[234]))
                    f.close
                    

                    def aug23sa():
                        od=test.get()
                        test.delete(0,END)
                        con[234]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        augL.configure(text="23일에 할일: {}".format(con[234]))
                        
                    augb=Button(aug,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=aug23sa)
                    augb.place(x=250,y=10)                

                    txt=StringVar()
                    test=Entry(aug, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)
                    
                def aug24ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    augL.configure(text="24일에 할일: {}".format(con[235]))
                    f.close
                    

                    def aug24sa():
                        od=test.get()
                        test.delete(0,END)
                        con[235]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        augL.configure(text="24일에 할일: {}".format(con[235]))
                        
                    augb=Button(aug,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=aug24sa)
                    augb.place(x=250,y=10)                

                    txt=StringVar()
                    test=Entry(aug, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)
                    
                def aug25ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    augL.configure(text="25일에 할일: {}".format(con[236]))
                    f.close
                    

                    def aug25sa():
                        od=test.get()
                        test.delete(0,END)
                        con[236]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        augL.configure(text="25일에 할일: {}".format(con[236]))
                        
                    augb=Button(aug,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=aug25sa)
                    augb.place(x=250,y=10)                

                    txt=StringVar()
                    test=Entry(aug, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)
                    
                def aug26ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    augL.configure(text="26일에 할일: {}".format(con[237]))
                    f.close
                    

                    def aug26sa():
                        od=test.get()
                        test.delete(0,END)
                        con[237]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        augL.configure(text="26일에 할일: {}".format(con[237]))
                        
                    augb=Button(aug,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=aug26sa)
                    augb.place(x=250,y=10)                

                    txt=StringVar()
                    test=Entry(aug, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)
                    
                def aug27ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    augL.configure(text="27일에 할일: {}".format(con[238]))
                    f.close
                    

                    def aug27sa():
                        od=test.get()
                        test.delete(0,END)
                        con[238]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        augL.configure(text="27일에 할일: {}".format(con[238]))
                        
                    augb=Button(aug,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=aug27sa)
                    augb.place(x=250,y=10)                

                    txt=StringVar()
                    test=Entry(aug, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def aug28ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    augL.configure(text="28일에 할일: {}".format(con[239]))
                    f.close
                    

                    def aug28sa():
                        od=test.get()
                        test.delete(0,END)
                        con[239]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        augL.configure(text="28일에 할일: {}".format(con[239]))
                        
                    augb=Button(aug,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=aug28sa)
                    augb.place(x=250,y=10)                

                    txt=StringVar()
                    test=Entry(aug, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)
                    
                def aug29ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    augL.configure(text="29일에 할일: {}".format(con[240]))
                    f.close
                    

                    def aug29sa():
                        od=test.get()
                        test.delete(0,END)
                        con[240]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        augL.configure(text="29일에 할일: {}".format(con[240]))
                        
                    augb=Button(aug,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=aug29sa)
                    augb.place(x=250,y=10)                

                    txt=StringVar()
                    test=Entry(aug, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)
                    
                def aug30ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    augL.configure(text="30일에 할일: {}".format(con[241]))
                    f.close
                    

                    def aug30sa():
                        od=test.get()
                        test.delete(0,END)
                        con[241]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        augL.configure(text="30일에 할일: {}".format(con[241]))
                        
                    augb=Button(aug,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=aug30sa)
                    augb.place(x=250,y=10)                

                    txt=StringVar()
                    test=Entry(aug, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)
                    
                def aug31ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    augL.configure(text="31일에 할일: {}".format(con[242]))
                    f.close
                    

                    def aug31sa():
                        od=test.get()
                        test.delete(0,END)
                        con[242]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        augL.configure(text="31일에 할일: {}".format(con[242]))
                        
                    augb=Button(aug,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=aug31sa)
                    augb.place(x=250,y=10)                

                    txt=StringVar()
                    test=Entry(aug, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                aug1b=Button(aug,text="1", width=0, height=0, font=('휴먼엑스포', 20), command=aug1ex)
                aug1b.place(x=340,y=100)

                aug2b=Button(aug,text="2", width=0, height=0, font=('휴먼엑스포', 20), command=aug2ex)
                aug2b.place(x=420,y=100)
                
                aug3b=Button(aug,text="3", width=0, height=0, font=('휴먼엑스포', 20), command=aug3ex)
                aug3b.place(x=500,y=100)
                
                aug4b=Button(aug,text="4", width=0, height=0, font=('휴먼엑스포', 20), command=aug4ex)
                aug4b.place(x=20,y=200)
                
                aug5b=Button(aug,text="5", width=0, height=0, font=('휴먼엑스포', 20), command=aug5ex)
                aug5b.place(x=100,y=200)
                
                aug6b=Button(aug,text="6", width=0, height=0, font=('휴먼엑스포', 20), command=aug6ex)
                aug6b.place(x=180,y=200)
                
                aug7b=Button(aug,text="7", width=0, height=0, font=('휴먼엑스포', 20), command=aug7ex)
                aug7b.place(x=260,y=200)
                
                aug8b=Button(aug,text="8", width=0, height=0, font=('휴먼엑스포', 20), command=aug8ex)
                aug8b.place(x=340,y=200)
                
                aug9b=Button(aug,text="9", width=0, height=0, font=('휴먼엑스포', 20), command=aug9ex)
                aug9b.place(x=420,y=200)

                aug10b=Button(aug,text="10", width=0, height=0, font=('휴먼엑스포', 20), command=aug10ex)
                aug10b.place(x=500,y=200)
                
                aug11b=Button(aug,text="11", width=0, height=0, font=('휴먼엑스포', 20), command=aug11ex)
                aug11b.place(x=20,y=300)

                aug12b=Button(aug,text="12", width=0, height=0, font=('휴먼엑스포', 20), command=aug12ex)
                aug12b.place(x=100,y=300)
                
                aug13b=Button(aug,text="13", width=0, height=0, font=('휴먼엑스포', 20), command=aug13ex)
                aug13b.place(x=180,y=300)

                aug14b=Button(aug,text="14", width=0, height=0, font=('휴먼엑스포', 20), command=aug14ex)
                aug14b.place(x=260,y=300)
                
                aug15b=Button(aug,text="15",fg="red", width=0, height=0, font=('휴먼엑스포', 20), command=aug15ex)
                aug15b.place(x=340,y=300)
                
                aug16b=Button(aug,text="16", width=0, height=0, font=('휴먼엑스포', 20), command=aug16ex)
                aug16b.place(x=420,y=300)
                
                aug17b=Button(aug,text="17", width=0, height=0, font=('휴먼엑스포', 20), command=aug17ex)
                aug17b.place(x=500,y=300)

                aug18b=Button(aug,text="18", width=0, height=0, font=('휴먼엑스포', 20), command=aug18ex)
                aug18b.place(x=20,y=400)

                aug19b=Button(aug,text="19", width=0, height=0, font=('휴먼엑스포', 20), command=aug19ex)
                aug19b.place(x=100,y=400)

                aug20b=Button(aug,text="20", width=0, height=0, font=('휴먼엑스포', 20), command=aug20ex)
                aug20b.place(x=180,y=400)

                aug21b=Button(aug,text="21", width=0, height=0, font=('휴먼엑스포', 20), command=aug21ex)
                aug21b.place(x=260,y=400)

                aug22b=Button(aug,text="22", width=0, height=0, font=('휴먼엑스포', 20), command=aug22ex)
                aug22b.place(x=340,y=400)

                aug23b=Button(aug,text="23", width=0, height=0, font=('휴먼엑스포', 20), command=aug23ex)
                aug23b.place(x=420,y=400)

                aug24b=Button(aug,text="24", width=0, height=0, font=('휴먼엑스포', 20), command=aug24ex)
                aug24b.place(x=500,y=400)

                aug25b=Button(aug,text="25", width=0, height=0, font=('휴먼엑스포', 20), command=aug25ex)
                aug25b.place(x=20,y=500)

                aug26b=Button(aug,text="26", width=0, height=0, font=('휴먼엑스포', 20), command=aug26ex)
                aug26b.place(x=100,y=500)

                aug27b=Button(aug,text="27", width=0, height=0, font=('휴먼엑스포', 20), command=aug27ex)
                aug27b.place(x=180,y=500)

                aug28b=Button(aug,text="28", width=0, height=0, font=('휴먼엑스포', 20), command=aug28ex)
                aug28b.place(x=260,y=500)

                aug29b=Button(aug,text="29", width=0, height=0, font=('휴먼엑스포', 20), command=aug29ex)
                aug29b.place(x=340,y=500)

                aug30b=Button(aug,text="30", width=0, height=0, font=('휴먼엑스포', 20), command=aug30ex)
                aug30b.place(x=420,y=500)

                aug31b=Button(aug,text="31", width=0, height=0, font=('휴먼엑스포', 20), command=aug31ex)
                aug31b.place(x=500,y=500)
                def 월간8():
                    toj=Tk()
                    toj.title("8월 총 계획")
                    toj.geometry('700x700')

                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    f.close
                    
                    for i in range(212,243):
                        tojL=Label(toj, text="8월 {}일:{}".format(i-211,con[i]), font=('휴먼엑스포', 15))
                        tojL.place(x=0,y=(i-212)*20)
                        
                    
                tojb=Button(aug, text="월간", height=0, font=('휴먼엑스포', 20), command=월간8)   
                tojb.place(x=580,y=500)


               
            augb=Button(cal, text="8월", width=4, height=2, fg='yellow green', font=('휴먼엑스포', 20), command=aug)   
            augb.place(x=260,y=340)


            
            def sep():
                sep=Tk()
                sep.title("9월 달력")
                sep.geometry('700x600')
                '''
                sepP=PhotoImage(file="sep1.gif")
                sepPlabel=Label(sep, image=sepP)
                sepPlabel.pack()
                '''
                sepL=Label(sep, text="", font=('휴먼엑스포', 20))
                sepL.place(x=350,y=0)
                LL=Label(sep, text="9월 달력", font=('휴먼엑스포', 20))
                LL.place(x=0, y=0)

                LL=Label(sep, text="일", fg="red", font=('휴먼엑스포', 15))
                LL.place(x=25, y=65)
                LL=Label(sep, text="월", font=('휴먼엑스포', 15))
                LL.place(x=105, y=65)
                LL=Label(sep, text="화", font=('휴먼엑스포', 15))
                LL.place(x=185, y=65)
                LL=Label(sep, text="수", font=('휴먼엑스포', 15))
                LL.place(x=265, y=65)
                LL=Label(sep, text="목", font=('휴먼엑스포', 15))
                LL.place(x=345, y=65)
                LL=Label(sep, text="금", font=('휴먼엑스포', 15))
                LL.place(x=425, y=65)
                LL=Label(sep, text="토", fg="blue", font=('휴먼엑스포', 15))
                LL.place(x=505, y=65)

                def sep1ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    sepL.configure(text="1일에 할일: {}".format(con[243]))
                    f.close
                    

                    def sep1sa():
                        od=test.get()
                        test.delete(0,END)
                        con[243]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        sepL.configure(text="1일에 할일: {}".format(con[243]))
                        
                    sepb=Button(sep,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=sep1sa)
                    sepb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(sep, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def sep2ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    sepL.configure(text="2일에 할일: {}".format(con[244]))
                    f.close
                    

                    def sep2sa():
                        od=test.get()
                        test.delete(0,END)
                        con[244]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        sepL.configure(text="2일에 할일: {}".format(con[244]))
                        
                    sepb=Button(sep,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=sep2sa)
                    sepb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(sep, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def sep3ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    sepL.configure(text="3일에 할일: {}".format(con[245]))
                    f.close
                    

                    def sep3sa():
                        od=test.get()
                        test.delete(0,END)
                        con[245]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        sepL.configure(text="3일에 할일: {}".format(con[245]))
                        
                    sepb=Button(sep,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=sep3sa)
                    sepb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(sep, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def sep4ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    sepL.configure(text="4일에 할일: {}".format(con[246]))
                    f.close
                    

                    def sep4sa():
                        od=test.get()
                        test.delete(0,END)
                        con[246]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        sepL.configure(text="4일에 할일: {}".format(con[246]))
                        
                    sepb=Button(sep,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=sep4sa)
                    sepb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(sep, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def sep5ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    sepL.configure(text="5일에 할일: {}".format(con[247]))
                    f.close
                    

                    def sep5sa():
                        od=test.get()
                        test.delete(0,END)
                        con[247]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        sepL.configure(text="5일에 할일: {}".format(con[247]))
                        
                    sepb=Button(sep,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=sep5sa)
                    sepb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(sep, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def sep6ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    sepL.configure(text="6일에 할일: {}".format(con[248]))
                    f.close
                    

                    def sep6sa():
                        od=test.get()
                        test.delete(0,END)
                        con[248]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        sepL.configure(text="6일에 할일: {}".format(con[248]))
                        
                    sepb=Button(sep,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=sep6sa)
                    sepb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(sep, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def sep7ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    sepL.configure(text="7일에 할일: {}".format(con[249]))
                    f.close
                    

                    def sep7sa():
                        od=test.get()
                        test.delete(0,END)
                        con[249]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        sepL.configure(text="7일에 할일: {}".format(con[249]))
                        
                    sepb=Button(sep,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=sep7sa)
                    sepb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(sep, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def sep8ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    sepL.configure(text="8일에 할일: {}".format(con[250]))
                    f.close
                    

                    def sep8sa():
                        od=test.get()
                        test.delete(0,END)
                        con[250]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        sepL.configure(text="8일에 할일: {}".format(con[250]))
                        
                    sepb=Button(sep,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=sep8sa)
                    sepb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(sep, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def sep9ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    sepL.configure(text="9일에 할일: {}".format(con[251]))
                    f.close
                    

                    def sep9sa():
                        od=test.get()
                        test.delete(0,END)
                        con[251]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        sepL.configure(text="9일에 할일: {}".format(con[251]))
                        
                    sepb=Button(sep,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=sep9sa)
                    sepb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(sep, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def sep10ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    sepL.configure(text="10일에 할일: {}".format(con[252]))
                    f.close
                    

                    def sep10sa():
                        od=test.get()
                        test.delete(0,END)
                        con[252]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        sepL.configure(text="10일에 할일: {}".format(con[252]))
                        
                    sepb=Button(sep,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=sep10sa)
                    sepb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(sep, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)
            
                def sep11ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    sepL.configure(text="11일에 할일: {}".format(con[253]))
                    f.close
                    

                    def sep11sa():
                        od=test.get()
                        test.delete(0,END)
                        con[253]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        sepL.configure(text="11일에 할일: {}".format(con[253]))
                        
                    sepb=Button(sep,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=sep11sa)
                    sepb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(sep, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def sep12ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    sepL.configure(text="12일에 할일: {}".format(con[254]))
                    f.close
                    al=Tk()
                    al.geometry('150x100')
                    al.title("공휴일 알림")
                    alL=Label(al, text="추석연휴", font=("휴먼엑스포", 15), fg="red")
                    alL.place(x=20, y=30)

                    def 종료():
                        al.destroy()

                    alB=Button(al, text="닫기", width=0, height=0, font=(10), command=종료)
                    alB.place(x=40, y=60)

                    def sep12sa():
                        od=test.get()
                        test.delete(0,END)
                        con[254]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        sepL.configure(text="12일에 할일: {}".format(con[254]))
                        
                    sepb=Button(sep,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=sep12sa)
                    sepb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(sep, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def sep13ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    sepL.configure(text="13일에 할일: {}".format(con[255]))
                    f.close
                    al=Tk()
                    al.geometry('150x100')
                    al.title("공휴일 알림")
                    alL=Label(al, text="추석연휴", font=("휴먼엑스포", 15), fg="red")
                    alL.place(x=20, y=30)

                    def 종료():
                        al.destroy()

                    alB=Button(al, text="닫기", width=0, height=0, font=(10), command=종료)
                    alB.place(x=40, y=60)
                    

                    def sep13sa():
                        od=test.get()
                        test.delete(0,END)
                        con[255]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        sepL.configure(text="13일에 할일: {}".format(con[255]))
                        
                    sepb=Button(sep,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=sep13sa)
                    sepb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(sep, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)
                    
                def sep14ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    sepL.configure(text="14일에 할일: {}".format(con[256]))
                    f.close
                    al=Tk()
                    al.geometry('150x100')
                    al.title("공휴일 알림")
                    alL=Label(al, text="추석연휴", font=("휴먼엑스포", 15), fg="red")
                    alL.place(x=20, y=30)

                    def 종료():
                        al.destroy()

                    alB=Button(al, text="닫기", width=0, height=0, font=(10), command=종료)
                    alB.place(x=40, y=60)
                    

                    def sep14sa():
                        od=test.get()
                        test.delete(0,END)
                        con[256]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        sepL.configure(text="14일에 할일: {}".format(con[256]))
                        
                    sepb=Button(sep,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=sep14sa)
                    sepb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(sep, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def sep15ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    sepL.configure(text="15일에 할일: {}".format(con[257]))
                    f.close
                    

                    def sep15sa():
                        od=test.get()
                        test.delete(0,END)
                        con[257]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        sepL.configure(text="15일에 할일: {}".format(con[257]))
                        
                    sepb=Button(sep,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=sep15sa)
                    sepb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(sep, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def sep16ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    sepL.configure(text="16일에 할일: {}".format(con[258]))
                    f.close
                    

                    def sep16sa():
                        od=test.get()
                        test.delete(0,END)
                        con[258]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        sepL.configure(text="16일에 할일: {}".format(con[258]))
                        
                    sepb=Button(sep,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=sep16sa)
                    sepb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(sep, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def sep17ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    sepL.configure(text="17일에 할일: {}".format(con[259]))
                    f.close
                    

                    def sep17sa():
                        od=test.get()
                        test.delete(0,END)
                        con[259]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        sepL.configure(text="17일에 할일: {}".format(con[259]))
                        
                    sepb=Button(sep,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=sep17sa)
                    sepb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(sep, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)


                def sep18ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    sepL.configure(text="18일에 할일: {}".format(con[260]))
                    f.close
                    

                    def sep18sa():
                        od=test.get()
                        test.delete(0,END)
                        con[260]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        sepL.configure(text="18일에 할일: {}".format(con[260]))
                        
                    sepb=Button(sep,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=sep18sa)
                    sepb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(sep, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def sep19ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    sepL.configure(text="19일에 할일: {}".format(con[261]))
                    f.close
                    

                    def sep19sa():
                        od=test.get()
                        test.delete(0,END)
                        con[261]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        sepL.configure(text="19일에 할일: {}".format(con[261]))
                        
                    sepb=Button(sep,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=sep19sa)
                    sepb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(sep, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def sep20ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    sepL.configure(text="20일에 할일: {}".format(con[262]))
                    f.close
                    

                    def sep20sa():
                        od=test.get()
                        test.delete(0,END)
                        con[262]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        sepL.configure(text="20일에 할일: {}".format(con[262]))
                        
                    sepb=Button(sep,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=sep20sa)
                    sepb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(sep, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def sep21ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    sepL.configure(text="21일에 할일: {}".format(con[263]))
                    f.close
                    

                    def sep21sa():
                        od=test.get()
                        test.delete(0,END)
                        con[263]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        sepL.configure(text="21일에 할일: {}".format(con[263]))
                        
                    sepb=Button(sep,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=sep21sa)
                    sepb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(sep, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def sep22ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    sepL.configure(text="22일에 할일: {}".format(con[264]))
                    f.close
                    

                    def sep22sa():
                        od=test.get()
                        test.delete(0,END)
                        con[264]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        sepL.configure(text="22일에 할일: {}".format(con[264]))
                        
                    sepb=Button(sep,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=sep22sa)
                    sepb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(sep, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)
                    
                def sep23ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    sepL.configure(text="23일에 할일: {}".format(con[265]))
                    f.close
                    

                    def sep23sa():
                        od=test.get()
                        test.delete(0,END)
                        con[265]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        sepL.configure(text="23일에 할일: {}".format(con[265]))
                        
                    sepb=Button(sep,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=sep23sa)
                    sepb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(sep, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def sep24ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    sepL.configure(text="24일에 할일: {}".format(con[266]))
                    f.close
                    

                    def sep24sa():
                        od=test.get()
                        test.delete(0,END)
                        con[266]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        sepL.configure(text="24일에 할일: {}".format(con[266]))
                        
                    sepb=Button(sep,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=sep24sa)
                    sepb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(sep, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def sep25ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    sepL.configure(text="25일에 할일: {}".format(con[267]))
                    f.close
                    al=Tk()
                    al.geometry('300x100')
                    al.title("공휴일 알림")
                    alL=Label(al, text="성균관대학교 개교기념일", font=("휴먼엑스포", 15), fg="green")
                    alL.place(x=20, y=30)

                    def 종료():
                        al.destroy()

                    alB=Button(al, text="닫기", width=0, height=0, font=(10), command=종료)
                    alB.place(x=40, y=60)
                    

                    def sep25sa():
                        od=test.get()
                        test.delete(0,END)
                        con[267]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        sepL.configure(text="25일에 할일: {}".format(con[267]))
                        
                    sepb=Button(sep,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=sep25sa)
                    sepb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(sep, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def sep26ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    sepL.configure(text="26일에 할일: {}".format(con[268]))
                    f.close
                    

                    def sep26sa():
                        od=test.get()
                        test.delete(0,END)
                        con[268]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        sepL.configure(text="26일에 할일: {}".format(con[268]))
                        
                    sepb=Button(sep,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=sep26sa)
                    sepb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(sep, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def sep27ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    sepL.configure(text="27일에 할일: {}".format(con[269]))
                    f.close
                    

                    def sep27sa():
                        od=test.get()
                        test.delete(0,END)
                        con[269]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        sepL.configure(text="27일에 할일: {}".format(con[269]))
                        
                    sepb=Button(sep,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=sep27sa)
                    sepb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(sep, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)
                    
                def sep28ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    sepL.configure(text="28일에 할일: {}".format(con[270]))
                    f.close
                    al=Tk()
                    al.geometry('200x100')
                    al.title("공휴일 알림")
                    alL=Label(al, text="공부자탄강일", font=("휴먼엑스포", 15), fg="green")
                    alL.place(x=20, y=30)

                    def 종료():
                        al.destroy()

                    alB=Button(al, text="닫기", width=0, height=0, font=(10), command=종료)
                    alB.place(x=40, y=60)
                    

                    def sep28sa():
                        od=test.get()
                        test.delete(0,END)
                        con[270]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        sepL.configure(text="28일에 할일: {}".format(con[270]))
                        
                    sepb=Button(sep,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=sep28sa)
                    sepb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(sep, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)
                    
                def sep29ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    sepL.configure(text="29일에 할일: {}".format(con[271]))
                    f.close
                    

                    def sep29sa():
                        od=test.get()
                        test.delete(0,END)
                        con[271]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        sepL.configure(text="29일에 할일: {}".format(con[271]))
                        
                    sepb=Button(sep,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=sep29sa)
                    sepb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(sep, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)
                    
                def sep30ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    sepL.configure(text="30일에 할일: {}".format(con[272]))
                    f.close
                    

                    def sep30sa():
                        od=test.get()
                        test.delete(0,END)
                        con[272]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        sepL.configure(text="30일에 할일: {}".format(con[272]))
                        
                    sepb=Button(sep,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=sep30sa)
                    sepb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(sep, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)
                    
                sep1b=Button(sep,text="1", width=0, height=0, font=('휴먼엑스포', 20), command=sep1ex)
                sep1b.place(x=20,y=100)

                sep2b=Button(sep,text="2", width=0, height=0, font=('휴먼엑스포', 20), command=sep2ex)
                sep2b.place(x=100,y=100)

                sep3b=Button(sep,text="3", width=0, height=0, font=('휴먼엑스포', 20), command=sep3ex)
                sep3b.place(x=180,y=100)

                sep4b=Button(sep,text="4", width=0, height=0, font=('휴먼엑스포', 20), command=sep4ex)
                sep4b.place(x=260,y=100)

                sep5b=Button(sep,text="5", width=0, height=0, font=('휴먼엑스포', 20), command=sep5ex)
                sep5b.place(x=340,y=100)

                sep6b=Button(sep,text="6", width=0, height=0, font=('휴먼엑스포', 20), command=sep6ex)
                sep6b.place(x=420,y=100)

                sep7b=Button(sep,text="7", width=0, height=0, font=('휴먼엑스포', 20), command=sep7ex)
                sep7b.place(x=500,y=100)

                sep8b=Button(sep,text="8", width=0, height=0, font=('휴먼엑스포', 20), command=sep8ex)
                sep8b.place(x=20,y=200)

                sep9b=Button(sep,text="9", width=0, height=0, font=('휴먼엑스포', 20), command=sep9ex)
                sep9b.place(x=100,y=200)

                sep10b=Button(sep,text="10", width=0, height=0, font=('휴먼엑스포', 20), command=sep10ex)
                sep10b.place(x=180,y=200)

                sep11b=Button(sep,text="11", width=0, height=0, font=('휴먼엑스포', 20), command=sep11ex)
                sep11b.place(x=260,y=200)

                sep12b=Button(sep,text="12",fg="red", width=0, height=0, font=('휴먼엑스포', 20), command=sep12ex)
                sep12b.place(x=340,y=200)

                sep13b=Button(sep,text="13",fg="red", width=0, height=0, font=('휴먼엑스포', 20), command=sep13ex)
                sep13b.place(x=420,y=200)

                sep14b=Button(sep,text="14",fg="red", width=0, height=0, font=('휴먼엑스포', 20), command=sep14ex)
                sep14b.place(x=500,y=200)

                sep15b=Button(sep,text="15", width=0, height=0, font=('휴먼엑스포', 20), command=sep15ex)
                sep15b.place(x=20,y=300)

                sep16b=Button(sep,text="16", width=0, height=0, font=('휴먼엑스포', 20), command=sep16ex)
                sep16b.place(x=100,y=300)

                sep17b=Button(sep,text="17", width=0, height=0, font=('휴먼엑스포', 20), command=sep17ex)
                sep17b.place(x=180,y=300)

                sep18b=Button(sep,text="18", width=0, height=0, font=('휴먼엑스포', 20), command=sep18ex)
                sep18b.place(x=260,y=300)

                sep19b=Button(sep,text="19", width=0, height=0, font=('휴먼엑스포', 20), command=sep19ex)
                sep19b.place(x=340,y=300)

                sep20b=Button(sep,text="20", width=0, height=0, font=('휴먼엑스포', 20), command=sep20ex)
                sep20b.place(x=420,y=300)

                sep21b=Button(sep,text="21", width=0, height=0, font=('휴먼엑스포', 20), command=sep21ex)
                sep21b.place(x=500,y=300)
                
                sep22b=Button(sep,text="22", width=0, height=0, font=('휴먼엑스포', 20), command=sep22ex)
                sep22b.place(x=20,y=400)

                sep23b=Button(sep,text="23", width=0, height=0, font=('휴먼엑스포', 20), command=sep23ex)
                sep23b.place(x=100,y=400)

                sep24b=Button(sep,text="24", width=0, height=0, font=('휴먼엑스포', 20), command=sep24ex)
                sep24b.place(x=180,y=400)

                sep25b=Button(sep,text="25",fg="green", width=0, height=0, font=('휴먼엑스포', 20), command=sep25ex)
                sep25b.place(x=260,y=400)

                sep26b=Button(sep,text="26", width=0, height=0, font=('휴먼엑스포', 20), command=sep26ex)
                sep26b.place(x=340,y=400)

                sep27b=Button(sep,text="27", width=0, height=0, font=('휴먼엑스포', 20), command=sep27ex)
                sep27b.place(x=420,y=400)

                sep28b=Button(sep,text="28",fg="green", width=0, height=0, font=('휴먼엑스포', 20), command=sep28ex)
                sep28b.place(x=500,y=400)

                sep29b=Button(sep,text="29", width=0, height=0, font=('휴먼엑스포', 20), command=sep29ex)
                sep29b.place(x=20,y=500)

                sep30b=Button(sep,text="30", width=0, height=0, font=('휴먼엑스포', 20), command=sep30ex)
                sep30b.place(x=100,y=500)

                def 월간9():
                    toj=Tk()
                    toj.title("9월 총 계획")
                    toj.geometry('700x700')

                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    f.close
                    
                    for i in range(243,273):
                        tojL=Label(toj, text="9월 {}일:{}".format(i-242,con[i]), font=('휴먼엑스포', 15))
                        tojL.place(x=0,y=(i-243)*20)
                        
                    
                tojb=Button(sep, text="월간", height=0, font=('휴먼엑스포', 20), command=월간9)   
                tojb.place(x=450,y=500)
                
            sepb=Button(cal, text="9월", width=4, height=2, fg='dark blue', font=('휴먼엑스포', 20), command=sep)   
            sepb.place(x=410,y=340)


            def oct():
                oct=Tk()
                oct.title("10월 달력")
                oct.geometry('700x600')
                octL=Label(oct, text="", font=('휴먼엑스포', 20))
                octL.place(x=350,y=0)

                LL=Label(oct, text="10월 달력", font=('휴먼엑스포', 20))
                LL.place(x=0, y=0)

                LL=Label(oct, text="일", fg="red", font=('휴먼엑스포', 15))
                LL.place(x=25, y=65)
                LL=Label(oct, text="월", font=('휴먼엑스포', 15))
                LL.place(x=105, y=65)
                LL=Label(oct, text="화", font=('휴먼엑스포', 15))
                LL.place(x=185, y=65)
                LL=Label(oct, text="수", font=('휴먼엑스포', 15))
                LL.place(x=265, y=65)
                LL=Label(oct, text="목", font=('휴먼엑스포', 15))
                LL.place(x=345, y=65)
                LL=Label(oct, text="금", font=('휴먼엑스포', 15))
                LL.place(x=425, y=65)
                LL=Label(oct, text="토", fg="blue", font=('휴먼엑스포', 15))
                LL.place(x=505, y=65)

                def oct1ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    octL.configure(text="1일에 할일: {}".format(con[273]))
                    f.close
                    

                    def oct1sa():
                        od=test.get()
                        test.delete(0,END)
                        con[273]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        octL.configure(text="1일에 할일: {}".format(con[273]))


                    octb=Button(oct,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=oct1sa)
                    octb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(oct, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def oct2ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    octL.configure(text="2일에 할일: {}".format(con[274]))
                    f.close
                    

                    def oct2sa():
                        od=test.get()
                        test.delete(0,END)
                        con[274]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        octL.configure(text="2일에 할일: {}".format(con[274]))


                    octb=Button(oct,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=oct2sa)
                    octb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(oct, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def oct3ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    octL.configure(text="3일에 할일: {}".format(con[275]))
                    f.close
                    al=Tk()
                    al.geometry('150x100')
                    al.title("공휴일 알림")
                    alL=Label(al, text="개천절", font=("휴먼엑스포", 15), fg="red")
                    alL.place(x=20, y=30)

                    def 종료():
                        al.destroy()

                    alB=Button(al, text="닫기", width=0, height=0, font=(10), command=종료)
                    alB.place(x=40, y=60)
                    

                    def oct3sa():
                        od=test.get()
                        test.delete(0,END)
                        con[275]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        octL.configure(text="3일에 할일: {}".format(con[275]))


                    octb=Button(oct,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=oct3sa)
                    octb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(oct, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)
                    
                def oct4ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    octL.configure(text="4일에 할일: {}".format(con[276]))
                    f.close
                    

                    def oct4sa():
                        od=test.get()
                        test.delete(0,END)
                        con[276]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        octL.configure(text="4일에 할일: {}".format(con[276]))


                    octb=Button(oct,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=oct4sa)
                    octb.place(x=250,y=10)
                    
                    txt=StringVar()
                    test=Entry(oct, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def oct5ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    octL.configure(text="5일에 할일: {}".format(con[277]))
                    f.close
                    

                    def oct5sa():
                        od=test.get()
                        test.delete(0,END)
                        con[277]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        octL.configure(text="5일에 할일: {}".format(con[277]))


                    octb=Button(oct,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=oct5sa)
                    octb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(oct, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)
                    
                def oct6ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    octL.configure(text="6일에 할일: {}".format(con[278]))
                    f.close
                    

                    def oct6sa():
                        od=test.get()
                        test.delete(0,END)
                        con[278]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        octL.configure(text="6일에 할일: {}".format(con[278]))


                    octb=Button(oct,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=oct6sa)
                    octb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(oct, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def oct7ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    octL.configure(text="7일에 할일: {}".format(con[279]))
                    f.close
                    

                    def oct7sa():
                        od=test.get()
                        test.delete(0,END)
                        con[279]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        octL.configure(text="7일에 할일: {}".format(con[279]))


                    octb=Button(oct,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=oct7sa)
                    octb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(oct, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                    
                def oct8ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    octL.configure(text="8일에 할일: {}".format(con[280]))
                    f.close
                    

                    def oct8sa():
                        od=test.get()
                        test.delete(0,END)
                        con[280]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        octL.configure(text="8일에 할일: {}".format(con[280]))


                    octb=Button(oct,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=oct8sa)
                    octb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(oct, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def oct9ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    octL.configure(text="9일에 할일: {}".format(con[281]))
                    f.close
                    al=Tk()
                    al.geometry('150x100')
                    al.title("공휴일 알림")
                    alL=Label(al, text="한글날", font=("휴먼엑스포", 15), fg="red")
                    alL.place(x=20, y=30)

                    def 종료():
                        al.destroy()

                    alB=Button(al, text="닫기", width=0, height=0, font=(10), command=종료)
                    alB.place(x=40, y=60)
                    

                    def oct9sa():
                        od=test.get()
                        test.delete(0,END)
                        con[281]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        octL.configure(text="9일에 할일: {}".format(con[281]))


                    octb=Button(oct,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=oct9sa)
                    octb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(oct, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def oct10ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    octL.configure(text="10일에 할일: {}".format(con[282]))
                    f.close
                    

                    def oct10sa():
                        od=test.get()
                        test.delete(0,END)
                        con[282]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        octL.configure(text="10일에 할일: {}".format(con[282]))


                    octb=Button(oct,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=oct10sa)
                    octb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(oct, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def oct11ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    octL.configure(text="11일에 할일: {}".format(con[283]))
                    f.close
                    

                    def oct11sa():
                        od=test.get()
                        test.delete(0,END)
                        con[283]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        octL.configure(text="11일에 할일: {}".format(con[283]))


                    octb=Button(oct,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=oct9sa)
                    octb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(oct, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)


                    octb=Button(oct,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=oct11sa)
                    octb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(oct, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def oct12ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    octL.configure(text="12일에 할일: {}".format(con[284]))
                    f.close
                    

                    def oct12sa():
                        od=test.get()
                        test.delete(0,END)
                        con[284]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        octL.configure(text="12일에 할일: {}".format(con[284]))


                    octb=Button(oct,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=oct12sa)
                    octb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(oct, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)


                def oct13ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    octL.configure(text="13일에 할일: {}".format(con[285]))
                    f.close
                    

                    def oct13sa():
                        od=test.get()
                        test.delete(0,END)
                        con[285]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        octL.configure(text="13일에 할일: {}".format(con[285]))


                    octb=Button(oct,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=oct13sa)
                    octb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(oct, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def oct14ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    octL.configure(text="14일에 할일: {}".format(con[286]))
                    f.close
                    

                    def oct14sa():
                        od=test.get()
                        test.delete(0,END)
                        con[286]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        octL.configure(text="14일에 할일: {}".format(con[286]))


                    octb=Button(oct,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=oct14sa)
                    octb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(oct, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)
                    

                def oct15ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    octL.configure(text="15일에 할일: {}".format(con[287]))
                    f.close
                    

                    def oct15sa():
                        od=test.get()
                        test.delete(0,END)
                        con[287]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        octL.configure(text="15일에 할일: {}".format(con[287]))


                    octb=Button(oct,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=oct15sa)
                    octb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(oct, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def oct16ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    octL.configure(text="15일에 할일: {}".format(con[288]))
                    f.close
                    

                    def oct16sa():
                        od=test.get()
                        test.delete(0,END)
                        con[288]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        octL.configure(text="16일에 할일: {}".format(con[288]))


                    octb=Button(oct,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=oct16sa)
                    octb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(oct, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def oct17ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    octL.configure(text="17일에 할일: {}".format(con[289]))
                    f.close
                    

                    def oct17sa():
                        od=test.get()
                        test.delete(0,END)
                        con[289]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        octL.configure(text="17일에 할일: {}".format(con[289]))


                    octb=Button(oct,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=oct17sa)
                    octb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(oct, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def oct18ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    octL.configure(text="18일에 할일: {}".format(con[290]))
                    f.close
                    

                    def oct18sa():
                        od=test.get()
                        test.delete(0,END)
                        con[290]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        octL.configure(text="18일에 할일: {}".format(con[290]))


                    octb=Button(oct,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=oct18sa)
                    octb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(oct, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def oct19ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    octL.configure(text="19일에 할일: {}".format(con[291]))
                    f.close
                    

                    def oct19sa():
                        od=test.get()
                        test.delete(0,END)
                        con[291]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        octL.configure(text="19일에 할일: {}".format(con[291]))


                    octb=Button(oct,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=oct19sa)
                    octb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(oct, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def oct20ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    octL.configure(text="20일에 할일: {}".format(con[292]))
                    f.close
                    

                    def oct20sa():
                        od=test.get()
                        test.delete(0,END)
                        con[292]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        octL.configure(text="20일에 할일: {}".format(con[292]))


                    octb=Button(oct,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=oct20sa)
                    octb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(oct, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def oct21ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    octL.configure(text="21일에 할일: {}".format(con[293]))
                    f.close
                    

                    def oct21sa():
                        od=test.get()
                        test.delete(0,END)
                        con[293]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        octL.configure(text="21일에 할일: {}".format(con[293]))


                    octb=Button(oct,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=oct21sa)
                    octb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(oct, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def oct22ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    octL.configure(text="22일에 할일: {}".format(con[294]))
                    f.close
                    

                    def oct22sa():
                        od=test.get()
                        test.delete(0,END)
                        con[294]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        octL.configure(text="22일에 할일: {}".format(con[294]))


                    octb=Button(oct,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=oct22sa)
                    octb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(oct, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def oct23ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    octL.configure(text="23일에 할일: {}".format(con[295]))
                    f.close
                    

                    def oct23sa():
                        od=test.get()
                        test.delete(0,END)
                        con[295]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        octL.configure(text="23일에 할일: {}".format(con[295]))


                    octb=Button(oct,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=oct23sa)
                    octb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(oct, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def oct24ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    octL.configure(text="24일에 할일: {}".format(con[296]))
                    f.close
                    

                    def oct24sa():
                        od=test.get()
                        test.delete(0,END)
                        con[296]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        octL.configure(text="24일에 할일: {}".format(con[296]))


                    octb=Button(oct,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=oct24sa)
                    octb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(oct, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def oct25ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    octL.configure(text="25일에 할일: {}".format(con[297]))
                    f.close
                    

                    def oct25sa():
                        od=test.get()
                        test.delete(0,END)
                        con[297]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        octL.configure(text="25일에 할일: {}".format(con[297]))


                    octb=Button(oct,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=oct25sa)
                    octb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(oct, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def oct26ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    octL.configure(text="26일에 할일: {}".format(con[298]))
                    f.close
                    

                    def oct26sa():
                        od=test.get()
                        test.delete(0,END)
                        con[298]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        octL.configure(text="26일에 할일: {}".format(con[298]))


                    octb=Button(oct,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=oct26sa)
                    octb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(oct, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)
                    
                def oct27ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    octL.configure(text="27일에 할일: {}".format(con[299]))
                    f.close
                    

                    def oct15sa():
                        od=test.get()
                        test.delete(0,END)
                        con[299]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        octL.configure(text="27일에 할일: {}".format(con[299]))


                    octb=Button(oct,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=oct27sa)
                    octb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(oct, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)
                    
                def oct28ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    octL.configure(text="28일에 할일: {}".format(con[300]))
                    f.close
                    

                    def oct28sa():
                        od=test.get()
                        test.delete(0,END)
                        con[300]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        octL.configure(text="28일에 할일: {}".format(con[300]))
                        
                    octb=Button(oct,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=oct28sa)
                    octb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(oct, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def oct29ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    octL.configure(text="29일에 할일: {}".format(con[301]))
                    f.close
                    

                    def oct29sa():
                        od=test.get()
                        test.delete(0,END)
                        con[301]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        octL.configure(text="29일에 할일: {}".format(con[301]))


                    octb=Button(oct,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=oct29sa)
                    octb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(oct, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def oct30ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    octL.configure(text="30일에 할일: {}".format(con[302]))
                    f.close
                    

                    def oct30sa():
                        od=test.get()
                        test.delete(0,END)
                        con[302]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        octL.configure(text="30일에 할일: {}".format(con[302]))


                    octb=Button(oct,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=oct30sa)
                    octb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(oct, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def oct31ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    octL.configure(text="31일에 할일: {}".format(con[303]))
                    f.close
                    

                    def oct31sa():
                        od=test.get()
                        test.delete(0,END)
                        con[303]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        octL.configure(text="31일에 할일: {}".format(con[303]))


                    octb=Button(oct,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=oct31sa)
                    octb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(oct, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                oct1b=Button(oct,text="1", width=0, height=0, font=('휴먼엑스포', 20), command=oct1ex)
                oct1b.place(x=180,y=100)

                oct2b=Button(oct,text="2", width=0, height=0, font=('휴먼엑스포', 20), command=oct2ex)
                oct2b.place(x=260,y=100)

                oct3b=Button(oct,text="3",fg="red", width=0, height=0, font=('휴먼엑스포', 20), command=oct3ex)
                oct3b.place(x=340,y=100)

                oct4b=Button(oct,text="4", width=0, height=0, font=('휴먼엑스포', 20), command=oct4ex)
                oct4b.place(x=420,y=100)

                oct5b=Button(oct,text="5", width=0, height=0, font=('휴먼엑스포', 20), command=oct5ex)
                oct5b.place(x=500,y=100)

                oct6b=Button(oct,text="6", width=0, height=0, font=('휴먼엑스포', 20), command=oct6ex)
                oct6b.place(x=20,y=200)

                oct7b=Button(oct,text="7", width=0, height=0, font=('휴먼엑스포', 20), command=oct7ex)
                oct7b.place(x=100,y=200)

                oct8b=Button(oct,text="8", width=0, height=0, font=('휴먼엑스포', 20), command=oct8ex)
                oct8b.place(x=180,y=200)

                oct9b=Button(oct,text="9",fg="red", width=0, height=0, font=('휴먼엑스포', 20), command=oct9ex)
                oct9b.place(x=260,y=200)

                oct10b=Button(oct,text="10", width=0, height=0, font=('휴먼엑스포', 20), command=oct10ex)
                oct10b.place(x=340,y=200)

                oct11b=Button(oct,text="11", width=0, height=0, font=('휴먼엑스포', 20), command=oct11ex)
                oct11b.place(x=420,y=200)

                oct12b=Button(oct,text="12", width=0, height=0, font=('휴먼엑스포', 20), command=oct12ex)
                oct12b.place(x=500,y=200)

                oct13b=Button(oct,text="13", width=0, height=0, font=('휴먼엑스포', 20), command=oct13ex)
                oct13b.place(x=20,y=300)

                oct14b=Button(oct,text="14", width=0, height=0, font=('휴먼엑스포', 20), command=oct14ex)
                oct14b.place(x=100,y=300)

                oct15b=Button(oct,text="15", width=0, height=0, font=('휴먼엑스포', 20), command=oct15ex)
                oct15b.place(x=180,y=300)

                oct16b=Button(oct,text="16", width=0, height=0, font=('휴먼엑스포', 20), command=oct16ex)
                oct16b.place(x=260,y=300)

                oct17b=Button(oct,text="17", width=0, height=0, font=('휴먼엑스포', 20), command=oct17ex)
                oct17b.place(x=340,y=300)

                oct18b=Button(oct,text="18", width=0, height=0, font=('휴먼엑스포', 20), command=oct18ex)
                oct18b.place(x=420,y=300)

                oct19b=Button(oct,text="19", width=0, height=0, font=('휴먼엑스포', 20), command=oct19ex)
                oct19b.place(x=500,y=300)

                oct20b=Button(oct,text="20", width=0, height=0, font=('휴먼엑스포', 20), command=oct20ex)
                oct20b.place(x=20,y=400)

                oct21b=Button(oct,text="21", width=0, height=0, font=('휴먼엑스포', 20), command=oct21ex)
                oct21b.place(x=100,y=400)

                oct22b=Button(oct,text="22", width=0, height=0, font=('휴먼엑스포', 20), command=oct22ex)
                oct22b.place(x=180,y=400)

                oct23b=Button(oct,text="23", width=0, height=0, font=('휴먼엑스포', 20), command=oct23ex)
                oct23b.place(x=260,y=400)

                oct24b=Button(oct,text="24", width=0, height=0, font=('휴먼엑스포', 20), command=oct24ex)
                oct24b.place(x=340,y=400)

                oct25b=Button(oct,text="25", width=0, height=0, font=('휴먼엑스포', 20), command=oct25ex)
                oct25b.place(x=420,y=400)

                oct26b=Button(oct,text="26", width=0, height=0, font=('휴먼엑스포', 20), command=oct26ex)
                oct26b.place(x=500,y=400)

                oct27b=Button(oct,text="27", width=0, height=0, font=('휴먼엑스포', 20), command=oct27ex)
                oct27b.place(x=20,y=500)

                oct28b=Button(oct,text="28", width=0, height=0, font=('휴먼엑스포', 20), command=oct28ex)
                oct28b.place(x=100,y=500)

                oct29b=Button(oct,text="29", width=0, height=0, font=('휴먼엑스포', 20), command=oct29ex)
                oct29b.place(x=180,y=500)

                oct30b=Button(oct,text="30", width=0, height=0, font=('휴먼엑스포', 20), command=oct30ex)
                oct30b.place(x=260,y=500)

                oct31b=Button(oct,text="31", width=0, height=0, font=('휴먼엑스포', 20), command=oct31ex)
                oct31b.place(x=340,y=500)

                def 월간10():
                    toj=Tk()
                    toj.title("10월 총 계획")
                    toj.geometry('700x700')

                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    f.close
                    
                    for i in range(273,304):
                        tojL=Label(toj, text="10월 {}일:{}".format(i-272,con[i]), font=('휴먼엑스포', 15))
                        tojL.place(x=0,y=(i-273)*20)
                        
                    
                tojb=Button(oct, text="월간", height=0, font=('휴먼엑스포', 20), command=월간10)   
                tojb.place(x=450,y=500)
                


            octb=Button(cal, text="10월", width=4, height=2, fg='white', font=('휴먼엑스포', 20), command=oct)   
            octb.place(x=110,y=450)

            
            def nov():
                nov=Tk()
                nov.title("11월 달력")
                nov.geometry('700x600')
                novL=Label(nov, text="", font=('휴먼엑스포', 20))
                novL.place(x=350,y=0)

                LL=Label(nov, text="11월 달력", font=('휴먼엑스포', 20))
                LL.place(x=0, y=0)

                LL=Label(nov, text="일", fg="red", font=('휴먼엑스포', 15))
                LL.place(x=25, y=65)
                LL=Label(nov, text="월", font=('휴먼엑스포', 15))
                LL.place(x=105, y=65)
                LL=Label(nov, text="화", font=('휴먼엑스포', 15))
                LL.place(x=185, y=65)
                LL=Label(nov, text="수", font=('휴먼엑스포', 15))
                LL.place(x=265, y=65)
                LL=Label(nov, text="목", font=('휴먼엑스포', 15))
                LL.place(x=345, y=65)
                LL=Label(nov, text="금", font=('휴먼엑스포', 15))
                LL.place(x=425, y=65)
                LL=Label(nov, text="토", fg="blue", font=('휴먼엑스포', 15))
                LL.place(x=505, y=65)

                def nov1ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    novL.configure(text="1일에 할일: {}".format(con[304]))
                    f.close
                    

                    def nov1sa():
                        od=test.get()
                        test.delete(0,END)
                        con[304]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        novL.configure(text="1일에 할일: {}".format(con[304]))
                        
                    novb=Button(nov,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=nov1sa)
                    novb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(nov, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def nov2ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    novL.configure(text="2일에 할일: {}".format(con[305]))
                    f.close
                    

                    def nov2sa():
                        od=test.get()
                        test.delete(0,END)
                        con[305]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        novL.configure(text="2일에 할일: {}".format(con[305]))
                        
                    novb=Button(nov,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=nov2sa)
                    novb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(nov, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def nov3ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    novL.configure(text="3일에 할일: {}".format(con[306]))
                    f.close
                    

                    def nov3sa():
                        od=test.get()
                        test.delete(0,END)
                        con[306]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        novL.configure(text="3일에 할일: {}".format(con[306]))
                        
                    novb=Button(nov,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=nov3sa)
                    novb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(nov, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def nov4ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    novL.configure(text="4일에 할일: {}".format(con[307]))
                    f.close
                    

                    def nov4sa():
                        od=test.get()
                        test.delete(0,END)
                        con[307]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        novL.configure(text="4일에 할일: {}".format(con[307]))
                        
                    novb=Button(nov,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=nov4sa)
                    novb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(nov, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def nov5ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    novL.configure(text="5일에 할일: {}".format(con[308]))
                    f.close
                    

                    def nov5sa():
                        od=test.get()
                        test.delete(0,END)
                        con[308]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        novL.configure(text="5일에 할일: {}".format(con[308]))
                        
                    novb=Button(nov,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=nov5sa)
                    novb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(nov, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def nov6ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    novL.configure(text="6일에 할일: {}".format(con[309]))
                    f.close
                    

                    def nov6sa():
                        od=test.get()
                        test.delete(0,END)
                        con[309]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        novL.configure(text="6일에 할일: {}".format(con[309]))
                        
                    novb=Button(nov,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=nov6sa)
                    novb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(nov, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def nov7ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    novL.configure(text="7일에 할일: {}".format(con[310]))
                    f.close
                    

                    def nov7sa():
                        od=test.get()
                        test.delete(0,END)
                        con[310]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        novL.configure(text="7일에 할일: {}".format(con[310]))
                        
                    novb=Button(nov,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=nov7sa)
                    novb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(nov, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def nov8ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    novL.configure(text="8일에 할일: {}".format(con[311]))
                    f.close
                    

                    def nov8sa():
                        od=test.get()
                        test.delete(0,END)
                        con[311]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        novL.configure(text="8일에 할일: {}".format(con[311]))
                        
                    novb=Button(nov,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=nov8sa)
                    novb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(nov, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def nov9ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    novL.configure(text="9일에 할일: {}".format(con[312]))
                    f.close
                    

                    def nov9sa():
                        od=test.get()
                        test.delete(0,END)
                        con[312]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        novL.configure(text="9일에 할일: {}".format(con[312]))
                        
                    novb=Button(nov,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=nov9sa)
                    novb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(nov, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def nov10ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    novL.configure(text="10일에 할일: {}".format(con[313]))
                    f.close
                    

                    def nov10sa():
                        od=test.get()
                        test.delete(0,END)
                        con[313]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        novL.configure(text="10일에 할일: {}".format(con[313]))
                        
                    novb=Button(nov,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=nov10sa)
                    novb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(nov, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def nov11ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    novL.configure(text="11일에 할일: {}".format(con[314]))
                    f.close
                    

                    def nov11sa():
                        od=test.get()
                        test.delete(0,END)
                        con[314]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        novL.configure(text="11일에 할일: {}".format(con[314]))
                        
                    novb=Button(nov,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=nov11sa)
                    novb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(nov, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def nov12ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    novL.configure(text="12일에 할일: {}".format(con[315]))
                    f.close
                    

                    def nov12sa():
                        od=test.get()
                        test.delete(0,END)
                        con[315]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        novL.configure(text="12일에 할일: {}".format(con[315]))
                        
                    novb=Button(nov,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=nov12sa)
                    novb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(nov, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def nov13ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    novL.configure(text="13일에 할일: {}".format(con[316]))
                    f.close
                    

                    def nov13sa():
                        od=test.get()
                        test.delete(0,END)
                        con[316]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        novL.configure(text="13일에 할일: {}".format(con[316]))
                        
                    novb=Button(nov,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=nov13sa)
                    novb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(nov, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def nov14ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    novL.configure(text="14일에 할일: {}".format(con[317]))
                    f.close
                    

                    def nov14sa():
                        od=test.get()
                        test.delete(0,END)
                        con[317]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        novL.configure(text="14일에 할일: {}".format(con[317]))
                        
                    novb=Button(nov,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=nov14sa)
                    novb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(nov, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def nov15ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    novL.configure(text="15일에 할일: {}".format(con[318]))
                    f.close
                    

                    def nov15sa():
                        od=test.get()
                        test.delete(0,END)
                        con[318]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        novL.configure(text="15일에 할일: {}".format(con[318]))
                        
                    novb=Button(nov,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=nov15sa)
                    novb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(nov, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def nov16ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    novL.configure(text="16일에 할일: {}".format(con[319]))
                    f.close
                    

                    def nov16sa():
                        od=test.get()
                        test.delete(0,END)
                        con[319]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        novL.configure(text="16일에 할일: {}".format(con[319]))
                        
                    novb=Button(nov,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=nov16sa)
                    novb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(nov, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def nov17ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    novL.configure(text="17일에 할일: {}".format(con[320]))
                    f.close
                    

                    def nov17sa():
                        od=test.get()
                        test.delete(0,END)
                        con[320]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        novL.configure(text="17일에 할일: {}".format(con[320]))
                        
                    novb=Button(nov,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=nov17sa)
                    novb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(nov, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def nov18ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    novL.configure(text="18일에 할일: {}".format(con[321]))
                    f.close
                    

                    def nov18sa():
                        od=test.get()
                        test.delete(0,END)
                        con[321]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        novL.configure(text="18일에 할일: {}".format(con[321]))
                        
                    novb=Button(nov,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=nov18sa)
                    novb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(nov, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def nov19ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    novL.configure(text="19일에 할일: {}".format(con[322]))
                    f.close
                    

                    def nov19sa():
                        od=test.get()
                        test.delete(0,END)
                        con[322]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        novL.configure(text="19일에 할일: {}".format(con[322]))
                        
                    novb=Button(nov,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=nov19sa)
                    novb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(nov, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def nov20ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    novL.configure(text="20일에 할일: {}".format(con[323]))
                    f.close
                    

                    def nov20sa():
                        od=test.get()
                        test.delete(0,END)
                        con[323]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        novL.configure(text="20일에 할일: {}".format(con[323]))
                        
                    novb=Button(nov,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=nov20sa)
                    novb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(nov, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def nov21ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    novL.configure(text="21일에 할일: {}".format(con[324]))
                    f.close
                    

                    def nov21sa():
                        od=test.get()
                        test.delete(0,END)
                        con[324]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        novL.configure(text="21일에 할일: {}".format(con[324]))
                        
                    novb=Button(nov,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=nov21sa)
                    novb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(nov, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def nov22ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    novL.configure(text="22일에 할일: {}".format(con[325]))
                    f.close
                    

                    def nov22sa():
                        od=test.get()
                        test.delete(0,END)
                        con[325]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        novL.configure(text="22일에 할일: {}".format(con[325]))
                        
                    novb=Button(nov,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=nov22sa)
                    novb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(nov, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def nov23ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    novL.configure(text="23일에 할일: {}".format(con[326]))
                    f.close
                    

                    def nov23sa():
                        od=test.get()
                        test.delete(0,END)
                        con[326]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        novL.configure(text="23일에 할일: {}".format(con[326]))
                        
                    novb=Button(nov,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=nov23sa)
                    novb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(nov, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def nov24ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    novL.configure(text="24일에 할일: {}".format(con[327]))
                    f.close
                    

                    def nov24sa():
                        od=test.get()
                        test.delete(0,END)
                        con[327]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        novL.configure(text="24일에 할일: {}".format(con[327]))
                        
                    novb=Button(nov,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=nov24sa)
                    novb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(nov, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def nov25ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    novL.configure(text="25일에 할일: {}".format(con[328]))
                    f.close
                    

                    def nov25sa():
                        od=test.get()
                        test.delete(0,END)
                        con[328]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        novL.configure(text="25일에 할일: {}".format(con[328]))
                        
                    novb=Button(nov,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=nov25sa)
                    novb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(nov, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def nov26ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    novL.configure(text="26일에 할일: {}".format(con[329]))
                    f.close
                    

                    def nov26sa():
                        od=test.get()
                        test.delete(0,END)
                        con[329]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        novL.configure(text="26일에 할일: {}".format(con[329]))
                        
                    novb=Button(nov,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=nov26sa)
                    novb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(nov, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def nov27ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    novL.configure(text="27일에 할일: {}".format(con[330]))
                    f.close
                    

                    def nov27sa():
                        od=test.get()
                        test.delete(0,END)
                        con[330]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        novL.configure(text="27일에 할일: {}".format(con[330]))
                        
                    novb=Button(nov,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=nov27sa)
                    novb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(nov, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def nov28ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    novL.configure(text="28일에 할일: {}".format(con[331]))
                    f.close
                    

                    def nov28sa():
                        od=test.get()
                        test.delete(0,END)
                        con[331]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        novL.configure(text="28일에 할일: {}".format(con[331]))
                        
                    novb=Button(nov,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=nov28sa)
                    novb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(nov, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def nov29ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    novL.configure(text="29일에 할일: {}".format(con[332]))
                    f.close
                    

                    def nov29sa():
                        od=test.get()
                        test.delete(0,END)
                        con[332]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        novL.configure(text="29일에 할일: {}".format(con[332]))
                        
                    novb=Button(nov,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=nov29sa)
                    novb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(nov, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def nov30ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    novL.configure(text="30일에 할일: {}".format(con[333]))
                    f.close
                    

                    def nov30sa():
                        od=test.get()
                        test.delete(0,END)
                        con[333]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        novL.configure(text="30일에 할일: {}".format(con[333]))
                        
                    novb=Button(nov,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=nov30sa)
                    novb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(nov, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)


                nov1b=Button(nov,text="1", width=0, height=0, font=('휴먼엑스포', 20), command=nov1ex)
                nov1b.place(x=420,y=100)

                nov2b=Button(nov,text="2", width=0, height=0, font=('휴먼엑스포', 20), command=nov2ex)
                nov2b.place(x=500,y=100)

                nov3b=Button(nov,text="3", width=0, height=0, font=('휴먼엑스포', 20), command=nov3ex)
                nov3b.place(x=20,y=200)

                nov4b=Button(nov,text="4", width=0, height=0, font=('휴먼엑스포', 20), command=nov4ex)
                nov4b.place(x=100,y=200)

                nov5b=Button(nov,text="5", width=0, height=0, font=('휴먼엑스포', 20), command=nov5ex)
                nov5b.place(x=180,y=200)

                nov6b=Button(nov,text="6", width=0, height=0, font=('휴먼엑스포', 20), command=nov6ex)
                nov6b.place(x=260,y=200)

                nov7b=Button(nov,text="7", width=0, height=0, font=('휴먼엑스포', 20), command=nov7ex)
                nov7b.place(x=340,y=200)

                nov8b=Button(nov,text="8", width=0, height=0, font=('휴먼엑스포', 20), command=nov8ex)
                nov8b.place(x=420,y=200)

                nov9b=Button(nov,text="9", width=0, height=0, font=('휴먼엑스포', 20), command=nov9ex)
                nov9b.place(x=500,y=200)

                nov10b=Button(nov,text="10", width=0, height=0, font=('휴먼엑스포', 20), command=nov10ex)
                nov10b.place(x=20,y=300)

                nov11b=Button(nov,text="11", width=0, height=0, font=('휴먼엑스포', 20), command=nov11ex)
                nov11b.place(x=100,y=300)

                nov12b=Button(nov,text="12", width=0, height=0, font=('휴먼엑스포', 20), command=nov12ex)
                nov12b.place(x=180,y=300)

                nov13b=Button(nov,text="13", width=0, height=0, font=('휴먼엑스포', 20), command=nov13ex)
                nov13b.place(x=260,y=300)

                nov14b=Button(nov,text="14", width=0, height=0, font=('휴먼엑스포', 20), command=nov14ex)
                nov14b.place(x=340,y=300)

                nov15b=Button(nov,text="15", width=0, height=0, font=('휴먼엑스포', 20), command=nov15ex)
                nov15b.place(x=420,y=300)

                nov16b=Button(nov,text="16", width=0, height=0, font=('휴먼엑스포', 20), command=nov16ex)
                nov16b.place(x=500,y=300)

                nov17b=Button(nov,text="17", width=0, height=0, font=('휴먼엑스포', 20), command=nov17ex)
                nov17b.place(x=20,y=400)

                nov18b=Button(nov,text="18", width=0, height=0, font=('휴먼엑스포', 20), command=nov18ex)
                nov18b.place(x=100,y=400)

                nov19b=Button(nov,text="19", width=0, height=0, font=('휴먼엑스포', 20), command=nov19ex)
                nov19b.place(x=180,y=400)

                nov20b=Button(nov,text="20", width=0, height=0, font=('휴먼엑스포', 20), command=nov20ex)
                nov20b.place(x=260,y=400)

                nov21b=Button(nov,text="21", width=0, height=0, font=('휴먼엑스포', 20), command=nov21ex)
                nov21b.place(x=340,y=400)

                nov22b=Button(nov,text="22", width=0, height=0, font=('휴먼엑스포', 20), command=nov22ex)
                nov22b.place(x=420,y=400)

                nov23b=Button(nov,text="23", width=0, height=0, font=('휴먼엑스포', 20), command=nov23ex)
                nov23b.place(x=500,y=400)

                nov24b=Button(nov,text="24", width=0, height=0, font=('휴먼엑스포', 20), command=nov24ex)
                nov24b.place(x=20,y=500)

                nov25b=Button(nov,text="25", width=0, height=0, font=('휴먼엑스포', 20), command=nov25ex)
                nov25b.place(x=100,y=500)

                nov26b=Button(nov,text="26", width=0, height=0, font=('휴먼엑스포', 20), command=nov26ex)
                nov26b.place(x=180,y=500)

                nov27b=Button(nov,text="27", width=0, height=0, font=('휴먼엑스포', 20), command=nov27ex)
                nov27b.place(x=260,y=500)

                nov28b=Button(nov,text="28", width=0, height=0, font=('휴먼엑스포', 20), command=nov28ex)
                nov28b.place(x=340,y=500)

                nov29b=Button(nov,text="29", width=0, height=0, font=('휴먼엑스포', 20), command=nov29ex)
                nov29b.place(x=420,y=500)

                nov30b=Button(nov,text="30", width=0, height=0, font=('휴먼엑스포', 20), command=nov30ex)
                nov30b.place(x=500,y=500)
                def 월간11():
                    toj=Tk()
                    toj.title("11월 총 계획")
                    toj.geometry('700x700')

                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    f.close
                    
                    for i in range(304,334):
                        tojL=Label(toj, text="11월 {}일:{}".format(i-303,con[i]), font=('휴먼엑스포', 15))
                        tojL.place(x=0,y=(i-304)*20)
                        
                    
                tojb=Button(nov, text="월간", height=0, font=('휴먼엑스포', 20), command=월간11)   
                tojb.place(x=580,y=500)
                

            novb=Button(cal, text="11월", width=4, height=2, fg='gold', font=('휴먼엑스포', 20), command=nov)    
            novb.place(x=260,y=450)

            def dec():
                dec=Tk()
                dec.title("12월 달력")
                dec.geometry('700x600')
                decL=Label(dec, text="", font=('휴먼엑스포', 20))
                decL.place(x=350,y=0)

                LL=Label(dec, text="12월 달력", font=('휴먼엑스포', 20))
                LL.place(x=0, y=0)

                LL=Label(dec, text="일", fg="red", font=('휴먼엑스포', 15))
                LL.place(x=25, y=65)
                LL=Label(dec, text="월", font=('휴먼엑스포', 15))
                LL.place(x=105, y=65)
                LL=Label(dec, text="화", font=('휴먼엑스포', 15))
                LL.place(x=185, y=65)
                LL=Label(dec, text="수", font=('휴먼엑스포', 15))
                LL.place(x=265, y=65)
                LL=Label(dec, text="목", font=('휴먼엑스포', 15))
                LL.place(x=345, y=65)
                LL=Label(dec, text="금", font=('휴먼엑스포', 15))
                LL.place(x=425, y=65)
                LL=Label(dec, text="토", fg="blue", font=('휴먼엑스포', 15))
                LL.place(x=505, y=65)

                def dec1ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    decL.configure(text="1일에 할일: {}".format(con[334]))
                    f.close
                    

                    def dec1sa():
                        od=test.get()
                        test.delete(0,END)
                        con[334]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        decL.configure(text="1일에 할일: {}".format(con[334]))
                        
                    decb=Button(dec,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=dec1sa)
                    decb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(dec, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def dec2ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    decL.configure(text="2일에 할일: {}".format(con[335]))
                    f.close
                    

                    def dec2sa():
                        od=test.get()
                        test.delete(0,END)
                        con[335]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        decL.configure(text="2일에 할일: {}".format(con[335]))
                        
                    decb=Button(dec,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=dec2sa)
                    decb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(dec, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def dec3ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    decL.configure(text="3일에 할일: {}".format(con[336]))
                    f.close
                    

                    def dec3sa():
                        od=test.get()
                        test.delete(0,END)
                        con[336]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        decL.configure(text="3일에 할일: {}".format(con[336]))
                        
                    decb=Button(dec,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=dec3sa)
                    decb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(dec, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def dec4ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    decL.configure(text="4일에 할일: {}".format(con[337]))
                    f.close
                    

                    def dec4sa():
                        od=test.get()
                        test.delete(0,END)
                        con[337]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        decL.configure(text="4일에 할일: {}".format(con[337]))
                        
                    decb=Button(dec,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=dec4sa)
                    decb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(dec, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def dec5ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    decL.configure(text="5일에 할일: {}".format(con[338]))
                    f.close
                    

                    def dec5sa():
                        od=test.get()
                        test.delete(0,END)
                        con[338]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        decL.configure(text="5일에 할일: {}".format(con[338]))
                        
                    decb=Button(dec,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=dec5sa)
                    decb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(dec, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def dec6ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    decL.configure(text="6일에 할일: {}".format(con[339]))
                    f.close
                    

                    def dec6sa():
                        od=test.get()
                        test.delete(0,END)
                        con[339]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        decL.configure(text="6일에 할일: {}".format(con[339]))
                        
                    decb=Button(dec,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=dec6sa)
                    decb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(dec, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def dec7ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    decL.configure(text="7일에 할일: {}".format(con[340]))
                    f.close
                    

                    def dec7sa():
                        od=test.get()
                        test.delete(0,END)
                        con[340]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        decL.configure(text="7일에 할일: {}".format(con[340]))
                        
                    decb=Button(dec,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=dec7sa)
                    decb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(dec, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def dec8ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    decL.configure(text="8일에 할일: {}".format(con[341]))
                    f.close
                    

                    def dec8sa():
                        od=test.get()
                        test.delete(0,END)
                        con[341]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        decL.configure(text="8일에 할일: {}".format(con[341]))
                        
                    decb=Button(dec,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=dec8sa)
                    decb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(dec, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def dec9ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    decL.configure(text="9일에 할일: {}".format(con[342]))
                    f.close
                    

                    def dec9sa():
                        od=test.get()
                        test.delete(0,END)
                        con[342]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        decL.configure(text="9일에 할일: {}".format(con[342]))
                        
                    decb=Button(dec,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=dec9sa)
                    decb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(dec, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def dec10ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    decL.configure(text="10일에 할일: {}".format(con[343]))
                    f.close
                    

                    def dec10sa():
                        od=test.get()
                        test.delete(0,END)
                        con[343]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        decL.configure(text="10일에 할일: {}".format(con[343]))
                        
                    decb=Button(dec,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=dec10sa)
                    decb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(dec, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def dec11ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    decL.configure(text="11일에 할일: {}".format(con[344]))
                    f.close
                    

                    def dec11sa():
                        od=test.get()
                        test.delete(0,END)
                        con[344]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        decL.configure(text="11일에 할일: {}".format(con[344]))
                        
                    decb=Button(dec,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=dec11sa)
                    decb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(dec, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def dec12ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    decL.configure(text="12일에 할일: {}".format(con[345]))
                    f.close
                    

                    def dec12sa():
                        od=test.get()
                        test.delete(0,END)
                        con[345]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        decL.configure(text="12일에 할일: {}".format(con[345]))
                        
                    decb=Button(dec,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=dec12sa)
                    decb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(dec, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def dec13ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    decL.configure(text="13일에 할일: {}".format(con[346]))
                    f.close
                    

                    def dec13sa():
                        od=test.get()
                        test.delete(0,END)
                        con[346]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        decL.configure(text="13일에 할일: {}".format(con[346]))
                        
                    decb=Button(dec,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=dec13sa)
                    decb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(dec, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def dec14ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    decL.configure(text="14일에 할일: {}".format(con[347]))
                    f.close
                    

                    def dec14sa():
                        od=test.get()
                        test.delete(0,END)
                        con[347]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        decL.configure(text="14일에 할일: {}".format(con[347]))
                        
                    decb=Button(dec,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=dec14sa)
                    decb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(dec, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def dec15ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    decL.configure(text="15일에 할일: {}".format(con[348]))
                    f.close
                    

                    def dec15sa():
                        od=test.get()
                        test.delete(0,END)
                        con[348]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        decL.configure(text="15일에 할일: {}".format(con[348]))
                        
                    decb=Button(dec,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=dec15sa)
                    decb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(dec, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def dec16ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    decL.configure(text="16일에 할일: {}".format(con[349]))
                    f.close
                    

                    def dec16sa():
                        od=test.get()
                        test.delete(0,END)
                        con[349]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        decL.configure(text="16일에 할일: {}".format(con[349]))
                        
                    decb=Button(dec,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=dec16sa)
                    decb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(dec, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def dec17ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    decL.configure(text="17일에 할일: {}".format(con[350]))
                    f.close
                    

                    def dec17sa():
                        od=test.get()
                        test.delete(0,END)
                        con[350]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        decL.configure(text="17일에 할일: {}".format(con[350]))
                        
                    decb=Button(dec,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=dec17sa)
                    decb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(dec, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def dec18ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    decL.configure(text="18일에 할일: {}".format(con[351]))
                    f.close
                    

                    def dec18sa():
                        od=test.get()
                        test.delete(0,END)
                        con[351]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        decL.configure(text="18일에 할일: {}".format(con[351]))
                        
                    decb=Button(dec,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=dec18sa)
                    decb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(dec, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def dec19ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    decL.configure(text="19일에 할일: {}".format(con[352]))
                    f.close
                    

                    def dec19sa():
                        od=test.get()
                        test.delete(0,END)
                        con[352]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        decL.configure(text="19일에 할일: {}".format(con[352]))
                        
                    decb=Button(dec,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=dec19sa)
                    decb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(dec, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def dec20ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    decL.configure(text="20일에 할일: {}".format(con[353]))
                    f.close
                    

                    def dec20sa():
                        od=test.get()
                        test.delete(0,END)
                        con[353]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        decL.configure(text="20일에 할일: {}".format(con[353]))
                        
                    decb=Button(dec,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=dec20sa)
                    decb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(dec, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def dec21ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    decL.configure(text="21일에 할일: {}".format(con[354]))
                    f.close
                    

                    def dec21sa():
                        od=test.get()
                        test.delete(0,END)
                        con[354]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        decL.configure(text="21일에 할일: {}".format(con[354]))
                        
                    decb=Button(dec,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=dec21sa)
                    decb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(dec, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def dec22ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    decL.configure(text="22일에 할일: {}".format(con[355]))
                    f.close
                    

                    def dec22sa():
                        od=test.get()
                        test.delete(0,END)
                        con[355]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        decL.configure(text="22일에 할일: {}".format(con[355]))
                        
                    decb=Button(dec,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=dec22sa)
                    decb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(dec, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def dec23ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    decL.configure(text="23일에 할일: {}".format(con[356]))
                    f.close
                    

                    def dec23sa():
                        od=test.get()
                        test.delete(0,END)
                        con[356]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        decL.configure(text="23일에 할일: {}".format(con[356]))
                        
                    decb=Button(dec,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=dec23sa)
                    decb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(dec, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def dec24ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    decL.configure(text="24일에 할일: {}".format(con[357]))
                    f.close
                    

                    def dec24sa():
                        od=test.get()
                        test.delete(0,END)
                        con[357]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        decL.configure(text="24일에 할일: {}".format(con[357]))
                        
                    decb=Button(dec,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=dec24sa)
                    decb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(dec, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def dec25ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    decL.configure(text="25일에 할일: {}".format(con[358]))
                    f.close
                    al=Tk()
                    al.geometry('150x100')
                    al.title("공휴일 알림")
                    alL=Label(al, text="크리스마스", font=("휴먼엑스포", 15), fg="red")
                    alL.place(x=20, y=30)

                    def 종료():
                        al.destroy()

                    alB=Button(al, text="닫기", width=0, height=0, font=(10), command=종료)
                    alB.place(x=40, y=60)
                    

                    def dec25sa():
                        od=test.get()
                        test.delete(0,END)
                        con[358]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        decL.configure(text="25일에 할일: {}".format(con[358]))
                        
                    decb=Button(dec,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=dec25sa)
                    decb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(dec, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def dec26ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    decL.configure(text="26일에 할일: {}".format(con[359]))
                    f.close
                    

                    def dec26sa():
                        od=test.get()
                        test.delete(0,END)
                        con[359]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        decL.configure(text="26일에 할일: {}".format(con[359]))
                        
                    decb=Button(dec,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=dec26sa)
                    decb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(dec, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def dec27ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    decL.configure(text="27일에 할일: {}".format(con[360]))
                    f.close
                    

                    def dec27sa():
                        od=test.get()
                        test.delete(0,END)
                        con[360]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        decL.configure(text="27일에 할일: {}".format(con[360]))
                        
                    decb=Button(dec,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=dec27sa)
                    decb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(dec, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def dec28ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    decL.configure(text="28일에 할일: {}".format(con[361]))
                    f.close
                    

                    def dec28sa():
                        od=test.get()
                        test.delete(0,END)
                        con[361]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        decL.configure(text="28일에 할일: {}".format(con[361]))
                        
                    decb=Button(dec,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=dec28sa)
                    decb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(dec, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def dec29ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    decL.configure(text="29일에 할일: {}".format(con[362]))
                    f.close
                    

                    def dec29sa():
                        od=test.get()
                        test.delete(0,END)
                        con[362]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        decL.configure(text="29일에 할일: {}".format(con[362]))
                        
                    decb=Button(dec,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=dec29sa)
                    decb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(dec, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)


                def dec30ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    decL.configure(text="30일에 할일: {}".format(con[363]))
                    f.close
                    

                    def dec30sa():
                        od=test.get()
                        test.delete(0,END)
                        con[363]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        decL.configure(text="30일에 할일: {}".format(con[363]))
                        
                    decb=Button(dec,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=dec30sa)
                    decb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(dec, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                def dec31ex():
                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    decL.configure(text="31일에 할일: {}".format(con[364]))
                    f.close
                    

                    def dec31sa():
                        od=test.get()
                        test.delete(0,END)
                        con[364]=od
                        f=open("{}.txt".format(idlog), mode='w', encoding='UTF8')
                        f.write(str(con))
                        f.close
                        decL.configure(text="31일에 할일: {}".format(con[364]))
                        
                    decb=Button(dec,text="저장", width=0, height=0, font=('휴먼엑스포', 20), command=dec31sa)
                    decb.place(x=250,y=10)

                    txt=StringVar()
                    test=Entry(dec, width = 50, textvariable = txt)
                    test.place(x=350 ,y=40)

                dec1b=Button(dec,text="1", width=0, height=0, font=('휴먼엑스포', 20), command=dec1ex)
                dec1b.place(x=20,y=100)

                dec2b=Button(dec,text="2", width=0, height=0, font=('휴먼엑스포', 20), command=dec2ex)
                dec2b.place(x=100,y=100)

                dec3b=Button(dec,text="3", width=0, height=0, font=('휴먼엑스포', 20), command=dec3ex)
                dec3b.place(x=180,y=100)

                dec4b=Button(dec,text="4", width=0, height=0, font=('휴먼엑스포', 20), command=dec4ex)
                dec4b.place(x=260,y=100)

                dec5b=Button(dec,text="5", width=0, height=0, font=('휴먼엑스포', 20), command=dec5ex)
                dec5b.place(x=340,y=100)

                dec6b=Button(dec,text="6", width=0, height=0, font=('휴먼엑스포', 20), command=dec6ex)
                dec6b.place(x=420,y=100)

                dec7b=Button(dec,text="7", width=0, height=0, font=('휴먼엑스포', 20), command=dec7ex)
                dec7b.place(x=500,y=100)

                dec8b=Button(dec,text="8", width=0, height=0, font=('휴먼엑스포', 20), command=dec8ex)
                dec8b.place(x=20,y=200)

                dec9b=Button(dec,text="9", width=0, height=0, font=('휴먼엑스포', 20), command=dec9ex)
                dec9b.place(x=100,y=200)

                dec10b=Button(dec,text="10", width=0, height=0, font=('휴먼엑스포', 20), command=dec10ex)
                dec10b.place(x=180,y=200)

                dec11b=Button(dec,text="11", width=0, height=0, font=('휴먼엑스포', 20), command=dec11ex)
                dec11b.place(x=260,y=200)

                dec12b=Button(dec,text="12", width=0, height=0, font=('휴먼엑스포', 20), command=dec12ex)
                dec12b.place(x=340,y=200)

                dec13b=Button(dec,text="13", width=0, height=0, font=('휴먼엑스포', 20), command=dec13ex)
                dec13b.place(x=420,y=200)

                dec14b=Button(dec,text="14", width=0, height=0, font=('휴먼엑스포', 20), command=dec14ex)
                dec14b.place(x=500,y=200)

                dec15b=Button(dec,text="15", width=0, height=0, font=('휴먼엑스포', 20), command=dec15ex)
                dec15b.place(x=20,y=300)

                dec16b=Button(dec,text="16", width=0, height=0, font=('휴먼엑스포', 20), command=dec16ex)
                dec16b.place(x=100,y=300)

                dec17b=Button(dec,text="17", width=0, height=0, font=('휴먼엑스포', 20), command=dec17ex)
                dec17b.place(x=180,y=300)

                dec18b=Button(dec,text="18", width=0, height=0, font=('휴먼엑스포', 20), command=dec18ex)
                dec18b.place(x=260,y=300)

                dec19b=Button(dec,text="19", width=0, height=0, font=('휴먼엑스포', 20), command=dec19ex)
                dec19b.place(x=340,y=300)

                dec20b=Button(dec,text="20", width=0, height=0, font=('휴먼엑스포', 20), command=dec20ex)
                dec20b.place(x=420,y=300)

                dec21b=Button(dec,text="21", width=0, height=0, font=('휴먼엑스포', 20), command=dec21ex)
                dec21b.place(x=500,y=300)

                dec22b=Button(dec,text="22", width=0, height=0, font=('휴먼엑스포', 20), command=dec22ex)
                dec22b.place(x=20,y=400)

                dec23b=Button(dec,text="23", width=0, height=0, font=('휴먼엑스포', 20), command=dec23ex)
                dec23b.place(x=100,y=400)

                dec24b=Button(dec,text="24", width=0, height=0, font=('휴먼엑스포', 20), command=dec24ex)
                dec24b.place(x=180,y=400)

                dec25b=Button(dec,text="25",fg="red",width=0, height=0, font=('휴먼엑스포', 20), command=dec25ex)
                dec25b.place(x=260,y=400)

                dec26b=Button(dec,text="26", width=0, height=0, font=('휴먼엑스포', 20), command=dec26ex)
                dec26b.place(x=340,y=400)

                dec27b=Button(dec,text="27", width=0, height=0, font=('휴먼엑스포', 20), command=dec27ex)
                dec27b.place(x=420,y=400)

                dec28b=Button(dec,text="28", width=0, height=0, font=('휴먼엑스포', 20), command=dec28ex)
                dec28b.place(x=500,y=400)

                dec29b=Button(dec,text="29", width=0, height=0, font=('휴먼엑스포', 20), command=dec29ex)
                dec29b.place(x=20,y=500)

                dec30b=Button(dec,text="30", width=0, height=0, font=('휴먼엑스포', 20), command=dec30ex)
                dec30b.place(x=100,y=500)

                dec31b=Button(dec,text="31", width=0, height=0, font=('휴먼엑스포', 20), command=dec31ex)
                dec31b.place(x=180,y=500)

                def 월간12():
                    toj=Tk()
                    toj.title("12월 총 계획")
                    toj.geometry('700x700')

                    f=open("{}.txt".format(idlog), mode='r', encoding='UTF8')
                    con=eval(f.read())
                    f.close
                    
                    for i in range(334,365):
                        tojL=Label(toj, text="12월 {}일:{}".format(i-333,con[i]), font=('휴먼엑스포', 15))
                        tojL.place(x=0,y=(i-334)*20)
                        
                    
                tojb=Button(dec, text="월간", height=0, font=('휴먼엑스포', 20), command=월간12)   
                tojb.place(x=450,y=500)
            

            decb=Button(cal, text="12월", width=4, height=2, fg='turquoise',font=('휴먼엑스포', 20), command=dec)   
            decb.place(x=410,y=450)

            cal.mainloop()
                    
                   
            
        if idcheck2 != passlog:
            checkL.configure(text="패스워드가 틀립니다. 다시 입력하세요")
            hssx.delete(0,END)
            hx.delete(0,END)

    else:
        checkL.configure(text="해당하는 아이디가 없습니다")

   

   
def 회원가입():
    checkin = Tk()
    checkin.title("회원가입")
    checkin.geometry('400x300')
    checkinL = Label(checkin, text="")
    checkinL.place(x=1,y=3)
    checkinLL=Label(checkin, text= "아이디")
    checkinLL.place(x=150,y=30)

    checkinLL=Label(checkin, text= "비밀번호")
    checkinLL.place(x=145,y=60)

    checkinLL=Label(checkin, text= "이름")
    checkinLL.place(x=150,y=100)

    def 가입신청():     
        idca=yyx.get()
        name=nan.get()
        passw=hyx.get()
        global pp
        global spl
        global spla
        if idca in idinfo:
            checkinL.configure(text="아이디가 중복됩니다. 다시 입력하세요")
            yyx.delete(0,END)
            hyx.delete(0,END)
            nan.delete(0,END)

        elif idca=="":
            checkinL.configure(text="아이디를 입력하세요")
            
        elif passw =="":
            checkinL.configure(text="비밀번호를 입력하세요")

        elif name =="":
            checkinL.configure(text="이름을 입력하세요")

        else:
            pp+=1
            checkinL.configure(text="회원가입이 완료되었습니다.")
            f=open("회원정보.txt",mode='w', encoding='UTF8')
            spl=("{}{}/*{}/*{}/*".format(spl,idca,passw,name))
            spla=spl.split("/*")
            pp=int((int(spl.count("/*")))/3)
            ppp=pp+1
            for t in range(1,ppp):
                i=3*t-3
                a=spla[i]
                b=spla[i+1]
                c=spla[i+2]
                idinfo[a]=[b,c]
            f.write(spl)
            f.close()
            frr=open("{}.txt".format(idca), mode='w', encoding='UTF8')
            frr.write("['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']")
            frr.close()
                          
    
        
    inib=Button(checkin,text="회원가입", width=0, height=0, font=('휴먼엑스포', 20), command=가입신청)
    inib.place(x=70,y=180)    
  
    txt=StringVar()
    yyx=Entry(checkin, width = 10, textvariable = txt)
    yyx.place(x=200 ,y=30)

    txt=StringVar()
    hyx=Entry(checkin, width = 10, textvariable = txt)
    hyx.place(x=200 ,y=60)

    txt=StringVar()
    nan=Entry(checkin, width = 10, textvariable = txt)
    nan.place(x=200 ,y=100)
    

def 찾기():
    fou=Tk()
    fou.title("아이디 찾기")
    fou.geometry('400x300')
    fouL = Label(fou, text="아이디와 이름을 맞게 입력하면 비밀번호를 알려드립니다")
    fouL.place(x=1,y=3)
    fouLL = Label(fou, text="아이디")
    fouLL.place(x=150,y=70)
    fouLL = Label(fou, text="이름")
    fouLL.place(x=150,y=100)

    def 아이디찾():
        nanfind=nanfi.get()
        idfind=idfi.get()
        global pp
        global spl
        global spla
        nanfi.delete(0,END)
        idfi.delete(0,END)
        
        if idfind in idinfo:
            idfind1=idinfo[idfind]
            idfind2=idfind1[1]

            if nanfind == idfind2:
                fouL.configure(text="비밀번호는 {}입니다".format(idfind1[0]))

            else:
                fouL.configure(text="아이디와 이름이 다릅니다")
                
        else:
            fouL.configure(text="해당하는 아이디가 없습니다")
            idfind.delete(0,END)
            nanfind.delete(0,END)
            


        
        
                
    

    txt=StringVar()
    idfi=Entry(fou, width = 10, textvariable = txt)
    idfi.place(x=200 ,y=70)

    txt=StringVar()
    nanfi=Entry(fou, width = 10, textvariable = txt)
    nanfi.place(x=200 ,y=100)

    idf=Button(fou,text="비밀번호 찾기", width=0, height=0, font=('휴먼엑스포', 20), command=아이디찾)
    idf.place(x=180,y=200)

    

inib=Button(integ,text="로그인", width=0, height=0, font=('휴먼엑스포', 20), command=로그인)
inib.place(x=200,y=370)

inib=Button(integ,text="회원가입", width=0, height=0, font=('휴먼엑스포', 15), command=회원가입)
inib.place(x=400,y=440)

inib=Button(integ,text="비밀번호 찾기", width=0, height=0, font=('휴먼엑스포', 15), command=찾기)
inib.place(x=400,y=500)



txt=StringVar()
hssx=Entry(integ, width = 10, textvariable = txt)
hssx.place(x=200 ,y=300)


txt=StringVar()
hx=Entry(integ, width = 10, textvariable = txt)
hx.place(x=200 ,y=330)


integ.mainloop()



