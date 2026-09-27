from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/links/10")
    sleep(3)

    links = driver.find_elements(By.TAG_NAME, "a")

    assert len(links) == 9, f"Должно отображаться 9 ссылок, но найдено {len(links)}"

    for i, link in enumerate(links, 1):
        assert link.is_displayed(), f"Ссылка №{i} не найдена"

    first_link_text = links[0].text
    assert "1" in first_link_text, f"Текст первой ссылки '{first_link_text}' не содержит '1'"

    sleep(3)

    driver.quit()





