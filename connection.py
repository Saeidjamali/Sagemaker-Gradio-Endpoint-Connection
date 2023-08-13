#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install gradio


# In[7]:


import gradio as gr
import boto3
import json

# Replace these values with your own
region_name = 'eu-west-2'  # Replace with your region
endpoint_name = 'Your end point name'  # Replace with your endpoint name

# Create a SageMaker runtime client
sagemaker_runtime = boto3.client('sagemaker-runtime', region_name=region_name)

def predict_text(text_input):
    payload = {
        "inputs": text_input,
        "max_length": 50
    }

    response = sagemaker_runtime.invoke_endpoint(
        EndpointName=endpoint_name,
        ContentType="application/json",
        Body=json.dumps(payload)
    )

    response_body = response['Body'].read()
    predicted_result = json.loads(response_body)
    
   # print(predicted_result)  # Print the response for debugging purposes

   # return predicted_result  # Return the entire response for analysis

    return predicted_result['generated_texts'][0]

# Create a Gradio interface
iface = gr.Interface(
    fn=predict_text,
    inputs=gr.inputs.Textbox(label="Text Input"),
    outputs=gr.outputs.Textbox(label="Generated Text"),
    live=False  # Use live=True to dynamically update output without needing a button
)

# Launch the interface
iface.launch()




