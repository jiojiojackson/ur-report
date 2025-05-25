# 🏠 房产信息表

<style>
.property-table {
    width: 100%;
    border-collapse: collapse;
    margin: 20px 0;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: white;
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
}

.property-table th {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 15px 12px;
    text-align: left;
    font-weight: 600;
    font-size: 1.1em;
}

.property-table td {
    padding: 12px;
    border-bottom: 1px solid #e0e0e0;
    transition: all 0.3s ease;
}

.property-table tr:hover {
    background-color: #f8f9ff;
}

.property-table tr:last-child td {
    border-bottom: none;
}

.time-good {
    color: #27ae60;
    font-weight: 600;
    background: linear-gradient(135deg, #a8e6cf 0%, #dcedc8 100%);
    padding: 6px 10px;
    border-radius: 15px;
    display: inline-block;
}

.time-good::before {
    content: "✓ ";
    font-weight: bold;
}

.time-normal {
    color: #e67e22;
    font-weight: 500;
    padding: 6px 10px;
    background: #fff3e0;
    border-radius: 15px;
    display: inline-block;
}

.price {
    font-weight: 600;
    color: #8e44ad;
    background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
    padding: 8px 12px;
    border-radius: 20px;
    display: inline-block;
}

.address {
    font-weight: 500;
    color: #2c3e50;
}

.stats-container {
    display: flex;
    justify-content: space-around;
    margin: 20px 0;
    padding: 20px;
    background: #f8f9fa;
    border-radius: 10px;
    border-left: 4px solid #667eea;
}

.stat-item {
    text-align: center;
}

.stat-number {
    font-size: 1.8em;
    font-weight: bold;
    color: #667eea;
    margin: 0;
}

.stat-label {
    color: #6c757d;
    font-size: 0.9em;
    margin: 5px 0 0 0;
}

.header-info {
    background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
    color: white;
    padding: 20px;
    margin: 20px 0;
    border-radius: 10px;
    text-align: center;
}

.header-info h2 {
    margin: 0;
    font-weight: 300;
}

.header-info p {
    margin: 10px 0 0 0;
    opacity: 0.9;
}
</style>

<div class="header-info">
<h2>房产信息汇总报告</h2>
<p>生成时间: 2025-05-25 09:31:55</p>
</div>


<div class="stats-container">
    <div class="stat-item">
        <p class="stat-number">7</p>
        <p class="stat-label">房产总数</p>
    </div>
    <div class="stat-item">
        <p class="stat-number">¥79,343</p>
        <p class="stat-label">平均价格</p>
    </div>
    <div class="stat-item">
        <p class="stat-number">0</p>
        <p class="stat-label">优质通勤房产</p>
    </div>
    <div class="stat-item">
        <p class="stat-number">¥66,500 - ¥98,400</p>
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
<tr>
<td class="address">横浜市神奈川区菅田町488</td>
<td><span class="time-normal">89分钟</span></td>
<td><span class="time-normal">82分钟</span></td>
<td><span class="price">¥66,500</span></td>
</tr>
<tr>
<td class="address">横浜市青葉区奈良町2913</td>
<td><span class="time-normal">73分钟</span></td>
<td><span class="time-normal">111分钟</span></td>
<td><span class="price">¥74,000</span></td>
</tr>
<tr>
<td class="address">川崎市麻生区虹ケ丘2-2</td>
<td><span class="time-normal">81分钟</span></td>
<td><span class="time-normal">82分钟</span></td>
<td><span class="price">¥75,100</span></td>
</tr>
<tr>
<td class="address">横浜市神奈川区神大寺2-9</td>
<td><span class="time-normal">84分钟</span></td>
<td><span class="time-normal">98分钟</span></td>
<td><span class="price">¥74,000</span></td>
</tr>
<tr>
<td class="address">横浜市青葉区すすき野3-6-1</td>
<td><span class="time-normal">77分钟</span></td>
<td><span class="time-normal">85分钟</span></td>
<td><span class="price">¥80,700</span></td>
</tr>
<tr>
<td class="address">横浜市緑区霧が丘3-22-5</td>
<td><span class="time-normal">88分钟</span></td>
<td><span class="time-normal">101分钟</span></td>
<td><span class="price">¥86,700</span></td>
</tr>
<tr>
<td class="address">川崎市多摩区菅北浦5-7</td>
<td><span class="time-normal">67分钟</span></td>
<td><span class="time-normal">105分钟</span></td>
<td><span class="price">¥98,400</span></td>
</tr>
</tbody>
</table>


