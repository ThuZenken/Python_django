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
    filepath = './001Before.txt'
    # f = open("./001Before.txt", "r", encoding="utf-8")
    filepath_new = './001After.txt'
    new_file = open(filepath_new, 'w', encoding="utf-8")
    # content = f.read()
    # content = re.sub(
    #     r"^(☆merg☆∋)([^〒]*)〒(.*)∈([^〒]*)〒(.*)", "\\1\\3〒∈🌊\\5", content)
    with open(filepath, encoding="utf8") as fp:
        line = fp.readline()
        while line:
            if "☆merg☆" in line:
                result = re.sub(
                    r"^(☆merg☆∋)([^〒]*)〒(.*)∈([^〒]*)〒(.*)", "\\1\\3〒∈🌊\\5", line)
                result1 = re.sub(r"\n", "〒\n", result)

                result3 = re.sub(
                    r"^(☆merg☆∋)([^〒]*)〒([^🌊]*)🌊(〒*[^〒]*)〒", "\\1\\3●○○●[効能効果1:\\2]●=>●\\4🌊", result1)
                result4 = re.sub(r"(☆merg☆∋)([^〒]*)〒([^🌊]*)🌊([^〒]*)〒",
                                 "\\1\\3●○○●[効能効果2:\\2]●=>●\\4🌊", result3)
                result5 = re.sub(r"(☆merg☆∋)([^〒]*)〒([^🌊]*)🌊([^〒]*)〒",
                                 "\\1\\3●○○●[効能効果3:\\2]●=>●\\4🌊", result4)
                result6 = re.sub(r"(☆merg☆∋)([^〒]*)〒([^🌊]*)🌊([^〒]*)〒",
                                 "\\1\\3●○○●[効能効果4:\\2]●=>●\\4🌊", result5)
                result7 = re.sub(r"(☆merg☆∋)([^〒]*)〒([^🌊]*)🌊([^〒]*)〒",
                                 "\\1\\3●○○●[効能効果5:\\2]●=>●\\4🌊", result6)
                result8 = re.sub(r"(☆merg☆∋)([^〒]*)〒([^🌊]*)🌊([^〒]*)〒",
                                 "\\1\\3●○○●[効能効果6:\\2]●=>●\\4🌊", result7)
                result9 = re.sub(r"(☆merg☆∋)([^〒]*)〒([^🌊]*)🌊([^〒]*)〒",
                                 "\\1\\3●○○●[効能効果7:\\2]●=>●\\4🌊", result8)
                result10 = re.sub(
                    r"(☆merg☆∋)([^〒]*)〒([^🌊]*)🌊([^〒]*)〒", "\\1\\3●○○●[効能効果8:\\2]●=>●\\4🌊", result9)
                result11 = re.sub(r"(☆merg☆∋)([^〒]*)〒([^🌊]*)🌊([^〒]*)〒",
                                  "\\1\\3●○○●[効能効果9:\\2]●=>●\\4🌊", result10)
                result12 = re.sub(r"(☆merg☆∋)([^〒]*)〒([^🌊]*)🌊([^〒]*)〒",
                                  "\\1\\3●○○●[効能効果10:\\2]●=>●\\4🌊", result11)
                result13 = re.sub(r"(☆merg☆∋)([^〒]*)〒([^🌊]*)🌊([^〒]*)〒",
                                  "\\1\\3●○○●[効能効果11:\\2]●=>●\\4🌊", result12)
                result14 = re.sub(r"(☆merg☆∋)([^〒]*)〒([^🌊]*)🌊([^〒]*)〒",
                                  "\\1\\3●○○●[効能効果12:\\2]●=>●\\4🌊", result13)
                result15 = re.sub(r"(☆merg☆∋)([^〒]*)〒([^🌊]*)🌊([^〒]*)〒",
                                  "\\1\\3●○○●[効能効果13:\\2]●=>●\\4🌊", result14)
                line = re.sub(
                    r"(☆merg☆∋)([^🌊]*)🌊([^\n]*)", "\\1\\2〒", result15)
            if "☆none☆" in line:
                line = re.sub(
                    r"\n", "〒〒\n", line)
            if "☆repm☆" in line:
                result = re.sub(
                    r"^(☆repm☆∋)([^〒]*)〒(.*)∈([^〒]*)〒(.*)", "\\1\\3〒∈🌊\\5", line)
                result1 = re.sub(r"\n", "〒\n", result)
                result2 = re.sub(
                    r"^(☆repm☆∋)([^〒]+)〒([^🌊]*)🌊(〒*[^〒]+)〒", "\\1\\3●○○●[効能効果1:\\2]●=>●\\4🌊\\4〒", result1)
                result3 = re.sub(
                    r"(☆repm☆∋)([^〒]+)〒([^🌊]*)🌊([^〒]+)〒", "\\1\\3●○○●[効能効果2:\\2]●=>●\\4🌊\\4〒", result2)
                result4 = re.sub(
                    r"(☆repm☆∋)([^〒]*)〒([^🌊]*)🌊([^〒]*)〒", "\\1\\3●○○●[効能効果3:\\2]●=>●\\4🌊\\4〒", result3)
                result5 = re.sub(
                    r"(☆repm☆∋)([^〒]*)〒([^🌊]*)🌊([^〒]*)〒", "\\1\\3●○○●[効能効果4:\\2]●=>●\\4🌊\\4〒", result4)
                result6 = re.sub(
                    r"(☆repm☆∋)([^〒]*)〒([^🌊]*)🌊([^〒]*)〒", "\\1\\3●○○●[効能効果5:\\2]●=>●\\4🌊\\4〒", result5)
                result7 = re.sub(
                    r"(☆repm☆∋)([^〒]*)〒([^🌊]*)🌊([^〒]*)〒", "\\1\\3●○○●[効能効果6:\\2]●=>●\\4🌊\\4〒", result6)
                result8 = re.sub(
                    r"(☆repm☆∋)([^〒]*)〒([^🌊]*)🌊([^〒]*)〒", "\\1\\3●○○●[効能効果7:\\2]●=>●\\4🌊\\4〒", result7)
                result9 = re.sub(
                    r"(☆repm☆∋)([^〒]*)〒([^🌊]*)🌊([^〒]*)〒", "\\1\\3●○○●[効能効果8:\\2]●=>●\\4🌊\\4〒", result8)
                result10 = re.sub(
                    r"(☆repm☆∋)([^〒]*)〒([^🌊]*)🌊([^〒]*)〒", "\\1\\3●○○●[効能効果9:\\2]●=>●\\4🌊\\4〒", result9)
                result11 = re.sub(
                    r"(☆repm☆∋)([^〒]*)〒([^🌊]*)🌊([^〒]*)〒", "\\1\\3●○○●[効能効果10:\\2]●=>●\\4🌊\\4〒", result10)
                result12 = re.sub(
                    r"(☆repm☆∋)([^〒]*)〒([^🌊]*)🌊([^〒]*)〒", "\\1\\3●○○●[効能効果11:\\2]●=>●\\4🌊\\4〒", result11)
                result13 = re.sub(
                    r"(☆repm☆∋)([^〒]*)〒([^🌊]*)🌊([^〒]*)〒", "\\1\\3●○○●[効能効果12:\\2]●=>●\\4🌊\\4〒", result12)
                result14 = re.sub(
                    r"(☆repm☆∋)([^〒]*)〒([^🌊]*)🌊([^〒]*)〒", "\\1\\3●○○●[効能効果13:\\2]●=>●\\4🌊\\4〒", result13)
                result15 = re.sub(
                    r"(☆repm☆∋)([^〒]*)〒([^🌊]*)🌊([^〒]*)〒", "\\1\\3●○○●[効能効果14:\\2]●=>●\\4🌊\\4〒", result14)
                result16 = re.sub(
                    r"(☆repm☆∋)([^〒]*)〒([^🌊]*)🌊([^〒]*)〒", "\\1\\3●○○●[効能効果15:\\2]●=>●\\4🌊\\4〒", result15)
                result17 = re.sub(
                    r"(☆repm☆∋)([^〒]*)〒([^🌊]*)🌊([^〒]*)〒", "\\1\\3●○○●[効能効果16:\\2]●=>●\\4🌊\\4〒", result16)
                result18 = re.sub(
                    r"(☆repm☆∋)([^〒]*)〒([^🌊]*)🌊([^〒]*)〒", "\\1\\3●○○●[効能効果17:\\2]●=>●\\4🌊\\4〒", result17)
                result19 = re.sub(
                    r"(☆repm☆∋)([^〒]*)〒([^🌊]*)🌊([^〒]*)〒", "\\1\\3●○○●[効能効果18:\\2]●=>●\\4🌊\\4〒", result18)
                result20 = re.sub(
                    r"(☆repm☆∋)([^〒]*)〒([^🌊]*)🌊([^〒]*)〒", "\\1\\3●○○●[効能効果19:\\2]●=>●\\4🌊\\4〒", result19)
                result21 = re.sub(
                    r"(☆repm☆∋)([^〒]*)〒([^🌊]*)🌊([^〒]*)〒", "\\1\\3●○○●[効能効果20:\\2]●=>●\\4🌊\\4〒", result20)
                result22 = re.sub(
                    r"(☆repm☆∋)([^〒]*)〒([^🌊]*)🌊([^〒]*)〒", "\\1\\3●○○●[効能効果21:\\2]●=>●\\4🌊\\4〒", result21)
                # line = re.sub(r"🌊\n", "〒🌊\n", result22)
                line = re.sub(
                    r"(☆repm☆∋)([^🌊]*)🌊([^\n]*)", "\\1\\2", result22)
                # line = re.sub(r"\n", "〒🌊\n", result23)

            # if "☆none☆" in line:
            #     line = re.sub(r"\n", "〒〒〒🌊\n", line)

            if "☆inli☆" in line:
                result = re.sub(
                    r"(☆inli☆∋)([^〒]*)〒", "\\1🌊", line)
                result1_0 = re.sub(r"\n", "〒\n", result)
                result1 = re.sub(
                    r"(☆inli☆∋)🌊([^〒]*)〒([^〒]*)〒", "\\1●○○●[効能効果1:\\2]●=>●\\3🌊", result1_0)
                result2 = re.sub(
                    r"([^🌊]*)🌊([^〒]*)〒([^〒]*)〒", "\\1●○○●[効能効果2:\\2]●=>●\\3🌊", result1)
                result3 = re.sub(
                    r"([^🌊]*)🌊([^〒]*)〒([^〒]*)〒", "\\1●○○●[効能効果3:\\2]●=>●\\3🌊", result2)
                result4 = re.sub(
                    r"([^🌊]*)🌊([^〒]*)〒([^〒]*)〒", "\\1●○○●[効能効果4:\\2]●=>●\\3🌊", result3)
                result5 = re.sub(
                    r"([^🌊]*)🌊([^〒]*)〒([^〒]*)〒", "\\1●○○●[効能効果5:\\2]●=>●\\3🌊", result4)
                result6 = re.sub(
                    r"([^🌊]*)🌊([^〒]*)〒([^〒]*)〒", "\\1●○○●[効能効果6:\\2]●=>●\\3🌊", result5)
                result7 = re.sub(
                    r"([^🌊]*)🌊([^〒]*)〒([^〒]*)〒", "\\1●○○●[効能効果7:\\2]●=>●\\3🌊", result6)
                result8 = re.sub(
                    r"([^🌊]*)🌊([^〒]*)〒([^〒]*)〒", "\\1●○○●[効能効果8:\\2]●=>●\\3🌊", result7)
                result9 = re.sub(
                    r"([^🌊]*)🌊([^〒]*)〒([^〒]*)〒", "\\1●○○●[効能効果9:\\2]●=>●\\3🌊", result8)
                result10 = re.sub(
                    r"([^🌊]*)🌊([^〒]*)〒([^〒]*)〒", "\\1●○○●[効能効果10:\\2]●=>●\\3🌊", result9)
                result11 = re.sub(
                    r"([^🌊]*)🌊([^〒]*)〒([^〒]*)〒", "\\1●○○●[効能効果11:\\2]●=>●\\3🌊", result10)
                result12 = re.sub(
                    r"([^🌊]*)🌊([^〒]*)〒([^〒]*)〒", "\\1●○○●[効能効果12:\\2]●=>●\\3🌊", result11)
                result13 = re.sub(
                    r"([^🌊]*)🌊([^〒]*)〒([^〒]*)〒", "\\1●○○●[効能効果13:\\2]●=>●\\3🌊", result12)
                result14 = re.sub(
                    r"([^🌊]*)🌊([^〒]*)〒([^〒]*)〒", "\\1●○○●[効能効果14:\\2]●=>●\\3🌊", result13)
                result15 = re.sub(
                    r"([^🌊]*)🌊([^〒]*)〒([^〒]*)〒", "\\1●○○●[効能効果15:\\2]●=>●\\3🌊", result14)
                result16 = re.sub(
                    r"([^🌊]*)🌊([^〒]*)〒([^〒]*)〒", "\\1●○○●[効能効果16:\\2]●=>●\\3🌊", result15)
                result17 = re.sub(
                    r"([^🌊]*)🌊([^〒]*)〒([^〒]*)〒", "\\1●○○●[効能効果17:\\2]●=>●\\3🌊", result16)
                result18 = re.sub(
                    r"([^🌊]*)🌊([^〒]*)〒([^〒]*)〒", "\\1●○○●[効能効果18:\\2]●=>●\\3🌊", result17)
                result19 = re.sub(
                    r"([^🌊]*)🌊([^〒]*)〒([^〒]*)〒", "\\1●○○●[効能効果19:\\2]●=>●\\3🌊", result18)
                result20 = re.sub(
                    r"([^🌊]*)🌊([^〒]*)〒([^〒]*)〒", "\\1●○○●[効能効果20:\\2]●=>●\\3🌊", result19)
                result21 = re.sub(
                    r"([^🌊]*)🌊([^〒]*)〒([^〒]*)〒", "\\1●○○●[効能効果21:\\2]●=>●\\3🌊", result20)
                result22 = re.sub(
                    r"([^🌊]*)🌊([^〒]*)〒([^〒]*)〒", "\\1●○○●[効能効果22:\\2]●=>●\\3🌊", result21)
                result23 = re.sub(
                    r"([^🌊]*)🌊([^〒]*)〒([^〒]*)〒", "\\1●○○●[効能効果23:\\2]●=>●\\3🌊", result22)
                result24 = re.sub(
                    r"([^🌊]*)🌊([^〒]*)〒([^〒]*)〒", "\\1●○○●[効能効果24:\\2]●=>●\\3🌊", result23)
                result25 = re.sub(
                    r"([^🌊]*)🌊([^〒]*)〒([^〒]*)〒", "\\1●○○●[効能効果25:\\2]●=>●\\3🌊", result24)
                result26 = re.sub(
                    r"([^🌊]*)🌊([^〒]*)〒([^〒]*)〒", "\\1●○○●[効能効果26:\\2]●=>●\\3🌊", result25)
                result27 = re.sub(
                    r"([^🌊]*)🌊([^〒]*)〒([^〒]*)〒", "\\1●○○●[効能効果27:\\2]●=>●\\3🌊", result26)
                result28 = re.sub(
                    r"([^🌊]*)🌊([^〒]*)〒([^〒]*)〒", "\\1●○○●[効能効果28:\\2]●=>●\\3🌊", result27)
                line = re.sub(
                    r"([^🌊]*)🌊([^〒]*)〒([^〒]*)〒", "\\1●○○●[効能効果29:\\2]●=>●\\3🌊", result28)

            result_01 = re.sub(
                r"([」』])[♫🎶♩♪♬🎼「」『』♂∋∈]*([「『])", "\\1、\\2", line)
            result_02 = re.sub(r"(場合)([」』<])", "\\1:\\2", result_01)
            result_03 = re.sub(r"([ぁ-ん])([」』<])", "\\1。\\2", result_02)
            result_04 = re.sub(r"[「」『』]", "", result_03)
            result_05 = re.sub(r"</*[⊇⊆∪⊃]low\\d>", "", result_04)
            result_06 = re.sub(r"←\\/*(chr|bold)→", "", result_05)
            result_07 = re.sub(r"↑↑2:[効能効果2:]〒", "", result_06)
            result_08 = re.sub(r"[♫🎶♩♪♬🎼「」『』♂∋∈♪]", "", result_07)
            final = re.sub(r"</*[⊇⊆∪⊃]low\\d>", "", result_08)
            new_file.write(final)
            line = fp.readline()
        new_file.close()
    return HttpResponse("Oke")
