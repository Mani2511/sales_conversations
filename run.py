import csv
import random
import time

def generate_sales_conversations(num_sets, min_response_words, max_response_words):
    sales_conversations = []
    products = ["Smartphone", "Laptop", "Smartwatch", "Headphones", "Tablet"]
    prompts = [
        "Hello, welcome to our store. How may I assist you today?",
        "Are you looking for anything specific?",
        "Would you like to know more about our latest products?"
    ]
    for _ in range(num_sets):
        salesman_name = "SalesBotAgent"
        user_name = "Customer"
        conversation = []
        conversation.append((salesman_name, random.choice(prompts)))

        while len(conversation) < 5:
            user_response = generate_user_response(products)
            conversation.append((user_name, user_response))
            salesman_response = generate_salesman_response(user_response, products)
            conversation.append((salesman_name, salesman_response))
            sales_conversations.append(conversation)

    return sales_conversations

def generate_user_response(products):
    product = random.choice(products)
    user_response = f"I’m interested in buying a {product}. Can you provide more information?"
    return user_response

def generate_salesman_response(user_response, products):
    if "price" in user_response:
        response = f"The price of {random.choice(products)} starts at $XXX."
    elif "features" in user_response:
        response = f"Sure, let me tell you about the features of {random.choice(products)}."
    else:
        response = "Certainly, we have a wide range of products to suit your needs."
    return response

def write_to_csv(sales_conversations):
    with open('sales_conversations.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Salesman', 'User', 'Timestamp'])

        for conversation_set in sales_conversations:
            for role, message in conversation_set:
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                writer.writerow([role, message, timestamp])

if __name__ == "__main__":
    num_sets = 100
    min_response_words = 50
    max_response_words = 75
    sales_conversations = generate_sales_conversations(num_sets, min_response_words, max_response_words)
    write_to_csv(sales_conversations)
