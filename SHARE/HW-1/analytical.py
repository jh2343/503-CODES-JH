#IMPORT
import pandas as pd

# NOTES:
# FIRST MANUALLY REMANE
# rename "id" column in various files using filename  
#		--> loan_id  link_id ... etc
# ALSO: UNIT OF ANALYSIS=ACCOUNT --> columns=variables associated with accounts

#---------------------------------
#READ ACCOUNTS 
#---------------------------------
dfA = pd.read_csv('data/accounts.csv')
print("ACCOUNTS\n",dfA)

#RENAME id
dfA=dfA.rename(columns={"id": "account_id"})
dfA=dfA.rename(columns={"date": "open_date"})

#---------------------------------
#CONVERT DISRICT ID TO DISTRICT NAME
#---------------------------------

dfD = pd.read_csv('districts_py.csv')
dfD = dfD[['district_id','name']]
dfD=dfD.rename(columns={"name": "district_name"})

dfA=dfA.merge(dfD, how='left'); #print("ACCOUNTS\n",dfA)
dfA.to_csv('tmp.csv',index=False)  
dfA=dfA.drop('district_id',axis=1);

#--------------------------------- 
# num_customers: 
# The total number of clients associated with the account (owner and users)
#---------------------------------
#READ LINKS
dfL = pd.read_csv('data/links.csv')
# print("LINKS\n",dfL.iloc[0:20])

#RENAME id
dfL=dfL.rename(columns={"id": "link_id"})

#SORT BY ACCOUNT THEN COUNT THE NUMBER OF ENTRIES=ACCOUNT'SNUMBER OF CLIENTS 
tmp  = dfL.groupby('account_id')['account_id'].count()

#CONERT SERIES TO DATA FRAME
tmp  = pd.DataFrame({'account_id':tmp.index, 'num_customers':tmp.values}); # print(tmp)

#JOIN
print("SHAPE:", dfA.shape,tmp.shape)
dfA=dfA.merge(tmp, how='left'); #print("ACCOUNTS\n",dfA)

#---------------------------------
# credit_cards: Number of credit cards for an account or zero if none
#---------------------------------

#READ 
dfC = pd.read_csv('data/cards.csv')

#RENAME
dfC=dfC.rename(columns={"id": "card_id"})

#RENAME TO AVOID CONFLICT WITH "type" OWNER from links.csv
dfC = dfC.rename(columns={"type": "card_type"})
#print(dfL); print(dfC)

#JOIN LINKS AND CARDS
tmp=dfL.merge(dfC, how='inner')
# print(tmp.groupby('account_id').head())

#GROUP BY ACCOUNT-ID THEN COUNT THE NUMBER OF ENTRIES=CARDS PER ACCOUNT 
tmp  = tmp.groupby('account_id')['account_id'].count()
tmp  = pd.DataFrame({'account_id':tmp.index, 'credit_cards':tmp.values}); # print(tmp)
#print(tmp); tmp.to_csv('tmp.csv',index=False)  

#JOIN
print("SHAPE:", dfA.shape,tmp.shape)
dfA = dfA.merge(tmp, how='left')

#CONVERT NaN TO ZERO FOR THIS COLUMN
dfA["credit_cards"]=dfA["credit_cards"].fillna(0)

#---------------------------------
#loan: T/F if the account has a loan
#---------------------------------
dfl = pd.read_csv('loans_py.csv')
#print("LOANS\n",dfl.iloc[0:20])

#CHECK IF THERE IS ONLY 1 LOAN PER ACCOUNT (THERE IS)
# tmp  = dfl.groupby('account_id')['account_id'].count()
# tmp.to_csv('tmp.csv',index=False)  

#SELECT REQUIRED COLUMNS FROM LOANS
dfl=dfl[['account_id','loan_amount','loan_payments','loan_term','loan_status','loan_default']]; 

#MAKE A NEW COLUMN
dfl['loan'] = True

#MERGE
dfA=dfA.merge(dfl, how='left')

#REPLACE NaN AS NEEDED
dfA["loan"]=dfA["loan"].fillna('False')
dfA =dfA.fillna("NA")
print("ACCOUNTS\n",dfA.iloc[50:70])

#---------------------------------
# max_withdrawal: Maximum amount withdrawn for the account
# min_withdrawal: Minimum amount withdrawn for the account
#---------------------------------

#transaction_id,account_id,date,type,amount,balance,bank,account,method,category
#58,1,1995-09-05,debit,2452,19035,YZ,87144583,bank transfer,household payment

#READ
dft = pd.read_csv('data/transactions.csv')
print("TRANSACTIONS\n",dft.iloc[0:20])

#RENAME
dft=dft.rename(columns={"id": "transaction_id"})

#ISOLATED WITHDRAWLS 
w =  dft[dft.type=='debit']; #print(w)

#GET MIN/MAX WITHDRAWLS FOR EACH ACCOUNT
min_max_w  = pd.DataFrame(w.groupby('account_id')['amount'].min())
min_max_w  = pd.DataFrame({'account_id':min_max_w.index, 'min_withdrawal':min_max_w.amount}); # print(tmp)
min_max_w['max_withdrawal']=w.groupby('account_id')['amount'].max()
min_max_w.index.name = None
# print(min_max_w)

#SWITCH ORDER
min_max_w=min_max_w[['account_id','max_withdrawal','min_withdrawal']]

#JOIN
dfA=dfA.merge(min_max_w, how='left')
print(dfA)


#---------------------------------
# cc_payments: Count of credit payments for the account for all cards
#---------------------------------

#ISOLATE WITHDRAWLS WITH METHOD=CREDIT CARD
w =  w[w.method=='credit card']; #print(w)

#GET NUMBER OF PAYMENTS
num_payments = pd.DataFrame(w.groupby('account_id')['account_id'].count())
num_payments = pd.DataFrame({'account_id':num_payments.index, 'cc_payments':num_payments.account_id}); # print(tmp)
num_payments.index.name = None
print(num_payments)

#JOIN
dfA=dfA.merge(num_payments, how='left')
print(dfA.iloc[0:15])

#---------------------------------
# max_balance: Maximum balance in the account
# min_balance: Minimum balance in the account
#---------------------------------

#GET MIN/MAX BALANCE FOR EACH ACCOUNT
min_max_b = pd.DataFrame(dft.groupby('account_id')['balance'].min())
min_max_b = pd.DataFrame({'account_id':min_max_b.index, 'min_balance':min_max_b.balance}); # print(tmp)
min_max_b['max_balance']=dft.groupby('account_id')['balance'].max()
min_max_b.index.name = None
# print(min_max_b)

#SWITCH ORDER
min_max_b=min_max_b[['account_id','max_balance','min_balance']]

#JOIN
dfA=dfA.merge(min_max_b, how='left')
# print(dfA)

#SAVE
dfA.to_csv('analytical_py.csv',index=False)  
print("END\n",dfA)
exit()

