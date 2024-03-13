from django.shortcuts import render

def login(request):
    if request.method == "GET":
        return render(request, "login.html")

    user_name = request.POST.get("user_name", "")
    user_pwd = request.POST.get("user_pwd", "")
    
    

def home(request):
    if request.method == "GET":
        return render(request,"home.html")
    
def my_templates(request):
    user_input= request.POST.get("user_input")
    user_response = generate_dream(user_input)
    return render(request,"my_templates.html",user_response=user_response)

def vision_manage(request):
    return render(request,"vision_manage.html")

def vision_create(request):
    return render(request,"vision_create.html")

def okr(request):
    return render(request,"okr.html")

def milestone(request):
    return render(request,"milestone.html")

def schedule(request):
    return render(request,"schedule.html")

from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
#from langchain.prompts import MessagesPlaceholder

#----------------------------------------

def generate_dream(user_input):

    system_txt="""
你是一个计划制定管家，我将告知你我的目标和想完成的期限。
请你依此帮我把我想实现的目标精确化，并依此以及依据我给出的时间期限来划分几个阶段并制定okr，每个阶段内部设置milestone。
"""

    prompt = ChatPromptTemplate.from_messages(
        [("system",system_txt),
        ("user","{user_input}")
        ])
    model=ChatOpenAI(model="gpt-3.5-turbo", openai_api_key="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") 
    chain = prompt|model

    result=chain.invoke({
    "user_input": user_input,
    })
    return result