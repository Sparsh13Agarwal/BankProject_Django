import json
def read_data():
    with open('/Users/sparshagarwal/Desktop/Bank5/Bank 5/find_details.txt','r') as f:
        data = f.read()
    js = json.loads(data)
    return js
def write_data(gen_data):
    with open('/Users/sparshagarwal/Desktop/Bank5/Bank 5/find_details.txt','w') as f:
        f.write(json.dumps(gen_data))

def generate_customer_id_acc_id():
    try: 
        gen_data = read_data()
        cust_id = "DDB" + str(gen_data['cust_id'])
        gen_data['cust_id'] = gen_data['cust_id'] + 1
        acc_no = gen_data['acc_no']
        gen_data['acc_no'] = gen_data['acc_no'] +1
        write_data(gen_data)
        return cust_id,acc_no
    except Exception as err:
        print(err)
        
        

def generate_transaction_id():
    gen_data = read_data()
    trans_id = "TRANS" + str(gen_data['trans'])
    gen_data['trans'] = gen_data['trans'] + 1
    write_data(gen_data)
    return trans_id
