import django.forms as forms


class RodoForm(forms.Form):
    first_name = forms.CharField(
        label="Imię",
        widget=forms.TextInput()
    )
    last_name = forms.CharField(
        label="Nazwisko",
        widget=forms.TextInput()
    )
    email = forms.CharField(
        label="Adres e-mail",
        widget=forms.EmailInput()
    )
    phone = forms.CharField(
        label="Numer telefonu",
        widget=forms.TextInput()
    )
    address = forms.CharField(
        label="Ulica i numer budynku",
        widget=forms.TextInput()
    )
    post_code = forms.CharField(
        label="Kod pocztowy",
        widget=forms.TextInput()
    )
    city = forms.CharField(
        label="Miasto",
        widget=forms.TextInput()
    )
    consent_1 = forms.BooleanField(
        label="Wyrażam zgodę na przetwarzanie moich danych osobowych w celu i zakresie niezbędnym do realizacji szkolenia.",
        widget=forms.CheckboxInput()
    )
    consent_2 = forms.ChoiceField(
        label="Wyrażam zgodę na przekazywanie moich danych do podmiotu organizującego szkolenie.",
        widget=forms.CheckboxInput()
    )
    consent_3 = forms.ChoiceField(
        label="Wyrażam zgodę na przekazywanie moich danych w związku z moim udziałem w egzaminie.",
        widget=forms.CheckboxInput()
    )
