from django.shortcuts import render,redirect
from .forms import DataInputForm
from django.utils import timezone
from .models import TestResult
import pickle
def getPrediction(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal,modelChoice):
    dtree = pickle.load(open("decisionTree.sav", "rb"))
    sc = pickle.load(open("standardScaler.sav", "rb"))
    gaussianNB = pickle.load(open("gaussianNB.sav", "rb"))
    logReg = pickle.load(open("logisticRegression.sav", "rb"))
    stochasticGD = pickle.load(open("stochasticGradientDescent.sav", "rb"))
    SVC = pickle.load(open("SVC.sav", "rb"))
    knn = pickle.load(open("knn.sav", "rb"))
    rfc = pickle.load(open("randomForestClassifier.sav", "rb"))
    modelDict = {
        "gaussianNB":gaussianNB,
        "knn":knn,
        "logReg":logReg,
        "dtree":dtree,
        "rfc":rfc,
        "sdg":stochasticGD,
        "SVC":SVC
    }
    prediction=modelDict[modelChoice].predict(sc.transform([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]]))
    return(prediction)
def saveResult(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,
        ca,thal,name,modelChoice,result):
    timezone.activate('Asia/Kolkata')
    date_time=timezone.localtime()
    print(date_time)
    model_names= {
        "gaussianNB":"Gaussian Naive Bayes",
        "knn":"K-nearest Neighbors",
        "logReg":"Logistic Regression",
        "dtree":"Decision Tree",
        "rfc":"Random Forest Classifier",
        "sdg":"Stochastic Gradient Descent",
        "SVC":"Support Vector Classifier"
    }
    TestResult.objects.create(age=age, sex=sex, cp=cp,trestbps=trestbps,
        chol=chol, fbs=fbs, restecg=restecg, thalach=thalach, exang=exang,
        oldpeak=oldpeak, slope=slope, ca=ca, thal=thal,
        date_time=date_time,name=name,modelChoice=model_names[modelChoice],
        result=result
    )
# Create your views here.
def data_input_view(request):
    form = DataInputForm()
    if form.is_valid():
        pass
    context = {'form': form}
    return(render(request,"dataInput.html",context))
def result_view(request):
    if(request.method != "POST"):
        return(redirect('../input/'))
    else:
        (name,modelChoice) = (request.POST["name"],request.POST["modelChoice"])
        (age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,
        ca,thal)=tuple(map(float,[
            request.POST['age'],
            request.POST['sex'],
            request.POST['cp'],
            request.POST["trestbps"],
            request.POST["chol"],
            request.POST["fbs"],
            request.POST["restecg"],
            request.POST["thalach"],
            request.POST["exang"],
            request.POST["oldpeak"],
            request.POST["slope"],
            request.POST["ca"],
            request.POST["thal"]
        ]))
        #print("Types",type(sex),type(cp),type(name))
        prediction=getPrediction(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal,modelChoice)
        result={
            "0":"Heart disease not present.",
            "1":"Heart disease present"
        }
        context = {'result': result[str(prediction[0])]}
        saveResult(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,
        slope,ca,thal,name,modelChoice,result[str(prediction[0])])
    return(render(request,"result.html",context))
def result_history_view(request):
    return(render(request,"resultHistory.html",{"querySet":TestResult.objects.all()}))