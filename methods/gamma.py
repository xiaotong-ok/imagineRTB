import numpy as np
import scipy.stats as stats
from scipy.stats import gamma


def gamma_test(train_file_dict, test_file_dict, budget):
    click = list(test_file_dict['data']['click'])
    winning_bids = list(test_file_dict['data']['winprice'])
    impressions = 0
    clicks = 0
    cost = 0
    win_rate = 0
    ecpc = 0
    ecpi = 0

    param = np.array(list(train_file_dict['data']['winprice'])).mean()  
    for i in range(test_file_dict['imp']):
        bid = np.random.gamma(param,param)
        # bid = gamma.ppf(ctr_estimations[i], shape_parameter, scale=scale_parameter)
        if bid > winning_bids[i] and bid < budget:
            impressions += 1
            budget -= winning_bids[i]
            clicks += click[i]
            cost += winning_bids[i]
            win_rate += 1 / test_file_dict['imp']
        else:
            continue     

    if clicks > 0:
        ecpc = cost / clicks
        cer = clicks**2 / cost
        wrc = win_rate / cost
    else:
        cer = 0
        wrc = 0
    if impressions > 0:
        ecpi = cost / impressions

    print("testing Gamma--- click: {}, win_rate: {}, ecpc: {}, cer:{}, wrc:{}".format(clicks, win_rate, ecpc, cer, wrc))
        
    return impressions, clicks, cost, win_rate, ecpc, ecpi, cer, wrc