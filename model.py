import re
from datetime import datetime
import pytz


def get_house_info(text):
    lines = text.split('\n')

    # 使用正则表达式匹配价格格式：数字,数字円(数字,数字円)
    prices = []
    address = ""
    for i, line in enumerate(lines):
        if not address and "空室状況" in line and i > 0:
            address = lines[i-1]

        # 匹配主要价格（例如：72,600円）
        rent_match = re.search(r'(\d{2,3},\d{3})円', line)
        if rent_match:
            next_line = lines[i + 1] if i + 1 < len(lines) else ""
            # 匹配括号中的价格（例如：(4,000円)）
            maintenance_match = re.search(r'\((\d{1,3},\d{3})円\)', next_line)
            if maintenance_match:
                rent = rent_match.group(1)
                maintenance = maintenance_match.group(1)
                price_info = f"{rent}円({maintenance}円)"
                prices.append(price_info)
    address = address.split("ほか")[0]
    return address, prices

def convert_to_minutes(time_str):
    """将时间字符串转换为分钟数
    支持格式：
    - "1 時間 26 分" -> 86分钟
    - "58 分" -> 58分钟
    """
    total_minutes = 0
    
    # 处理包含小时的情况
    if "時間" in time_str:
        # 提取小时数
        hours = int(re.search(r'(\d+)\s*時間', time_str).group(1))
        total_minutes += hours * 60
    
    # 处理包含分钟的情况
    if "分" in time_str:
        # 提取分钟数
        minutes = int(re.search(r'(\d+)\s*分', time_str).group(1))
        total_minutes += minutes
    
    return total_minutes

def convert_to_minutes_en(time_str):
    """将时间字符串转换为分钟数
    支持格式：
    - "1 時間 26 分" -> 86分钟
    - "58 分" -> 58分钟
    """
    total_minutes = 0
    
    # 处理包含小时的情况
    if "hr" in time_str:
        # 提取小时数
        hours = int(re.search(r'(\d+)\s*hr', time_str).group(1))
        total_minutes += hours * 60
    
    # 处理包含分钟的情况
    if "min" in time_str:
        # 提取分钟数
        minutes = int(re.search(r'(\d+)\s*min', time_str).group(1))
        total_minutes += minutes
    
    return total_minutes

def sum_prices(price_str):
    """提取价格字符串中的两个数字并求和
    例如: "110,200円(2,300円)" -> 112500
    """
    # 使用正则表达式提取两个价格数字
    # 移除逗号后转换为整数
    prices = re.findall(r'(\d{1,3},\d{3})円', price_str)
    if len(prices) == 2:
        # 移除逗号并转换为整数
        rent = int(prices[0].replace(',', ''))
        maintenance = int(prices[1].replace(',', ''))
        total = rent + maintenance
        return total
    return None

def generate_html_table(data):
    # 获取日本时区的当前时间
    japan_tz = pytz.timezone('Asia/Tokyo')
    current_time = datetime.now(japan_tz).strftime("%Y-%m-%d %H:%M:%S")
    
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