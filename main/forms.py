from django.forms import ModelForm
from models import SSL


class SSLForm(ModelForm):
	class Meta:
		model = SSL

