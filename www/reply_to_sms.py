from flask import Flask, request
import plivo, plivoxml

app = Flask(__name__)

@app.route('/reply_to_sms/',methods=['GET','POST'])
def inbound_sms():
    # Sender's phone number
    from_number = request.values.get('From')
    # Receiver's phone number - Plivo number
    to_number = request.values.get('To')
    # The text which was received
    text = request.values.get('Text')

    params = {
      "src": to_number,
      "dst": from_number,
    }
    body = "Thanks, we've received your message."

    # Generate a Message XML with the details of
    # the reply to be sent.
    r = plivoxml.Response()
    r.addMessage(body, **params)
    return r.to_xml()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
