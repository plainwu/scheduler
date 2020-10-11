from django.forms import ModelForm, DateInput, ValidationError, IntegerField, NumberInput, TextInput, Textarea
from django import forms
from WeekSchedule.models import Event

import datetime
a = datetime.datetime.now()
print(a)
class EventForm(ModelForm):
    
    start_time = forms.RegexField(regex=r'\d{4}\/\d{2}\/\d{2}\s\d{2}\:\d{2}', widget=forms.TextInput(attrs={'placeholder': "2020/10/10 12:00"}))
    
    def __init__(self, *args, **kwargs):
        now = datetime.datetime.now()
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['subject'].widget.attrs['placeholder'] = 'Math'
        self.fields['description'].widget.attrs['placeholder'] = 'Chapter.1'
        self.fields['start_time'].widget.attrs['placeholder'] = '{}'.format(now.strftime("%Y/%m/%d %H:%M"))
        self.fields['start_time'].widget.attrs['value'] = '{}'.format(now.strftime("%Y/%m/%d %H:%M"))
        self.fields['start_time'].widget.attrs['class'] = 'form-control'
        self.fields['clock'].widget.attrs['placeholder'] = 'How many clocks?'

    class Meta:
        model = Event
        widgets = {
            'subject': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control'}),
            'clock': NumberInput(attrs={'type': 'number', 'class': 'form-control'}),
        }
        exclude = ['user', 'status', 'end_time']

    def clean_start_time(self, *args, **kwargs):
        print(self)
        start_time_str = self.cleaned_data["start_time"]
        start_time = datetime.datetime.strptime(start_time_str, "%Y/%m/%d %H:%M")
        clock = int(self.data["clock"])
        minute = clock * 30
        end_time = start_time + datetime.timedelta(minutes = minute)

        check_event = Event.objects.filter(start_time__contains = start_time.date())
        print(check_event)
        for event in check_event:
            print('hi')
            event_start_time = event.start_time
            event_end_time = event.end_time
            if start_time.time() < event_start_time.time():
                if end_time.time() > event_start_time.time():
                    print(start_time, event_start_time, event_end_time)
                    raise ValidationError("Your time has conflicted!!")
            elif start_time.time() < event_end_time.time():
                print(start_time, event_start_time, event_end_time)
                raise ValidationError("Your time has conflicted!!")

        return start_time
