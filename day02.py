#===============
# Section 1: Fuctions yang benar
#===============

def calculate_average(number:list) -> float:
    '''Hitung rata-rata dari list angka.'''
    if not number:
        return 0.0
    return sum(number) / len(number)

def format_currency(amount:float, currency:str = 'IDR') -> str:
    '''Format angka jadi stirng mata uang.'''
    return f'{currency} {amount:,.0f}'

#test

scores =[85,90,78,92,88]
print(calculate_average(scores))
print(calculate_average([]))
print(format_currency(5000000))
print(format_currency(99.99, 'USD'))

#===============
# Section 2: Dictionary & List - pola AI Engineer
#===============

customer = [
    {'id': 1,'name': 'Budi', 'plan': 'premium','score': 88},
    {'id': 2,'name': 'Sari','plan': 'free', 'score': 45},
    {'id': 3,'name': 'Tono','plan':'premium','score':92},
    {'id': 4,'name': 'Dewi', 'plan':'free', 'score': 30},
    {'id': 5,'name': 'Andi', 'plan': 'premium', 'score':76},
]

#1. FIlter
premium_customer = [c for c in customer if c['plan'] =='premium']
print('Premium:', premium_customer)

#2. Extract
names = [c['name'] for c in customer]
print('names:', names)

#Sort
sorted_customers = sorted(customer, key=lambda x: x['score'], reverse=True)
print('Top customer:', sorted_customers[0]['name'])

#4. Transform
for c in customer: 
    c['risk'] = 'high' if c['score'] < 50 else 'low'

#5. Find
def find_customer(customer_list:list, customer_id: int) -> dict:
    '''Cari customer berdasarkan ID.'''
    return next((c for c in customer_list if c['id'] == customer_id), None)

print('Find id=2:', find_customer(customer,2))
print('Find id=99:', find_customer(customer,99))

#===============
# Section 3 : JSON -format data AI & API
#===============

import json

api_respons = {
    'model' : 'gpt-4',
    'usage' : {
        'prompt_tokens' : 150,
        'completion_tokens' : 80,
        'total_tokens': 230
    },
    'message' : {
        'role': 'assistant',
        'content' : 'Berdasakan data, customer Sari berisiko Churn.'
    }
}

#1. Dict -> JSON string
json_string = json.dumps(api_respons, indent=2)
print('JSON String:')

#2. JSON string -> Dict
parsed =json.loads(json_string)
print('\nContent:', parsed['message']['content'])
print('Total tokens used:', parsed['usage']['total_tokens'])

#3. Simpan ke file JSON
with open('data/sample_respons.json','w') as f:
    json.dump(api_respons,f, indent=2)
    print('\nFIle saved!')

#4. Baca dari file JSON
with open('data/sample_respons.json','r') as f:
    loaded = json.load(f)
print('Loaded from file:' , loaded['model'])

#===============
# Section 4 : Erro Handling - kode yang tidak mudah crash
#===============

def safe_divide(a: float, b: float) -> float:
    ''' Pembagian yang aman - tidak crash kalu b=0.'''
    try:
        return a/b
    except ZeroDivisionError:
        print ('Error: tidak bisa dibagi 0')
        return 0.0
    
def safe_get_customer(customer_list: list, customer_id: int) -> dict:
        '''Ambil customer dengan error handling lengkap.'''
        try:
            customer = find_customer(customer_list,customer_id)
            if customer is None:
                raise ValueError(f'Customer ID {customer_id} tidak ditemukan')
            return customer
        except ValueError as e:
            print(f'Warning: {0}')
            return{}
        
#Test
print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_get_customer(customer, 1))
print(safe_get_customer(customer, 99))

#Latihan

{
    'total_customer': 5,
    'high_risk_count': 2,
    'high_risk_names': ['Sari', 'Dewi'],
    'average_score': 66.2
}

def analyze_churn_risk(customers):
    high_risk = [c for c in customers if c['score'] < 50]
    high_risk_names = [c['name'] for c in high_risk]
    total_customers = len(customers)
    scores = [c['score'] for c in customers]
    average_score = calculate_average(scores)

    return {
        'total_customers': total_customers,
        'high_risk_count': len(high_risk),
        'high_risk_names': high_risk_names,
        'average_scores': calculate_average(scores)
    }
result = analyze_churn_risk(customer)
print(result)