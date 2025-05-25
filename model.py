import re


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
    # CSS样式
    css_style = """
    <style>
        .property-table {
            border-collapse: collapse;
            width: 100%;
            margin: 20px 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
            overflow: hidden;
        }
        
        .property-table th {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            font-weight: bold;
            text-align: center;
            padding: 15px 10px;
            font-size: 14px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        .property-table td {
            text-align: center;
            padding: 12px 10px;
            border-bottom: 1px solid #e0e0e0;
            font-size: 13px;
        }
        
        .property-table tr:nth-child(even) {
            background-color: #f8f9fa;
        }
        
        .property-table tr:hover {
            background-color: #e3f2fd;
            transform: scale(1.01);
            transition: all 0.2s ease;
        }
        
        .time-good {
            background-color: #4CAF50 !important;
            color: white;
            font-weight: bold;
            border-radius: 4px;
            padding: 6px 8px;
        }
        
        .time-normal {
            background-color: #FF9800;
            color: white;
            border-radius: 4px;
            padding: 6px 8px;
        }
        
        .address-cell {
            text-align: left;
            font-weight: 500;
            color: #333;
        }
        
        .price-cell {
            font-weight: bold;
            color: #2E7D32;
            font-size: 14px;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        
        .title {
            text-align: center;
            color: #333;
            margin-bottom: 20px;
            font-size: 24px;
            font-weight: 300;
        }
    </style>
    """
    
    # HTML开始
    html = f"""
    <!DOCTYPE html>
    <html lang="ja">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>房产信息表格</title>
        {css_style}
    </head>
    <body>
        <div class="container">
            <h1 class="title">🏠 房产信息一览表</h1>
            <table class="property-table">
                <thead>
                    <tr>
                        <th>地址</th>
                        <th>通勤时间Y (分钟)</th>
                        <th>通勤时间Z (分钟)</th>
                        <th>价格 (円)</th>
                    </tr>
                </thead>
                <tbody>
    """
    
    # 生成表格行
    for item in data:
        # 判断时间成本的样式类
        time_y_class = "time-good" if item['time_costY'] < 60 else "time-normal"
        time_z_class = "time-good" if item['time_costZ'] < 60 else "time-normal"
        
        # 格式化价格
        formatted_price = f"¥{item['prices']:,}"
        
        html += f"""
                    <tr>
                        <td class="address-cell">{item['address']}</td>
                        <td><span class="{time_y_class}">{item['time_costY']}</span></td>
                        <td><span class="{time_z_class}">{item['time_costZ']}</span></td>
                        <td class="price-cell">{formatted_price}</td>
                    </tr>
        """
    
    # HTML结束
    html += """
                </tbody>
            </table>
        </div>
    </body>
    </html>
    """
    
    return html