from django.shortcuts import render, redirect
from django.views import generic
from quiz.forms import AdminLoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from QuizTest import settings
from quiz.models import Questions, QuizSubmission, QuizResult
from quiz.messages import AuthMessages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.


class LoginView(generic.FormView):
    template_name = 'login.html'
    success_url = 'quiz-view'
    form_class = AdminLoginForm
    msg_ob = AuthMessages()
    
    def get_context_data(self, **kwargs):
        context_dict = super(LoginView, self).get_context_data(**kwargs)
        if 'form' not in kwargs:
            context_dict['login_form'] = self.form_class
        else:context_dict['login_form'] = kwargs.get('form')
        return context_dict
    
    def form_valid(self, form):
        """Security check complete. Log the user in."""
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user:
            login(self.request, user)
            return redirect(self.success_url)
        else:
            messages.error(self.request, self.msg_ob.login_failed)
        return redirect(self.request.META.get('HTTP_REFERER'))
    
    def form_invalid(self, form):
        """
            If the form is invalid, re-render the context data with the
            data-filled form and errors.
        """
        return self.render_to_response(self.get_context_data(form=form))
    
    def get(self, request):
        if request.user.is_authenticated:
            return redirect(self.success_url)
        context_dict = self.get_context_data()
        return render(request, self.template_name, context_dict)


class AdminLogout(generic.RedirectView):
    redirect_url = settings.LOGIN_URL
    
    def get(self, request):
        logout(request)
        return redirect(self.redirect_url)


@method_decorator(login_required, name='dispatch')
class QuizView(generic.ListView):
    model = Questions
    context_object_name = 'question_list'
    template_name = 'quiz.html'
    

@method_decorator(login_required, name='dispatch')
class ResultView(generic.ListView):
    model = QuizResult
    context_object_name = 'result_list'
    template_name = 'result_list.html'
    paginate_by = 10
    
    def get_queryset(self):
        return QuizResult.objects.filter(user_id=self.request.user.id)
    
    def calculate_quiz_result(self, question_ans):
        submission_list = []
        for question_id, ans_id in question_ans.items():
            submission_obj = QuizSubmission.objects.create(
                user_id=self.request.user.id, question_id=question_id,
                answer_id=ans_id)
            submission_list.append(submission_obj)
        submission_obj_lists = QuizSubmission.objects.filter(
            id__in=[x.id for x in submission_list])
        correct_ans = submission_obj_lists.filter(is_correct=True).count()
        question_count = Questions.objects.filter(is_active=True).count()
        result_obj = QuizResult.objects.create(user_id=self.request.user.id,
            no_of_questions=question_count,
            attended=submission_obj_lists.count(),
            correct_ans=correct_ans,
            incorrect_ans=submission_obj_lists.filter(is_correct=False).count(),
            total_score=settings.CORRECT_ANS_WEIGHT * question_count,
            achieved_score=settings.CORRECT_ANS_WEIGHT * correct_ans
        )
        return result_obj
    
    def post(self, request):
        question_ans = {}
        for key, val in request.POST.items():
            if key.startswith('question_'):
                key = key.lstrip('question_').strip()
                question_ans[key] = val
                
        result_obj = self.calculate_quiz_result(question_ans)
        context_data = {}
        context_data['result_obj'] = result_obj
        return render(request, 'result.html', context_data)
        









































        

    






