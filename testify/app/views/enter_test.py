from django.shortcuts import render, redirect
from ..models import Test, Question, Answer

def enter_code_view(request, code):
    if request.method == 'GET':
        code = request.GET.get('code')  # Retrieve the code from the URL parameters

        try:
            # Attempt to retrieve the test based on the provided ID (code)
            test = Test.objects.get(id=code)
            
            # Get all questions for the test
            questions = Question.objects.filter(test=test)
            
            # Get all answers for each question
            questions_with_answers = []
            for question in questions:
                answers = Answer.objects.filter(question=question)
                questions_with_answers.append({'question': question, 'answers': answers})

            # Render the page with the retrieved test and questions
            return render(request, 'app/enter_code.html', {'test': test, 'questions_with_answers': questions_with_answers})
        except Test.DoesNotExist:
            # If the test does not exist, render the same page with an error message
            return render(request, 'app/enter_code.html', {'error': 'Test with this code does not exist.', 'code': code})
    else:
        # If the request method is not GET, render the same page without processing the request
        return render(request, 'app/enter_code.html')

def submit_test_view(request):
    if request.method == 'POST':
        test_id = request.POST.get('test_id')
        selected_answers = request.POST.getlist('selected_answers')

        # Now you have the test_id and the list of selected answers, you can process the submission
        # For example, you can check the selected answers against the correct answers in the database

        return redirect('index')  # Redirect to the homepage after submitting the test
    else:
        return redirect('index')