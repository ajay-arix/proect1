import os
import sys
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

from django.urls import path
from myapp import views

urlpatterns = [
    path('section1/', views.face_detection, name='section1'),
    path('section2/', views.kyc_form, name='section2'),
    path('section3/', views.instructions, name='section3'),
]

from django import forms

class KYCForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    address = forms.CharField(widget=forms.Textarea)
    

import cv2
from django.shortcuts import render
from myapp.forms import KYCForm

def face_detection(request):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    video_capture = cv2.VideoCapture(0)

    while True:
        ret, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        percentage = len(faces) / 10 * 100

        cv2.putText(frame, f'Matching: {percentage}%', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow('Face Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

    return render(request, 'section1.html')

def kyc_form(request):
    form = KYCForm()

    if request.method == 'POST':
        form = KYCForm(request.POST)
        if form.is_valid():
            return render(request, 'section2.html')

    return render(request, 'kyc_form.html', {'form': form})

def instructions(request):
    if request.method == 'POST':
        return render(request, 'section3.html')

    return render(request, 'instructions.html')
