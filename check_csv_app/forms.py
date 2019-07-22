from django import forms
from check_csv_app.models import Document
from django.core.validators import FileExtensionValidator
import pandas as pd


class DocumentForm(forms.ModelForm):
    # description = forms.CharField(max_length=255)
    document = forms.FileField(required=True, validators=[FileExtensionValidator(allowed_extensions=['csv'])])
    # filetype = mag

    class Meta:
        model = Document
        fields = ('document',)

    def clean_document(self):

        document = self.cleaned_data['document']

        if document:

            file_name = document.name

            if file_name.endswith('csv'):
                if document.size < (5 * 1024 * 1024):
                    df=pd.read_csv(document)
                    if(df.shape[0]==0):
                        raise forms.ValidationError("Uploaded file is blank")
                    else:
                        if (pd.read_csv(document).shape[0]<50):
                            raise forms.ValidationError("Please upload csv with more than 15 rows")
                    return document
                else:
                    raise forms.ValidationError("Size greater than 5MB")
            else:
                raise forms.ValidationError("Please upload a csv")

        return document
