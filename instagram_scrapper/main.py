from selenium import webdriver
import urllib3

OUTPUT_FOLDER = 'imgs'

def main():
    url = 'https://www.instagram.com/lillemaville/?hl=fr'
    http = urllib3.PoolManager()

    driver = webdriver.Firefox()
    driver.set_window_size(412, 732)
    driver.get(url)

    imgs = driver.find_elements_by_class_name('FFVAD')
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    driver.implicitly_wait(5)

    for i, img in enumerate(imgs):
        src = img.get_attribute('src')
        name = str(i)+'.jpg'
        r = http.request('GET', src, preload_content=False)

        with open(OUTPUT_FOLDER + "/" + name, 'wb') as out:
            while True:
                data = r.read()
                if not data:
                    break
                out.write(data)




    driver.close()
    







if __name__ == "__main__":
    main()