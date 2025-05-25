from datetime import datetime

def generate_styled_markdown(data):
    # 获取当前时间
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Markdown文件开始，包含HTML样式
    markdown_content = f"""# 🏠 房产信息表

<style>
.property-table {{
    width: 100%;
    border-collapse: collapse;
    margin: 20px 0;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: white;
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
}}

.property-table th {{
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 15px 12px;
    text-align: left;
    font-weight: 600;
    font-size: 1.1em;
}}

.property-table td {{
    padding: 12px;
    border-bottom: 1px solid #e0e0e0;
    transition: all 0.3s ease;
}}

.property-table tr:hover {{
    background-color: #f8f9ff;
}}

.property-table tr:last-child td {{
    border-bottom: none;
}}

.time-good {{
    color: #27ae60;
    font-weight: 600;
    background: linear-gradient(135deg, #a8e6cf 0%, #dcedc8 100%);
    padding: 6px 10px;
    border-radius: 15px;
    display: inline-block;
}}

.time-good::before {{
    content: "✓ ";
    font-weight: bold;
}}

.time-normal {{
    color: #e67e22;
    font-weight: 500;
    padding: 6px 10px;
    background: #fff3e0;
    border-radius: 15px;
    display: inline-block;
}}

.price {{
    font-weight: 600;
    color: #8e44ad;
    background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
    padding: 8px 12px;
    border-radius: 20px;
    display: inline-block;
}}

.address {{
    font-weight: 500;
    color: #2c3e50;
}}

.stats-container {{
    display: flex;
    justify-content: space-around;
    margin: 20px 0;
    padding: 20px;
    background: #f8f9fa;
    border-radius: 10px;
    border-left: 4px solid #667eea;
}}

.stat-item {{
    text-align: center;
}}

.stat-number {{
    font-size: 1.8em;
    font-weight: bold;
    color: #667eea;
    margin: 0;
}}

.stat-label {{
    color: #6c757d;
    font-size: 0.9em;
    margin: 5px 0 0 0;
}}

.header-info {{
    background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
    color: white;
    padding: 20px;
    margin: 20px 0;
    border-radius: 10px;
    text-align: center;
}}

.header-info h2 {{
    margin: 0;
    font-weight: 300;
}}

.header-info p {{
    margin: 10px 0 0 0;
    opacity: 0.9;
}}
</style>

<div class="header-info">
<h2>房产信息汇总报告</h2>
<p>生成时间: {current_time}</p>
</div>

"""

    # 计算统计信息
    total_properties = len(data)
    avg_price = sum(item['prices'] for item in data) / len(data)
    good_commute_count = sum(1 for item in data if item['time_costY'] < 60 or item['time_costZ'] < 60)
    min_price = min(item['prices'] for item in data)
    max_price = max(item['prices'] for item in data)
    
    # 添加统计信息
    markdown_content += f"""
<div class="stats-container">
    <div class="stat-item">
        <p class="stat-number">{total_properties}</p>
        <p class="stat-label">房产总数</p>
    </div>
    <div class="stat-item">
        <p class="stat-number">¥{avg_price:,.0f}</p>
        <p class="stat-label">平均价格</p>
    </div>
    <div class="stat-item">
        <p class="stat-number">{good_commute_count}</p>
        <p class="stat-label">优质通勤房产</p>
    </div>
    <div class="stat-item">
        <p class="stat-number">¥{min_price:,} - ¥{max_price:,}</p>
        <p class="stat-label">价格区间</p>
    </div>
</div>

## 📊 详细信息表格

<table class="property-table">
<thead>
<tr>
<th>📍 地址</th>
<th>🚇 Y点通勤时间</th>
<th>🚇 Z点通勤时间</th>
<th>💰 价格</th>
</tr>
</thead>
<tbody>
"""
    
    # 生成表格行
    for item in data:
        y_time = item['time_costY']
        z_time = item['time_costZ']
        
        # 处理通勤时间显示
        y_class = "time-good" if y_time < 60 else "time-normal"
        z_class = "time-good" if z_time < 60 else "time-normal"
        
        y_display = f'<span class="{y_class}">{y_time}分钟</span>'
        z_display = f'<span class="{z_class}">{z_time}分钟</span>'
        
        # 格式化价格
        price_formatted = f'<span class="price">¥{item["prices"]:,}</span>'
        
        markdown_content += f"""<tr>
<td class="address">{item['address']}</td>
<td>{y_display}</td>
<td>{z_display}</td>
<td>{price_formatted}</td>
</tr>
"""
    
    # 结束表格
    markdown_content += """</tbody>
</table>


"""
    
    return markdown_content

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

# 生成带样式的Markdown
styled_markdown = generate_styled_markdown(data)

# 保存到Markdown文件
with open('property_report.md', 'w', encoding='utf-8') as f:
    f.write(styled_markdown)

print("带样式的Markdown报告已生成并保存到 property_report.md 文件中")
print("可以用支持HTML的Markdown查看器打开，如：")
print("- GitHub")
print("- Typora") 
print("- Mark Text")
print("- VS Code的Markdown预览")