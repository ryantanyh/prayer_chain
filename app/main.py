from flask import Flask, render_template, request
import requests
import random
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        names=request.form.getlist('checkbox')
        prayer_chain=random.sample(names, len(names))
        prayer_chain.append(prayer_chain[0])
        for i in range(len(prayer_chain)-1):
            prayer_chain[i]= prayer_chain[i] + ' > '
        prayer_chain_message = "".join(prayer_chain)
        TOKEN = "5353815025:AAEoXS_qHKagYc3L62qXx1BYfLZUxBoKnkE"
        chat_id = "-1001478470448"
#         chat_id="-721120522"
        text = "test1"
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={prayer_chain_message}"
        r=requests.get(url)
        print(r)
        a=str(r)
        if a == '<Response [200]>':
            return ('Prayer Chain Sent')
    return render_template('index.html')



if __name__ == "__main__":
    app.run()