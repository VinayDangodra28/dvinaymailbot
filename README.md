# Flask Mail API

This is a simple Flask app that can be used as an API to send emails. The API accepts POST requests with a JSON payload in the following format:

{
  "receivers": ["recipient1@example.com", "recipient2@example.com"],
  "subject": "Email Subject",
  "body": "Email Body",
  "bodyType": "html"
}

The `receivers` field is a list of email addresses to which the email will be sent. The `subject` field is the subject of the email. The `body` field is the body of the email. The `bodyType` field is optional and can be either `text` or `html`. If it is not provided, the default value is `text`.


## Requirements

* Python 3.6 or higher
* Flask
* Flask-Mail
* Flask-Cors


## Configuration

Before running the app, make sure to configure the following parameters in the `app.config` dictionary:

* `MAIL_SERVER`: The SMTP server address for the email provider.
* `MAIL_PORT`: The SMTP server port.
* `MAIL_USERNAME`: Your email address.
* `MAIL_PASSWORD`: Your email account password.
* `MAIL_USE_TLS`: Whether or not to use TLS for secure connections. Set to `True` or `False`.
* `MAIL_USE_SSL`: Whether or not to use SSL for secure connections. Set to `True` or `False`.


## Usage

uncommand the last 2 lines from the code if running on local host

To run the app, use the following command:

<pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>Python</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg> Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs">python app.py
</code></div></div></pre>

Once the app is running, you can send emails by sending POST requests to the `/` endpoint with the JSON payload described above. For example, using the `curl` command:

<pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>Command</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg> Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-json">curl -i -H "Content-Type: application/json" -X POST -d '{"receivers": ["recipient1@example.com", "recipient2@example.com"], "subject": "Email Subject", "body": "Email Body", "bodyType": "html"}' http://localhost:5000/</code></div></div></pre>
