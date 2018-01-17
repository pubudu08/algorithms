# Constants
TRADE_TYPE_SELL = 'SELL'
TRADE_TYPE_BUY = 'BUY'
THRESHOLD = 500000
PERIOD_THRESHOLD = 3


def feed_analyser(feed):
    """This method does following processes
            * Track trade logs using with respect to the market date
            * Cross check with the threshold value whether it flags as an insider trade
                * If so populate the flagged traders with respect to the market date

    """
    current_stock_price = 0
    log_trades = dict()
    insider_traders = set()
    noise_array = feed.split("\n")
    for item in noise_array:
        values = item.split("|")
        current_date = int(values[0])
        if len(values) == 2:
            current_stock_price = int(values[1])

            # Iterating all 3 days
            for day in range(current_date - PERIOD_THRESHOLD, current_date):
                if day in log_trades:
                    for (trader_name, _type, previous_amount, amount)
                    in log_trades[day]:
                        if (day, trader_name) in insider_traders:
                            continue
                        if TRADE_TYPE_BUY == _type and
                        (current_stock_price - previous_amount) * amount >= THRESHOLD:
                            insider_traders.add((day, trader_name))
                        elif TRADE_TYPE_SELL == _type and
                        (previous_amount - current_stock_price) * amount >= THRESHOLD:
                            insider_traders.add((day, trader_name))
        else:
            options = int(values[3])
            trader_name = values[1]
            process_type = values[2]
            if current_date not in log_trades:
                log_trades[current_date] = []
            log_trades[current_date].
            append((trader_name, process_type, current_stock_price, options))
    insider_traders = sorted(list(insider_traders))
    return string_builder(insider_traders)


def string_builder(flagged_trades):
    """ This method will reformat the elements based on the requested output"""
    temp_list = list()
    for x in flagged_trades:
        temp_list.append(str(x[0]) + '|' + str(x[1]))
    return temp_list


feed2 = """0|20
0|Kristi|SELL|300
0|Will|BUY|500
0|Tom|BUY|5000
0|Shilpa|BUY|150
1|Tom|BUY|150000
3|25
5|Shilpa|SELL|150
8|Kristi|SELL|60000
9|Shilpa|BUY|50
10|15
11|5
14|Will|BUY|10000
15|Will|BUY|10000
16|Will|BUY|10000
17|25"""

print(feed_analyser(feed2))

feed1 = """0|100
0|Shilpa|BUY|3000
0|Will|BUY|5000
0|Tom|BUY|4000
0|Kristi|BUY|1500
1|Kristi|BUY|1100
1|Tom|BUY|100
1|Will|BUY|1900
1|Shilpa|BUY|2500
2|150
2|Will|SELL|700
2|Shilpa|SELL|800
2|Kristi|SELL|600
2|Tom|SELL|900
3|500
38|100
78|Shilpa|BUY|3000
79|Kristi|BUY|6000
80|1100
81|1200"""

print(feed_analyser(feed1))
