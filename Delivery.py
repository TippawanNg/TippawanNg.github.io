#list
shop=["1.ร้านน้ำ","2.ร้านก๋วยเตี๋ยว","3.ร้านของหวาน","4.ร้านสเต็ก","5.ร้านอาหารญี่ปุ่น","6.ออกจากโปรแกรม"]
list_dt=["ไม่ถึง 2 กิโล ส่งฟรี","ไม่เกิน 10 กิโล ค่าส่ง 50 บาท","ไม่เกิน 20 กิโล ค่าส่ง 100 บาท","ไม่เกิน 30 กิโล ค่าส่ง 200 บาท","มากกว่า 30 กิโลขึ้นไป ค่าส่ง 500 บาท"]

#Dictionary
watershop={"น้ำเปล่า":5,"โค้ก":10,"น้ำแดง":10,"น้ำเขียว":10,"ชาเขียว":30,"ชานม":30,"นมเย็น":30,"กาแฟ":30}
noodleshop={"น้ำตก":40,"น้ำใส":30,"ต้มยำ":50}
dessertshop={"บิงซู":120,"ไอศกรีม":20,"เค้ก":150,"คุกกี้":50,"วาฟเฟิล":50}
steakshop={"หมู":70,"ไก่":70,"เนื้อวากิว":150,"ปลา":100,"สลัด":50}
japanshop={"ทงคัตสึ":80,"ราเมง":89,"อูด้ง":89,"ซูชิ":5,"เทมปุระ":80,"ทาโกะยากิ":5}

#main menu
def main() :
    try :
        print("----------------------------------------------")
        print(shop)
        print("----------------------------------------------")
        shopsel=int(input("เลือกหมายเลขที่คุณลูกค้าต้องการทำรายการ : "))
        if shopsel == 1 :
            wts()
        elif shopsel == 2 :
            nds()
        elif shopsel == 3 :
            dss()
        elif shopsel == 4 :
            sts()
        elif shopsel == 5 :
            jps()
        elif shopsel == 6 :
            end2()
        else :
            print("ไม่พบร้านค้าที่คุณลูกค้าต้องการ")
    except ValueError :
        print("โปรดใส่ตัวเลขเท่านั้น")
        shopsel="error"
        return shopsel
    except KeyboardInterrupt :
        print ("ขอบคุณที่ใช้บริการ")
        
#watershop
def wts() :
    print("----------------------------------------------")
    print(watershop)
    print("----------------------------------------------")
    sumprice=0
    while True :
        menu=(input("เลือกเมนูที่ต้องการ หากไม่ต้องการพิมพ์ end : "))
        print("-----")
        if menu in watershop :
            many=int(input("จำนวน(ขวด) : "))
            print("-----")
            print(menu,"จำนวน ",many ,"ขวด ราคา ",watershop[menu]*many," บาท")
            print("-----")
            price = watershop[menu]*many
            sumprice += price
        elif menu == "end" :
            print("-----")
            print(f"ราคาสินค้ารวมทั้งหมด {sumprice} บาท")
            print("-----")
            dist(sumprice)
        elif menu not in watershop :
            print("-----")
            print("ไม่มีรายการที่คุณลูกค้าต้องการ")
            print("-----")
            print("-----")

#noodleshop
def nds() :
    print("----------------------------------------------")
    print(noodleshop)
    print("----------------------------------------------")
    sumprice=0
    while True :
        menu=(input("เลือกเมนูที่ต้องการ หากไม่ต้องการพิมพ์ end : "))
        print("-----")
        if menu in noodleshop :
            sel=(input("เส้นที่คุณลูกค้าต้องการ : "))
            print(sel ,menu," ราคา ",noodleshop[menu]," บาท")
            print("-----")
            price = noodleshop[menu]
            sumprice += price
        elif menu == "end" :
            print("-----")
            print(f"ราคาสินค้ารวมทั้งหมด {sumprice} บาท")
            print("-----")
            dist(sumprice)
        elif menu not in noodleshop :
            print("-----")
            print("ไม่มีรายการที่คุณลูกค้าต้องการ")
            print("-----")
            print("-----")
    
#dessertshop
def dss() :
    print("----------------------------------------------")
    print(dessertshop)
    print("----------------------------------------------")
    sumprice=0
    while True :
        menu=(input("เลือกเมนูที่ต้องการ หากไม่ต้องการพิมพ์ end : "))
        print("-----")
        if menu in dessertshop :
            print(menu," ราคา ",dessertshop[menu]," บาท")
            print("-----")
            price = dessertshop[menu]
            sumprice += price
        elif menu == "end" :
            print("-----")
            print(f"ราคาสินค้ารวมทั้งหมด {sumprice} บาท")
            print("-----")
            dist(sumprice)
        elif menu not in dessertshop :
            print("-----")
            print("ไม่มีรายการที่คุณลูกค้าต้องการ")
            print("-----")
            print("-----")

#steakshop
def sts():
    print("----------------------------------------------")
    print(steakshop)
    print("----------------------------------------------")
    sumprice=0
    while True :
        menu=(input("เลือกเมนูที่ต้องการ หากไม่ต้องการพิมพ์ end : "))
        print("-----")
        if menu in steakshop :
            ms=(input("หมายเหตุถึงร้านค้า :"))
            print(f"{menu} ราคา {steakshop[menu]} บาท ({ms})")
            print("-----")
            price = steakshop[menu]
            sumprice += price
        elif menu == "end" :
            print("-----")
            print(f"ราคาสินค้ารวมทั้งหมด {sumprice} บาท")
            print("-----")
            dist(sumprice)
        elif menu not in steakshop :
            print("-----")
            print("ไม่มีรายการที่คุณลูกค้าต้องการ")
            print("-----")
            print("-----")
 
#japanshop
def jps():  
    print("----------------------------------------------")     
    print(japanshop)
    print("----------------------------------------------")
    sumprice=0
    while True :
        menu=(input("เลือกเมนูที่ต้องการ หากไม่ต้องการพิมพ์ end : "))
        print("-----")
        if menu in japanshop :
            print(menu," ราคา ",japanshop[menu]," บาท")
            print("-----")
            price = japanshop[menu]
            sumprice += price
        elif menu == "end" :
            print("-----")
            print(f"ราคาสินค้ารวมทั้งหมด {sumprice} บาท")
            print("-----")
            dist(sumprice)
        elif menu not in japanshop :
            print("-----")
            print("ไม่มีรายการที่คุณลูกค้าต้องการ")
            print("-----")
            print("-----")

#distance pay
def dist(sumprice) :
    print("----------------------------------------------")
    print("1.ชำระเงิน")
    print("2.เลือกร้านใหม่อีกครั้ง")
    print("3.ออกจากโปรแกรม")
    print("----------------------------------------------")
    con=int(input("เลือกหมายเลยที่ต้องการทำรายการ : "))
    if con == 1 :
        print("-----")
        print(list_dt)
        print("-----")
        dt=int(input("กรอกระยะทางที่ต้องการจัดส่ง(กิโล) : "))
        print("-----")
        while dt != 0 :
            if  dt <= 2 :
                paydt = 0
            elif dt > 2 and dt <= 10 :
                paydt = 50
            elif dt >= 11 and dt <= 20 :
                paydt = 100
            elif dt >= 21 and dt <= 30 :
                paydt = 200
            elif dt > 30 :
                paydt = 500
            print("-----")
            print("ค่าจัดส่ง : ",paydt," บาท")
            total = sumprice + paydt
            print("ราคาที่คุณลูกค้าต้องชำระ : ", total ," บาท")
            print("-----")
            print("ไรเดอร์ได้รับรายการสั่งซื้อของคุณแล้ว")
            print("-----")
            if total > 0 :
                end()
                break
    elif con == 2 :
        main()
    elif con == 3 :
        end2()

#Pre end
def end() :
    print("-----")
    ans=str(input("ต้องการรายการอื่นหรือไม่ yes or no : "))
    if ans == "yes" :
        main()
    elif ans == "no" :
        end2()
    else :
        print("ไม่มีตัวเลือกที่เลือก กรุณากรอกใหม่อีกครั้ง")

#final end
def end2() :
    print("-----")
    print("ขอบคุณที่ใช้บริการ")
    print("----------------------------------------------")
    exit()

#main program
print("----------------------------------------------")
print("ยินดีต้องรับเข้าสู่ The flash Delivery คุณลูกค้าสามารถเลือกซื้อของได้หนึ่งร้านต่อหนึ่งครั้ง หากต้องการสั่งซื้อร้านอื่นเพิ่มเติม คุณลูกค้าต้องทำรายการใหม่อีกครั้ง")
print("----------------------------------------------")
selshop = main()