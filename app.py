from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=['POST'])
def whatsapp_bot():
    incoming_msg = request.values.get('Body', '').lower()
    response = MessagingResponse()
    msg = response.message()

    if 'hola' in incoming_msg:
        msg.body("¡Hola! ¿En qué puedo ayudarte?")
    elif 'gracias' in incoming_msg:
        msg.body("Con gusto, estoy para ayudarte.")
    else:
        msg.body("No entendí eso. Intenta escribir 'hola'.")

    return str(response)

if __name__ == "__main__":
    app.run()
