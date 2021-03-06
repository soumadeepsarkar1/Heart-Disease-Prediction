from django import forms
class DataInputForm(forms.Form):
    name=forms.CharField()
    age=forms.DecimalField(max_digits=6,decimal_places=2,min_value=0)
    sex=forms.ChoiceField(
        choices=[('1','Male'),('0','Female')],#(value, what is to be displayed)
        widget=forms.RadioSelect
    )
    cp=forms.DecimalField(max_digits=6,decimal_places=2,min_value=0)
    trestbps=forms.DecimalField(max_digits=6,decimal_places=2,min_value=0)
    chol=forms.DecimalField(max_digits=6,decimal_places=2,min_value=0)
    fbs=forms.DecimalField(max_digits=6,decimal_places=2,min_value=0)
    restecg=forms.DecimalField(max_digits=6,decimal_places=2,min_value=0)
    thalach=forms.DecimalField(max_digits=6,decimal_places=2,min_value=0)
    exang=forms.DecimalField(max_digits=6,decimal_places=2,min_value=0)
    oldpeak=forms.DecimalField(max_digits=6,decimal_places=2,min_value=0)
    slope=forms.DecimalField(max_digits=6,decimal_places=2,min_value=0)
    ca=forms.DecimalField(max_digits=6,decimal_places=2,min_value=0)
    thal=forms.DecimalField(max_digits=6,decimal_places=2,min_value=0)
    modelChoice=forms.ChoiceField(label="Model choice",
        choices=[
            ('gaussianNB','Gaussian Naive Bayes (Accuracy: 84%)'),
            ('knn','K-nearest Neighbors (Accuracy: 99%)'),
            ('logReg','Logistic Regression (Accuracy: 87%)'),
            ('dtree','Decision Tree (Accuracy: 99%)'),
            ('rfc',"Random Forest Classifier (Accuracy: 99%)"),
            ('sdg',"Stochastic Gradient Descent (Accuracy: 78%)"),
            ("SVC","Support Vector Classifier (Accuracy: 99%)")
        ],#(value, what is to be displayed)
        widget=forms.RadioSelect
    )