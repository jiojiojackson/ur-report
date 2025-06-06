import re
from playwright.sync_api import Playwright, sync_playwright, expect
import time
from model import get_house_info, sum_prices, convert_to_minutes_en, generate_html_table
import requests



wait_milliseconds = 3000
addressY = "〒160-0021 東京都新宿区歌舞伎町２丁目１９−１３ Ask ビル"
addressZ = "みなとみらい駅"



def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch()
    context = browser.new_context()

    #修改
    houses = []
    page = context.new_page()
    page.goto("https://www.ur-net.go.jp/chintai/")
    page.locator("#js-pref_map").get_by_text("東京都").click()
    page.get_by_role("link", name="エリアから探す").click()
    page.wait_for_timeout(wait_milliseconds)
    page.get_by_role("heading", name="区南").locator("label").click()
    page.wait_for_timeout(wait_milliseconds)
    text_element = page.get_by_text("該当空室件数").nth(1)  # nth(1) 如果你确定要找第二个
    full_text = text_element.inner_text()

    # 用正则提取数字
    match = re.search(r"該当空室件数\s*：\s*(\d+)件", full_text)
    if match:
        count = int(match.group(1))
        print(f"空室件数为：{count}")
        if count > 0:
            # 点击搜索按钮
            page.get_by_role("button", name="この条件で検索する").nth(1).click()
            # 这里等待时间可以稍长一些，因为是搜索操作
            page.wait_for_timeout(wait_milliseconds*2)
            print("搜索完成")
            
            pages = page.locator(".js-module_searchs_property").all()
            print("获取到", len(pages), "个房源")
            
            for page in pages:
                text_content = page.text_content()
                text_content = re.sub(r'\s{2,}', '\n', text_content.strip())
                #修改
                if "駅 徒歩" not in text_content:
                    continue
                # 修改
                address, prices = get_house_info(text_content)
                try:
                    price = sum_prices(prices[0])
                except:
                    continue
                if price > 100000:
                    break
                houses.append({
                    "address": address,
                    "prices": prices
                })

    #修改

    page = context.new_page()
    page.goto("https://www.ur-net.go.jp/chintai/")
    page.locator("#js-pref_map").get_by_text("神奈川県").click()
    page.wait_for_timeout(wait_milliseconds)
    page.get_by_role("link", name="エリアから探す").click()
    page.wait_for_timeout(wait_milliseconds)
    # 点击川崎地区
    page.get_by_role("heading", name="川崎地区").locator("label").click()
    # 等待一小段时间确保点击生效
    page.wait_for_timeout(wait_milliseconds)
    
    # 点击横浜北部
    page.get_by_role("heading", name="横浜北部").locator("label").click()
    page.wait_for_timeout(wait_milliseconds)
    
    # 点击搜索按钮
    page.get_by_role("button", name="この条件で検索する").nth(1).click()
    # 这里等待时间可以稍长一些，因为是搜索操作
    page.wait_for_timeout(wait_milliseconds*2)
    print("搜索完成")
    
    pages = page.locator(".js-module_searchs_property").all()
    print("获取到", len(pages), "个房源")
    for page in pages:
        text_content = page.text_content()
        text_content = re.sub(r'\s{2,}', '\n', text_content.strip())
        #修改
        if "駅 徒歩" not in text_content:
            continue
        # 修改
        address, prices = get_house_info(text_content)
        print(prices)
        try:
            price = sum_prices(prices[0])
        except:
            continue
        if price > 100000:
            break
        houses.append({
            "address": address,
            "prices": prices
        })
    


    for house in houses:
        address = house["address"]
        print("开始计算", address, "到", addressY, "的时间")

        page = context.new_page()
        page.goto("https://www.google.com/maps/dir/")
        page.wait_for_timeout(wait_milliseconds)
        page.get_by_role("textbox", name="Choose starting point, or").fill(addressY)
        page.get_by_role("textbox", name="Choose destination, or click").fill(address)
        page.wait_for_timeout(wait_milliseconds)
        page.get_by_role("radio", name="Transit").click()
        page.wait_for_timeout(wait_milliseconds)
        link = page.get_by_role("link").nth(0)
        text = link.inner_text()
        lines = text.split('\n')
        time_cost = lines[1]
        house["time_costY"] = convert_to_minutes_en(time_cost)
        page.wait_for_timeout(wait_milliseconds)

        page = context.new_page()
        page.goto("https://www.google.com/maps/dir/")
        page.wait_for_timeout(wait_milliseconds)
        page.get_by_role("textbox", name="Choose starting point, or").fill(addressZ)
        page.get_by_role("textbox", name="Choose destination, or click").fill(address)
        page.wait_for_timeout(wait_milliseconds)
        page.get_by_role("radio", name="Transit").click()
        page.wait_for_timeout(wait_milliseconds*2)
        link = page.get_by_role("link").nth(0)
        text = link.inner_text()
        lines = text.split('\n')
        time_cost = lines[1]
        house["time_costZ"] = convert_to_minutes_en(time_cost)
        page.wait_for_timeout(wait_milliseconds)
    
    simple_houses = []
    for house in houses:
        simple_houses.append({
            "address": house["address"],
            "time_costY": house["time_costY"],
            "time_costZ": house["time_costZ"],
            "prices": sum_prices(house["prices"][0])
        })
    print(simple_houses)
    # 生成HTML
    html_content = generate_html_table(simple_houses)

    # 保存到文件
    with open('docs/index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)

    # 简单的GET请求
    response = requests.get('https://api.day.app/9C8dEGLSjiQEMe7Wk2pN6g/UR House?url=https://jiojiojackson.github.io/ur-report/')
    print(response.text)
        

    # 等待用户输入任意键后才继续

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)