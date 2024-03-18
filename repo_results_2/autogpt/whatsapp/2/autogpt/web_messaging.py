from flask import Flask, request

app = Flask(__name__)

@app.route('/send_message', methods=['POST'])
def send_message():
    # This is a placeholder. In a real system, you would send the message from the sender to the receiver.
    sender_id = request.form['sender_id']
    receiver_id = request.form['receiver_id']
    message = request.form['message']
    print(f'Sending message from user {sender_id} to user {receiver_id}...')

    # Send the message (placeholder)
    return 'Message sent successfully'

if __name__ == '__main__':
    app.run(debug=True)