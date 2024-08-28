import requests
import json
import time

def send_request(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": "Bearer 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",  # Replace with your actual API key
                    
    }
    data = {
        "model": "sao10k/l3.1-euryale-70b",  # Optional
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Debug output
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)

    if response.status_code == 200:
        try:
            return response.json()
        except requests.exceptions.JSONDecodeError:
            print("Error decoding JSON response")
            return None
    else:
        print(f"API request failed with status code {response.status_code}")
        return None

def main():
    # Read prompts from the input file
    with open("input.txt", "r") as file:
        prompts = file.readlines()

    results = []
    for prompt in prompts:
        prompt = prompt.strip()
        if prompt:  # Ensure the prompt is not empty
            print(f"Sending prompt: {prompt}")
            start_time = time.time()
            response = send_request(prompt)
            end_time = time.time()
            
            result = {
                "Prompt": prompt,
                "Message": response.get("choices", [{}])[0].get("message", "No response received") if response else "No response received",
                "TimeSent": start_time,
                "TimeRecvd": end_time,
                "Source": "OpenRouter.ai"
            }
            results.append(result)

    # Save results to output.json
    with open("output.json", "w") as file:
        json.dump(results, file, indent=4)

if __name__ == "__main__":
    main()