from datetime import datetime

def generate_html_table(data):
    # 获取当前时间
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # HTML模板开始
    html_template = f"""
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>房产信息表</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 15px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            overflow: hidden;
        }}
        
        .header {{
            background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }}
        
        .header h1 {{
            margin: 0;
            font-size: 2.5em;
            font-weight: 300;
            text-shadow: 0 2px 4px rgba(0,0,0,0.3);
        }}
        
        .header p {{
            margin: 10px 0 0 0;
            font-size: 1.1em;
            opacity: 0.9;
        }}
        
        .table-container {{
            padding: 30px;
            overflow-x: auto;
        }}
        
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 0;
            background: white;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }}
        
        th {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px 15px;
            text-align: left;
            font-weight: 600;
            font-size: 1.1em;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}
        
        td {{
            padding: 18px 15px;
            border-bottom: 1px solid #e0e0e0;
            transition: all 0.3s ease;
        }}
        
        tr:hover {{
            background-color: #f8f9ff;
            transform: scale(1.01);
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }}
        
        tr:last-child td {{
            border-bottom: none;
        }}
        
        .address {{
            font-weight: 500;
            color: #2c3e50;
            font-size: 1.05em;
        }}
        
        .time-good {{
            color: #27ae60;
            font-weight: 600;
            background: linear-gradient(135deg, #a8e6cf 0%, #dcedc8 100%);
            padding: 8px 12px;
            border-radius: 20px;
            display: inline-block;
            position: relative;
        }}
        
        .time-good::before {{
            content: "✓";
            margin-right: 5px;
            font-weight: bold;
        }}
        
        .time-normal {{
            color: #e67e22;
            font-weight: 500;
            padding: 8px 12px;
            background: #fff3e0;
            border-radius: 20px;
            display: inline-block;
        }}
        
        .price {{
            font-weight: 600;
            color: #8e44ad;
            font-size: 1.1em;
            background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
            padding: 10px 15px;
            border-radius: 25px;
            display: inline-block;
        }}
        
        .stats {{
            display: flex;
            justify-content: space-around;
            padding: 20px;
            background: #f8f9fa;
            margin: 20px 0;
            border-radius: 10px;
        }}
        
        .stat-item {{
            text-align: center;
        }}
        
        .stat-number {{
            font-size: 2em;
            font-weight: bold;
            color: #667eea;
        }}
        
        .stat-label {{
            color: #6c757d;
            font-size: 0.9em;
            margin-top: 5px;
        }}
        
        @media (max-width: 768px) {{
            .header h1 {{
                font-size: 2em;
            }}
            
            th, td {{
                padding: 12px 8px;
                font-size: 0.9em;
            }}
            
            .stats {{
                flex-direction: column;
                gap: 15px;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🏠 房产信息表</h1>
            <p>生成时间: {current_time}</p>
        </div>
        
        <div class="table-container">
"""

    # 计算统计信息
    total_properties = len(data)
    avg_price = sum(item['prices'] for item in data) / len(data)
    good_commute_count = sum(1 for item in data if item['time_costY'] < 60 or item['time_costZ'] < 60)
    
    # 添加统计信息
    html_template += f"""
            <div class="stats">
                <div class="stat-item">
                    <div class="stat-number">{total_properties}</div>
                    <div class="stat-label">房产总数</div>
                </div>
                <div class="stat-item">
                    <div class="stat-number">¥{avg_price:,.0f}</div>
                    <div class="stat-label">平均价格</div>
                </div>
                <div class="stat-item">
                    <div class="stat-number">{good_commute_count}</div>
                    <div class="stat-label">优质通勤</div>
                </div>
            </div>
            
            <table>
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
        
        html_template += f"""
                    <tr>
                        <td class="address">{item['address']}</td>
                        <td>{y_display}</td>
                        <td>{z_display}</td>
                        <td>{price_formatted}</td>
                    </tr>
"""
    
    # HTML模板结束
    html_template += """
                </tbody>
            </table>
        </div>
    </div>
</body>
</html>
"""
    
    return html_template

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