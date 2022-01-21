import requests

# wolframAPI
appid = ""


# 简单结果
def easy_res(query, appid=appid):
    base_url = "http://api.wolframalpha.com/v1/simple"
    query = "&i=" + query.replace('+', 'plus').replace(' ', '+')
    api_url = base_url + appid + query
    with open('easy_result.jpg', 'wb') as file:
        file.write(requests.post(api_url).content)
    send_msg('group', group_id, '[CQ:image,file=' + str('test.jpg') + "]")


# 简短回答
def short_answers(query, appid=appid):
    base_url = "http://api.wolframalpha.com/v1/result"
    query = "&i=" + query.replace('+', 'plus').replace(' ', '+') + "%3f"
    api_url = base_url + appid + query
    show(requests.post(api_url).content)


conversational_user_id = {}


# 会话式
def conversational(query, user_id, appid=appid):
    units = "&units=metric"

    # 初次会话
    if user_id not in conversational_user_id:
        base_url = "http://api.wolframalpha.com/v1/conversation.jsp"
        query = "&i=" + query.replace('+', 'plus').replace(' ', '+') + "%3f"
        api_url = base_url + appid + query + units

    # 多次对话
    else:
        base_url = "http://" + conversational_user_id[user_id]["host_data"] + "/api/v1/conversation.jsp"
        query = "&i=" + query.replace('+', 'plus').replace(' ', '+') + "%3f"
        api_url = base_url + appid \
                  + "&conversationid=" \
                  + conversational_user_id[user_id]["conversationID_data"] \
                  + query

        if "s_data" in conversational_user_id[user_id]:
            api_url = api_url + "&s=" + conversational_user_id[user_id]["s_data"]

        api_url = api_url + units

    answer = requests.post(api_url).content

    res_data = answer["result"]
    conversationID_data = answer["conversationID"]
    host_data = answer["host"]
    if "s" in answer:
        s_data = answer["s"]

    conversational_user_id[user_id] = answer

    show(res_data)
