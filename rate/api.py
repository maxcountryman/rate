from flask import Blueprint, jsonify, request

import requests


api = Blueprint('api', __name__)

ORDER_DEPTH_URI = 'http://data.mtgox.com/api/1/BTCUSD/depth/fetch'


def get_rate(amount, type='asks'):
    data = requests.get(ORDER_DEPTH_URI).json()['return'][type]
    data = sorted(data, key=lambda d: d['price'], reverse=(type == 'bids'))

    sum_amounts = 0
    amounts = []
    prices = []
    for o in data:
        amounts.append(o['amount'])
        prices.append(o['price'])
        sum_amounts += amounts[-1]
        if sum_amounts >= amount:
            break

    return sum(o[0] * o[1] for o in zip(prices, amounts)) / sum(amounts)


@api.route('/rate', methods=['POST'])
def rate():
    type = request.form.get('type')
    amount = request.form.get('amount', type=float)

    if None in (type, amount):
        return jsonify({'error': 'missing param'})

    if type not in ('bids', 'asks'):
        return jsonify({'error': 'type must be one of `asks`, `bids`'})

    rate = get_rate(amount, type=type)
    if rate is None:
        return jsonify({'error': 'error calculating exchange rate'})

    amount = amount * rate if type == 'bids' else amount / rate
    return jsonify({'rate': rate, 'amount': amount})
