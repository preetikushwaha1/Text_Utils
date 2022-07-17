
from zlib import decompressobj
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#===========Remove Punctuation ================================#

def remove_punctuation_fun(request):
    # get text from text area
    dj_Text = request.GET.get('text','default')

    #check checkbox is on or off
    removepunc =request.GET.get('removepunctuation', "off")
    capitalize_text = request.GET.get('capitalize','off')
    upper_text =request.GET.get('upper','off')
    new_line_remover = request.GET.get('new_line_remove', "off")
    space_remover = request.GET.get('space_remover','off')


    punctuation='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyze_text =''
    if removepunc == "on":
        for char in dj_Text:
            if char not in punctuation:
                analyze_text = analyze_text+char
       
        params_list = {'purpose':"Remove Punctuation", 'analyzed_text':analyze_text}

        #return render(request, "Analyze.html", params_list )
        dj_Text= analyze_text

    if(capitalize_text == "on"):

        analyze_text= dj_Text.capitalize()
        params_list = {'purpose':"First Letter Capitalize ", 'analyzed_text':analyze_text}

        #return render(request, "Analyze.html", params_list )
        dj_Text= analyze_text

    if(upper_text=="on"):
        analyze_text =""
        for char in dj_Text:
            analyze_text = analyze_text+ char.upper()
        params_list = {'purpose':"First Letter Capitalize ", 'analyzed_text':analyze_text}

        #return render(request, "Analyze.html", params_list )
        dj_Text= analyze_text

    if(new_line_remover =="on"):
        analyze_text =""
        for char in dj_Text:
            if(char !="\n" and char != "\r"):
                analyze_text = analyze_text + char
        params_list = {'purpose':"New Line remover", 'analyzed_text':analyze_text}

        #return render(request, "Analyze.html", params_list )
        dj_Text= analyze_text

    if(space_remover =="on"):
        analyze_text =""
        for char in dj_Text:
            if char !=" ":
                analyze_text = analyze_text+char
        params_list ={ 'purpose':"Space remover", 'analyzed_text':analyze_text}
        #return render(request, "Analyze.html", params_list )



    if(removepunc != "on" and capitalize_text != "on"and upper_text != "on" and new_line_remover != "on" and space_remover != "on"  ):
        return HttpResponse("please select any check box ")



    return render(request, "Analyze.html", params_list )

    


#===========Capitalize First==============================#

def capitalize_first_fun(request):
    return HttpResponse('<h1>Capitalize First</h1>')

#================NewLine Remover============================#

def new_line_remover_fun(request):
    return HttpResponse('<h1>NewLine Remover</h1>')


#=======Space Remover==============================#

def space_remover_fun(request):
    return HttpResponse('<h1>Space Remover</h1>')

#============Char Count=====================#

def char_count_fun(request):
    return HttpResponse('<h1>Char Count</h1>')