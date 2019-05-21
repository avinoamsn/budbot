from flask import Flask, request
import plivo

app = Flask(__name__)

auth_id = "MAZWQ1NTE0NTY4YWVLYZ"
auth_token = "ZTM3MmJlNzk1MDc2MDc0YmM3MDk2MWI5NjAxNGRm"

p = plivo.RestAPI(auth_id, auth_token)

@app.route('/reply_to_sms/', methods=['GET','POST'])
def inbound_sms():
    # Sender's phone number
    from_number = request.values.get('From')
    # Receiver's phone number - Plivo number
    to_number = request.values.get('To')
    # The text which was received
    text = (request.values.get('Text'))

    params = {
      'src': to_number,
      'dst': from_number,
      'text' : response(text),
    }

    p.send_message(params)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

def response(text):
    # format to caps, remove trailing white space
    text = text.upper()
    text = text.rstrip()

    # hardcoded responses
    if(text == "MENU"):
        return menu
    elif(text == "HELP"):
        return help
    elif(text == "FORMAT"):
        return format
    elif(text.count(";") == 2):
        parse(text)
        return confirmation
    else:
        return error;

def parse(text):
    msg_list = text.split(";")
    msg_list.append(request.values.get('From'))
    # TODO: send msg_list to dispatcher
    return

# UI
menu = """Menu:
lemonade, $50
lemonade, $90
lemonade, $170
Reply HELP for more info."""

help = """Welcome to Budbot, your marijuana and rolling paper delivery service!
Reply MENU for menu and donation amount(s), or FORMAT for a sample order text.
For further assistance, reach us at contact@budbot.co.
Reply HELP to display this message again."""

format = """Order format:
menu item; donation amount; address.
Example:
lemonade; 50; 123 Example St., Washington, DC 20052"""

error = "Buddy didn't understand that. Please make sure you are using the correct format."

confirmation = "Your delivery is on its way!"
