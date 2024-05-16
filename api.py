from flask import Flask,render_template,flash,request,jsonify
import requests


app = Flask(__name__)
app.secret_key='sethu'
tag = """<select name="state" class="input" required="required" id="OutletState"><option value="">All</option><option value="andhra-pradesh">Andhra Pradesh</option><option value="arunachal-pradesh">Arunachal Pradesh</option><option value="assam">Assam</option><option value="bihar">Bihar</option><option value="chandigarh">Chandigarh</option><option value="chhattisgarh">Chhattisgarh</option><option value="delhi">Delhi</option><option value="goa">Goa</option><option value="gujarat">Gujarat</option><option value="haryana">Haryana</option><option value="himachal-pradesh">Himachal Pradesh</option><option value="jammu-and-kashmir">Jammu And Kashmir</option><option value="jharkhand">Jharkhand</option><option value="karnataka">Karnataka</option><option value="kerala">Kerala</option><option value="ladakh">Ladakh</option><option value="madhya-pradesh">Madhya Pradesh</option><option value="maharashtra">Maharashtra</option><option value="manipur">Manipur</option><option value="meghalaya">Meghalaya</option><option value="mizoram">Mizoram</option><option value="nagaland">Nagaland</option><option value="odisha">Odisha</option><option value="puducherry">Puducherry</option><option value="punjab">Punjab</option><option value="rajasthan">Rajasthan</option><option value="sikkim">Sikkim</option><option value="tamil-nadu">Tamil Nadu</option><option value="telangana">Telangana</option><option value="tripura">Tripura</option><option value="uttar-pradesh">Uttar Pradesh</option><option value="uttarakhand">Uttarakhand</option><option value="west-bengal">West Bengal</option></select>"""
@app.route('/',methods=['GET','POST'])
def index():
    co = request.form.get('country')
    st = request.form.get('state')
    print(co)
    print(st)
    if request.method=='GET':
        return render_template('index.html',tag=tag)
    
    elif request.method=='POST':
        st = request.form.get('state')
        pg = requests.get(f'https://stores.amaron.in/getCitiesByMasterOutletIdAndStateName.php?master_outlet_id=243295&state_name={st}',headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'})
        op = '<form action="/" method="POST"><label>District</label><select name="district" class="input" required="required">'+''.join([f'<option value="{i[0]}">{i[1]}</option>' for i in pg.json().items()])+'</select><input type="submit" value="Submit"></form>'
        return render_template('index.html',tag=tag, dist=op)
@app.route('/api/getDist/<st>',methods=['GET'])
def getDist(st):
    # elif request.method=='POST':
        # st = request.form.get('state')
        pg = requests.get(f'https://stores.amaron.in/getCitiesByMasterOutletIdAndStateName.php?master_outlet_id=243295&state_name={st}',headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'})
        op = '<select id="Locality" onchange="getLoc(this.value)">'+''.join([f'<option value="{i[0]}">{i[1]}</option>' for i in pg.json().items()])+'</select>'
        return pg.json()
@app.route('/api/GetLoc/<st>/<ci>',methods=['GET'])
def GetLoc(st,ci):
    # elif request.method=='POST':
        # st = request.form.get('state')
        pg = requests.get(f'https://stores.amaron.in/getLocalitiesByMasterOutletIdAndCityName.php?master_outlet_id=243295&city_name={ci}&state_name={st}',headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'})
        print(pg)
        op = '<select id="Locality">'+''.join([f'<option value="{i[0]}">{i[1]}</option>' for i in pg.json().items()])+'</select>'
        return op
if __name__=='__main__':
    app.run(debug=True)

