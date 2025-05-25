from model import generate_html_table

# 你的数据
data = [
    {'address': '横浜市神奈川区菅田町488', 'time_costY': 89, 'time_costZ': 82, 'prices': 66500},
    {'address': '横浜市青葉区奈良町2913', 'time_costY': 73, 'time_costZ': 111, 'prices': 74000},
    {'address': '川崎市麻生区虹ケ丘2-2', 'time_costY': 81, 'time_costZ': 82, 'prices': 75100},
    {'address': '横浜市神奈川区神大寺2-9', 'time_costY': 84, 'time_costZ': 98, 'prices': 74000},
    {'address': '横浜市青葉区すすき野3-6-1', 'time_costY': 77, 'time_costZ': 85, 'prices': 80700},
    {'address': '横浜市緑区霧が丘3-22-5', 'time_costY': 88, 'time_costZ': 101, 'prices': 86700},
    {'address': '川崎市多摩区菅北浦5-7', 'time_costY': 67, 'time_costZ': 105, 'prices': 98400}
]

# 生成HTML表格
html_result = generate_html_table(data)

# 保存到文件
with open('docs/index.html', 'w', encoding='utf-8') as f:
    f.write(html_result)

print("美观的HTML表格已生成并保存到 property_table.html 文件中")
print("请用浏览器打开该文件查看效果")