from django.shortcuts import render, redirect
from ..models import Test, Question, Answer

def create_test_view(request):
    if request.method == 'POST':
        test_name = request.POST.get('test_name')
        test = Test.objects.create(name=test_name)
        for key, value in request.POST.items():
            if key.startswith('question_'):
                question_text = value
                question = Question.objects.create(test=test, question_text=question_text)
                for i in range(1, 5):
                    answer_text = request.POST.get(f'answer_{key.split("_")[1]}_{i}')
                    if answer_text is not None and answer_text.strip():
                        is_correct = request.POST.get(f'is_correct_{key.split("_")[1]}_{i}', False)
                        is_correct = is_correct == 'true'
                        Answer.objects.create(question=question, answer_text=answer_text, is_correct=is_correct)

        return redirect('index')
    else:
        return render(request, 'app/create_test.html')
