""" Playground to use ChatGPT to summarize documents.
"""
import openai
import pdfplumber
import sys
import os


def summarize(content):
    tldr_tag = "\n\nTl;dr:"
    openai.api_key = os.environ["OPENAI_KEY"]
    response = openai.Completion.create(engine="text-davinci-003", prompt=content + tldr_tag, temperature=0.7,
                                        max_tokens=140,
                                        top_p=1,
                                        frequency_penalty=0,
                                        presence_penalty=1,
                                        )
    return response["choices"][0]["text"]


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        contents = f.read()
        print(summarize(contents))