INPUTS: input.txt is a text file containing one prompt on each line

OUTPUTS : The Python script outputs a json file titled "output.json" with the following format

The file contains a JSON array of JSON Objects.

The format of the JSON Objects is as follows:

"Prompt" which stores the original prompt sent by the client.

"Message" which stores the response string from the API.

"TimeSent" which stores the Time that the prompt was originally sent out by the client as a UNIX Timestamp

"TimeRecvd" which stores the Time that the response was received by the client as a UNIX Timestamp

"Source" which specifies the source of the response, in this case, I have used openrouter.ai and specifically the model l3.1-euryale-70b's api to handle the prompts.

