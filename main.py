"""
xpath = /html/body/div[1]/div[2]/div[3]/div/iframe 
class city;
class total;
class daynow red
class die
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium
#from selenium.webdriver.chrome.options import Options
import datetime 
import os,time

if __name__ == "__main__":
    data_save_file_cvs = [] #Để 1 biến này để lưu data vào đây
    #url_file_driver = os.path.join('etc','chromedriver.exe') #tuừ thư mục hiện tại nối với thư mục etc và lấy file chromedriver 
    #driver.get("https://covid19.gov.vn/") =>in lastest ver of selenium u dont need to add executable_url and dont need to down chromedriver
    driver=webdriver.Chrome()
    driver.get("https://covid19.gov.vn/") 
    print("Đã truy cập được trang web")
    #cái bảng mình cần là iframe thứ 2 => [1]
    driver.switch_to.frame(1)
    #target = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div")
    target = driver.find_elements("xpath", '/html/body/div[2]/div[1]/div')
    for data in target: #Vì là list nên dùng for mới lấy data được
        cities = data.find_elements(By.CLASS_NAME, "city")
        totals = data.find_elements(By.CLASS_NAME,"total")
        today = data.find_elements(By.CLASS_NAME,"daynow")
        deads = data.find_elements(By.CLASS_NAME,"die")
    #for i in cities :
        #print(i.text) 
    list_cities = [city.text for city in cities]
    list_total  = [total.text for total in totals]
    list_today  = [today.text for today in today]
    list_dead   = [dead.text for dead in deads]
    for i in range(len(list_cities)):
        row = "{},{},{},{}\n".format(list_cities[i], list_total[i], list_today[i], list_dead[i])
        data_save_file_cvs.append(row)
    #giờ thì tạo file => tạo file ngày siowf để dễ phân biệt 
    #Phải lưu tự động => Chỉ cần chạy code sẽ lấy data và lưu với 1 tên file mới
    #=> Chứ ko vào đổi tên file bằng tay lưu vào thư mục
    today_ = (datetime.datetime.now()).strftime("%Y-%m-%d")
    filename = f"{today_}.csv"
    with open(os.path.join("data", filename),'w+',encoding='utf-8') as f:
        f.writelines(data_save_file_cvs)
    time.sleep(3) 
    driver.close()