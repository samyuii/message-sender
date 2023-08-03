# Task 4: Use Python Code to send WhatsApp to everyone


import pywhatkit as pwk

# using Exception Handling to avoid unexpected errors
try:
    # sending message on WhatsApp in India so using Indian dial code (+91)
    pwk.sendwhatmsg("+917014471298", "Hello how are you?", 11, 25, wait_time=3)
  # Sending at 1:00 AM

    print("Message Sent!")  # Prints success message in console

except Exception as e:
    print("Error in sending the message:", str(e))



