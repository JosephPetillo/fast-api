from flask import Flask, request 
import pandas as pd 

df = pd.read_csv('./data/provider012622.csv')

app = Flask(__name__)

@app.route('/', methods=["GET"])
def home():
    return 'this is a API service for MN provider code details'

@app.route('/preview', methods=["GET"])
def preview():
    top10rows = df.head(1)
    result = top10rows.to_json(orient="records")
    return result

@app.route('/provider/<value>', methods=['GET'])
def icdcode(value):
    print('value: ', value)
    filtered = df[df['UNIQUE_PROVIDERS'] == value]
    if len(filtered) <= 0:
        return 'There is nothing here'
    else: 
        return filtered.to_json(orient="records")

@app.route('/provider/<value>/cd/<value2>')
def icdcode2(value, value2):
    filtered = df[df['UNIQUE_PROVIDERS'] == value]
    filtered2 = filtered[filtered['PROVIDER_TYPE_CD'] == value2]
    if len(filtered2) <= 0:
        return 'There is nothing here'
    else: 
        return filtered2.to_json(orient="records")    
    

if __name__ == '__main__':
    app.run(debug=True)
