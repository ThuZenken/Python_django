from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Choice, Question
from django.contrib.auth.models import User
import csv
import pandas as pd
import sys
import os
import re
import fileinput


try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO


# Create your views here.


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})


def results(question, question_id):
    def results(request, question_id):
        question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return render(request, 'polls/results.html', {'question': question})


def export(request):
    # filepath = './001Before.txt'
    # filepath_new = './001After.txt'
    # new_file = open(filepath_new, 'w', encoding="utf-8")
    # with open(filepath, encoding="utf8") as fp:
    #     line = fp.readline()
    #     new_file.write(line.replace('∋〒', '●○○●[効能効果1:'))
    #     cnt = 1
    #     while line:
    #         # print("Line {}: {}".format(cnt, line.strip()))
    #         line = fp.readline()
    #         cnt += 1
    #         a = re.search("^∋〒$", line)

    #         if re.search("^☆repm☆∋〒", line):
    #             new_file.write(line.replace('∋〒', '●○○●[効能効果1:'))
    #         if re.search("^☆merg☆∋〒♪", line):
    #             new_file.write(line.replace('∋〒', '●○○●[効能効果1:'))
    #         if re.search("^∋〒「", line):
    #             new_file.write(line.replace('∋〒', '●○○●[効能効果1:'))
    #         if re.search("☆inli☆∋〒♪", line):
    #             new_file.write(line.replace('∋〒', '●○○●[効能効果1:'))

    #         else:
    #             new_file.write(line)
    # new_file.close()
    

    sentence = "☆merg☆∋〒♪<⊇LOW1>『消化管撮影』<⊆LOW2>『下記の場合における消化管造影』「狭窄の疑いのあるとき<BR>急性出血<BR>穿孔の恐れのあるとき(消化器潰瘍,憩室)<BR>その他,外科手術を要する急性症状時<BR>胃及び腸切除後(穿孔の危険,縫合不全)<BR>内視鏡検査法実施前の異物及び腫瘍の造影<BR>胃・腸瘻孔の造影」</⊆LOW2>〒♪『コンピューター断層撮影における上部消化管造影』</⊇LOW1>∈〒♪<DOSEADMIN><⊇LOW1><⊆LOW2>『消化管撮影』『(経口)』「通常成人1回60mL(レリーフ造影には,10〜30mL)を経口投与する.」『(注腸)』「通常成人3〜4倍量の水で希釈し,最高500mLを注腸投与する.」</⊇LOW1></DOSEADMIN>〒♪『コンピューター断層撮影における上部消化管造影』『(経口)』「通常成人30〜50倍量の水で希釈し,250〜300mLを経口投与する.」</⊆LOW2>7211001X1030_2_07"
    # replacing both lowercase and 
    # uppercase characters with 0 in   
    # the variable sentence by using  
    # flag and printing the modified string  
    result =   re.sub(r"^(☆merg☆∋)([^〒]*)〒(.*)∈([^〒]*)〒(.*)", "\\1\\3〒∈🌊\\5", sentence)
    result1 =  re.sub(r"$", "〒", result)
    result2 = re.sub(r"^(☆merg☆∋)([^〒]*)〒(.*)∈([^〒]*)〒(.*)", "\\1\\3〒∈🌊\\5", result1)
    result3 =  re.sub(r"^(☆merg☆∋)([^〒]*)〒([^🌊]*)🌊(〒*[^〒]*)〒", "\\1\\3●○○●[効能効果1:\\2]●=>●\\4🌊", result2)
    result4 =  re.sub(r"(☆merg☆∋)([^〒]*)〒([^🌊]*)🌊([^〒]*)〒", "\\1\\3●○○●[効能効果2:\\2]●=>●\\4🌊", result3)
    result5 =  re.sub(r"(☆merg☆∋)([^〒]*)〒([^🌊]*)🌊([^〒]*)〒", "\\1\\3●○○●[効能効果3:\\2]●=>●\\4🌊", result4)
    result6 =  re.sub(r"(☆merg☆∋)([^〒]*)〒([^🌊]*)🌊([^〒]*)〒", "\\1\\3●○○●[効能効果4:\\2]●=>●\\4🌊", result5)
    result7 =  re.sub(r"(☆merg☆∋)([^〒]*)〒([^🌊]*)🌊([^〒]*)〒", "\\1\\3●○○●[効能効果5:\\2]●=>●\\4🌊", result6)
    result8 =  re.sub(r"(☆merg☆∋)([^〒]*)〒([^🌊]*)🌊([^〒]*)〒", "\\1\\3●○○●[効能効果6:\\2]●=>●\\4🌊", result7)
    result9 =  re.sub(r"(☆merg☆∋)([^〒]*)〒([^🌊]*)🌊([^〒]*)〒", "\\1\\3●○○●[効能効果7:\\2]●=>●\\4🌊", result8)
    result10 =  re.sub(r"(☆merg☆∋)([^〒]*)〒([^🌊]*)🌊([^〒]*)〒", "\\1\\3●○○●[効能効果8:\\2]●=>●\\4🌊", result9)
    result11 =  re.sub(r"(☆merg☆∋)([^〒]*)〒([^🌊]*)🌊([^〒]*)〒", "\\1\\3●○○●[効能効果9:\\2]●=>●\\4🌊", result10)
    result12 =  re.sub(r"(☆merg☆∋)([^〒]*)〒([^🌊]*)🌊([^〒]*)〒", "\\1\\3●○○●[効能効果10:\\2]●=>●\\4🌊", result11)
    result13 =  re.sub(r"(☆merg☆∋)([^〒]*)〒([^🌊]*)🌊([^〒]*)〒", "\\1\\3●○○●[効能効果11:\\2]●=>●\\4🌊", result12)
    result14 =  re.sub(r"(☆merg☆∋)([^〒]*)〒([^🌊]*)🌊([^〒]*)〒", "\\1\\3●○○●[効能効果12:\\2]●=>●\\4🌊", result13)
    result15 =  re.sub(r"(☆merg☆∋)([^〒]*)〒([^🌊]*)🌊([^〒]*)〒", "\\1\\3●○○●[効能効果13:\\2]●=>●\\4🌊", result14)
    result16 =  re.sub(r"(☆merg☆∋)([^🌊]*)🌊([^\n]*)", "\\1\\2", result15)
    result17 =  re.sub(r"([」』])[♫🎶♩♪♬🎼「」『』♂∋∈]*([「『])", "\\1、\\2" , result16)
    result18 =  re.sub(r"(場合)([」』<])" , "\\1:\\2", result17)
    result19 =  re.sub(r"([ぁ-ん])([」』<])" , "\\1:\\2", result18)
    result20 =  re.sub(r"[「」『』]" , "", result19)
    result21 =  re.sub(r"</*[⊇⊆∪⊃]low\\d>" , "", result20)
    result22 =  re.sub(r"←\\/*(chr|bold)→" , "", result21)
    result23 =  re.sub(r"↑↑2:[効能効果2:]〒" , "", result22)
    result24 =  re.sub(r"[♫🎶♩♪♬🎼「」『』♂∋∈♪]" , "", result23)
    result25 =  re.sub(r"</*[⊇⊆∪⊃]low\\d>" , "", result24)
   
    return HttpResponse(result25)
