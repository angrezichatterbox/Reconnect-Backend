from django.forms import ModelForm
from flutter_app.models import EventPage

class EventForm(ModelForm):
    class Meta:
        model = EventPage
        fields = '__all__'

