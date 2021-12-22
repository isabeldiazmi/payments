import pandas as pd


data1 = pd.read_csv('/Users/isabeldiazmiranda/OneDrive/Jeeves/PaymentsScript/STP.csv', encoding= 'unicode_escape')
STP = data1.filter(['org_id', 'date', 'amount_platform', 'amount_local'], axis=1)
STP['bank_code'] = "STP"
STP.insert(1,'stmt_ID',"")
STP.insert(2,'stmt_status',"")
STP.insert(4,'pmt_currency',"MXN")

data2 = pd.read_csv('/Users/isabeldiazmiranda/OneDrive/Jeeves/PaymentsScript/RBC.csv', encoding= 'unicode_escape')
RBC = data2.filter(['org_id', 'date', 'amount_platform', 'amount_local'], axis=1)
RBC['bank_code'] = "RBC"
RBC.insert(1,'stmt_ID',"")
RBC.insert(2,'stmt_status',"")
RBC.insert(4,'pmt_currency',"")

frames = [STP, RBC]
allPayments = pd.concat(frames)
allPayments.to_csv('paymentsToCMS.csv')

#print(allPayments)