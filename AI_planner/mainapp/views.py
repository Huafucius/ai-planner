from django.shortcuts import render

from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
#from langchain.prompts import MessagesPlaceholder

def login(request):
    if request.method == "GET":
        return render(request, "login.html")

    user_name = request.POST.get("user_name", "")
    user_pwd = request.POST.get("user_pwd", "")
    
    

def home(request):
    if request.method == "GET":
        return render(request,"home.html")
    
def my_templates(request):
    if request.method == "GET":
        user_input= request.GET.get("user_input")
        user_response = generate_dream(user_input)
        print(1)
        return render(request,"my_templates.html",{"user_response":user_response})

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
    result=chain.invoke({"user_input": user_input})
    print("dfgasgesf")
    return result