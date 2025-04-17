# 🤖 Docyon: ChatGPT in the Terminal with OpenAI API

This project implements **Docyon**, a conversational chatbot using the **GPT-3.5-Turbo** model from OpenAI in the terminal. It features message history and supports a mock mode for testing without consuming API credits, making it ideal for testing and experimentation. 🗨️

## Overview  
The system simulates a conversation with **Docyon** directly in the terminal. Users can send messages and receive real-time responses from the GPT-3.5-Turbo model. A mock mode is also available, allowing responses without connecting to the real API — great for development and testing. 🖥️

This project can be used in various practical applications, such as customer support, task automation, or even as an educational tool for interacting with students. It can also serve to prototype custom chatbots for businesses.

Key features of this project:
- 🧠 **Interaction with GPT-3.5-Turbo** via OpenAI API  
- 🧪 **Support for simulated (mock) responses** for local testing without cost  
- 📝 **Message history maintenance** during the session for contextual responses  
- 🖥️ **Terminal-based interface**, simple and accessible  

## How to Use
1. Install the required package:<br/>
  *pip install openai*

2. To test without consuming the real API, just keep the variable **<test_mode>** set to **True**. The mock is already implemented in the script and ready for use.

## Simulated Mode
This project includes a mock function that mimics the behavior of the API. When **<test_mode>** is set to **True**, all inputs receive a simulated response based on the user's last message. This allows testing the functionality without an internet connection or an active API key. 🧪</br>
Ideal for moments when the legendary Docyon just wants to play around without spending tokens.

## Example
*What are you thinking? What's the capital of France?*  
Docyon: *You said: 'What's the capital of France?'. That's very interesting! =)*

*What are you thinking? leave*
