import selenium
import time
import sys
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException

url_baltezers = "https://www.baltezers.lv/sortiment"
url_stadu_audzetsva = "https://stadu-audzetava.lv/katalogi/"

putes_veids = input("Kadu augu Jus gribat?: ")


store_bltezers = []
store_stadu_audzetsva = []


service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)


with open("output.txt", "w", encoding="utf-8") as file:
    file.write("**baltezers.lv**\n")  

    
    driver.get(url_baltezers)
    time.sleep(2)

    try:
        find = driver.find_element(By.CLASS_NAME, "form-control")
        find.send_keys(str(putes_veids))
        find.send_keys(Keys.RETURN)
        current_page = 1

        while True:
            elements = WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "item")))
            if elements:
                names = driver.find_elements(By.CLASS_NAME, "primaryTitle")
                prices = driver.find_elements(By.CLASS_NAME, "price.text-right.col-7")
                names2 = driver.find_elements(By.CLASS_NAME, "secondaryTitle")

                for name, name2, price in zip(names, names2, prices):
                    name_text = name.text.strip().lower()  
                    name2_text = name2.text.strip().lower()  
                    price_text = price.text.strip()

                    if putes_veids.lower() in name_text or putes_veids.lower() in name2_text:
                        output = f"{name_text}\n{name2_text}\n{price_text}\n"
                        store_bltezers.append(output)
                        file.write(output)
                        

            try:
                next_button = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//a[@aria-label='Next page' and not(@aria-disabled='true')]")))
                driver.execute_script("arguments[0].click();", next_button)
                current_page += 1
            except TimeoutException:
                break

    except WebDriverException as e:
        file.write("\nNav tadas preces.\n")

    finally:
        driver.quit()
        file.write("\n**stadu-audzetava.lv**\n")  

        
        driver = webdriver.Chrome(service=service, options=option)
        driver.get(url_stadu_audzetsva)
        time.sleep(2)

        plant_found_on_first_page = False
        find = driver.find_element(By.ID, "product-search-field-0")
        find.send_keys(str(putes_veids))
        find.send_keys(Keys.RETURN)

        try:
            temp_element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "product_title.entry-title")))
            temp_text = temp_element.text
            if putes_veids.lower() == temp_text.lower():
                cena = driver.find_element(By.CLASS_NAME, "price")
                cena_value = cena.text
                output = f"{putes_veids}\n{cena_value}\n"
                store_stadu_audzetsva.append(output)
                file.write(output)
                
                plant_found_on_first_page = True
            else:
                sys.exit()

        except TimeoutException:
            file.write("\nPieprasījums izpildīts, tālāk visas preces, kas ir šajā vietnē...\n")
            
                
        if not plant_found_on_first_page:
            while True:
                elements = WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "box-content")))
                if elements:
                    box_content_elements = driver.find_elements(By.CLASS_NAME, "box-content")
                    for box_content_element in box_content_elements:
                        box_content_text = box_content_element.text
                        if putes_veids.lower() in box_content_text.lower():
                            output = f"{box_content_text}\n"
                            store_stadu_audzetsva.append(output)
                            file.write(output)
                            

                try:
                    next_button = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "next.page-numbers")))
                    driver.execute_script("arguments[0].click();", next_button)
                except (TimeoutException, NoSuchElementException):
                    
                    break
            
        driver.quit()


print("Dati saglabāti output.txt.")



