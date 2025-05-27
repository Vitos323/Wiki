from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

def open_article(title):
    url = f"https://ru.wikipedia.org/wiki/{title.replace(' ', '_')}"
    driver.get(url)
    time.sleep(2)

def show_paragraphs():
    paras = driver.find_elements(By.CSS_SELECTOR, "p")
    for i, p in enumerate(paras):
        text = p.text.strip()
        if text:
            print(f"\n[{i+1}] {text}")
            if input("Enter — далее, q — выход: ").lower() == 'q':
                break

def show_links():
    links = driver.find_elements(By.CSS_SELECTOR, "#bodyContent a[href^='/wiki/']")
    internal = [(l.text, l.get_attribute("href")) for l in links if l.text and ":" not in l.get_attribute("href")]
    internal = list(dict.fromkeys(internal))[:5]  # удалить повторы, взять первые 5
    for i, (txt, _) in enumerate(internal):
        print(f"{i+1}. {txt}")
    choice = input("Номер статьи для перехода (или Enter для отмены): ")
    if choice.isdigit() and 1 <= int(choice) <= len(internal):
        driver.get(internal[int(choice)-1][1])
        time.sleep(1)


query = input(" Поиск Википедии: ")
open_article(query)

while True:
    print("\n1 — Читать параграфы\n2 — Внутренние статьи\n3 — Выход")
    cmd = input("Выбор: ")
    if cmd == '1':
        show_paragraphs()
    elif cmd == '2':
        show_links()
    elif cmd == '3':
        break
    else:
        print("Некорректный ввод.")

driver.quit()
