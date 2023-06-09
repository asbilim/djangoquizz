from django.shortcuts import render,redirect
from django.contrib.auth import login as login2,authenticate,logout
from django.contrib.auth import get_user_model
from listings.models import Quiz,Answer

def home(request):

    return render(request, 'listings/index.html')


def login(request):

    if request.user.is_authenticated:

        return redirect('explore')

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        if len(username) and len(password):

            user = authenticate(username=username, password=password)
            if user is not None:
                login2(request, user)
                return redirect('main-home-page')
        
    
    return render(request,'listings/auth/login.html')


def register(request):

    if request.user.is_authenticated:

        return redirect('main-home-page')
    
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        confirm = request.POST['confirm']
        User = get_user_model()

        if confirm != password:
            return render(request,'listings/auth/register.html')
        
        user = User.objects.create(username=username, password=password)

        if user:
            login2(request, user)
            return redirect('main-home-page')

    
    return render(request,'listings/auth/register.html')


def signout(request):

    if request.user.is_authenticated:

        logout(request)
        return redirect('auth-login')
    

def single_quiz(request,quiz_id,question_id):

    if request.method == 'POST':

        choice = request.POST.get('choice')
        quiz = Quiz.objects.get(id=quiz_id)
        questions = list(quiz.questions.all())
        current_question = questions[question_id-1]
        current_question.is_done = True
        correct_question = current_question.answers.filter(is_correct=True).get()
        

        try:
            choice = Answer.objects.get(id=choice)
        except Answer.DoesNotExist:
            return redirect('main-home-page')
        
        if not current_question.is_done and choice==correct_question:
            if quiz.final_score:
                quiz.final_score+=10
            else:
                quiz.final_score=10
            
            quiz.save()

            current_question.is_done = True

        current_question.save()
        quiz.save()

        # current_question.choice = choice
        # current_question.save()

                
    try:
        quiz = Quiz.objects.get(id=quiz_id)
        questions = list(quiz.questions.all())

        if question_id > len(questions):
            print(question_id,len(questions))
            return redirect('error')
        
        current_question = questions[question_id-1]
        
        if current_question.is_done:
            if len(questions) == question_id:

                return redirect("done",score=quiz.final_score) 
            else:
                return redirect("single-quiz",quiz_id=quiz_id,question_id=question_id+1 )
        current_question_answers = current_question.answers.all()
        

    except Exception as e:
        print(e)
        return redirect('error')

    
    return render(request,'listings/quiz/single.html',{"question":current_question,"current_question_answers":current_question_answers,"question_number":question_id,"number_questions":len(questions),"is_done":current_question.is_done})

def quiz_done(request,score):

    return render(request,'listings/finish.html',{"score":score})


def quiz_error(request):

    return render(request,'listings/error.html')

def explore(request):

    quiz = Quiz.objects.all()

    return render(request,'listings/all.html',{"quiz":quiz})