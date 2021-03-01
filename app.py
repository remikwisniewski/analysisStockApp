from flask import Flask, request, render_template

def input_process(s):
    return eval(s)

def stop_loss_1_atr(low_price, average_true_range):
    return low_price - average_true_range

def stop_loss_2_atr(low_price, average_true_range):
    return low_price - average_true_range * 2

def stop_loss_3_atr(low_price, average_true_range):
    return low_price - average_true_range * 3

#########################################################################

def number_shares_1_atr(max_stop_loss, actual_price, low_price, average_true_range):
    return max_stop_loss / (actual_price - stop_loss_1_atr(low_price, average_true_range))

def number_shares_2_atr(max_stop_loss, actual_price, low_price, average_true_range):
    return max_stop_loss / (actual_price - stop_loss_2_atr(low_price, average_true_range))

def number_shares_3_atr(max_stop_loss, actual_price, low_price, average_true_range):
    return max_stop_loss / (actual_price - stop_loss_3_atr(low_price, average_true_range))

#########################################################################

def forex_lots_1_atr(max_stop_loss, actual_price, low_price, average_true_range):
    return max_stop_loss / (actual_price - stop_loss_1_atr(low_price, average_true_range)) / 100000

def forex_lots_2_atr(max_stop_loss, actual_price, low_price, average_true_range):
    return max_stop_loss / (actual_price - stop_loss_2_atr(low_price, average_true_range)) / 100000

def forex_lots_3_atr(max_stop_loss, actual_price, low_price, average_true_range):
    return max_stop_loss / (actual_price - stop_loss_3_atr(low_price, average_true_range)) / 100000

app = Flask(__name__)
@app.route('/')

@app.route('/')
def index():
    return render_template('stoploss.html')

@app.route('/', methods = ['POST'])
def request_data():
    actual_price_pre = input_process(request.form['actual_price_input'])
    average_true_range_pre = input_process(request.form['average_true_range_input'])
    low_price_pre = input_process(request.form['low_price_input'])
    max_stop_loss_pre = input_process(request.form['max_stop_loss_input'])

    stop_loss_1_atr_post = stop_loss_1_atr(low_price_pre, average_true_range_pre)
    stop_loss_2_atr_post = stop_loss_2_atr(low_price_pre, average_true_range_pre)
    stop_loss_3_atr_post = stop_loss_3_atr(low_price_pre, average_true_range_pre)

    number_shares_1_atr_post = round(number_shares_1_atr(max_stop_loss_pre, actual_price_pre, low_price_pre, average_true_range_pre))
    number_shares_2_atr_post = round(number_shares_2_atr(max_stop_loss_pre, actual_price_pre, low_price_pre, average_true_range_pre))
    number_shares_3_atr_post = round(number_shares_3_atr(max_stop_loss_pre, actual_price_pre, low_price_pre, average_true_range_pre))

    forex_lots_1_atr_post = round(forex_lots_1_atr(max_stop_loss_pre, actual_price_pre, low_price_pre, average_true_range_pre))
    forex_lots_2_atr_post = round(forex_lots_2_atr(max_stop_loss_pre, actual_price_pre, low_price_pre, average_true_range_pre))
    forex_lots_3_atr_post = round(forex_lots_3_atr(max_stop_loss_pre, actual_price_pre, low_price_pre, average_true_range_pre))

    # return render_template('stoploss.html', sl1atr = stop_loss_1_atr_post, sl2atr = stop_loss_2_atr_post#,
    #                     # sl3atr = stop_loss_3_atr_post, ns1atr = number_shares_1_atr_post, ns2atr = number_shares_2_atr_post,
    #                     # ns3atr = number_shares_3_atr_post, fl1atr = forex_lots_1_atr_post, fl2atr = forex_lots_2_atr_post,
    #                     # fl3atr = forex_lots_3_atr_post)
    return render_template('stoploss.html', sl1atr = stop_loss_1_atr_post, sl2atr = stop_loss_2_atr_post,
                        sl3atr = stop_loss_3_atr_post, ns1atr = number_shares_1_atr_post, ns2atr = number_shares_2_atr_post,
                        ns3atr = number_shares_3_atr_post, fl1atr = forex_lots_1_atr_post, fl2atr = forex_lots_2_atr_post,
                        fl3atr = forex_lots_3_atr_post)

def main():
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug = True, use_reloader = True)
main()