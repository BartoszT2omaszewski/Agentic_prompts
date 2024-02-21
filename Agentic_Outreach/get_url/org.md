template = """
                Given the full name of a person
                i want you to get the url link to the person"s linkeldin profile page

                Your answer should only contain a linkeldin profile url link.


                {tools}

                Use the following format:

                Question: the input question you must answer
                Thought: you should always think about what to do
                Action: the action to take, should be one of [{tool_names}]
                Action Input: the input to the action
                Observation: the result of the action
                ... (this Thought/Action/Action Input/Observation can repeat N times)
                Thought: I now know the final answer
                Final Answer: the final answer to the original input question

                ***Your answer should only contain a linkeldin profile url link***

                Begin!

               Question: {input}
               Thought:{agent_scratchpad}"""

prompt = PromptTemplate.from_template(template=template, MessagesPlaceholder=["{agent_scratchpad"] )


