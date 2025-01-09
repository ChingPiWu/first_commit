from openai import OpenAI
client = OpenAI()


def complete_chat(user_message, pre_prompt="你是一位公平公正的記者，請幫我摘要30字以內的新聞大綱"):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system",
             "content": pre_prompt
             },
            {
                "role": "user",
                "content": user_message
            }
        ]
    )

    return completion.choices[0].message.content
