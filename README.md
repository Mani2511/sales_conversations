# Sales Conversations Dataset

This dataset contains simulated sales conversations between a virtual SalesBotagent and Customers. The dataset is generated programmatically and aims to provide a diverse set of interactions related to various products.

## Dataset Details

- *Total Conversations*: 100 sets
- *Salesman*: SalesBotagent
- *User*: Customer
- *Products*: Smartphone, Laptop, Smartwatch, Headphones, Tablet
- *Conversation Format*: Each conversation set includes alternating dialogues between the SalesBotagent and Customer.
- *Conversation Length*: Each conversation set consists of 5 dialogues.
- *Response Length*: User responses range from 50 to 75 words.

## File Structure

- sales_conversations.csv: CSV file containing the sales conversations data.
- generate_sales_conversations.py: Python script to generate the sales conversations dataset.

## Dataset Generation

The dataset is generated using Python script generate_sales_conversations.py. It utilizes random prompts and product information to simulate sales conversations between the SalesBotagent and Customers.

### Instructions for Dataset Generation

1. *Dependencies*: Ensure you have Python installed along with the required libraries (csv, random, time).
2. *Run Script*: Execute the generate_sales_conversations.py script to generate the dataset.
3. *Output*: The generated dataset will be saved as sales_conversations.csv in the same directory.

## Dataset Usage

- This dataset can be used for training and testing conversational AI models in a sales context.
- It provides a structured format for evaluating model performance in generating coherent and contextually relevant responses.
- Researchers and developers can use this dataset to benchmark their models and explore advancements in natural language generation.

## Dataset License

This dataset is provided under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).

## Acknowledgements

This dataset is generated for the purpose of research and educational use. It draws inspiration from real-world sales conversations and aims to facilitate advancements in conversational AI technologies.

