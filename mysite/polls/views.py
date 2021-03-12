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
    filepath_new = './001After.txt'
    new_file = open(filepath_new, 'w', encoding="utf-8")
    with open(filepath, encoding="utf8") as fp:
        line = fp.readline()
        new_file.write(line.replace('∋〒', '●○○●[効能効果1:'))
        cnt = 1
        while line:
            # print("Line {}: {}".format(cnt, line.strip()))
            line = fp.readline()
            cnt += 1
            a = re.search("^∋〒$", line)

            if re.search("^☆repm☆∋〒", line):
                new_file.write(line.replace('∋〒', '●○○●[効能効果1:'))
            if re.search("^☆merg☆∋〒♪", line):
                new_file.write(line.replace('∋〒', '●○○●[効能効果1:'))
            if re.search("^∋〒「", line):
                new_file.write(line.replace('∋〒', '●○○●[効能効果1:'))
            if re.search("☆inli☆∋〒♪", line):
                new_file.write(line.replace('∋〒', '●○○●[効能効果1:'))

            else:
                new_file.write(line)

    for line1 in fileinput.input():
        line1 = re.sub(r'\* \[(.*)\]\(#(.*)\)', r'\1', line.rstrip())
        print(line1)

    new_file.close()

    return HttpResponse("You have read file!!!")
