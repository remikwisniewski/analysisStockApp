def calculate_stop_loss():

    actual_price = float(input("Actual price: "))
    low_price = float(input("Low price: "))
    average_true_range = float(input("Average true range: "))
    max_stop_loss = float(input("Max Stoploss in $: "))

    stoploss_1_atr = low_price - average_true_range
    stoploss_2_atr = low_price - average_true_range * 2
    stoploss_3_atr = low_price - average_true_range * 3

    num_shares_1_atr = max_stop_loss / (actual_price - stoploss_1_atr)
    num_shares_2_atr = max_stop_loss / (actual_price - stoploss_2_atr)
    num_shares_3_atr = max_stop_loss / (actual_price - stoploss_3_atr)

    forex_lots_1_atr = (max_stop_loss / (actual_price - stoploss_1_atr)) / 100000
    forex_lots_2_atr = (max_stop_loss / (actual_price - stoploss_2_atr)) / 100000
    forex_lots_3_atr = (max_stop_loss / (actual_price - stoploss_3_atr)) / 100000

    print("Actual price: ", actual_price)
    print("Low price: ", low_price)
    print("Average true range: ", average_true_range)
    print("Max stop loss in $: ", max_stop_loss)

    print("-----------------------------------------")

    print("Stoploss 1 ATR: ", stoploss_1_atr)
    print("Number of shares: ", num_shares_1_atr)
    print("Forex Lots: ", forex_lots_1_atr)

    print("*************************")

    print("Stoploss 2 ATR: ", stoploss_2_atr)
    print("Number of shares: ", num_shares_2_atr)
    print("Forex Lots: ", forex_lots_2_atr)    

    print("*************************")

    print("Stoploss 3 ATR: ", stoploss_3_atr)
    print("Number of shares: ", num_shares_3_atr)
    print("Forex Lots: ", forex_lots_3_atr)

def main():
    calculate_stop_loss()
main()