from flask import request,render_template
import requests
from app import app



@app.route('/date_g',methods=['POST','GET'])
def get_date_g():

    if request.method == 'POST':
        if request.form['action'] == 'Submit':
           date_details = request.form.get('g_date')
           list_date_details = date_details.split('-')
           year = list_date_details[0]
           month = list_date_details[1]
           day = list_date_details[2]
           payload = {'cfg':'json', 'gy':year, 'gm': month, 'gd': day, 'g2h':1, 'gs':'on' }
           r = requests.get('https://www.hebcal.com/converter', params=payload)
           data = r.json()
           return render_template('basic.html',data = data['hebrew'])
        else:
            data = ''
            return render_template('basic.html', data='')
    return render_template('basic.html',data='')








