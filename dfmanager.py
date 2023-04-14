from google.cloud import dialogflow

project_id = 'alrighty-alex'
language_code = 'en'

continue_conversation = ["greeting"]


def detect_intent(session_id, text):
    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)
    text_input = dialogflow.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.QueryInput(text=text_input)

    response = session_client.detect_intent(
        request={"session": session, "query_input": query_input}
    )

    intent_name = response.query_result.intent.display_name
    result_text = response.query_result.fulfillment_text
    print("-" * 20)
    print("Running intent " + intent_name)
    print("Result: " + result_text)

    # return the information and whether the conversation should be continued
    return [result_text, continue_conversation.count(intent_name) > 0]
